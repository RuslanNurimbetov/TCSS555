# --------------------------------------------
# Script Name: text.py
# Author: Kannika Armstrong
# Date: October 14, 2024
# Description: 
#   The script for the TCSS555 Machine Learning Project.
#   to predict the user info from text/comments.
# --------------------------------------------

import csv
import os
import codecs
import random
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import ComplementNB

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

##### Main Method #####
def main():
    # prepare_training_data()
    # prepare_public_data()
    # predict_gender_NB()
    # predict_age_NB()
    # predict_open_LR()
    # predict_neurotic_LR()
    # predict_extrovert_LR()
    # predict_agreeable_LR()
    # predict_conscientious_LR()
    write_predicted_to_table()


    

##### Write the prediction age and gender data into the profile.csv in public-test-data
def write_predicted_to_table():
    y_gender_predicted = predict_gender_NB()
    y_age_predicted = predict_age_NB()
    y_ope_predicted = predict_open_LR()
    y_neu_predicted = predict_neurotic_LR()
    y_ext_predicted = predict_extrovert_LR()
    y_agr_predicted = predict_agreeable_LR()
    y_con_predicted = predict_conscientious_LR()

    # Comment for VM
    # file_path = "../data/public-test-data/profile/profile.csv"
    #----------> uncomment for VM
    file_path = "/home/itadmin/data/public-test-data/profile/profile.csv"

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Convert reader to a list of rows

    header = rows[0]
    for i, row in enumerate(rows[1:], start=0):
        age_range = y_age_predicted[i]
        if age_range == 1:
            row[2]="xx-24"
        elif age_range == 2:
            row[2]="25-34"
        elif age_range == 3:
            row[2]="35-49"
        elif age_range == 4:
            row[2]="50-xx"
        # row[2] = y_age_predicted[i]
        row[3] = y_gender_predicted[i]
        row[4] = y_ope_predicted[i]
        row[5] = y_con_predicted[i]
        row[6] = y_ext_predicted[i]
        row[7] = y_agr_predicted[i]
        row[8] = y_neu_predicted[i]

    # Comment for VM
    # out_path = "../data/public-test-data/profile/profile_predict.csv"
    #----------> uncomment for VM
    out_path = "/data/public-test-data/profile/profile_predict.csv"
    with open(out_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

##### Linear regression to predict agreeable
def predict_agreeable_LR():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")
    
    data_Facebook = df.loc[:,['agr', 'text']]
    # print(data_Facebook)
    
    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # convert text to numerical data
    t_vect = TfidfVectorizer()
    X_train = t_vect.fit_transform(data_train['text'])
    y_train = data_train['agr']

    slRegressor = LinearRegression()
    slRegressor.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = t_vect.transform(data_test['text'])
    y_test = data_test['agr']
    y_test_predicted = slRegressor.predict(X_test)
    
    mse = mean_squared_error(y_test, y_test_predicted)
    mae = mean_absolute_error(y_test, y_test_predicted)
    r2 = r2_score(y_test, y_test_predicted)
    rmse = np.sqrt(mse)

    print("### Score for Agreeable Prediction")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")
    print(f"Root Mean Squared Error: {rmse}")
    print()

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")

    public_data_Facebook = df2.loc[:,['agr', 'text']]
    X_public = t_vect.transform(public_data_Facebook['text'])
    y_agr_predicted = slRegressor.predict(X_public)
    # print(y_agr_predicted)
    # print(len(y_age_predicted))

    # return the list of result
    return y_agr_predicted

##### Linear regression to predict conscientious
def predict_conscientious_LR():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")
    
    data_Facebook = df.loc[:,['con', 'text']]
    # print(data_Facebook)
    
    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # convert text to numerical data
    t_vect = TfidfVectorizer()
    X_train = t_vect.fit_transform(data_train['text'])
    y_train = data_train['con']

    slRegressor = LinearRegression()
    slRegressor.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = t_vect.transform(data_test['text'])
    y_test = data_test['con']
    y_test_predicted = slRegressor.predict(X_test)
    
    mse = mean_squared_error(y_test, y_test_predicted)
    mae = mean_absolute_error(y_test, y_test_predicted)
    r2 = r2_score(y_test, y_test_predicted)
    rmse = np.sqrt(mse)

    print("### Score for Conscientious Prediction")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")
    print(f"Root Mean Squared Error: {rmse}")
    print()

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")

    public_data_Facebook = df2.loc[:,['con', 'text']]
    X_public = t_vect.transform(public_data_Facebook['text'])
    y_con_predicted = slRegressor.predict(X_public)
    # print(y_con_predicted)
    # print(len(y_age_predicted))

    # return the list of result
    return y_con_predicted


##### Linear regression to predict extrovert
def predict_extrovert_LR():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")
    
    data_Facebook = df.loc[:,['ext', 'text']]
    # print(data_Facebook)
    
    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # convert text to numerical data
    t_vect = TfidfVectorizer()
    X_train = t_vect.fit_transform(data_train['text'])
    y_train = data_train['ext']

    slRegressor = LinearRegression()
    slRegressor.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = t_vect.transform(data_test['text'])
    y_test = data_test['ext']
    y_test_predicted = slRegressor.predict(X_test)
    
    mse = mean_squared_error(y_test, y_test_predicted)
    mae = mean_absolute_error(y_test, y_test_predicted)
    r2 = r2_score(y_test, y_test_predicted)
    rmse = np.sqrt(mse)

    print("### Score for Extrovert Prediction")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")
    print(f"Root Mean Squared Error: {rmse}")
    print()

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")

    public_data_Facebook = df2.loc[:,['ext', 'text']]
    X_public = t_vect.transform(public_data_Facebook['text'])
    y_ext_predicted = slRegressor.predict(X_public)
    # print(y_ext_predicted)
    # print(len(y_age_predicted))

    # return the list of result
    return y_ext_predicted

##### Linear regression to predict neurotic
def predict_neurotic_LR():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")
    
    data_Facebook = df.loc[:,['neu', 'text']]
    # print(data_Facebook)
    
    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # convert text to numerical data
    t_vect = TfidfVectorizer()
    X_train = t_vect.fit_transform(data_train['text'])
    y_train = data_train['neu']

    slRegressor = LinearRegression()
    slRegressor.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = t_vect.transform(data_test['text'])
    y_test = data_test['neu']
    y_test_predicted = slRegressor.predict(X_test)
    
    mse = mean_squared_error(y_test, y_test_predicted)
    mae = mean_absolute_error(y_test, y_test_predicted)
    r2 = r2_score(y_test, y_test_predicted)
    rmse = np.sqrt(mse)

    print("### Score for Neurotic Prediction")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")
    print(f"Root Mean Squared Error: {rmse}")
    print()

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")

    public_data_Facebook = df2.loc[:,['neu', 'text']]
    X_public = t_vect.transform(public_data_Facebook['text'])
    y_neu_predicted = slRegressor.predict(X_public)
    # print(y_neu_predicted)
    # print(len(y_age_predicted))

    # return the list of result
    return y_neu_predicted
    

##### Linear regression to predict the open 
def predict_open_LR():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")
    
    data_Facebook = df.loc[:,['ope', 'text']]
    # print(data_Facebook)
    
    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # convert text to numerical data
    t_vect = TfidfVectorizer()
    X_train = t_vect.fit_transform(data_train['text'])
    y_train = data_train['ope']

    slRegressor = LinearRegression()
    slRegressor.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = t_vect.transform(data_test['text'])
    y_test = data_test['ope']
    y_test_predicted = slRegressor.predict(X_test)
    
    mse = mean_squared_error(y_test, y_test_predicted)
    mae = mean_absolute_error(y_test, y_test_predicted)
    r2 = r2_score(y_test, y_test_predicted)
    rmse = np.sqrt(mse)

    print("### Score for Open Prediction")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")
    print(f"Root Mean Squared Error: {rmse}")
    print()

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")

    public_data_Facebook = df2.loc[:,['ope', 'text']]
    X_public = t_vect.transform(public_data_Facebook['text'])
    y_ope_predicted = slRegressor.predict(X_public)
    # print(y_ope_predicted)
    # print(len(y_age_predicted))

    # return the list of result
    return y_ope_predicted



##### Naive Bayes model for gender recognition #####
def predict_age_NB():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")

    data_Facebook = df.loc[:,['age', 'text']]
    # print(data_Facebook)

    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # Training a Naive Bayes model
    count_vect = CountVectorizer()
    X_train = count_vect.fit_transform(data_train['text'])
    y_train = data_train['age']
    clf = MultinomialNB(alpha=0.1)
    clf.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = count_vect.transform(data_test['text'])
    # print(X_test)
    y_test = data_test['age']
    y_test_predicted = clf.predict(X_test)
    # print(len(y_predicted))
    # print(y_predicted)
    # Reporting on classification performance
    print("Accuracy: %.2f" % accuracy_score(y_test,y_test_predicted))
    classes = [1, 2, 3, 4]
    cnf_matrix = confusion_matrix(y_test,y_test_predicted,labels=classes)
    print("Confusion matrix:")
    print(cnf_matrix)

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")

    public_data_Facebook = df2.loc[:,['age', 'text']]
    X_public = count_vect.transform(public_data_Facebook['text'])
    y_age_predicted = clf.predict(X_public)
    # print(y_age_predicted)
    # print(len(y_age_predicted))

    # return the list of result
    return y_age_predicted

    
##### Naive Bayes model for gender recognition #####
def predict_gender_NB():
    # Reading the data into a dataframe and selecting the columns we need
    # Comment for VM
    # df = pd.read_csv("training_list.csv")
    #----------> uncomment for VM
    df = pd.read_csv("/home/itadmin/training_list.csv")

    data_Facebook = df.loc[:,['gender', 'text']]
    # print(data_Facebook)

    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    all_Ids = np.arange(len(data_Facebook))
    # print(all_Ids)
    # random.shuffle(all_Ids)
    test_Ids = all_Ids[0:n]
    train_Ids = all_Ids[n:]
    data_test = data_Facebook.loc[test_Ids, :]
    data_train = data_Facebook.loc[train_Ids, :]

    # Training a Naive Bayes model
    count_vect = CountVectorizer()
    X_train = count_vect.fit_transform(data_train['text'])
    y_train = data_train['gender']
    clf = MultinomialNB(alpha=0.5)
    clf.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = count_vect.transform(data_test['text'])
    # print(X_test)
    y_test = data_test['gender']
    y_test_predicted = clf.predict(X_test)
    # print(len(y_predicted))
    # print(y_predicted)
    # Reporting on classification performance
    print("Accuracy: %.2f" % accuracy_score(y_test,y_test_predicted))
    classes = ["male","female"]
    cnf_matrix = confusion_matrix(y_test,y_test_predicted,labels=classes)
    print("Confusion matrix:")
    print(cnf_matrix)

    # Predicting the data From Naive Bayes model
    # Reading data from the public list
    # Comment for VM
    # df2 = pd.read_csv("public_data_list.csv")
    #----------> uncomment for VM
    df2 = pd.read_csv("/home/itadmin/public_data_list.csv")
    
    public_data_Facebook = df2.loc[:,['gender', 'text']]
    X_public = count_vect.transform(public_data_Facebook['text'])
    y_gender_predicted = clf.predict(X_public)
    # print(y_gender_predicted)
    # print(len(y_gender_predicted))

    # return the list of result
    return y_gender_predicted

##### Method to Prepare the training data by adding the text from text files to the profele.csv #####
def prepare_training_data():
    # Arrays for training data
    # Create empty array for userid, age, gender and five persionality - openness(ope), conscientiousness(con)
    # extroversion(ext), agreeableness(agr), emotional stability(neu)
    userIDArr = []
    ageArr = []
    genderArr = []
    opeArr = []
    conArr = []
    extArr = []
    agrArr = []
    neuArr = []

    # Create Emptyarray for userid and content in text file corresponding with userid in the training data.
    textIDArr = []
    textContentArr = []

    # size of training list table
    w_training_table = 9
    h_training_table = 9500

    # Create the training list as a 2D array
    # Initialize an empty list
    training_list = []

    # Create the empty table and add 0 to all cells to prepare the table
    for y in range(h_training_table):
        # Create a row of zeros
        row = [0] * w_training_table
        # Append the row to the training_list
        training_list.append(row)

    # size of text files table
    w_text_files = 2
    h_text_files = 9500

    # Initialize an empty list
    text_list = []

    # Create the empty table and add 0 to all cells to prepare the table
    for y in range(h_text_files):
        # Create a row of zeros
        row = [0] * w_text_files
        # Append the row to text_list
        text_list.append(row)
    
    # the header is use for output csv file
    header_training = ['userid', 'age', 'gender', 'ope', 'con', 'ext', 'agr', 'neu', 'text']

    # path for the directory of profile.csv
    # Comment for VM
    # path_profile_csv = open('../data/training/profile/profile.csv')
    # ----------> uncomment for VM
    path_profile_csv = open('/home/itadmin/data/training/profile/profile.csv')

    #path for the text files of the training data
    # Comment for VM
    # path_training_data_text = '../data/training/text/'
    # ----------> uncomment for VM
    path_training_data_text = '/home/itadmin/data/training/text/'


    # open training data csv file 
    with path_profile_csv as csv_file:
        read_csv = csv.reader(csv_file, delimiter = ',')

        # skip the first row
        next(csv_file)

        # row count is to count the total of training target
        row_count = 0

        # Get all training  target info into arrays by using for loop
        # and increment the row_count variable
        for row in read_csv:
            userid = row[1]
            age = row[2]
            gender = row[3]
            ope = row[4]
            con = row[5]
            ext = row[6]
            agr = row[7]
            neu = row[8]

            userIDArr.append(userid)
            ageArr.append(age)
            genderArr.append(gender)
            opeArr.append(ope)
            conArr.append(con)
            extArr.append(ext)
            agrArr.append(agr)
            neuArr.append(neu)
            row_count += 1

        # total amount of text files
        row_count_txt_file = 0

        # Use a for loop to insert data into the training data list.
        for row in range(row_count):
            training_list[row][0] = userIDArr[row]
            training_list[row][1] = "%.0f" % float(ageArr[row])
            training_list[row][2] = "%.0f" % float(genderArr[row])
            training_list[row][3] = opeArr[row]
            training_list[row][4] = conArr[row]
            training_list[row][5] = extArr[row]
            training_list[row][6] = agrArr[row]
            training_list[row][7] = neuArr[row]
            row_count_txt_file += 1

        # Convert age number to age range
        # xx-24 = 1; 25-34 = 2; 35-49 = 3; 50-xx = 4;
        # Convert gender number to text
        # 0 = "male", 1 = "female"

        for row in range(len(training_list)):
            for col in range(7):
                if(col == 1):
                    if int(training_list[row][1]) <= 24:
                        training_list[row][1] = 1
                    elif 24 < int(training_list[row][1]) <= 34:
                        training_list[row][1] = 2
                    elif 34 < int(training_list[row][1]) <= 49:
                        training_list[row][1] = 3
                    else:
                        training_list[row][1] = 4
                if(col == 2):
                    if int(training_list[row][2]) == 0:
                        training_list[row][2] = "male"
                    else:
                        training_list[row][2] = "female"
        
        # Use for loop to go over every files in text folder
        for filename in os.listdir(path_training_data_text):   

            # create content variable
            content = ""

            # There is an user id in every text file
            # filename[:-4] is get rid of last four characters for the text file name (.txt)
            textIDArr.append(filename[:-4])

            # UUse the codecs module to handle UnicodeDecodeError in some text files. 
            # The key to solving this issue is setting errors='ignore'.
            contents = codecs.open(path_training_data_text + filename, encoding='utf-8', errors='ignore')

            # Go over content by line
            for line in contents:

                # combine all into the content variable
                content += line

            # Append content in text file to an array
            textContentArr.append(content)

        # Add textIDArr and textContentArr into text_list
        for row in range(row_count_txt_file):
            text_list[row][0] = textIDArr[row]
            text_list[row][1] = textContentArr[row]

        # Compare user ID in training_list and user ID in text_list
        training_list.sort(key=lambda elem: elem[0])
        text_list.sort(key=lambda elem: elem[0])
        for row in range(row_count):
            training_list[row][8] = text_list[row][1]
        
    # create the training list for our model: training_list.csv
    # Comment for VM
    # with codecs.open('training_list.csv', 'w', encoding='utf-8', errors='ignore') as csv_output_file:
    # ----------> uncomment for VM
    with codecs.open('/home/itadmin/training_list.csv', 'w', encoding='utf-8', errors='ignore') as csv_output_file:
        write_csv = csv.writer(csv_output_file, delimiter = ',')
        write_csv.writerow(header_training)
        write_csv.writerows(training_list)
        
    # close all files.
    csv_file.close()
    contents.close()
    csv_output_file.close()

##### Method to Prepare the public data by adding the text from text files to the profele.csv #####
def prepare_public_data():
    # Arrays for data we want to predict
    # Create empty array for userid, age, gender and five persionality - openness(ope), conscientiousness(con)
    # extroversion(ext), agreeableness(agr), emotional stability(neu)
    userIDArr = []
    ageArr = []
    genderArr = []
    opeArr = []
    conArr = []
    extArr = []
    agrArr = []
    neuArr = []

    # Create Emptyarray for userid and content in text file corresponding with userid in the training data.
    textIDArr = []
    textContentArr = []

    # size of training list table
    w_table = 9
    h_table = 334

    # Create the training list as a 2D array
    # Initialize an empty list
    public_data_list = []

    # Create the empty table and add 0 to all cells to prepare the table
    for y in range(h_table):
        # Create a row of zeros
        row = [0] * w_table
        # Append the row to the training_list
        public_data_list.append(row)

    # size of text files table
    w_text_files = 2
    h_text_files = 334

    # Initialize an empty list
    text_list = []

    # Create the empty table and add 0 to all cells to prepare the table
    for y in range(h_text_files):
        # Create a row of zeros
        row = [0] * w_text_files
        # Append the row to text_list
        text_list.append(row)
    
    # the header is use for output csv file
    header_table = ['userid', 'age', 'gender', 'ope', 'con', 'ext', 'agr', 'neu', 'text']

    # path for the directory of profile.csv
    # Comment for VM
    # path_profile_csv = open('../data/public-test-data/profile/profile.csv')
    # ----------> uncomment for VM
    path_profile_csv = open('/home/itadmin/data/public-test-data/profile/profile.csv')

    # path for the text files of the public-test-data data
    # Comment for VM
    # path_public_data_text = '../data/public-test-data/text/'
    # ----------> uncomment for VM
    path_public_data_text = '/home/itadmin/data/public-test-data/text/'

    # open training data csv file 
    with path_profile_csv as csv_file:
        read_csv = csv.reader(csv_file, delimiter = ',')

        # skip the first row
        next(csv_file)

        # row count is to count the total of training target
        row_count = 0

        # Get all training  target info into arrays by using for loop
        # and increment the row_count variable
        for row in read_csv:
            userid = row[1]
            age = row[2]
            gender = row[3]
            ope = row[4]
            con = row[5]
            ext = row[6]
            agr = row[7]
            neu = row[8]

            userIDArr.append(userid)
            ageArr.append(age)
            genderArr.append(gender)
            opeArr.append(ope)
            conArr.append(con)
            extArr.append(ext)
            agrArr.append(agr)
            neuArr.append(neu)
            row_count += 1

        # total amount of text files
        row_count_txt_file = 0

        # Use a for loop to insert data into the training data list.
        for row in range(row_count):
            public_data_list[row][0] = userIDArr[row]
            public_data_list[row][1] = ageArr[row]
            public_data_list[row][2] = genderArr[row]
            public_data_list[row][3] = opeArr[row]
            public_data_list[row][4] = conArr[row]
            public_data_list[row][5] = extArr[row]
            public_data_list[row][6] = agrArr[row]
            public_data_list[row][7] = neuArr[row]
            row_count_txt_file += 1
        # print(public_data_list[0])

        

        # Use for loop to go over every files in text folder
        for filename in os.listdir(path_public_data_text):   

            # create content variable
            content = ""

            # There is an user id in every text file
            # filename[:-4] is get rid of last four characters for the text file name (.txt)
            textIDArr.append(filename[:-4])

            # UUse the codecs module to handle UnicodeDecodeError in some text files. 
            # The key to solving this issue is setting errors='ignore'.
            contents = codecs.open(path_public_data_text + filename, encoding='utf-8', errors='ignore')

            # Go over content by line
            for line in contents:

                # combine all into the content variable
                content += line

            # Append content in text file to an array
            textContentArr.append(content)
        
        # Add textIDArr and textContentArr into text_list
        for row in range(row_count_txt_file):
            text_list[row][0] = textIDArr[row]
            text_list[row][1] = textContentArr[row]

        # Compare user ID in training_list and user ID in text_list
        public_data_list.sort(key=lambda elem: (str(elem[0]) if isinstance(elem[0], int) else elem[0]))
        text_list.sort(key=lambda elem: (str(elem[0]) if isinstance(elem[0], int) else elem[0]))

        for row in range(row_count):
            public_data_list[row][8] = text_list[row][1]
        
    # create the training list for our model: training_list.csv
    # Comment for VM
    # with codecs.open('public_data_list.csv', 'w', encoding='utf-8', errors='ignore') as csv_output_file:
    # ----------> uncomment for VM
    with codecs.open('/home/itadmin/public_data_list.csv', 'w', encoding='utf-8', errors='ignore') as csv_output_file:
        write_csv = csv.writer(csv_output_file, delimiter = ',')
        write_csv.writerow(header_table)
        write_csv.writerows(public_data_list)
        
    # close all files.
    csv_file.close()
    contents.close()
    csv_output_file.close()

if __name__=="__main__":
    main()

