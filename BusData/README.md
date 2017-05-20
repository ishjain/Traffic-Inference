# Traffic-Inference on Bus Dataset
Part of course project for CSGY2620 Networks and Mobile Systems

This is MTA bus data Analysis.
Note: If analysing new data- go to step 1 and step-2. If analysing my data- use my file M15Day1.txt etc and go to Step-3.

Step-1: **Download MTA** historical data from http://web.mta.info/developers/MTA-Bus-Time-historical-data.html
You must have the txt file- MTA-Bus-Time_.2014-09-01.txt in your folder

Step-2: **Linux-Python** Run extractData2.py It will extract the data for two segments of M15 and display it on terminal. Copy and paste it to a txt file (Already done at M15Day1.txt)

Step-3: **Windows-Matlab** To visualize the data, run dataplot.m

Step-4: To run **Linear or Quadratic Regression**, run LinearRegression.m 
You can change the parameters inside the code (very easy with well commented file)
Note that LinearRegression.m calls handleZeroSpeeds.m function for linear interpolating the zero speed data points.


