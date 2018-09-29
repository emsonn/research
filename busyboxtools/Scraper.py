# Edward M. Abrahamson
#
# REFERENCE FOR CODE:
# https://stackoverflow.com/questions/23306653/python-accessing-nested-json-data
#
# I've only been coding in Python for a few days now, so let me know if anything should be changed/optimized,
#   as I am brand new to this language.
#
# Using regular spaces rather than tabs in print formatting so the file can be more consistent regardless of
#   text editor.

# The real MVP here
import json

# Makes some of the json-read text formatting consistent.
import textwrap


def main():

    # Opens .json file, loads, reads, and stores to variable.
    # Don't have to explicitly close out of this due to how the function works.
    jdata = json.loads(open('unique.json').read())

    # Output file created, will hold all of the information we need, taken from the unique.json file.
    new_file = open("FixedBugReport.txt", "w")
    dead_store_file = open("DeadStoreBugs.txt", "w")

    # Call to function that will do the header printing without polluting the main function.
    fileHeaders(new_file, dead_store_file)

    # Counter variable to keep track of the number of bugs we have to find.
    # Makes talking about a specific bug a LOT easier.
    i = 1
    j = 1

    # Will help to not print the last "+---------+" line that separates bug entries.
    last = jdata[-1]

    # Regular for loop that will go through each line in the input .json file
    for line in jdata:

        # Will write to FixedBugReport.txt
        if line['category'].lower() != "dead store":

            # Disgusting-looking print formatting, don't worry about this.
            # The main part are the first two lines (everything before the "\n\nNOTES:\n\n\n":
            #   Is checking the .json file for specified tags and storing them as either a
            #   list or a dictionary, depending on the format in the .json (I think?).
            new_file.write("\n\n[ISSUE " + str(i) + ": " + line['category'].upper() + "]\n" +
                           textwrap.fill(line['description'], 70) + ".\n\nFILE: " + line['file'] + "\n" +
                           str(line['location']) +
                           "\n\nNOTES:\n\n\n"
                           "Is this an actual issue?\n\n"
                           "    -\n\n\n"
                           "[COMPLETE?]: ")

            # Will not print this in the last iteration.
            if line is not last:
                new_file.write("\n\n+------------------------------------------------------------------------+")

            # Bug count incrementer.
            i += 1

        # Will write to DeadStoreBug.txt.
        else:
            dead_store_file.write("\n\n[ISSUE " + str(j) + "]\n" +
                                  textwrap.fill(line['description'], 70) + ".\n\nFILE: " + line['file'] + "\n" +
                                  str(line['location']) +
                                  "\n\nNOTES:\n\n\n"
                                  "Is this an actual issue?\n\n"
                                  "    -\n\n\n"
                                  "[COMPLETE?]: ")

            # Will not print this in the last iteration.
            # Did not want to hard-code this, but it did the job for the time being.
            if j < 94:
                dead_store_file.write("\n\n+------------------------------------------------------------------------+")

            # Bug count incrementer.
            j += 1

    # Close out of output files that were opened.
    new_file.close()
    dead_store_file.close()

def fileHeaders(new_file, dead_store_file):

    # Bunch of print statements and formatting that will be done to the new specified file.
    new_file.write("FixedBugReport by Edward M. Abrahamson.\n\n"
                   "Created a script in Python to filter out the unnecessary bug-finding\n"
                   "information from the the beautified \"unique.json\" file (courtesy of Da Kim),\n"
                   "making the information easier to read.\n"
                   "Cut unique.json down from 168,008 lines of text to 3,431 lines of text.\n"
                   "Removed some pieces of info that didn't seem to help much - can add back if\n"
                   "needed.\n\n"
                   "NOTE: Removed \"DEAD STORE\" issues from this output file - we do not\n"
                   "need to do them.  I put them in their own file (\"DeadStoreBugs.txt\")\n"
                   "if anyone is interested in looking at them.\n\n"

                   "BUG BREAKDOWN:"
                   "\n\n0/  6   API Issues          (solved)"
                   "\n0/ 17   Memory Errors       (solved)"
                   "\n0/ 42   Security Issues     (solved)"
                   "\n0/119   Logic Errors        (solved)"
                   "\n.........................................."
                   "\n0/184   Total Issues        (solved)\n\n"
                   "===============================================================================\n")

    # Bunch of print statements and formatting that will be done to the new specified file.
    dead_store_file.write("DEAD STORE bug report by Edward M. Abrahamson.\n\n"
                          "Created a script in Python to filter out the unnecessary bug-finding\n"
                          "information from the the beautified \"unique.json\" file (courtesy of Da Kim),\n"
                          "making the information easier to read.\n"
                          "Cut unique.json down from 168,008 lines of text to 1,712 lines of text.\n"
                          "Removed some pieces of info that didn't seem to help much - can add back if\n"
                          "needed.\n\n"
                          "NOTE: THIS FILE ONLY COVERS THE \"DEAD STORE\" ISSUES THAT WERE CUT FROM\n"
                          "FixedBugReport.txt - WE DO NOT NEED TO DO THESE.\n\n"
                          "*Solving these bugs is just for personal practice*\n\n"

                          "BUG BREAKDOWN:"
                          "\n\n0/ 94   Dead Store Issues     (solved)"
                          "\n.........................................."
                          "\n0/ 94   Total Issues          (solved)\n\n"
                          "===============================================================================\n")

# Not entirely sure if this is how a main function is supposed to be referenced -
#   saw it in a video and thought it seemed legit
if __name__ == "__main__":
    main()
