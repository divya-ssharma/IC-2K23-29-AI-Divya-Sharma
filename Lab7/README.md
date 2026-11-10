# Lab 7
Name: Divya Sharma  
Roll No: IC-2K23-29
PCA, FGSM and the mini project. Wanted to do Grad-CAM too but the ResNet weights weren't downloading on the lab network.
pca_demo.py generates a 100x5 matrix with three of the columns correlated, then reduces it to 2 components with sklearn PCA. Prints the shape before and after and the explained variance ratio.
fgsm_demo.py is a tiny two layer net. I take one random input, compute the gradient of the loss with respect to the input, and add epsilon times the sign of that gradient to the input. With epsilon 0.1 the prediction changes. Tried 0.3 first and it was too far from the original input.
mini_project.py is a decision tree for pass or fail from hours studied and hours slept. Feature importance comes out showing hours studied is more important.
