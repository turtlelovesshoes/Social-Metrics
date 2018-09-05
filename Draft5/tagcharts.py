#Draft 5 of supported.py
#patch includes command line and read tag file
#ideally in the future, jupiter notebooks are helpful
#Note Dataset should  already be filtered by AoA and Help Me
#this also assumes that you have gone through the tags and triagged the corrections (ex CEO properly labeled)
import csv
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys

#constants
support_tags = []
trending_tags = []
language_tags = []
product_tags = []
#create list from file

#Tag - Firefox iOS, Android, Firefox Focus, Rocket
def opentag_savelist(file): #program to read tags into a list
    with open(file) as f:
        tags = f.readlines()
    tags = [x.strip() for x in tags]
    return tags
def plot_one_data(x, y, labels, xlabel, ylabel, title):
    plt.bar(x, y)
    plt.xticks(x, labels, rotation= "vertical")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def main():
#add arugment speficies which commandline options, in this case -f is the input file
    parser = argparse.ArgumentParser(description='Read the end of a file')
    parser.add_argument('-f', action="store", dest="input_file",
    					help='this is the filename and path argument')
    parser.add_argument('-s', action="store", dest="support_tag_file",
                        					help='this is the filename and path argument for the support tags')
    parser.add_argument('-p', action="store", dest="product_tag_file",
                        					help='this is the filename and path argument for the product tags')
    #parser.add_argument('-t', action="store", dest="trending_tag_file",
    #                    					help='this is the filename and path argument for the trending support tags')
    parser.add_argument('-t', action='store', dest="trending_tag_file", default=None, help="new tags created this release",)
    parser.add_argument('-l', action="store", dest="language_tag_file",
                        					help='this is the filename and path argument for the language tags')
    args = parser.parse_args()

    #save csv dump all data as dataframes
    with open(args.input_file) as file:
            df = pd.read_csv(file)

    # to remove whitespace characters like `\n` at the end of each line
    support_tags = opentag_savelist(args.support_tag_file)
    trending_tags = opentag_savelist(args.trending_tag_file)
    language_tags = opentag_savelist(args.language_tag_file)
    product_tags = opentag_savelist(args.product_tag_file)
    #print(support_tags, trending_tags, language_tags, product_tags)
    #split the tags to many columns where 'none' is default
    #   0 1 2 3
    #0  EN None none
    #1  AoA Solved DNE
    #2
    num = df.tags.str.split(',',expand=True).apply(Counter)
    #now the rows are each counter objects that need to be combined

    final = Counter()
    for i,row in num.iteritems():
        final = final + row
    #a = num[0]
    #b = num[1]
    #c = num[2]
    #d = num[3]
    #e = num[4]
    #f = num[5]
    #final = a+b+c+d+e
    final
     #plot user issues
    plot_one_data(range(len(final)), final.values(), final.keys(), "User Issue Categories", "Conversations about that User Issue", "User Issue Categories Firefox 62 Release Day 1")

    categories = {}
    data_totals = {}
    #Grab all the Categories for Defined user issues:
    for x,y in final.items():
        for i in support_tags:
           if (x == i) & (x not in categories):
               l=final[x]
               categories.update({x:l})
           if (x == "AoA") or (x == "Help Me"):
              l = final[x]
              data_totals.update({x:l})

    print("totals ^")
    print(data_totals)
    #New tags and trends created for release or during
    new_release_categories = {}
    for x,y in final.items():
        for i in trending_tags:
            if x == i:
               l = final[x]
               new_release_categories.update({x:l})
    print(new_release_categories)

    plt.gcf().clear()
    ## Plot two subplots for trends
    plt.subplots()

    plt.subplot(2,1,1)
    ax1 = plt.subplot(2,1,1)
    labels1 = categories.keys()
    pos = np.arange(len(labels1))

    ax1.bar(pos,categories.values(), log = 1)
    ax1.set_xticks(pos)
    ax1.set_xticklabels(labels1, rotation= 30 )
    plt.xlabel("User Issue Categories")
    #plt.ylabel("# Support Conversations")
    plt.title("User Issue Categories Firefox 62 Release Day 1 1")


    plt.subplot(2,1,2)
    ax = plt.subplot(2,1,2)
    labels = new_release_categories.keys()
    pos2 = np.arange(len(labels))
    plt.bar(range(len(labels)), new_release_categories.values())
    ax.set_xticks(pos2)
    ax.set_xticklabels(labels, rotation= 30 )
    plt.xlabel("New User Issue Categories")
    #plt.ylabel("# Support Conversations")
    plt.title("New User Issue Categories Firefox 62 Release Day 1 1")

    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.3   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.2   # the amount of width reserved for blank space between subplots
    hspace = 0.5

    plt.subplots_adjust(left=0.125, bottom=0.3, right=.9, top=0.9, wspace=None, hspace=0.9)

    plt.show()
    plt.gcf().clear()
    #Grab all Help Me - count instances of other tags
    #Dataset is already filtered by AoA and Help Me

    #Grab all Language counts
    #EN, ES, CS, TR, FR, PT_BR, NL
    lang = {}
    for x,y in final.items():
       for i in language_tags:
           if x == i:
              l = final[x]
              lang.update({x:l})
    #    if (x == 'EN') or (x =='ES') or (x =='CZ') or (x =='TR') or (x =='FR') or (x == 'DE') or (x == 'PT-BR'):
    #       lang.update({x:y})

    #plot languages
    labels = lang.keys()
    plt.bar(range(len(lang)), lang.values())
    plt.xticks(range(len(lang)), labels, rotation= "vertical")
    plt.xlabel("User Issue Languages")
    plt.ylabel("Number of Conversations in Language")
    plt.title("User Issue Languages Supported Firefox 62 Release Day 1 1")
    plt.show()

if __name__ == "__main__":
    main()
    #Show all non-help me tags by language

    #Grab A0A volume vs total #help me with response time
