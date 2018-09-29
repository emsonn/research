# Edward M. Abrahamson
#
# REFERENCE FOR CODE:
# https://stackoverflow.com/questions/23306653/python-accessing-nested-json-data
#
# I've only been coding in Python for a few days now, so let me know if anything should be changed/optimized,
#   as I am brand new to this language.

# The real MVP here
import json

def main():

    # Opens .json file, loads, reads, and stores to variable.
    # Don't have to explicitly close out of this due to how the function works.
    jdata = json.loads(open('unique.json').read())

    # Output file created, will hold all of the information we need, taken from the unique.json file.
    new_file = open("FixedBugFormat.txt", "w")

    # Bunch of print statements, did not know about pretty printing so I did it all manually.
    # Might look a bit gross on some machines.
    # The issue description wraps around the display, whereas my output is hard-coded and might have
    #   to be edited, depending on your machine.
    new_file.write("Edited bug report by Edward M. Abrahamson.\n\n"
                   "Created a script in Python to filter out the unnecessary bug-finding\n"
                   "information from the the beautified unique.json file (courtesy of Da Kim),\n"
                   "making the information easier to read.\n"
                   "Cut the unique.json file from 168,008 lines of text down to 4,751 lines of text.\n"
                   "Removed some pieces of info that didn't seem to help much - can add back if needed.\n\n"
                   "NOTE: For some reason, the 'col', 'file', and 'line' locations switch around sometimes -\n"
                   "probably due to how I read in input.  Regardless, the information is the exact same.\n\n\n"
                
                   "BUG BREAKDOWN:"
                                "\n\n0/  6\tAPI Issues\t\t\t(solved)"
                                "\n0/ 17\tMemory Errors\t\t(solved)"
                                "\n0/ 42\tSecurity Issues\t\t(solved)"
                                "\n0/ 94\tDead Store Issues\t(solved)"
                                "\n0/119\tLogic Errors\t\t(solved)"
                                "\n....................................."
                                "\n0/278\tTotal Issues\t\t(solved)\n\n"
                   "=============================================================================================="
                   "\n\n")

    # Counter variable to keep track of the number of bugs we have to find.
    # Makes talking about a specific bug a LOT easier.
    i = 1

    # Regular for loop that will go through each line in the input .json file
    for line in jdata:

        # Disgusting-looking print formatting, don't worry about this
        # The main part are the first two lines (everything before the "\n\nNOTES:\n\n\n":
        #   Is checking the .json file for certain tags and storing them as a dictionary (I think?)
        #   Not sure how to get the three components of the FILE input to stay constant ('line', 'col', 'file').
        # Also printing out one extra copy of the elongated "+---+" at the end of the file,
        #   not sure how to do that without hard-coding in a counter check for right now.
        new_file.write("\n\n[ISSUE " + str(i) + "!]\t" + str(line['category']).upper() + ": " + line['description'] +
                       ".\n" + "\nFILE: " + line['file'] + "\n" + str(line['location']) +
                       "\n\nNOTES:\n\n\n"
                       "Is this an actual issue?\n\n"
                       "\t-\n\n\n"
                       "[COMPLETE?]: \n\n"
                       "+-------------------------------------------------------------------------------+")

        # Not sure why "i++" is invalid in this language - something with how data is stored maybe?
        i += 1

    # Close out of output file that was opened.
    new_file.close()

# Not entirely sure if this is how a main function is supposed to be referenced -
#   saw it in a video and thought it seemed legit
if __name__ == "__main__":
    main()