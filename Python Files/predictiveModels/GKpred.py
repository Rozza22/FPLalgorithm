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
# sns.scatterplot(x='player_ID', y='total_points', data=gkData)
# plt.show()

# x values are ones which will be used to predict points (y)
# x = gkData[['form', 'strength', 'bps', 'clean_sheets', 'expected_goals_conceded', 'ict_index', 'minutes', 'oppStrength', 'penalties_saved', 'saves']]
a = gkData[['round']]
x = gkData[['form', 'strength', 'oppStrength', 'overallStrength', 'defenceStrength', 'attackStrength', 'value', 'player_ID', 'expectedGsConcededHistory', 'BPShistory', 'ictHistory']] # data we know before game 'valueForMoney',
y = gkData['total_points']

predictiveColumns = pd.concat([a,x,y], axis=1)
predictiveColumns = predictiveColumns.sort_values(['player_ID', 'round'])

# to csv is later on
# predictiveColumns.to_csv('/home/ruairi/FPL model/savedData/byPosition/GKpredictionData.csv')

# standardization (not needed before Logistic regression or tree based models)
scaler = preprocessing.StandardScaler().fit(x)
scaler
xScaled = scaler.transform(x)
xScaled

# split into test and training data
# creating train and test sets 
X_train, X_test, y_train, y_test = train_test_split( 
    xScaled, y, test_size=0.3, random_state=101) 

myModel = LinearRegression()
myModel.fit(X_train,y_train)

predictions = myModel.predict(X_test)
# can make predictions for whole season using 'x'

# model evaluation 
print('mean_squared_error : ', mean_squared_error(y_test, predictions)) 
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions)) 

# making predictions for next 5 games

# def prepFutureData(currentData, numFutureGames=5):
#     futureGames = pd.DataFrame()
#     for i in range(1, numFutureGames + 1):
#         futureGame = currentData.copy()
#         futureGame['round'] = currentData['round'] + i
#         futureGames = pd.concat([futureGames, futureGame], ignore_index=True)

#     futureGamesScaled = scaler.transform(futureGames[x.columns])
#     print(['future games scaled: ', futureGamesScaled])
#     return futureGamesScaled

# currentData = gkData.iloc[-1:]
# futureDataScaled = prepFutureData(currentData)
# futurePredictions = myModel.predict(futureDataScaled)

# Would be just to print off the predicted points from next 5 games
# for i, prediction in enumerate(future_predictions, start=1):
#     print(f"Predicted points for Game {current_data['round'].values[0] + i}: {prediction:.2f}")

# numGKs = gkData['player_ID'].nunique() # number of unique GKs

# futurePredictionsDF = pd.DataFrame(
#     futurePredictions.reshape(numGKs, futureGames),
#     index=gkData['player_ID'].unique(),
#     columns=[f'PredictedGame_{i}' for i in range(1,6)]
# )

# predictiveColumns = predictiveColumns.join(futurePredictionsDF)

# predictiveColumns.reset_index(inplace=True)

# predictiveColumns.to_csv('/home/ruairi/FPL model/savedData/byPosition/GKpredictionData.csv', index=False)

# predictiveColumns = pd.concat([predictiveColumns, futurePredictions], axis=1)


# regr = linear_model.LinearRegression()
# regr.fit(x,y)
# xVars = x.columns
# xCoefs = regr.coef_

# coeffsWithNames = pd.DataFrame({'Feature':xVars, 'Coefficient': xCoefs})

# print(coeffsWithNames)


# print([xVars,'\n',regr.coef_])