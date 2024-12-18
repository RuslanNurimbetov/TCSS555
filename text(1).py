#!/usr/bin/python3

import pandas as pd
import os
import xml.etree.ElementTree as ET
import argparse
import numpy as np
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import ComplementNB

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


##### Text Classification Using BERT #####
def text_classification_BERT():
    ...


##### Linear regression to predict agreeable #####
def predict_agreeable_LR(train_df, test_df):
    # convert text to numerical data
    tfid_vect = TfidfVectorizer(stop_words='english')
    # X_train = count_vect.fit_transform(train_df['text'])
    X_train = tfid_vect.fit_transform(train_df['text'])
    y_train = train_df['agr']

    # Use Linear Regression
    # slRegressor = LinearRegression()
    # slRegressor.fit(X_train, y_train)

    # Initialize RandomForestRegressor with some basic parameters
    rfRegressor = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42)
    rfRegressor.fit(X_train, y_train)

    # Initialize GradientBoostingRegressor with some basic parameters
    # gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    # gbr.fit(X_train, y_train)

    # Testing theLinear Regression model
    X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    # y_test_predicted = slRegressor.predict(X_test)
    y_test_predicted = rfRegressor.predict(X_test)
    # y_test_predicted = gbr.predict(X_test)
    # print(y_test_predicted)

    # Add the predicted age to the test dataframe using lambda function
    test_df['agr_predicted'] = y_test_predicted
    # print(test_df['agr_predicted'])

##### Linear regression to predict conscientious #####
def predict_conscientious_LR(train_df, test_df):
    # convert text to numerical data
    tfid_vect = TfidfVectorizer(stop_words='english')
    # X_train = count_vect.fit_transform(train_df['text'])
    X_train = tfid_vect.fit_transform(train_df['text'])
    y_train = train_df['con']

    # Use Linear Regression
    # slRegressor = LinearRegression()
    # slRegressor.fit(X_train, y_train)

    # Initialize RandomForestRegressor with some basic parameters
    rfRegressor = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42)
    rfRegressor.fit(X_train, y_train)

    # Initialize GradientBoostingRegressor with some basic parameters
    # gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    # gbr.fit(X_train, y_train)

    # Testing theLinear Regression model
    X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    # y_test_predicted = slRegressor.predict(X_test)
    y_test_predicted = rfRegressor.predict(X_test)
    # y_test_predicted = gbr.predict(X_test)
    # print(y_test_predicted)

    # Add the predicted age to the test dataframe using lambda function
    test_df['con_predicted'] = y_test_predicted
    # print(test_df['con_predicted'])

##### Linear regression to predict extrovert #####
def predict_extrovert_LR(train_df, test_df):
    # convert text to numerical data
    tfid_vect = TfidfVectorizer(stop_words='english')
    # X_train = count_vect.fit_transform(train_df['text'])
    X_train = tfid_vect.fit_transform(train_df['text'])
    y_train = train_df['ext']

    # Use Linear Regression
    # slRegressor = LinearRegression()
    # slRegressor.fit(X_train, y_train)

    # Initialize RandomForestRegressor with some basic parameters
    rfRegressor = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42)
    rfRegressor.fit(X_train, y_train)

    # Initialize GradientBoostingRegressor with some basic parameters
    # gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    # gbr.fit(X_train, y_train)

    # Testing theLinear Regression model
    X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    # y_test_predicted = slRegressor.predict(X_test)
    y_test_predicted = rfRegressor.predict(X_test)
    # y_test_predicted = gbr.predict(X_test)
    # print(y_test_predicted)

    # Add the predicted age to the test dataframe using lambda function
    test_df['ext_predicted'] = y_test_predicted
    # print(test_df['ext_predicted'])

##### Linear regression to predict neurotic #####
def predict_neurotic_LR(train_df, test_df):
    # convert text to numerical data
    tfid_vect = TfidfVectorizer(stop_words='english')
    # X_train = count_vect.fit_transform(train_df['text'])
    X_train = tfid_vect.fit_transform(train_df['text'])
    y_train = train_df['neu']

    # Use Linear Regression
    # slRegressor = LinearRegression()
    # slRegressor.fit(X_train, y_train)

    # Initialize RandomForestRegressor with some basic parameters
    rfRegressor = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42)
    rfRegressor.fit(X_train, y_train)

    # Initialize GradientBoostingRegressor with some basic parameters
    # gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    # gbr.fit(X_train, y_train)

    # Testing theLinear Regression model
    X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    # y_test_predicted = slRegressor.predict(X_test)
    y_test_predicted = rfRegressor.predict(X_test)
    # y_test_predicted = gbr.predict(X_test)
    # print(y_test_predicted)

    # Add the predicted age to the test dataframe using lambda function
    test_df['neu_predicted'] = y_test_predicted
    # print(test_df['neu_predicted'])

##### Linear regression to predict the open #####
def predict_open_LR(train_df, test_df):
    # convert text to numerical data
    tfid_vect = TfidfVectorizer(stop_words='english')
    # X_train = count_vect.fit_transform(train_df['text'])
    X_train = tfid_vect.fit_transform(train_df['text'])
    y_train = train_df['ope']

    # Use Linear Regression
    # slRegressor = LinearRegression()
    # slRegressor.fit(X_train, y_train)

    # Initialize RandomForestRegressor with some basic parameters
    rfRegressor = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42)
    rfRegressor.fit(X_train, y_train)

    # Initialize GradientBoostingRegressor with some basic parameters
    # gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    # gbr.fit(X_train, y_train)

    # Testing theLinear Regression model
    X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    # y_test_predicted = slRegressor.predict(X_test)
    y_test_predicted = rfRegressor.predict(X_test)
    # y_test_predicted = gbr.predict(X_test)
    # print(y_test_predicted)

    # Add the predicted age to the test dataframe using lambda function
    test_df['ope_predicted'] = y_test_predicted
    # print(test_df['ope_predicted'])

##### Naive Bayes model for age recognition #####
def predict_age_NB(train_df, test_df):
    # Training a Naive Bayes model
    count_vect = CountVectorizer(stop_words='english')
    tfid_vect = TfidfVectorizer()
    X_train = count_vect.fit_transform(train_df['text'])
    # X_train = tfid_vect.fit_transform(train_df['text'])
    #test_df['age_range'] = test_df['age'].apply(lambda value: 'xx-24' if value < 25  else ('25-34' if 25 <= value <= 34 else ('35-49' if 35<= value <= 49 else '50-xx')))

    y_train = train_df['age'].apply(lambda value: 'xx-24' if value < 25  else ('25-34' if 25 <= value <= 34 else ('35-49' if 35<= value <= 49 else '50-xx')))
    clf = MultinomialNB(alpha=0.7)
    clf.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = count_vect.transform(test_df['text'])
    # X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    y_test_predicted = clf.predict(X_test)

    # Add the predicted age to the test dataframe using lambda function
    test_df['age_predicted'] = y_test_predicted
    # test_df['age_predicted'] = test_df['age_predicted'].apply(lambda value: 'xx-24' if value < 25  else ('25-34' if 25 <= value <= 34 else ('35-49' if 35<= value <= 49 else '50-xx')))

    # Set up k-fold cross-validation
    k = KFold(n_splits=10, shuffle=False, random_state=None)
    cv_scores = cross_val_score(clf, X_train, y_train, cv=k, scoring='accuracy')

    # Calculate and print the mean accuracy
    # print(f"K-Fold Cross-Validation Accuracy Scores: {cv_scores}")
    # print(f"Age Prediction Mean Accuracy: {cv_scores.mean() * 100:.2f}%")

##### Naive Bayes model for gender recognition #####
def predict_gender_NB(train_df, test_df):
    # Training a Naive Bayes model
    count_vect = CountVectorizer()
    tfid_vect = TfidfVectorizer(stop_words='english')
    X_train = count_vect.fit_transform(train_df['text'])
    # X_train = tfid_vect.fit_transform(train_df['text'])
    y_train = train_df['gender']
    clf = MultinomialNB(alpha=0.3)
    clf.fit(X_train, y_train)

    # Testing the Naive Bayes model
    X_test = count_vect.transform(test_df['text'])
    # X_test = tfid_vect.transform(test_df['text'])
    # Make predictions on the test data
    y_test_predicted = clf.predict(X_test)

    # Add the predicted gender to the test dataframe using lambda function
    test_df['gender_predicted'] = y_test_predicted
    test_df['gender_predicted'] = test_df['gender_predicted'].apply(lambda value: 'male' if value == 0 else 'female')


    # Set up k-fold cross-validation
    k = KFold(n_splits=10, shuffle=False, random_state=None)
    cv_scores = cross_val_score(clf, X_train, y_train, cv=k, scoring='accuracy')

    # Calculate and print the mean accuracy
    # print(f"K-Fold Cross-Validation Accuracy Scores: {cv_scores}")
    # print(f"Gender Prediction Mean Accuracy: {cv_scores.mean() * 100:.2f}%")

##### Function to read the text/comments #####
def read_text(file_dir, userid):
    file_path = os.path.join(file_dir, f'{userid}.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            text = file.read()
            return text
    else:
        return "" 
    
##### Test function to test our model
def model_test_evaluation(train_df):
    # Splitting the data into 8000 training instances and 1500 test instances
    n = 1500
    data_test_df = train_df.iloc[:n]
    data_train_df = train_df.iloc[n:]

    #### test gender prediction model
    gender_data_test_df = data_test_df.copy()
    gender_data_train_df = data_train_df.copy()
    predict_gender_NB(gender_data_train_df, gender_data_test_df)
    # print(data_test_df)

    y_gender_test = gender_data_test_df['gender'].apply(lambda value: 'male' if value == 0 else 'female')
    y_gender_predicted = gender_data_test_df['gender_predicted']
    # Reporting on classification performance
    print("# Gender Prediction")
    print("Accuracy: %.2f" % accuracy_score(y_gender_test,y_gender_predicted))
    classes = ["male","female"]
    cnf_matrix = confusion_matrix(y_gender_test,y_gender_predicted,labels=classes)
    print("Confusion matrix:")
    print(cnf_matrix)

    #### test age prediction model
    age_data_test_df = data_test_df.copy()
    age_data_train_df = data_train_df.copy()
    predict_age_NB(age_data_train_df, age_data_test_df)

    y_age_test = age_data_test_df['age'].apply(lambda value: 'xx-24' if value < 25  else ('25-34' if 25 <= value <= 34 else ('35-49' if 35<= value <= 49 else '50-xx')))
    y_age_predicted = age_data_test_df['age_predicted']
    # Reporting on classification performance
    print("# Age Prediction")
    print("Accuracy: %.2f" % accuracy_score(y_age_test,y_age_predicted))
    classes = ["xx-24","25-34","35-49","50-xx"]
    cnf_matrix = confusion_matrix(y_age_test,y_age_predicted,labels=classes)
    print("Confusion matrix:")
    print(cnf_matrix)

    ### test predict_open_LR model
    open_data_test_df = data_test_df.copy()
    open_data_train_df = data_train_df.copy()
    predict_open_LR(open_data_train_df, open_data_test_df)

    y_open_test = open_data_test_df['ope']
    y_open_predicted = open_data_test_df['ope_predicted']
    mse = mean_squared_error(y_open_test, y_open_predicted)
    mae = mean_absolute_error(y_open_test, y_open_predicted)
    r2 = r2_score(y_open_test, y_open_predicted)
    rmse = np.sqrt(mse)

    print("# Openness Prediction")
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R^2: {r2:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print()

    ### test predict_neurotic_LR model
    neu_data_test_df = data_test_df.copy()
    neu_data_train_df = data_train_df.copy()
    predict_neurotic_LR(neu_data_train_df, neu_data_test_df)

    y_neu_test = neu_data_test_df['neu']
    y_neu_predicted = neu_data_test_df['neu_predicted']
    mse = mean_squared_error(y_neu_test, y_neu_predicted)
    mae = mean_absolute_error(y_neu_test, y_neu_predicted)
    r2 = r2_score(y_neu_test, y_neu_predicted)
    rmse = np.sqrt(mse)

    print("# Neuroticism Prediction")
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R^2: {r2:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print()

    ### test predict_extrovert_LR model
    ext_data_test_df = data_test_df.copy()
    ext_data_train_df = data_train_df.copy()
    predict_extrovert_LR(ext_data_train_df, ext_data_test_df)

    y_ext_test = ext_data_test_df['ext']
    y_ext_predicted = ext_data_test_df['ext_predicted']
    mse = mean_squared_error(y_ext_test, y_ext_predicted)
    mae = mean_absolute_error(y_ext_test, y_ext_predicted)
    r2 = r2_score(y_ext_test, y_ext_predicted)
    rmse = np.sqrt(mse)

    print("# Extroversion Prediction")
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R^2: {r2:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print()

    ### test predict_conscientious_LR model
    con_data_test_df = data_test_df.copy()
    con_data_train_df = data_train_df.copy()
    predict_conscientious_LR(con_data_train_df, con_data_test_df)

    y_con_test = con_data_test_df['con']
    y_con_predicted = con_data_test_df['con_predicted']
    mse = mean_squared_error(y_con_test, y_con_predicted)
    mae = mean_absolute_error(y_con_test, y_con_predicted)
    r2 = r2_score(y_con_test, y_con_predicted)
    rmse = np.sqrt(mse)

    print("# Conscientious Prediction")
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R^2: {r2:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print()

    ### test predict_agreeable_LR model
    agr_data_test_df = data_test_df.copy()
    agr_data_train_df = data_train_df.copy()
    predict_agreeable_LR(agr_data_train_df, agr_data_test_df)

    y_agr_test = agr_data_test_df['agr']
    y_agr_predicted = agr_data_test_df['agr_predicted']
    mse = mean_squared_error(y_agr_test, y_agr_predicted)
    mae = mean_absolute_error(y_agr_test, y_agr_predicted)
    r2 = r2_score(y_agr_test, y_agr_predicted)
    rmse = np.sqrt(mse)

    print("# Agreeableness Prediction")
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R^2: {r2:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print()



##### Generate the output with parsing arguments from the command #####
def save_to_XML_file(input_dir, output_dir):
    # Data path
    training_files_path = 'data/training/profile/profile.csv'
    text_files_dir = 'data/training/text/'
    # Read CSV files
    train_df = pd.read_csv(training_files_path)
    test_df = pd.read_csv(os.path.join(input_dir, 'profile/profile.csv'))

    # Add text/comments into the 'text' column, match with userid using lambda function
    train_df['text'] = train_df['userid'].apply(lambda userid: read_text(text_files_dir, userid))
    test_df['text'] = test_df['userid'].apply(lambda userid: read_text(os.path.join(input_dir, 'text/'), userid))

    # Test model
    # model_test_evaluation(train_df)

    # Predict the gender
    predict_gender_NB(train_df, test_df)

    # Predict the age
    predict_age_NB(train_df, test_df)
   
    # Predict Personality
    predict_open_LR(train_df, test_df)
    predict_conscientious_LR(train_df, test_df)
    predict_extrovert_LR(train_df, test_df)
    predict_agreeable_LR(train_df, test_df)
    predict_neurotic_LR(train_df, test_df)

    for index, row in test_df.iterrows():
        user = ET.Element("user")
        
        user.set("id", str(row['userid']))
        user.set("age_group", str(row['age_predicted']))
        user.set("gender", str(row['gender_predicted']))
        user.set("extrovert", str(row['ext_predicted']))
        user.set("neurotic", str(row['neu_predicted']))
        user.set("agreeable", str(row['agr_predicted']))
        user.set("conscientious", str(row['con_predicted']))
        user.set("open", str(row['ope_predicted']))
    
        file_name = f"{row['userid']}.xml"
        tree = ET.ElementTree(user)
        tree.write(os.path.join(output_dir, file_name), encoding='utf-8', xml_declaration=True)

    # print(f"All the XML files for each userId have been created in the '{output_dir}' directory.")

##### Main method to generate the output with parsing arguments from the command #####
def main():
    parser = argparse.ArgumentParser(description='Check input and output directory paths.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input directory')
    parser.add_argument('-o', '--output', required=True, help='Path to the output directory')
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    # os.makedirs(args.output, exist_ok=True)

    # Call the function to create XML files
    save_to_XML_file(args.input, args.output)

if __name__ == '__main__':
    main()
