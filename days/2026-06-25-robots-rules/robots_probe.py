#!/usr/bin/env python3
"""Small robots.txt rule probe for today's trace."""

from __future__ import annotations

from dataclasses import dataclass
import re


ROBOTS_TXT = """
user-agent: ExampleBot
disallow: /private/
allow: /private/press/

user-agent: ExampleBot
disallow: /tmp

user-agent: *
disallow: /archive/
allow: /archive/public$
"""


TEST_PATHS = [
    "/",
    "/private/",
    "/private/press/",
    "/private/press/release.html",
    "/tmp",
    "/tmp-not-the-same-place",
    "/archive/",
    "/archive/public",
    "/archive/public/index.html",
    "/robots.txt",
]


@dataclass(frozen=True)
class Rule:
    kind: str
    pattern: str


@dataclass(frozen=True)
class Group:
    agents: tuple[str, ...]
    rules: tuple[Rule, ...]


def strip_comment(line: str) -> str:
    return line.split("#", 1)[0].strip()


def parse_robots(text: str) -> list[Group]:
    groups: list[Group] = []
    agents: list[str] = []
    rules: list[Rule] = []

    def flush() -> None:
        nonlocal agents, rules
        if agents:
            groups.append(Group(tuple(agents), tuple(rules)))
        agents = []
        rules = []

    for raw_line in text.splitlines():
        line = strip_comment(raw_line)
        if not line or ":" not in line:
            continue

        key, value = (part.strip() for part in line.split(":", 1))
        key = key.lower()

        if key == "user-agent":
            if rules:
                flush()
            agents.append(value.lower())
        elif key in {"allow", "disallow"} and agents:
            rules.append(Rule(key, value))

    flush()
    return groups


def pattern_regex(pattern: str) -> re.Pattern[str]:
    exact = pattern.endswith("$")
    if exact:
        pattern = pattern[:-1]

    escaped = "".join(".*" if char == "*" else re.escape(char) for char in pattern)
    suffix = "$" if exact else ""
    return re.compile(f"^{escaped}{suffix}")


def matching_rules(groups: list[Group], user_agent: str) -> list[Rule]:
    token = user_agent.lower()
    exact = [group for group in groups if token in group.agents]
    wildcard = [group for group in groups if "*" in group.agents]
    selected = exact or wildcard
    return [rule for group in selected for rule in group.rules]


def decide(rules: list[Rule], path: str) -> tuple[bool, Rule | None]:
    if path == "/robots.txt":
        return True, None

    matches = [
        rule
        for rule in rules
        if rule.pattern and pattern_regex(rule.pattern).match(path)
    ]
    if not matches:
        return True, None

    winner = max(matches, key=lambda rule: (len(rule.pattern.rstrip("$")), rule.kind == "allow"))
    return winner.kind == "allow", winner


def main() -> None:
    groups = parse_robots(ROBOTS_TXT)
    rules = matching_rules(groups, "ExampleBot")

    print("| Path | Decision | Winning rule |")
    print("| --- | --- | --- |")
    for path in TEST_PATHS:
        allowed, rule = decide(rules, path)
        decision = "allow" if allowed else "disallow"
        winning_rule = "implicit" if rule is None else f"{rule.kind}: {rule.pattern}"
        print(f"| `{path}` | {decision} | `{winning_rule}` |")


if __name__ == "__main__":
    main()
