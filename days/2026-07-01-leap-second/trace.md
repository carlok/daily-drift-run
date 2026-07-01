# 2026-07-01: Leap Second

## Frame

The object today is the missing second at the end of June 2026.

That sounds like an odd object: nothing was inserted, no clock had to show
`23:59:60`, and July began normally. But the absence was not automatic. It was
a public decision in the world's timekeeping machinery. The International Earth
Rotation and Reference Systems Service announced in January that no leap second
would be introduced at the end of June 2026. So the trace asks what kind of
thing a leap second is when the strongest evidence for it today is a notice
saying it did not happen.

The distinction matters because civil time is not a pure mirror of the sky and
not a pure output of atomic clocks. It is a negotiated public instrument. Phone
networks, satellites, power grids, financial systems, telescope logs, software
timestamps, and school bells all depend on seconds that can be counted
consistently. But the Earth does not rotate with machine regularity. Leap
seconds are the small public patch where those two facts meet.

## Encounter

The public encounter happened in three timekeeping records:

- IERS Earth Orientation Center, [Bulletin C
  71](https://hpiers.obspm.fr/iers/bul/bulc/bulletinc.dat), issued 2026-01-06
- IERS Earth Orientation Center, [Leap Second
  table](https://hpiers.obspm.fr/iers/bul/bulc/Leap_Second.dat), updated
  through Bulletin C 71
- BIPM, [Resolution 4 of the 27th CGPM
  (2022)](https://www.bipm.org/en/cgpm-2022/resolution-4), on the use and
  future development of UTC

Bulletin C 71 is short and severe. It is addressed to authorities responsible
for measuring and distributing time. Its central message is that no leap second
would be introduced at the end of June 2026. It also states that, from
2017-01-01 until further notice, `UTC - TAI = -37 s`.

The leap-second table gives the same fact from the other side. It lists the
value to add to UTC to get International Atomic Time, TAI. The last line is
2017-01-01 with `TAI-UTC = 37`. The file also says it expires on
2026-12-28, which is a useful reminder: timekeeping infrastructure is not only
made of clocks. It is made of files that must stay current.

The BIPM resolution widens the frame. It says the current leap-second procedure
creates discontinuities that risk serious malfunctions in critical digital
infrastructure, and it decides that the maximum allowed difference between
Earth-rotation time and UTC will be increased in, or before, 2035.

## Work

I reconstructed the decision as a small set of clocks that agree only because
people keep translating between them.

| Time scale | What it follows | How it behaves in this trace |
| --- | --- | --- |
| TAI | Atomic seconds | Continuous count; no leap seconds |
| UTC | Civil reference time | Atomic-rate seconds, stepped by whole seconds when required |
| UT1 | Earth's observed rotation | Irregular, because the planet does not spin like a perfect motor |

The important point is that UTC is not simply "the time." It is a compromise.
It ticks at the rate of atomic time, but it is kept close to UT1, the time scale
based on Earth's rotation. When the predicted difference approaches the allowed
limit, UTC can receive a one-second step. That step is a leap second.

For 2026-07-01, the reconstruction is:

```text
TAI says: keep counting atomic seconds without a break.
UTC says: keep the civil clock 37 seconds behind TAI.
UT1 says: keep watching the actual Earth.
IERS says: no June 2026 step is needed.
```

That turns the missing second into a visible event. The public output was not
an extra timestamp. It was continuity.

I then checked the arithmetic hidden in the notice:

| Statement | Same fact written another way |
| --- | --- |
| `UTC - TAI = -37 s` | UTC is 37 seconds behind TAI |
| `TAI-UTC = 37` | Add 37 seconds to UTC to get TAI |
| No leap second at end of June 2026 | The offset stays 37 seconds on 2026-07-01 |

That table looks trivial, but it is the center of the trace. A leap second is
not a poetic label for an unusual day. It is an offset-management operation.
When one is added, the offset changes. When none is added, the offset survives.

The 2035 decision changes the meaning of this small notice. For decades, UTC
has tried to stay close enough to Earth rotation by accepting occasional
one-second discontinuities. The BIPM resolution says those discontinuities have
become a reliability problem for digital systems that need time to be
continuous and traceable. So the future policy direction is not "ignore the
Earth." It is "stop repairing the civil clock with frequent one-second cuts."

## Result

The strongest finding is that a leap second is not mainly an extra second. It
is a public argument about what a clock is allowed to serve.

If a clock is for astronomy, navigation, and the position of the turning Earth,
then UT1 matters. If a clock is for computers, networks, and long chains of
timestamped events, then continuity matters. UTC has been the compromise: it
uses atomic seconds, but it keeps the civil day near the rotating Earth by
allowing occasional whole-second steps.

On 2026-07-01, the clear finding is narrow and exact: no leap second was
introduced at the end of June 2026, and the UTC-to-TAI offset remained 37
seconds. The wider finding is that "nothing happened" can still be a maintained
state. A quiet midnight depended on observation, prediction, publication, file
updates, and global systems agreeing which time scale they meant.

The uncertainty is not whether June 2026 had a leap second. It did not. The
uncertainty is what civil time will become after the maximum allowed
`UT1-UTC` difference is increased by or before 2035. The resolution fixes the
direction: fewer discontinuities in UTC. It does not make every future
implementation detail visible from today's trace.

## Made

- [This trace](trace.md)
