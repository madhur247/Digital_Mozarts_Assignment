import pandas as pd    #Importing the pandas library
file = pd.read_csv("data.csv")    #importing the dataset csv file
df = pd.DataFrame(file)    #Converting the file into pandas dataframe

print("Sum of Impressions between age group of 30-34:")    
print(df[df["age"]=="30-34"]["impressions"].sum())     #Putting condition on age=='30-34' and calculating sum of impressions from that data

print("Displaying ad_ids for each campaign_id:")  
camp_id = df[["ad_id","campaign_id"]].groupby("campaign_id").groups #fetching ad-id and campaign-id columns from the dataset and grouping the data by campaign_id

for camp,ad in camp_id.items():
    print(camp,":",ad)  

df1 = df[pd.to_datetime(df["reporting_start"],dayfirst=True)<=pd.to_datetime("22/08/2017",dayfirst=True)]  #Putting condition on reporting_date<='22/08/2017'
df2 = df1[pd.to_datetime(df1["reporting_start"],dayfirst=True)>=pd.to_datetime("19/08/2017",dayfirst=True)]   #Putting further condition on reporting_date>='19/08/2017'
print("Sum of clicks between reporting_start date 19/08/2017 and 22/08/2017 (inclusive):") 
print(df2["clicks"].sum())   #Calculating sum of clicks from the filtered dataset 