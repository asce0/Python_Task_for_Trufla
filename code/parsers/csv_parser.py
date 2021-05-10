import pandas as pd
import numpy as np

def merge_csv(customers, vehicles): # this function will conbine the two csv into one file
    customers = pd.read_csv(customers)
    vehicles = pd.read_csv(vehicles)
    merged = pd.merge(customers, vehicles, left_on="id", right_on="owner_id", how="left") # merge the files by looking at the customer ID and the owner id
    merged = merged.drop(columns="owner_id")
    merged.to_csv("merged.csv", index=False) # generate the merged csv

def generate_json(): # this function will convert the merged csv file iton json format
    df = pd.read_csv ('merged.csv') # reading merged csv

    #now iterat over each row in merged csv and parse it into Json file
    for idx, group in df.groupby(np.arange(len(df))): 
        group.to_json(f'customer{idx+1}.json', orient='index')

def main():  # main function
    pass


if __name__ == "__main__":
    main()
    