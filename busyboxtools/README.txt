Scraper.py is a script that takes in "unique.json" as input and creates two different output text files.

FixedBugReport.txt is a file that lists the different types of bugs that have to be checked, as well as
basic information regarding them.  There is also a basic format I provided the user with to use for storing
notes for the bug they are working on.

DeadStoreBugs.txt is a file that lists all the Dead Store bugs that were a result of testing the BusyBox 
code. There is also a basic format I provided the user with to use for storing notes for the bug they are 
working on.

By producing these two output files I was able to filter out 150k+ lines of information that were unnecessary 
to read through, which will make bug-finding and tracking for BusyBox code a lot easier to go through.
