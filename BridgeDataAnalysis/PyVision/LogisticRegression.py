# -*- coding: utf-8 -*-
"""
..module ::Logistic Regression
File    : Logistic Regression 
Created on Fri Aug 29 17:12:50 2014

@author: pi19404


"""

import numpy
import numpy as np
import math
from scipy import optimize
from numpy.linalg import norm
import os
import sys
import time
from sklearn.metrics import confusion_matrix
import sklearn.metrics as met
import LoadDataSets
# Minimization routines
import pickle
#import sgd;
import pyvision_common as pyvision
from itertools import izip 
import Optimizer
import csv    
from sklearn.cross_validation import train_test_split

" The class encaspulates the Logistic Regression Classification Algorithms "
class LogisticRegression(object):
    """ initialize the parametes of the model """    
    def __init__(self,n_in,n_out,labels=None,Regularization=2,eta=0.01):
        if(n_in!=0):
            self.n_classes=n_out;
            self.n_dimensions=n_in;
            self.initialize_parameters(n_in,n_out);
        else:
            self.n_dimensions=0;
            self.n_classes=0;
            self.W=[];
            self.b=[];
            self.params=[];
            
        if(labels==None):
            self.labels=xrange(n_out);
            
        self.Regularization=Regularization;
        self.eta=eta;
    
      
    """function to initialize the parameters of the model """      
    def initialize_parameters(self,n_in,n_out):
        print "initializing the parameters of logistic regression"
        self.n_classes=n_out;
        self.n_dimensions=n_in;        
        self.W=numpy.zeros([n_out,n_in],dtype=float);
        self.b=numpy.zeros([n_out,1],dtype=float);
        self.params=numpy.zeros([n_out,n_in+1],dtype=float);
        self.params=self.params.flatten();
        #print np.shape(self.W),np.shape(self.b)
       
       
    """ function predicts the probability of input vector x"""
    """ the output y is MX1 vector (M is no of classse) """
    def predict(self,x):  
        y=pyvision.softmax(self.W,self.b,x);
        self.output=y;
        return y;

    """ function used for label assigment for predicted index """
    def lable(self,y):
        return self.labels[y];

    def probability(self,y):
        return self.output[y];
    """ function classifies the input vector x into one of output lables """
    """ input is NXD vector then output is NX1 vector """
    def classify(self,x):
        result=self.predict(x);
        indices=result.argmax(axis=1);
        #converting indices to lables
        lablels=map(self.lable, indices);
        return lablels;     
        
    def vector_mul(x,y):
        return x*y;
        
    """ function computes the negative log likelyhood over input dataset 
         params is optional argument to pass parameter to classifier 
        ,useful in cases of iterative optimization routines for function evaluations like scipy.optimization package """
    def negative_log_likelihood(self,params):
        # args contains the training data
        x,y=self.args;
                 
        self.update_params(params);
        sigmoid_activation = pyvision.softmax(self.W,self.b,x);
        index=[range(0,np.shape(sigmoid_activation)[0]),y];
        p=sigmoid_activation[index]
        l=-np.mean(np.log(p));
        return l;
##        self.validate(self.x,self.y)     
    """ function to set the training data for current computation loop"""
    """ useful in running algorithms for batch processing """
    def set_training_data(self,args):
        self.args=args;

    """ function to compute the gradient of parameters for a single data sample """
    def compute_gradients(self,out,y,x):
        out=(np.reshape(out,(np.shape(out)[0],1)));                
        out[y]=out[y]-1;   
        W=out*x.T;               
        res=np.vstack((W.T,out.flatten()))
        return res;

    """ function to compute the gradient of loss function over all input samples
        params is optional input parameter passed to the classifier,which is useful in cases 
        of iterative optimization routines,added for compatiblity with scipi.optimization package """
    def gradients(self,params=None):
        # args contains the training data
        x,y=self.args;
        self.update_params(params);
        sigmoid_activation = pyvision.softmax(self.W,self.b,x);        
        e = [ self.compute_gradients(a,c,b) for a, c,b in izip(sigmoid_activation,y,x)]                         
        mean1=np.mean(e,axis=0);        
        mean1=mean1.T.flatten();
        return mean1;


    def get_params(self):
        return self.params;
        
    def set_params(self,params):
        self.params=params;
        
    

    """ function to update the weights given parameter array """        
    def update_params(self,params):
        if params==None:
            return;
        nparam=self.n_dimensions+1;
        param1=params.reshape(-1,nparam);        
        self.W=param1[:,0:nparam-1];
        self.b=param1[:,nparam-1];        
        self.b=np.reshape(self.b,(np.shape(self.b)[0],1))
        
        
    """ function to update the parameter array given weights """
    def update_params_grads(self,W,b):
        nparam=self.n_dimensions+1;
        param1=self.params.reshape(-1,nparam);
        param1[:,0:nparam-1]=W;
        param1[:,nparam-1]=b;
        return param1.flatten();
   
    def callback(self,w,num,x,y,flag):       
        self.params=w;
        self.update_params(self.params);
        if flag==0:
            print "iteration   : ",num,":",np.shape(w);
            l=self.negative_log_likelihood(w);
            print "Loss function   : ",l;
        
  
        


    """ the function performs training for logistic regression classifier """        
    def train(self,train,test,validate):
        if self.n_dimensions==0:
            self.labels=np.unique(train[1]);            
            n_classes = len(self.labels) 
            n_dimensions=np.shape(x)[1];
            self.initialize_parameters(n_dimensions,n_classes);
                
        opti=Optimizer.Optimizer(200,"SGD",1,1,0.013);    
        #(self,maxiter=1000,method="SGD",validation_iter=1,batch_size=600,learning_rate=0.13):
        opti.set_datasets(train,test,validate);
        opti.set_functions(self.negative_log_likelihood,self.set_training_data,self.classify,self.gradients,self.get_params,self.callback);
        opti.run();
            
        #self.labels =np.unique(train[1]);
        #sgd1=sgd.SGD(0.13,600,1000);
        #sgd1.set_datasets(train,test,validate);
        #sgd1.set_functions(self.classify,self.gradients,self.get_params,self.callback);
        
        #sgd1.run();
        
      

if __name__ == "__main__":    
     '''
     model_name1="/home/ishjain/MininetIsh/mnist.pkl.gz"
     data=LoadDataSets.LoadDataSets();
     [train,test,validate]=data.load_pickle_data(model_name1);
     #print test[1]'''
     
     
     '''
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
        '''
     #print train[0].shape, test[0].shape, validate[1].shape;
     
     data = np.genfromtxt('test.csv', delimiter=',')
     dval = 1  #Change this value for different dataset (1 to 5)
     y1=data[:,dval-1]
     example = np.empty(0)
     label = np.empty(0)
     sizeData = 106#np.size(y1)
     for i in range(0,sizeData-6):
	     for j in range(0,5):
		     example = np.append(example, y1[i+j])
	     label= np.append(label,y1[i+5])
     #print example
     '''
     bins = np.empty(0)
     bins = np.append(bins,np.amin(label))
     bins = np.append(bins,(np.amin(label)+np.amax(label))/2)
     bins = np.append(bins,np.amax(label))
     '''
     #bins = np.arange(np.amin(label),np.amax(label))
     bins = np.linspace(np.amin(label),np.amax(label)+0.00001,4)#change this for every dataset (#bins+1)
     print 'bins:', np.shape(bins)
     print bins
     print label
     label = np.digitize(label,bins)
     
     label=label-1
     print label
     
     a = np.random.rand(np.size(example))
     a = 0.001*a
     #example = np.add(a,example)
     example = np.reshape(example, (sizeData-6, 5))
     data_train, data_test, labels_train, labels_test = train_test_split(example, label, test_size=0.20, random_state=42)
     train = [data_train,labels_train]
     test = [data_test,labels_test]
     validate = [data_test,labels_test]
     print train[0].shape, test[0].shape, validate[0].shape;
     
     '''
     x=train[0].get_value(borrow=True);
     y=train[1].eval();     
     train=[x,y];

     x=test[0].get_value(borrow=True);
     y=test[1].eval();
     test=[x,y];
     
     x=validate[0].get_value(borrow=True);
     y=validate[1].eval();
     validate=[x,y];'''
     
     x=test[0]
     y=test[1]
     classifier=LogisticRegression(0,0);
     classifier.Regularization=0;
     classifier.train(train,test,validate);
    
     print np.shape(x),np.shape(y);
     print 'bins:', bins
     print label
     
     
     
    
#softmax(numpy.array([1,1],[2,2],[3,3]),numpy.array([1,1,1]),numnp.array([1,2]))
