HI!

THis is the social metrics project where we are iterating on creating graphs to answer questions about social support. 

Draft #highest number is the most recent creating#
#index has all the questions that we want to answer in the program with the current export data that we can access and report to others at Mozilla#

#All of the data is private, but is public information on Twitter# 

Latest update Draft 5 folder: 
Needed: 
1. Whole directory
2. Updated tending tag file the txt should include a new tag created on each line
3. Export conversations details from Reports section of Reply by Buffer (one day or week of data)
4. Filter the css output to just Help Me and AoA tags (this is what we identified as ‘support conversations’)
5. Run the script with this new css file and with all of the tag files
6. Save the graphs
7.Save Data description
8. Read all conversations and add notes to describe each category 
9. If solved - a reply time will be present (search in spreadsheet for tag for the fastest way to find )


To run this script with the daily output use the command below: 

MacBook-Pro-20:Draft5 rmcguigan$ python tagcharts.py -f Week1Sept5.csv -s supporttags.txt -p producttags.txt -t trendingtags.txt -l languagetags.txt


Three graphs will generate, save each one then close them. 

This will appear in the console - record this for the data description section of your report
totals ^

{'Help Me': 44, 'AoA': 11}
{'New Release': 2}

Good Luck!

Open Lisence
