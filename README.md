# Source : MTA Turnstile Data

http://web.mta.info/developers/turnstile.html

# Source : MTA Station List

http://web.mta.info/developers/data/nyct/subway/Stations.csv

# Methodology :

- The numbers of entries and exits are calculated for each unique combination of C/A , UNIT, and SCP.  
- All negative deltas are converted to positive values.
- For each C/A , UNIT, and SCP, values that are 2 standard deviations above or below the mean are removed.  

**Note:** The code is configured for reading turnstile data from 2014-10-18 or later. Files from earlier dates are formatted differently and the code is not currently adapted for parsing them.
