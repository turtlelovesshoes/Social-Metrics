from matplotlib import pyplot as plt
import csv
import pandas as pd


#constants and dataframes

#function to open data dump and read into dataframe
def open_twitter(file):
    #df = create_df()
    with open(file) as csvDataFile:
      df = pd.read_csv(csvDataFile)
    return df
#
 # df1 = pd.DataFrame({
  #'Product ID': [1, 2, 3, 4],
  #'Product Name':[ "t-shirt", "skirt"],
  #'Color':[ 'blue', 'green', 'red', 'black']
#})
df1 = open_twitter("convoItems.csv")
print df1
