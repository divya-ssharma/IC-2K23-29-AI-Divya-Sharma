# Lab 5

Name: Divya Sharma  
Roll No: IC-2K23-29

This lab trains a decision tree classifier on a small placement dataset of ten records. The features are the ssc, hsc and degree percentages, and the target is whether the student was placed.

The first model was built with the default settings and fit the training data perfectly, which indicated overfitting for a dataset of this size. Setting max_depth to 3 produced a more reasonable tree. The test accuracy remains low, but that is a limitation of the dataset rather than the model.

The program prints the accuracy, confusion matrix and classification report, and saves the tree diagram as tree.png.
