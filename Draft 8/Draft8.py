##not finished - numpy datatype does not work with non-uniform Dataset

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
import pandas as pd

import argparse

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
    week_1 = pd.read_csv(args.input_file, delimiter=',')
    week_2 = pd.read_csv(args.second_input_file, delimiter=',')
    week_3 = pd.read_csv(args.third_input_file, delimiter=',')

    # clean file should be: text, tags(not), locale, conver date
    #now what do we do with each of them?
    #later create column with positive/negative
    #print(week_1)
    #only needed for join
    frames = [week_1, week_2, week_3]
    #merge
    weekcomparison = pd.merge(week_1, week_2,left_on='name',right_on='name', suffixes=['_week2', '_week2s'])
    weekcomparison_week3 = pd.merge(weekcomparison,week_3, left_on='name', right_on='name', suffixes=['_week3', '_week3s'])
    #append
    #I think what we really want is an append
    #weekcomparison= week_1.append(week_2)
    #weekcomparison_all = weekcomparison.append(week_3)
    #weekcomparison.columns = ['tag', 'week 1 total', 'week 1 percentage', 'week 2 total', 'week 2 percentage','week 3 total', 'week 3 percentage',]

    #join
    #weekcomparison = pd.concat(frames,axis=1, sort=False)
    #weekcomparison_join = pd.concat(frames, axis=1, join='inner')
    print(weekcomparison)
    print(weekcomparison_week3)
    #only needed for join
    #print(weekcomparison_join)

    #this method may not work 4pm fri  - look for another way to sort the data
    languages = weekcomparison_week3['name'].isin(['EN', 'CS', 'CZ','DA','DE','EL','ES','FR','Hebrew','Hindi', 'IT', 'Indonesian','Italian','JP','Japanese','Korean','Latvian','NL','PL','PT-BR','SL']).reset_index()
    users_isses = weekcomparison_week3[[weekcomparison_week3['name'].isin([])]].reset_index()
    product = weekcomparison_week3['name'].isin(['Pocket','Rocket', 'Rust','SeaMonkey', 'Search Engine','Security','Servo','Sync','Theme','WebVR','activity stream','beta','cloudflare','e10s','esr','firefox android','firefox oS','firefox scout','iOS','lockbox','reality','thunderbird','userchrome','windows phone']).reset_index()
    print(languages)
    #,
    print(user_issues)
    print(product)

    labels = language['name']
    plt.bar(range(len(lang)), )
    plt.xticks(range(len(lang)), labels, rotation= "vertical")
    plt.xlabel("User Issue Languages over First three weeks")
    plt.ylabel("Number of Conversations in Language")
    plt.title("User Issue Languages Supported Firefox 62 Release Week 1 - 3")
    plt.show()


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
