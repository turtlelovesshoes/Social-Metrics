# plot 3 data sets by week and by tags
# sort
#Count
#Create new data structure for each tag association
#plot
#plot bins and range
#plot product and
# compare weekly a nd plotlanguage seperatly by numbers of volume
#plot user issue from week to week
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def main():
#add arugment speficies which commandline options, in this case -f is the input file
    parser = argparse.ArgumentParser(description='Read the end of a file')
    parser.add_argument('-f', action="store", dest="input_file",
    					help='this is the filename and path argument')
    parser.add_argument('-2f', action="store", dest="second_input_file",
                        					help='this is the filename and path argument of the second data to compare')
    parser.add_argument('-3f', action="store", dest="third_input_file",
                            					help='this is the filename and path argument of the second data to compare')
    #parser.add_argument('-s', action="store", dest="support_tag_file",
                        					#help='this is the filename and path argument for the support tags')
    #parser.add_argument('-p', action="store", dest="product_tag_file",
                        					#help='this is the filename and path argument for the product tags')
    #parser.add_argument('-t', action="store", dest="trending_tag_file",
    #                    					help='this is the filename and path argument for the trending support tags')
    #parser.add_argument('-t', action='store', dest="trending_tag_file", default=None, help="new tags created this release",)
    #this one should be optional
    #parser.add_argument('-l', action="store", dest="language_tag_file",
                        				#	help='this is the filename and path argument for the language tags')
    args = parser.parse_args()

    #read csvs into nps
    week_1 = np.genfromtxt(args.input_file, delimiter = ',')
    week_2 = np.genfromtxt(args.second_input_file, delimiter = ',')
    week_3 = np.genfromtxt(args.third_input_file, delimiter = ',')
    ## clean file should be: text, tags(not), locale, conver date
    #now what do we do with each of them?
    #later create column with positive/negative
    print(week_1)
    #date gives histogram tag over time
    #language gives sorting data
    #tag user category gives pivot of sub language

    ## sort
    #Count
    #Create new data structure for each tag association
    #plot


    #plot bins and range - histogram
    #plot product - need product txt list
    # compare weekly a nd plotlanguage seperatly by numbers of volume
    #plot user issue from week to week
if __name__ == "__main__":
    main()
