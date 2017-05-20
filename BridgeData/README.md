# Time Series and Linear Regression on Bridge Dataset

Step-0: Use MySQL traffic data and copy paste to BridgeSegment.txt for 5 bridges data.

  * mysql -h 10.230.9.183 -u reader
  * use traffic;
  * show tables;
  * describe <table>; #describe node;
  * select id, name, owner, borough from node;
  * select id, name, owner, borough from node where borough='Manhattan';
  * select id, AsText(segment) from node where id =1 limit 1;
  * select * from reading limit 100;
  * select * from reading where node = 2 limit 40,285; #for 19-24 (5hour data, 55 points missing)
  * select * from reading where node = 2 limit 1453,272; #Day2 Sametime
  * select * from reading where node = 2 limit 40,285; # Day 3
  * select id from node;
  * select count(*) from reading where id=1,2,3,4;


Step-1: dataBridge.m contains Average speed and time data for 5 bridge segments. This file will be used by other code.

Step-2: Run plotBridge.m for visulaizing the data

Step-3: Run LinRegOnBridge.m for Linear Regession on this data.
