# -*- coding: utf-8 -*-
"""DDOSUINGMOUNTING.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13Ouh3SpIwH9kfcvMx4KX-WFGfiXf2eVM
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import GridSearchCV
import time

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn import metrics

path ="/content/drive/MyDrive/dataset/dataset_sdn.csv"
data = pd.read_csv(path)
data1 = data
data.head(5)

#shows rows and columns
data.shape

data.info()

##### Here we see that the label contains boolean values: 0 - Benign, 1-Maliciuous
data.label.unique()

data.label.value_counts()

label_dict = dict(data.label.value_counts())
sns.countplot(data.label)

labels = ["Benign",'Maliciuous']
sizes = [dict(data.label.value_counts())[0], dict(data.label.value_counts())[1]]
plt.figure(figsize = (13,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.legend(["Bening", "Maliciuous"])
plt.title('The percentage of Benign and Maliciuos Requests in dataset')
plt.show()

data.describe()

# Let's look at the vizualisation of Null valued features
figure(figsize=(9, 5), dpi=80)
data[data.columns[data.isna().sum() >= 0]].isna().sum().sort_values().plot.bar()
plt.title("Features which has NuLL values")

data.isnull().sum()

#hadling null values

mean_rx_kbps = data['rx_kbps'].mean()
mean_tot_kbps = data['tot_kbps'].mean()

data['rx_kbps'].fillna(mean_rx_kbps, inplace=True)
data['tot_kbps'].fillna(mean_tot_kbps, inplace=True)

print(data.isnull().sum())

#### Let's support which columns NUMERIC and which is OBJECT

numeric_df = data.select_dtypes(include=['int64', 'float64'])
object_df = data.select_dtypes(include=['object'])
numeric_cols = numeric_df.columns
object_cols = object_df.columns
print('Numeric Columns: ')
print(numeric_cols, '\n')
print('Object Columns: ')
print(object_cols, '\n')
print('Number of Numeric Features: ', len(numeric_cols))
print('Number of Object Features: ', len(object_cols))

object_df.head()



#### Let's look at Oblect columns (Source Destination Protocol)

figure(figsize=(12, 7), dpi=80)
plt.barh(list(dict(data.src.value_counts()).keys()), dict(data.src.value_counts()).values(), color='lawngreen')

for idx, val in enumerate(dict(data.src.value_counts()).values()):
    plt.text(x = val, y = idx-0.2, s = str(val), color='r', size = 13)

plt.xlabel('Number of Requests')
plt.ylabel('IP addres of sender')
plt.title('Number of all reqests')



figure(figsize=(12, 7), dpi=80)
plt.barh(list(dict(data[data.label == 1].src.value_counts()).keys()), dict(data[data.label == 1].src.value_counts()).values(), color='blue')

for idx, val in enumerate(dict(data[data.label == 1].src.value_counts()).values()):
    plt.text(x = val, y = idx-0.2, s = str(val), color='r', size = 13)

plt.xlabel('Number of Requests')
plt.ylabel('IP addres of sender')
plt.title('Number of Attack requests')

figure(figsize=(12, 7), dpi=80)
plt.barh(list(dict(data.src.value_counts()).keys()), dict(data.src.value_counts()).values(), color='lawngreen')
plt.barh(list(dict(data[data.label == 1].src.value_counts()).keys()), dict(data[data.label == 1].src.value_counts()).values(), color='blue')

for idx, val in enumerate(dict(data.src.value_counts()).values()):
    plt.text(x = val, y = idx-0.2, s = str(val), color='r', size = 13)

for idx, val in enumerate(dict(data[data.label == 1].src.value_counts()).values()):
    plt.text(x = val, y = idx-0.2, s = str(val), color='w', size = 13)


plt.xlabel('Number of Requests')
plt.ylabel('IP addres of sender')
plt.legend(['All','malicious'])
plt.title('Number of requests from different IP adress')

figure(figsize=(10, 6), dpi=80)
plt.bar(list(dict(data.Protocol.value_counts()).keys()), dict(data.Protocol.value_counts()).values(), color='r')
plt.bar(list(dict(data[data.label == 1].Protocol.value_counts()).keys()), dict(data[data.label == 1].Protocol.value_counts()).values(), color='b')

plt.text(x = 0 - 0.15, y = 41321 + 200, s = str(41321), color='black', size=17)
plt.text(x = 1 - 0.15, y = 33588 + 200, s = str(33588), color='black', size=17)
plt.text(x = 2 - 0.15, y = 29436 + 200, s = str(29436), color='black', size=17)

plt.text(x = 0 - 0.15, y = 9419 + 200, s = str(9419), color='w', size=17)
plt.text(x = 1 - 0.15, y = 17499 + 200, s = str(17499), color='w', size=17)
plt.text(x = 2 - 0.15, y = 13866 + 200, s = str(13866), color='w', size=17)

plt.xlabel('Protocol')
plt.ylabel('Count')
plt.legend(['All', 'malicious'])
plt.title('The number of requests from different protocols')

# #perform label encoding
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# # Assuming you have your data in a pandas DataFrame named 'data'
# categorical_cols = data.select_dtypes(include=['object'])

# # Create a LabelEncoder object for each categorical column
# encoders = {}
# for col in categorical_cols:
#     encoders[col] = LabelEncoder()

# # Encode each categorical column
# for col in categorical_cols:
#     data[col] = encoders[col].fit_transform(data[col])

data.head(10)

# perform one-hot encoding on the Data
#it performs better than label encoding
data = pd.get_dummies(data)
data.head(5)

#### Let's support which columns NUMERIC and which is OBJECT

numeric_df = data.select_dtypes(include=['int64', 'float64'])
object_df = data.select_dtypes(include=['object'])
numeric_cols = numeric_df.columns
object_cols = object_df.columns
print('Numeric Columns: ')
print(numeric_cols, '\n')
print('Object Columns: ')
print(object_cols, '\n')
print('Number of Numeric Features: ', len(numeric_cols))
print('Number of Object Features: ', len(object_cols))

df = data.copy()

figure(figsize=(8, 4), dpi=80)
plt.hist(df.dur, bins=20, color='b')
plt.title('Duration')
plt.show()

figure(figsize=(8, 4), dpi=80)
plt.hist(df.tx_bytes, bins=20, color='r')
plt.title('TX_BYTES - Transmitted Bytes')
plt.show()

figure(figsize=(8, 4), dpi=80)
plt.hist(df.tx_kbps, bins=10, color='g')
plt.title('TX_KBPC')
plt.show()

plt.hist(df.switch, bins=20, color='r')
plt.title('SWITCH')
plt.xlabel('SWITCH')
plt.show()

plt.hist(df[df['label'] == 1].switch, bins=20, color='r')
plt.title('SWITCH')
plt.xlabel('SWITCH')
plt.show()

class Model:
    global y
    def __init__(self, data):
        self.data = data
        X = preprocessing.StandardScaler().fit(self.data).transform(self.data)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, random_state=42, test_size=0.3)

    def LogisticRegression(self):
        solvers = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
        start_time = time.time()
        results_lr = []
        accuracy_list = []
        for solver in solvers:
            LR = LogisticRegression(C=0.03, solver=solver).fit(self.X_train, self.y_train)
            predicted_lr = LR.predict(self.X_test)
            accuracy_lr = accuracy_score(self.y_test, predicted_lr)
            #print("Accuracy: %.2f%%" % (accuracy_lr * 100.0))
            #print('################################################################')
            results_lr.append({'solver' : solver, 'accuracy': str(round(accuracy_lr * 100, 2)) + "%",
                                  'Coefficients': {'W' : LR.coef_, 'b': LR.intercept_}})

            accuracy_list.append(accuracy_lr)

        solver_name = solvers[accuracy_list.index(max(accuracy_list))]
        LR = LogisticRegression(C=0.03, solver=solver_name).fit(self.X_train,self.y_train)
        predicted_lr = LR.predict(self.X_test)
        accuracy_lr = accuracy_score(self.y_test, predicted_lr)
        print("Accuracy: %.2f%%" % (accuracy_lr * 100.0), '\n')
        print("########################################################################")
        print('Best solver is : ', solver_name)
        print("########################################################################")
        print(classification_report(predicted_lr, self.y_test), '\n')
        print("########################################################################")
        print("--- %s seconds --- time for LogisticRegression" % (time.time() - start_time))


    def SupportVectorMachine(self):
        start_time = time.time()
        accuracy_list = []
        result_svm = []
        kernels = ['linear', 'poly','rbf', 'sigmoid']
        #kernels = ['rbf']
        for kernel in kernels:
            SVM = svm.SVC(kernel=kernel).fit(self.X_train, self.y_train)
            predicted_svm = SVM.predict(self.X_test)
            accuracy_svm = accuracy_score(self.y_test, predicted_svm)
            result_svm.append({"kernel" : kernel, "accuracy": f"{round(accuracy_svm*100,2)}%"})
            print("Accuracy: %.2f%%" % round((accuracy_svm * 100.0),2))
            print('######################################################################')
            accuracy_list.append(accuracy_svm)

        kernel_name = kernels[accuracy_list.index(max(accuracy_list))]
        SVM = svm.SVC(kernel=kernel_name).fit(self.X_train, self.y_train)
        predicted_svm = SVM.predict(self.X_test)
        accuracy_svm = accuracy_score(self.y_test, predicted_svm)
        print(f"Accuracy of SVM model {round(accuracy_svm,2)*100}%", '\n')
        print("########################################################################")
        print('best kernel is : ', kernel_name)
        print("########################################################################")
        print(classification_report(predicted_svm, self.y_test))
        print("########################################################################")
        print("--- %s seconds ---" % (time.time() - start_time))

    def KNearetsNeighbor(self):
        start_time = time.time()
        Ks = 12
        accuracy_knn = np.zeros((Ks-1))
        std_acc = np.zeros((Ks-1))
        #print(accuracy_knn)
        for n in range(1,Ks):

            #Train Model and Predict
            neigh = KNeighborsClassifier(n_neighbors = n).fit(self.X_train,self.y_train)
            yhat=neigh.predict(self.X_test)
            accuracy_knn[n-1] = metrics.accuracy_score(self.y_test, yhat)


            std_acc[n-1]=np.std(yhat==self.y_test)/np.sqrt(yhat.shape[0])

        #print(accuracy_knn,'\n\n') # courseranyn ozinde tek osy gana jazylyp turdy
        #print(std_acc)
        #accuracy_knn[0] = 0
        plt.figure(figsize=(10,6))
        plt.plot(range(1,Ks),accuracy_knn,'g')
        plt.fill_between(range(1,Ks),accuracy_knn - 1 * std_acc,accuracy_knn + 1 * std_acc, alpha=0.10)
        plt.fill_between(range(1,Ks),accuracy_knn - 3 * std_acc,accuracy_knn + 3 * std_acc, alpha=0.10,color="green")
        plt.legend(('Accuracy ', '+/- 1xstd','+/- 3xstd'))
        plt.ylabel('Accuracy ')
        plt.xlabel('Number of Neighbors (K)')
        plt.tight_layout()
        plt.show()


        knnc = KNeighborsClassifier()
        knnc_search = GridSearchCV(knnc, param_grid={'n_neighbors': [3, 5, 10],
                                             'weights': ['uniform', 'distance'],
                                             'metric': ['euclidean', 'manhattan']},
                           n_jobs=-1, cv=3, scoring='accuracy', verbose=2)

        knnc_search.fit(self.X_train, self.y_train)
        #print(knnc_search.best_params_)
        #print(knnc_search.best_score_)
        n_neighbors = knnc_search.best_params_['n_neighbors']
        weights = knnc_search.best_params_['weights']
        metric = knnc_search.best_params_['metric']
        KNN = KNeighborsClassifier(n_neighbors=n_neighbors, metric=metric, weights=weights).fit(self.X_train,self.y_train)

        predicted_knn = KNN.predict(self.X_test)
        accuracy_knn = metrics.accuracy_score(self.y_test, predicted_knn)
        print(f"Accuracy of KNN model {round(accuracy_knn,2)*100}%", '\n')
        print("########################################################################")
        print(classification_report(predicted_knn, self.y_test))
        print("########################################################################")
        print("--- %s seconds ---" % (time.time() - start_time))


    def DecisionTree(self):
        start_time = time.time()
        tree = DecisionTreeClassifier()
        dt_search = GridSearchCV(tree, param_grid={'criterion' : ['gini', 'entropy'],
                                           'max_depth' : [2,3,4,5,6,7,8, 9, 10],
                                           'max_leaf_nodes' : [2,3,4,5,6,7,8,9,10, 11]},
                           n_jobs=-1, cv=5, scoring='accuracy', verbose=2)

        dt_search.fit(self.X_train, self.y_train)

        criterion = dt_search.best_params_['criterion']
        max_depth = dt_search.best_params_['max_depth']
        max_leaf_nodes = dt_search.best_params_['max_leaf_nodes']

        dtree = DecisionTreeClassifier(criterion=criterion,
                                       max_depth=max_depth,
                                       max_leaf_nodes=max_leaf_nodes).fit(self.X_train, self.y_train)
        predicted_dt = dtree.predict(self.X_test)
        accuracy_dt = metrics.accuracy_score(self.y_test, predicted_dt)
        print(f"criterion: {criterion}, max depth: {max_depth}, max_leaf: {max_leaf_nodes}")
        print(f"The Accuracy is : {round(accuracy_dt * 100,2)}%")
        print("########################################################################")
        print(classification_report(predicted_dt, self.y_test))
        print("########################################################################")

        print("--- %s seconds ---" % (time.time() - start_time))

    def RandomForest(self):
        start_time = time.time()
        RF = RandomForestClassifier(criterion='gini',
                                     n_estimators=500,
                                     min_samples_split=10,
                                     #min_samples_leaf=1,
                                     max_features='auto',
                                     oob_score=True,
                                     random_state=1,
                                     n_jobs=-1).fit(self.X_train, self.y_train)

        predicted_rf = RF.predict(self.X_test)
        svm_accuracy = accuracy_score(self.y_test, predicted_rf)
        print(f"Accuracy of RF is : {round(svm_accuracy*100,2)}%", '\n')
        print("########################################################################")
        print(classification_report(predicted_rf, self.y_test))
        print("########################################################################")

        print("--- %s seconds ---" % (time.time() - start_time))



df = data.copy()
df = df.dropna() #removes any rows from the DataFrame df that contain missing values and returns a new DataFrame with those rows removed.

X = df.drop(['label'], axis=1)
y = df.label

#X = pd.get_dummies(X)
#he code X = pd.get_dummies(X) in Python using the pandas library performs one-hot encoding on the DataFrame X

M = Model(X)

## Logistic Regression(Without FS)
M.LogisticRegression()

M.DecisionTree()

## Support Vector Machine(Without FS)
M.SupportVectorMachine()

## Random Forest Classification(Without FS)
M.RandomForest()

M.KNearetsNeighbor()

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_predict, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import time

class NewModel:
    global y

    def __init__(self, data):
        self.data = data
        X = StandardScaler().fit(self.data).transform(self.data)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, random_state=42, test_size=0.3)

    def LogisticRegression(self):
        solvers = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
        best_accuracy_5fold = 0
        best_accuracy_10fold = 0
        best_solver_5fold = ''
        best_solver_10fold = ''

        for solver in solvers:
            LR = LogisticRegression(C=0.03, solver=solver)
            # Perform 5-fold cross-validation
            lr_cv_pred_5fold = cross_val_predict(LR, self.X_train, self.y_train, cv=5)
            accuracy_lr_5fold = accuracy_score(self.y_train, lr_cv_pred_5fold)
            if accuracy_lr_5fold > best_accuracy_5fold:
                best_accuracy_5fold = accuracy_lr_5fold
                best_solver_5fold = solver
                lr_conf_matrix_5fold = confusion_matrix(self.y_train, lr_cv_pred_5fold)
                lr_classification_report_5fold = classification_report(self.y_train, lr_cv_pred_5fold)

            # Perform 10-fold cross-validation
            lr_cv_pred_10fold = cross_val_predict(LR, self.X_train, self.y_train, cv=10)
            accuracy_lr_10fold = accuracy_score(self.y_train, lr_cv_pred_10fold)
            if accuracy_lr_10fold > best_accuracy_10fold:
                best_accuracy_10fold = accuracy_lr_10fold
                best_solver_10fold = solver
                lr_conf_matrix_10fold = confusion_matrix(self.y_train, lr_cv_pred_10fold)
                lr_classification_report_10fold = classification_report(self.y_train, lr_cv_pred_10fold)

        print("For 5 fold cross validation:")
        print("Best solver is:", best_solver_5fold)
        print("Best accuracy:", round(best_accuracy_5fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(lr_conf_matrix_5fold)
        print("Classification Report:")
        print(lr_classification_report_5fold)

        print("\nFor 10 fold cross validation:")
        print("Best solver is:", best_solver_10fold)
        print("Best accuracy:", round(best_accuracy_10fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(lr_conf_matrix_10fold)
        print("Classification Report:")
        print(lr_classification_report_10fold)

    def DecisionTree(self):
        start_time = time.time()
        tree = DecisionTreeClassifier()
        dt_search = GridSearchCV(tree, param_grid={'criterion' : ['gini', 'entropy'],
                                           'max_depth' : [2,3,4,5,6,7,8, 9, 10],
                                           'max_leaf_nodes' : [2,3,4,5,6,7,8,9,10, 11]},
                           n_jobs=-1, cv=5, scoring='accuracy', verbose=2)

        dt_search.fit(self.X_train, self.y_train)

        criterion = dt_search.best_params_['criterion']
        max_depth = dt_search.best_params_['max_depth']
        max_leaf_nodes = dt_search.best_params_['max_leaf_nodes']

        dtree = DecisionTreeClassifier(criterion=criterion,
                                       max_depth=max_depth,
                                       max_leaf_nodes=max_leaf_nodes)
        # Perform 5-fold cross-validation
        dt_cv_pred_5fold = cross_val_predict(dtree, self.X_train, self.y_train, cv=5)
        dt_conf_matrix_5fold = confusion_matrix(self.y_train, dt_cv_pred_5fold)
        dt_classification_report_5fold = classification_report(self.y_train, dt_cv_pred_5fold)
        accuracy_dt_5fold = accuracy_score(self.y_train, dt_cv_pred_5fold)

        # Perform 10-fold cross-validation
        dt_cv_pred_10fold = cross_val_predict(dtree, self.X_train, self.y_train, cv=10)
        dt_conf_matrix_10fold = confusion_matrix(self.y_train, dt_cv_pred_10fold)
        dt_classification_report_10fold = classification_report(self.y_train, dt_cv_pred_10fold)
        accuracy_dt_10fold = accuracy_score(self.y_train, dt_cv_pred_10fold)

        print("For Decision Tree - 5 fold cross validation:")
        print("Best parameters - criterion:", criterion, "max depth:", max_depth, "max_leaf_nodes:", max_leaf_nodes)
        print("Accuracy:", round(accuracy_dt_5fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(dt_conf_matrix_5fold)
        print("Classification Report:")
        print(dt_classification_report_5fold)

        print("\nFor Decision Tree - 10 fold cross validation:")
        print("Best parameters - criterion:", criterion, "max depth:", max_depth, "max_leaf_nodes:", max_leaf_nodes)
        print("Accuracy:", round(accuracy_dt_10fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(dt_conf_matrix_10fold)
        print("Classification Report:")
        print(dt_classification_report_10fold)

        print("--- %s seconds ---" % (time.time() - start_time))

    def RandomForest(self):
        start_time = time.time()
        RF = RandomForestClassifier(criterion='gini',
                                     n_estimators=500,
                                     min_samples_split=10,
                                     max_features='auto',
                                     oob_score=True,
                                     random_state=1,
                                     n_jobs=-1)
        # Perform 5-fold cross-validation
        rf_cv_pred_5fold = cross_val_predict(RF, self.X_train, self.y_train, cv=5)
        rf_conf_matrix_5fold = confusion_matrix(self.y_train, rf_cv_pred_5fold)
        rf_classification_report_5fold = classification_report(self.y_train, rf_cv_pred_5fold)
        accuracy_rf_5fold = accuracy_score(self.y_train, rf_cv_pred_5fold)

        # Perform 10-fold cross-validation
        rf_cv_pred_10fold = cross_val_predict(RF, self.X_train, self.y_train, cv=10)
        rf_conf_matrix_10fold = confusion_matrix(self.y_train, rf_cv_pred_10fold)
        rf_classification_report_10fold = classification_report(self.y_train, rf_cv_pred_10fold)
        accuracy_rf_10fold = accuracy_score(self.y_train, rf_cv_pred_10fold)

        print("For Random Forest - 5 fold cross validation:")
        print("Accuracy:", round(accuracy_rf_5fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(rf_conf_matrix_5fold)
        print("Classification Report:")
        print(rf_classification_report_5fold)

        print("\nFor Random Forest - 10 fold cross validation:")
        print("Accuracy:", round(accuracy_rf_10fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(rf_conf_matrix_10fold)
        print("Classification Report:")
        print(rf_classification_report_10fold)

        print("--- %s seconds ---" % (time.time() - start_time))

    def SVM(self):
        start_time = time.time()
        # Define parameter grid for grid search
        param_grid = {'C': [0.01, 0.1, 1, 10], 'kernel': ['linear', 'rbf']}

        # Create SVC object
        svc = SVC()

        # Perform 5-fold cross-validation with GridSearchCV
        svm_cv_5fold = GridSearchCV(svc, param_grid=param_grid, cv=5, scoring='accuracy', verbose=2)
        svm_cv_5fold.fit(self.X_train, self.y_train)

        # Get best parameters and create new SVC object
        best_params = svm_cv_5fold.best_params_
        C = best_params['C']
        kernel = best_params['kernel']
        svm = SVC(C=C, kernel=kernel)

        # Make predictions and get evaluation metrics
        svm_cv_pred_5fold = cross_val_predict(svm, self.X_train, self.y_train, cv=5)
        svm_conf_matrix_5fold = confusion_matrix(self.y_train, svm_cv_pred_5fold)
        svm_classification_report_5fold = classification_report(self.y_train, svm_cv_pred_5fold)
        accuracy_svm_5fold = accuracy_score(self.y_train, svm_cv_pred_5fold)

        # Perform 10-fold cross-validation
        svm_cv_10fold = GridSearchCV(svc, param_grid=param_grid, cv=10, scoring='accuracy', verbose=2)
        svm_cv_10fold.fit(self.X_train, self.y_train)

        best_params = svm_cv_10fold.best_params_
        C = best_params['C']
        kernel = best_params['kernel']
        svm = SVC(C=C, kernel=kernel)

        svm_cv_pred_10fold = cross_val_predict(svm, self.X_train, self.y_train, cv=10)
        svm_conf_matrix_10fold = confusion_matrix(self.y_train, svm_cv_pred_10fold)
        svm_classification_report_10fold = classification_report(self.y_train, svm_cv_pred_10fold)
        accuracy_svm_10fold = accuracy_score(self.y_train, svm_cv_pred_10fold)

        # Print results
        print("For SVM - 5 fold cross validation:")
        print("Best parameters - C:", C, "kernel:", kernel)
        print("Accuracy:", round(accuracy_svm_5fold * 100, 2), "%")
        print("Confusion Matrix:")
        print(svm_conf_matrix_5fold)
        print("Classification Report:")
        print(svm_classification_report_5fold)

        print("\nFor SVM - 10 fold cross validation:")
        print("Best parameters - C:", C, "kernel:", kernel)
        print("Accuracy:", round(accuracy_svm_10fold * 100, 2), "%")

newdf = data.copy()
newdf = newdf.dropna()
X = newdf.drop(['label'], axis=1)
y = newdf.label

X = pd.get_dummies(X)

NewM = NewModel(X)

NewM.LogisticRegression()

NewM.DecisionTree()

NewM.RandomForest()

NewM.SVM()

df1 = data1.copy()

df1 = df1.dropna()

df1.columns

df1.info()

#So, I will use the Feature Selection result of this pape

important_features = [
    'src',
    'pktcount',
    'dst',
    'byteperflow',
    'pktperflow',
    'pktrate',
    'tot_kbps',
    'rx_kbps',
    'flows',
    'bytecount',
    'dt',
    'Protocol',
    'dur',
    'tot_dur'

                     ]


weights = [
    17.87,
    15.16,
    13.64,
    12.97,
    11.35,
    11.35,
    9.68,
    9.66,
    8.95,
    4.92,
    2.33,
    1.31,
    1.11,
    1.11
]

weighted_features = pd.DataFrame({'features':important_features,
                                 'weights':weights})
weighted_features

### But we dont need src, dst, dt, So, we will drop them
X = df1[important_features]
y = df1.label

X = X.drop(['src', 'dst', 'dt'], axis=1)

X.head()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
X['Protocol'] = le.fit_transform(X['Protocol'])

abs(X.corr())

fig, ax = plt.subplots(figsize=(10,7))
sns.heatmap(abs(X.corr()), annot=True)

##### There some duplicated features and high correlated features.
## "dur" and "tot_dur"
## "pktperflow" and "pktrate"

X = X.drop(['dur', "pktrate", "pktperflow"], axis=1)

X.columns

fig, ax = plt.subplots(figsize=(10,7))
sns.heatmap(abs(X.corr()), annot=True)

X = pd.get_dummies(X)

M = Model(X)

## Logistic Regression(With FS)
M.LogisticRegression()

## Support Vector Machine
M.SupportVectorMachine()

M.DecisionTree()

M.RandomForest()

##KNN with FS
M.KNearetsNeighbor()