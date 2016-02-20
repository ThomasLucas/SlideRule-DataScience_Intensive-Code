#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import cross_validation

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

# Version 1 - Same dataset for both training and testing
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
prediction = clf.predict(features)

print "Version1 - Accuracy: " + str(accuracy_score(labels, prediction))

# Version 2 - Use cross validation for splitting the dataset into a training set and a test set
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)
clf2 = tree.DecisionTreeClassifier()
clf2 = clf2.fit(features_train, labels_train)
prediction2 = clf2.predict(features_test)

print "Version2 - Accuracy: " + str(accuracy_score(labels_test, prediction2))





