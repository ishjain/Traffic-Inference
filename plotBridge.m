% plot speed and tarvel time for Bridge segments during time 19:00 to 21:00

close all;
dataBridge;
% B145speed B145time B149speed B149time B150speed B150time B223speed B223time B443speed B443time;

time=1:size(B145time);
figure; 
subplot(2,1,1);hold on;grid on;
plot(B145speed, 'r', 'LineWidth',2)
plot(B149speed, 'g', 'LineWidth',2)
plot(B150speed, 'b', 'LineWidth',2)
plot(B223speed, 'c', 'LineWidth',2)
plot(B443speed, 'm', 'LineWidth',2)
plot([60,60],[0,40],'-')
ylabel('Av. Speed')
xlabel('Time')
title('Average Speed at Bridge segments between 7 PM to 9 PM');
legend('segment 1', 'segment 2', 'segment 3', 'segment 4', 'segment 5')

% figure; 
subplot(2,1,2);hold on;grid on;
plot(B145time, 'r', 'LineWidth',2)
plot(B149time, 'g', 'LineWidth',2)
plot(B150time, 'b', 'LineWidth',2)
plot(B223time, 'c', 'LineWidth',2)
plot(B443time, 'm', 'LineWidth',2)
plot([60,60],[0,40],'-')
xlabel('Time')
ylabel('Travel Time')
title('Total time at Bridge segments between 7 PM to 9 PM');
legend('segment 1', 'segment 2', 'segment 3', 'segment 4', 'segment 5')

figure; 
subplot(2,1,1);hold on;grid on;
plot(smooth(B145speed), 'r', 'LineWidth',2)
plot(smooth(B149speed), 'g', 'LineWidth',2)
plot(smooth(B150speed), 'b', 'LineWidth',2)
plot(smooth(B223speed), 'c', 'LineWidth',2)
plot(smooth(B443speed), 'm', 'LineWidth',2)
plot([60,60],[0,40],'-')
ylabel('Av. Speed')
xlabel('Time')
title('Average Speed at Bridge segments between 7 PM to 9 PM');
legend('segment 1', 'segment 2', 'segment 3', 'segment 4', 'segment 5')

% figure; 
subplot(2,1,2);hold on;grid on;
plot(smooth(B145time), 'r', 'LineWidth',2)
plot(smooth(B149time), 'g', 'LineWidth',2)
plot(smooth(B150time), 'b', 'LineWidth',2)
plot(smooth(B223time), 'c', 'LineWidth',2)
plot(smooth(B443time), 'm', 'LineWidth',2)
plot([60,60],[0,40],'-')
xlabel('Time')
ylabel('Travel Time')
title('Total time at Bridge segments between 7 PM to 9 PM');
legend('segment 1', 'segment 2', 'segment 3', 'segment 4', 'segment 5')