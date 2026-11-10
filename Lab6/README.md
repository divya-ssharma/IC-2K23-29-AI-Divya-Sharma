# Lab 6

Name: Divya Sharma  
Roll No: IC-2K23-29

This lab implements linear regression using PyTorch. The data is a straight line of the form y = 3x + 2, and the objective is to check whether the model can recover the underlying weight and bias from the data alone.

The model is a single nn.Linear layer trained with mean squared error and SGD at a learning rate of 0.01 over 200 epochs. The initial version passed the input as a 1D tensor and produced shape errors in the loss, which was resolved by reshaping X into a column vector. A learning rate of 0.01 converged smoothly, whereas 0.1 caused the loss to oscillate.

At the end of training the weight is close to 3 and the bias is close to 2. The loss curve and the fitted line against the original data are both saved as loss.png and fit.png.
