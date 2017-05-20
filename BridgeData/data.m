% plot data of av. speed during time 18:00 to 19:00 for nodes 1,2,3,4.

speed1 = [ 4.97
 6.21
 6.21
 6.21
 6.21
 6.84
 6.21
 6.21
 6.84
 6.84
 6.84
 6.84
 6.84
 6.84
11.81
14.29
14.29
14.29
14.91
 ];

speed2 = [ 21.75
 24.23
 24.23
 21.75
 21.75
 21.75
 21.75
 21.75
 19.88
 21.75
 19.88
 21.75
 21.13
 21.75
 21.75
 19.26
 18.02
 21.75
 21.13
];
speed3=[ 9.94
 9.94
  8.7
 9.94
 9.94
 9.94
 9.94
 9.94
  8.7
  8.7
 9.94
  8.7
  8.7
  8.7
 9.94
11.18
11.18
11.18
11.81
];

speed4 = [13.05
13.05
14.29
14.29
14.91
14.29
14.29
14.29
13.05
14.29
13.05
13.05
11.81
11.81
14.91
16.16
16.16
16.16
16.16
];

time1=[910
843
861
802
802
747
807
806
750
732
729
751
753
748
418
365
369
370
357
];

time2 = [147
138
136
145
146
150
149
146
159
151
166
147
154
150
149
167
184
151
155
];

time3=[624
635
654
627
620
613
615
621
644
649
639
659
690
707
598
577
582
570
530
];

time4=[242
243
234
234
218
222
233
231
236
231
237
244
253
258
211
195
199
202
202
];


x=1:size(speed1);
figure; hold on;
plot(speed1, 'k', 'LineWidth',2)
plot(speed2, 'r', 'LineWidth',2)
plot(speed3, 'g', 'LineWidth',2)
plot(speed4, 'b', 'LineWidth',2)
ylabel('Av. Speed')
title('Average Speed at 4 segments between 6 PM to 7 PM');
legend('segment 1', 'segment 2', 'segment 3', 'segment 4')

figure; hold on;
plot(time1, 'k', 'LineWidth',2)
plot(time2, 'r', 'LineWidth',2)
plot(time3, 'g', 'LineWidth',2)
plot(time4, 'b', 'LineWidth',2)
ylabel('Total time')
title('Total time at 4 segments between 6 PM to 7 PM');
legend('segment 1', 'segment 2', 'segment 3', 'segment 4')