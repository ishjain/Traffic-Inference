
'''
Ish Kumar Jain: I ran logistic regression on this dummy data set and got 
train accuracy = 40%
test accuracy = 40%
validate accuracy = 60%
default learning rate (.13) 
'''
import numpy as np

x_tr = np.array([[1,2,3,4,5],[2,1,4,5,4]])
y_tr = np.array([1,-1,1,1,-1])

x_te = np.array([[4,5,6,7,8],[3,4,5,8,9]])
y_te = np.array([-1,-1,-1,1,1])

x_va = np.array([[4,5,6,7,8],[3,4,5,8,9]])
y_va = np.array([-1,-1,-1,1,1])


x_tr=np.transpose(x_tr)
x_te=np.transpose(x_te)
x_va=np.transpose(x_va)

test = [x_te,y_te];
train = [x_tr,y_tr];
validate = [x_va,y_va];
print x_tr.shape, y_tr.shape, train[0].shape
