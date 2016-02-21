#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn import cross_validation

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

# Use cross validation for splitting the dataset into a training set and a test set
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)

print "Accuracy: " + str(accuracy_score(labels_test, prediction))

count_test_poi = 0
for label in labels_test:
	if label == 1:
		count_test_poi += 1

print "Number of POI in the test set: " + str(count_test_poi)
print "Number of people in the test set: " + str(len(labels_test))

count_true_positive = 0
for index, item in enumerate(prediction):
	if item == labels_test[index] and item == 1:
		count_true_positive += 1

print "Number of true positive: " + str(count_true_positive)

print "Precision: " + str(precision_score(labels_test, prediction))
print "Recall: " + str(recall_score(labels_test, prediction))



