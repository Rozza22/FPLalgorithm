import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sklearn import preprocessing 


gkLastSeasonDataPath = '/home/ruairi/FPL model/savedData/byPosition/GK_23_24_data.csv'
gkData = pd.read_csv(gkLastSeasonDataPath)

# basic plot to visualise some variables
# sns.scatterplot(x='form', y='total_points', data=gkData)
# plt.show()

# x values are ones which will be used to predict points (y)
# x = gkData[['form', 'strength', 'bps', 'clean_sheets', 'expected_goals_conceded', 'ict_index', 'minutes', 'oppStrength', 'penalties_saved', 'saves']]
x = gkData[['form', 'strength', 'oppStrength', 'overallStrength', 'defenceStrength', 'attackStrength', 'value']] # data we know before game
y = gkData['total_points']

# standardization (not needed before Logistic regression or tree based models)
scaler = 

# split into test and training data
# creating train and test sets 
X_train, X_test, y_train, y_test = train_test_split( 
    x, y, test_size=0.3, random_state=101) 

myModel = LinearRegression()
myModel.fit(X_train,y_train)

predictions = myModel.predict(X_test)

# model evaluation 
print('mean_squared_error : ', mean_squared_error(y_test, predictions)) 
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions)) 

# regr = linear_model.LinearRegression()
# regr.fit(x,y)
# xVars = x.columns
# xCoefs = regr.coef_

# coeffsWithNames = pd.DataFrame({'Feature':xVars, 'Coefficient': xCoefs})

# print(coeffsWithNames)


# print([xVars,'\n',regr.coef_])