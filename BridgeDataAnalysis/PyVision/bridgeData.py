
'''
Ish Kumar Jain: Import bridge data from test.csv

'''
from scipy import stats
import numpy as np
#import pylab
import csv
from sklearn.cross_validation import train_test_split

data = np.genfromtxt('test.csv', delimiter=',')
#size1 = 10 # average data of 10 min
#size2 = np.size(data,0)/size1;

dval = 2
y1=data[:,dval-1]
example = np.empty(0)
label = np.empty(0)
sizeData = np.size(y1)
for i in range(0,sizeData-6):
	for j in range(0,5):
		example = np.append(example, y1[i+j])
	label= np.append(label,y1[i+5])
	
#work here
bins = np.empty(0)
bins = np.append(bins,np.amin(label))
bins = np.append(bins,(np.amin(label)+np.amax(label))/2)
bins = np.append(bins,np.amax(label))
label = np.digitize(label,bins)
print label

a = np.random.rand(np.size(example))
a = 0.01*a

#print 'a:', np.shape(a)
example = np.add(a,example)
example = np.reshape(example, (sizeData-6, 5))
data_train, data_test, labels_train, labels_test = train_test_split(example, label, test_size=0.20, random_state=42)


#print 'new'
#print example
#print np.shape(label)
print np.shape(example)
print np.shape(label)

'''
y = np.mean(y1.reshape(size1,size2),0)
x = np.arange(1,np.size(y)+1)
z = np.polyfit(x,y,2)
p = np.poly1d(z)
print np.size(p)

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)

# Calculate some additional outputs
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
print residual_std_error

# Plotting
pylab.plot(x, y, 'bo')
pylab.plot(x, p, 'k-')
#pylab.plot(x, predict_y, 'k-')
pylab.show()
'''
