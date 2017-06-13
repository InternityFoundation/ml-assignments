import numpy
import numpy as np
#pip3 install numpy
import pandas as pd
import csv
import pylab as p
from pandas import *
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def load_file_train():
    train_df = pd.read_csv("tatanic dataset.txt")
    cols = ["Pclass","Sex","Age"]
    #change male to 1 and female to 0
    train_df["Sex"] = train_df["Sex"].apply(lambda sex:1 if sex=="male" else 0)
    #handle missing values of age
    train_df["Age"] = train_df["Age"].fillna(train_df["Age"].mean())
    train_df["Fare"] = train_df["Fare"].fillna(train_df["Fare"].mean())
    survived = train_df["Survived"].values
    data = train_df[cols].values
    return survived,data
    
def load_file_test():
    train_df = pd.read_csv("../input/test.csv")
    cols = ["Pclass","Sex","Age"]
    #change male to 1 and female to 0
    train_df["Sex"] = train_df["Sex"].apply(lambda sex:1 if sex=="male" else 0)
    #handle missing values of age
    train_df["Age"] = train_df["Age"].fillna(train_df["Age"].mean())
    train_df["Fare"] = train_df["Fare"].fillna(train_df["Fare"].mean())
    data = train_df[cols].values
    return data

def learn_model(survived,data_train,data_test):
    #data_train, data_test, target_train, target_test = cross_validation.train_test_split(data, survived,                                                                                     test_size=0.4, random_state=43)
    model = LogisticRegression()
    model.fit(data_train,survived)
    predicted = model.predict(data_test)
    #evaluate_model(predicted,target_test)
    #my_logit <- data.frame(PassengerId=data_test["PassengerId"], Survived=predicted)
    #write.csv(my_logit, file = "logisticRegressionSubmit.csv")

def main():
    survived, data_train = load_file_train()
    data_test = load_file_test()
    learn_model(survived,data_train,data_test)

# main function
main()

#Any files you save will be available in the output tab below
#train.to_csv('copy_of_the_training_data.csv', index=False)
