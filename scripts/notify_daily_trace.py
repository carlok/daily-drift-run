#!/usr/bin/env python3
"""Send a small email notification for the latest Daily Drift trace."""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise SystemExit(f"{path}:{line_number}: expected KEY=value")

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]
        values[key] = value

    values.update(os.environ)
    return values


def load_recipients(path: Path) -> list[str]:
    data = json.loads(path.read_text())
    if isinstance(data, list):
        recipients = data
    elif isinstance(data, dict):
        recipients = data.get("recipients", [])
    else:
        recipients = []

    if not all(isinstance(item, str) and item.strip() for item in recipients):
        raise SystemExit(f"{path}: expected a JSON list, or an object with recipients")

    return [item.strip() for item in recipients]


def latest_day_dir() -> Path:
    days = sorted((ROOT / "days").glob("????-??-??-*"))
    if not days:
        raise SystemExit("No daily trace folders found under days/")
    return days[-1]


def github_url(base_url: str, relative_path: Path) -> str:
    parts = [quote(part) for part in relative_path.parts]
    return f"{base_url.rstrip('/')}/{'/'.join(parts)}"


def bool_env(env: dict[str, str], key: str, default: bool) -> bool:
    raw = env.get(key)
    if raw is None or raw == "":
        return default
    return raw.lower() in {"1", "true", "yes", "on"}


def required(env: dict[str, str], key: str) -> str:
    value = env.get(key, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment value: {key}")
    return value


def artifact_target(day_dir: Path) -> Path | None:
    artifact_dir = day_dir / "artifact"
    if artifact_dir.is_dir():
        files = sorted(path for path in artifact_dir.rglob("*") if path.is_file())
        markdown_files = [path for path in files if path.suffix.lower() == ".md"]
        if len(files) == 1 and len(markdown_files) == 1:
            return markdown_files[0]
        return artifact_dir

    extra_markdown = sorted(
        path
        for path in day_dir.glob("*.md")
        if path.is_file() and path.name != "trace.md"
    )
    if len(extra_markdown) == 1:
        return extra_markdown[0]

    return None


def build_message(env: dict[str, str], recipient: str, day_dir: Path) -> EmailMessage:
    base_url = required(env, "GITHUB_BASE_URL")
    from_address = required(env, "SMTP_FROM")
    relative_day = day_dir.relative_to(ROOT)
    folder_url = github_url(base_url, relative_day)
    trace_url = github_url(base_url, relative_day / "trace.md")
    artifact = artifact_target(day_dir)

    title = day_dir.name
    trace_path = day_dir / "trace.md"
    if trace_path.exists():
        first_line = trace_path.read_text().splitlines()[0].lstrip("# ").strip()
        if first_line:
            title = first_line

    subject_prefix = env.get("EMAIL_SUBJECT_PREFIX", "Daily Drift").strip()
    subject = f"{subject_prefix}: {title}" if subject_prefix else title

    body_lines = [
        "Today's Daily Drift trace is available here:",
        "",
        folder_url,
        "",
        f"Trace: {trace_url}",
    ]
    if artifact:
        body_lines.append(f"Artifact: {github_url(base_url, artifact.relative_to(ROOT))}")

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = from_address
    message["To"] = recipient
    message.set_content("\n".join(body_lines) + "\n")
    return message


def send_messages(env: dict[str, str], recipients: list[str], day_dir: Path) -> None:
    host = required(env, "SMTP_HOST")
    port = int(env.get("SMTP_PORT", "587"))
    username = env.get("SMTP_USERNAME", "").strip()
    password = env.get("SMTP_PASSWORD", "").strip()
    use_ssl = bool_env(env, "SMTP_USE_SSL", False)
    starttls = bool_env(env, "SMTP_STARTTLS", not use_ssl)

    if use_ssl:
        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as smtp:
            if username or password:
                smtp.login(username, password)
            for recipient in recipients:
                smtp.send_message(build_message(env, recipient, day_dir), to_addrs=[recipient])
        return

    with smtplib.SMTP(host, port) as smtp:
        if starttls:
            smtp.starttls(context=ssl.create_default_context())
        if username or password:
            smtp.login(username, password)
        for recipient in recipients:
            smtp.send_message(build_message(env, recipient, day_dir), to_addrs=[recipient])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env", default=".env", help="Path to env file")
    parser.add_argument(
        "--recipients",
        default="recipients.json",
        help="Path to JSON recipient file",
    )
    parser.add_argument("--day-dir", help="Specific day folder; defaults to latest")
    parser.add_argument("--dry-run", action="store_true", help="Print without sending")
    args = parser.parse_args()

    env = load_env(ROOT / args.env)
    recipients = load_recipients(ROOT / args.recipients)
    day_dir = (ROOT / args.day_dir) if args.day_dir else latest_day_dir()

    if args.dry_run:
        for index, recipient in enumerate(recipients, start=1):
            message = build_message(env, recipient, day_dir)
            if index > 1:
                print("\n---\n")
            print(f"To: {message['To']}")
            print(f"Subject: {message['Subject']}")
            print()
            print(message.get_content(), end="")
        return

    send_messages(env, recipients, day_dir)
    print(f"Sent {len(recipients)} email(s) for {day_dir.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
