# Calculate the Percentage and Count of Male Players

#thousands_of_dollars = data_file_df["Amount"]/1000
#data_file_df["Thousands of Dollars"] = thousands_of_dollars

# Calculate the Percentage and Count of Female Players


# Calculate the Percentage and Count of Other / Non-Disclosed


#data_file_df.head()

# Drop all rows with missing information
exclnull_df = purchase_file_df.dropna(how='any')


grouped_exclnull_df = exclnull_df.groupby(['Gender'])

#total number of players, excluding duplicates
cnt=grouped_exclnull_df["SN"].value_counts().count()
print(cnt)

#ngrp=exclnull_df.groupby("Gender").SN.nunique()
#percent_players= (ngrp / cnt) * 100
#newSummary_df=pd.DataFrame({"Total Count":ngrp,
             #"Percentage of Players":percent_players
              #})
#newSummary_df
