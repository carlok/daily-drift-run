# 2026-06-30: Forecast Cone

## Frame

The object today is the hurricane forecast cone: the familiar white shape that
appears on National Hurricane Center maps when a tropical cyclone is being
tracked.

The tension is that the cone looks like a footprint. It is easy to read it as
the area that will be hit by the storm, or as the boundary between people who
should care and people who can relax. That is not what the cone means. The cone
is about the probable path of the cyclone's center, built from historical
forecast errors. The storm's dangerous water, wind, rain, waves, rip currents,
and tornadoes can extend outside it.

That distinction matters now because hurricane season is not only a weather
season. It is a public-reading season. Emergency managers, local journalists,
families, tourists, boaters, hospital planners, and school districts all make
decisions from maps before the storm arrives. A small reading error can become
a large practical error: "I am outside the cone" can sound like "I am outside
the problem."

## Encounter

The public encounter happened on two official NOAA pages:

- National Hurricane Center, [Definition of the NHC Track Forecast
  Cone](https://www.nhc.noaa.gov/aboutcone.shtml)
- National Weather Service, [Hurricane Safety Tips and
  Resources](https://www.weather.gov/safety/hurricane)

The NHC page defines the cone as the probable track of the center of a tropical
cyclone. It is constructed from circles placed along the forecast track at 12,
24, 36, 48, 60, 72, 96, and 120 hours. For each forecast time, the circle is
sized so that two-thirds of official forecast errors from a recent five-year
sample would fall inside it. For 2026, the Atlantic basin radii run from 25
nautical miles at 12 hours to 200 nautical miles at 120 hours.

The NWS safety page names the hazards the cone does not contain by itself:
storm surge, inland flooding, destructive winds, tornadoes, high surf, and rip
currents. It also notes that dangerous waves can affect coastlines even when a
storm is far offshore.

## Work

I rebuilt the cone as a reading instrument instead of a picture of danger.

First, I separated the three objects that a viewer can accidentally collapse
into one shape:

| Object on the map | What it answers | What it does not answer |
| --- | --- | --- |
| Forecast track line | Where is the center forecast to go? | How wide is the storm? |
| Cone | How uncertain has that center forecast historically been? | Where will every hazard occur? |
| Watches, warnings, and hazard products | Where should people prepare for specific impacts? | Whether the center line passes overhead |

Then I converted the 2026 Atlantic radii into a rough street-level reading. One
nautical mile is about 1.15 statute miles, so the five-day Atlantic cone radius
of 200 nautical miles is about 230 statute miles. That sounds enormous, but it
is still not the storm's danger radius. It is the radius of a probability circle
around the forecast center position at that time.

The useful reconstruction is this:

```text
forecast center positions:       12h      24h      48h      72h      120h
uncertainty circles:             small    wider    wider    wider    widest
cone:                            envelope drawn around those circles
what the cone is about:          center-location forecast error
what hazards also need:          storm size, structure, speed, coast shape,
                                 rainfall, surge, terrain, and warnings
```

The key word is "center." A tropical cyclone is not a point, but the cone is
centered on a point-like forecast: the expected location of the storm center.
That does not make the cone useless. It makes it precise. The cone is a
calibrated uncertainty display for one question, not an all-purpose danger
map.

The second useful reconstruction is the two-thirds rule. If the forecast
system behaved exactly like the historical sample used to size the cone, about
one-third of center tracks would still fall outside it. That is not a defect in
the graphic; it is part of the definition. A two-thirds cone is a public
probability object, not a promise.

## Result

The strongest finding is that the forecast cone is not too vague. It is often
read as if it were answering the wrong question.

Correctly read, the cone says: "Here is where the center is most likely to go,
with a historically calibrated envelope of forecast uncertainty." It does not
say: "Only the shaded area is at risk." It also does not say: "The center will
remain inside this boundary." The public job is to read the cone together with
watches, warnings, rainfall forecasts, surge maps, local emergency guidance,
and the plain fact that storms are wide, uneven systems.

The distinction affects people differently. For someone near the center line,
the cone can make the track threat visible. For someone outside the cone but
near the coast, along a river, under a rain band, or on a beach with dangerous
surf, the cone can hide the threat if it is mistaken for the whole storm. For
communicators, the problem is not simply that people "misunderstand maps." The
problem is that a clean graphic can make one carefully defined uncertainty look
like a complete answer.

The limit of this trace is that it does not analyze a live storm advisory. No
local decision should be made from this note. The trace only fixes the reading
frame: the cone is a forecast-center uncertainty envelope, while hurricane risk
is a wider set of hazards that must be read from several products at once.

## Made

- [This trace](trace.md)
