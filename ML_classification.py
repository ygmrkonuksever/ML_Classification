# -*- coding: utf-8 -*-
"""dataMining.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FwU_jzCb-UvFrOn8qiX4WOBFnQiJuYtJ
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
# %matplotlib inline

data = pd.read_csv('drive/MyDrive/heart_disease_health_indicators_BRFSS2015.csv', sep=",")
names = ["HeartDiseaseorAttack","HighBP","HighCholesterol","CholesterolCheck","BMI","Smoker", "Stroke","Diabetes",
         "PhysicalActivity","Fruits","Veggies","HeavyAlcoholConsump","AnyHealthcare","NoDocbcCost", "GeneralHealth","MentalHealth",
        "PhysicalHealth", "WalkingDifficulty", "Sex", "Age", "Education", "Income"]
data             = data.rename(columns=dict(zip(data.columns, names)))

data.isnull().sum()

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
data.HeartDiseaseorAttack= le.fit_transform(data['HeartDiseaseorAttack'])

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

data.head()

dups = data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))

data.info()

data.hist(figsize = (20,15));

"""As the seen in figure 1 classes are imbalanced. Let see their counts"""

data.groupby(['HeartDiseaseorAttack']).size()

"""Sınıflar arasında bu kadar fark varken modelimizi kurarsak düzgün sonuç alamayız. 50-50 dağılımda daha düzgün sonuç alırız"""

#Get the 1s
is1 = data['HeartDiseaseorAttack'] == 1
data_5050_1 = data[is1]

#Get the 0s
is0 = data['HeartDiseaseorAttack'] == 0
data_5050_0 = data[is0] 


data_5050_0_rand1 = data_5050_0.take(np.random.permutation(len(data_5050_0))[:23893])


data_5050 = data_5050_0_rand1.append(data_5050_1, ignore_index = True)

data_5050.head()

data_5050.tail()

#See the classes are perfectly balanced now
data_5050.groupby(['HeartDiseaseorAttack']).size()

"""As the result dataset includes 47.786 instances."""

df_scaled = data_5050.copy()
    # apply maximum absolute scaling
for column in df_scaled.columns:
    df_scaled[column] = df_scaled[column]  / df_scaled[column].abs().max()
print(df_scaled.head())

df_standardize = data_5050.copy()
stdandard_scale = preprocessing.StandardScaler()
for column in df_standardize.columns:
  df_scaled[column] = df_scaled[column]  / df_scaled[column].abs().max()
  df_standardize[column]=stdandard_scale.fit_transform(data_5050[[column]])
df_standardize.head()

corr = df_scaled.corr()
plt.figure(figsize=(20,15))
sns.heatmap(corr, annot=True)
plt.show()

from sklearn.model_selection import train_test_split
predictors = data.drop(["HeartDiseaseorAttack"], axis=1)
target = data["HeartDiseaseorAttack"]
X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.1, random_state = 0)

from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier


models = []
models.append(('Logistic Regression', LogisticRegression()))
models.append(('Naive Bayes', GaussianNB()))
models.append(('Decision Tree (CART)',DecisionTreeClassifier())) 
models.append(('K-NN', KNeighborsClassifier()))
models.append(('SVM', SVC()))
models.append(('Gradient Boosting Classifier', GradientBoostingClassifier()))
models.append(('AdaBoostClassifier', AdaBoostClassifier()))
models.append(('BaggingClassifier', BaggingClassifier()))
models.append(('RandomForestClassifier', RandomForestClassifier()))
models.append(('MLPClassifier', MLPClassifier()))


for name, model in models:
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    from sklearn import metrics
 
    print("%s -> ACC: %%%.2f" % (name,metrics.accuracy_score(y_test, y_pred)*100))
    from sklearn.metrics import classification_report
    print(classification_report(y_test, y_pred))
    print()

predictors = data_5050.drop(["HeartDiseaseorAttack"], axis=1)
target = data_5050["HeartDiseaseorAttack"]
X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.1, random_state = 0)

models = []
models.append(('Logistic Regression', LogisticRegression()))
models.append(('Naive Bayes', GaussianNB()))
models.append(('Decision Tree (CART)',DecisionTreeClassifier())) 
models.append(('K-NN', KNeighborsClassifier()))
models.append(('SVM', SVC()))
models.append(('Gradient Boosting Classifier', GradientBoostingClassifier()))
models.append(('AdaBoostClassifier', AdaBoostClassifier()))
models.append(('BaggingClassifier', BaggingClassifier()))
models.append(('RandomForestClassifier', RandomForestClassifier()))
models.append(('MLPClassifier', MLPClassifier()))


for name, model in models:
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    from sklearn import metrics
 
    print("%s -> ACC: %%%.2f" % (name,metrics.accuracy_score(y_test, y_pred)*100))
    from sklearn.metrics import classification_report
    print(classification_report(y_test, y_pred))
    print()

predictors = df_scaled.drop(["HeartDiseaseorAttack"], axis=1)
target = df_scaled["HeartDiseaseorAttack"]
X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.1, random_state = 0)

models = []
models.append(('Logistic Regression', LogisticRegression()))
models.append(('Naive Bayes', GaussianNB()))
models.append(('Decision Tree (CART)',DecisionTreeClassifier())) 
models.append(('K-NN', KNeighborsClassifier()))
models.append(('SVM', SVC()))
models.append(('Gradient Boosting Classifier', GradientBoostingClassifier()))
models.append(('AdaBoostClassifier', AdaBoostClassifier()))
models.append(('BaggingClassifier', BaggingClassifier()))
models.append(('RandomForestClassifier', RandomForestClassifier()))
models.append(('MLPClassifier', MLPClassifier()))


for name, model in models:
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    from sklearn import metrics
 
    print("%s -> ACC: %%%.2f" % (name,metrics.accuracy_score(y_test, y_pred)*100))
    from sklearn.metrics import classification_report
    print(classification_report(y_test, y_pred))
    print()

from sklearn.model_selection import train_test_split
predictors = df_standardize.drop(["HeartDiseaseorAttack"], axis=1)
target = df_standardize["HeartDiseaseorAttack"]
X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.1, random_state = 0)

models = []
models.append(('Logistic Regression', LogisticRegression()))
models.append(('Naive Bayes', GaussianNB()))
models.append(('Decision Tree (CART)',DecisionTreeClassifier())) 
models.append(('K-NN', KNeighborsClassifier()))
models.append(('SVM', SVC()))
models.append(('Gradient Boosting Classifier', GradientBoostingClassifier()))
models.append(('AdaBoostClassifier', AdaBoostClassifier()))
models.append(('BaggingClassifier', BaggingClassifier()))
models.append(('RandomForestClassifier', RandomForestClassifier()))
models.append(('MLPClassifier', MLPClassifier()))


for name, model in models:
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    from sklearn import metrics
 
    print("%s -> ACC: %%%.2f" % (name,metrics.accuracy_score(y_test, y_pred)*100))
    from sklearn.metrics import classification_report
    print(classification_report(y_test, y_pred))
    print()

import numpy as np
import pandas as pd 

df = pd.read_csv("drive/MyDrive/heart_disease_health_indicators_BRFSS2015.csv")
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True,
                                   test_size=0.20, random_state=42)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE: ", np.round(rmse, 2))

from sklearn.utils import shuffle
X_shuffle, y_shuffle = shuffle(X, y, random_state=42)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(lr, X_shuffle, y_shuffle,
                         scoring="neg_mean_squared_error",
                         cv=5, n_jobs=1)
rmse = np.sqrt(-scores)
print("RMSE values: ", np.round(rmse, 2))
print("RMSE average: ", np.mean(rmse))

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100, criterion="mse",
                           bootstrap=True, oob_score=True, n_jobs=2,
                           random_state=42)

# Defining 3-dimensional hyperparameter space as a Python dictionary
hyperparameter_space = {'max_depth':[None,4,6,8,10,12,15,20], 
                        'min_samples_leaf':[1,2,4,6,8,10,20,30],
                        'max_features':['auto','sqrt','log2']}

from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(rf, param_grid=hyperparameter_space , 
                  scoring="neg_mean_squared_error",
                  n_jobs=2, cv=5, return_train_score=True)

gs.fit(X_train, y_train)
print("Optimal hyperparameter combination: ", gs.best_params_)
print("Mean cross-validated MSE or training score of the best_estimator: ",
       np.sqrt(-gs.best_score_))
gs.best_estimator_.fit(X_train, y_train)
y_pred = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_squared_error as MSE
rmse_test = np.sqrt(MSE(y_test, y_pred))
print("Test score: ", np.round(rmse_test, 2))