# Calculates the linear regression model and plots the data
# Limitations: only returns the most basic regression outputs

from scipy import stats
import numpy as np
import pylab



# Load CSV (using python)
import csv

#filename = 'test.csv'
#raw_data = open(filename, 'rb')
#reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
#x_temp = list(reader)
#y = np.array(x_temp).astype('float')
#print(data.shape)
data = np.genfromtxt('test.csv', delimiter=',')
size1 = 10 # average data of 10 min
size2 = np.size(data,0)/size1;

dval = 3
y1=data[:,dval-1]

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
