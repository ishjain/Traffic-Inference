% % % % function dataplot()

% figure
% subplot(2,2,1)
close all
T=readtable('M15Day1','Format','%f%f%f');
SIZE = size(T,1)/2;
% speedSeg1 = T{1:2:SIZE,3};
% speedSeg2 = T{2:2:SIZE,3};
speed1 = T{1:2:2*SIZE,3}; time1 = T{1:2:2*SIZE,2}; speed2 = T{2:2:2*SIZE,3}; time2=T{2:2:2*SIZE,2};

state=1;
plot(speed1)
figure
% sp1 = zeros(length(speed1),1);
% plotData(T,'Day1')
for i=1:SIZE-1
    s1 = speed1(i); s2 = speed1(i+1);
    if s1>0.5 && s2<0.5
        state=0;
        index1 = i; speedPrev=s1; timePrev = time1(i);
    elseif s1<0.5 && s2>0.5 && state==0
        speedcurr = speed1(i+1); timecurr = time1(i+1);
        p=polyfit([timePrev,timecurr],[speedPrev,speedcurr],1);
        for j=index1+1:i
            speed1(j) = polyval(p,time1(j));
        end
        state=1;
    end
   
end

%  x=speed1+sp1
% x=size(T,1)

plot (speed1)


%
% subplot(2,2,2)
% T=readtable('M15Day2','Format','%f%f%f');
% plotData(T,'Day2')
% subplot(2,2,3)
% T=readtable('M15Day3','Format','%f%f%f');
% plotData(T,'Day3')
% subplot(2,2,4)
% T=readtable('M15Day4','Format','%f%f%f');
% plotData(T,'Day4')
% end
% % % 
% % % % function plotData(T, Title)
% % % 
% % % plot(T{1:2:30,2},T{1:2:30,3},'bo-')
% % % hold on
% % % plot(T{2:2:30,2},T{2:2:30,3},'ro-')
% % % xlabel('Time (in minutes)', 'FontSize',14)
% % % ylabel('Av Speed (mph)', 'FontSize',14)
% % % leg=legend('segment 1','Segment 2');
% % % set (leg, 'FontSize',13)
% % % title(Title)
% % % % end

