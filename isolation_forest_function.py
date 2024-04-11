import pandas as pd
import seaborn as sns
from sklearn.ensemble import IsolationForest
import os

def trainModelAndUpdateOuputFile():
    # get the info and column headers for this file.
    df = pd.read_csv("inputDataForTraining.csv")
    print(df)
    # select the columns we want to train based off of.
    anamolly_inputs = ["numberOfTimesClickedAD", "Vpn"]
    print()
    print(df[anamolly_inputs])
    # create isolation forest model.
    # contamination is the percentage of outliers we're expecting
    # random_state allows us to control the random selection process for the splitting
    # of the trees. So if we run this model with the same fixed value and same data
    # and parameters then we should be able to get repeatable outputs. We can set this
    # to a random specific value like 42
    IF_model = IsolationForest(contamination=0.1, random_state=42)
    # we still haven't trained the model which is where the next line comes into play
    # this trains the model from our created data frame and trains it based off of our
    # anamollies we want to detect
    dfWithAnoms = df[anamolly_inputs]
    IF_model.fit(dfWithAnoms)
    # below will give an anamolly score with each sample in the dataset, the lower the
    # more abnormal that sample is compared to the rest of the value
    # negative values indicate outlier.
    # this will give us a new column called anamolly scores
    df['anomaly_scores'] = IF_model.decision_function(dfWithAnoms)
    # create a column within our dataframe, df, that has the score given by the model.
    # -1 indicates an anomaly
    df['anomaly_value'] = IF_model.predict(dfWithAnoms)
    print(df.loc[:, ["IP_Address", "Location", "numberOfTimesClickedAD", "Vpn", 'anomaly_scores', 'anomaly_value'] ])
    print("current dataframe is")
    df.to_csv("outputModelWithPredictions.csv", index=False)



    # we want to create a column that states if a row of data is an outlier or inlier



def modify_data_at_indices(row: int, column: int, value):
    """Below is why we need the indices, it allows us to modify a specific indices values"""
    df = pd.read_csv("inputDataForTraining.csv")
    df.iloc[row, column] = value
    df.to_csv("inputDataForTraining.csv", index=False)
    """End of modifying a specific indices values"""



if __name__ == "__main__":
    trainModelAndUpdateOuputFile()
    modify_data_at_indices(7, 1, "JAPAN")

