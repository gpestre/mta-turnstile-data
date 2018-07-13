# `lookup_stations.csv`

**Source :** MTA Developer Data - Stations

**URL :** http://web.mta.info/developers/data/nyct/subway/Stations.csv

**Downloaded :** 2018-06-05

**Notes :** Station complexes (`Complex ID`) comprise multiple stations (`Station ID`), which may have multiple GTFS identifiers (`GTFS Stop ID`); the values of `GTFS Stop ID` are unique in this table.

**Modifications :** The columns were reordered to create a hierarchichal index: `Complex ID` > `Station ID` > `GTFS Stop ID`. The rows were sorted according to this index.


# `lookup_booths.csv`

**Source :** MTA Turnstile Data - Remote Unit/Control Area/Station Name Key

**URL :** http://web.mta.info/developers/turnstile.html  ;  http://web.mta.info/developers/resources/nyct/turnstile/Remote-Booth-Station.xls

**Downloaded :** 2018-05-30

**Notes :** Station complexes (`Complex ID`) comprise multiple remotes (`Remote`) which each have multiple booths (`Booth`); the values of `Booth` are unique in this table.  Although a booth is located within a single station, multiple values of `Booth` may share a value of `Station` because the station names provided in this table are not unique (ex: there are a number of stations on different lines called `116 ST`).

**Modifications :** The `Complex ID` column was added at the result of a manual matching process, to create a hierarchical index `Complex ID` > `Remote` > `Booth`. The rows were sorted according to this index.


# `lookup_groupings.csv`

**Source :** Created manually 2018-06.

**Notes :** The grouping names are based on the names provided in Wikipedia. There is a one-to-one correspondence between groupings and values of `Complex ID` (besides the groupings which have no `Complex ID`).
