# Lab 7

Name: Divya Sharma  
Roll No: IC-2K23-29

This lab covers PCA, FGSM and a small mini project. Grad-CAM was also planned, but the ResNet weights could not be downloaded on the lab network, so it was left out of this submission.

The PCA script generates a 100 by 5 matrix in which three of the columns are correlated, then reduces it to two components using sklearn. It prints the shape before and after, along with the explained variance ratio.

The FGSM script defines a small two layer network and perturbs a single input by epsilon times the sign of the gradient of the loss with respect to that input. With epsilon 0.1 the prediction changes after the perturbation. An epsilon of 0.3 was tried first but moved the adversarial example too far from the original input.

The mini project is a decision tree that predicts pass or fail from hours studied and hours slept. The feature importances show that hours studied has a larger effect than hours slept.
