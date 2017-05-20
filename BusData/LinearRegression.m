% Linear Regression
% Day1 Only
%1. Predict seg2 given seg2 past data
clear all
  close all
Day = 1;% Use 1 for Day1 only, 12 for Day1+Day2, 123 for Day1+Day2+Day3
pastVal = 3:6;
futureVal = 1:3; %future max
polyValue = 1;% 1 for linear, 2 for quadratic
TableChoice =1; % 1 for SameOnly, 2 for NeighbourOnly, 3 for both SameSegment and Neighbour
T=readtable('M15Day1','Format','%f%f%f');
T2=readtable('M15Day2','Format','%f%f%f');
T3=readtable('M15Day4','Format','%f%f%f');
SIZE = size(T,1)/2;%70;
ch=size(T,1);

speed1 = T{1:2:2*SIZE,3}; time1 = T{1:2:2*SIZE,2}; speed2 = T{2:2:2*SIZE,3}; time2=T{2:2:2*SIZE,2};
speed1 = handleZeroSpeeds(speed1,time1,SIZE); speed2 = handleZeroSpeeds(speed2,time2,SIZE);

SIZE2 = size(T2,1)/2;%70;
speedD2S1 = T2{1:2:2*SIZE2,3}; timeD2S1 = T2{1:2:2*SIZE2,2}; speedD2S2 = T2{2:2:2*SIZE2,3}; timeD2S2=T2{2:2:2*SIZE2,2};
speedD2S1 = handleZeroSpeeds(speedD2S1,timeD2S1,SIZE2); speedD2S2 = handleZeroSpeeds(speedD2S2,timeD2S2,SIZE2);

SIZE3 = size(T3,1)/2;%70;
speedD3S1 = T3{1:2:2*SIZE3,3}; timeD3S1 = T3{1:2:2*SIZE3,2}; speedD3S2 = T3{2:2:2*SIZE3,3}; timeD3S2=T3{2:2:2*SIZE3,2};
speedD3S1 = handleZeroSpeeds(speedD3S1,timeD3S1,SIZE3); speedD3S2 = handleZeroSpeeds(speedD3S2,timeD3S2,SIZE3);
if Day == 12 || Day==123
    SIZE = SIZE2; %smallest
end

for futureInd = 1:length(futureVal)
    future=futureVal(futureInd);
    for pastInd = 1:length(pastVal)
        past = pastVal(pastInd);
        index=0;
        for i=1:past:(SIZE - past-future-1)
            index=index+1;
            %ch=time1(i:i+past-1)
            if Day==1
                if TableChoice==1
                    x(index,:) = time2(i:i+past-1);%train
                    y(index,:) = speed2(i:i+past-1);
                elseif TableChoice==2
                    x(index,:) = time1(i:i+past-1);%train
                    y(index,:) = speed1(i:i+past-1);
                elseif TableChoice==3
                    x(index,:) = [time1(i:i+past-1);time2(i:i+past-1)];%train
                    y(index,:) = [speed1(i:i+past-1); speed2(i:i+past-1)];
                end
                
            elseif Day==12
                if TableChoice==1
                    x(index,:) = [time2(i:i+past-1);timeD2S2(i:i+past-1)];%train
                    y(index,:) = [speed2(i:i+past-1);speedD2S2(i:i+past-1)];
                elseif TableChoice==2
                    x(index,:) = [time1(i:i+past-1);timeD2S1(i:i+past-1)];%train
                    y(index,:) = [speed1(i:i+past-1);speedD2S1(i:i+past-1)];
                elseif TableChoice==3
                    x(index,:) = [time1(i:i+past-1);time2(i:i+past-1);timeD2S1(i:i+past-1);timeD2S2(i:i+past-1)];%train
                    y(index,:) = [speed1(i:i+past-1); speed2(i:i+past-1);speedD2S1(i:i+past-1);speedD2S2(i:i+past-1)];
                end
                
            elseif Day==123
                if TableChoice==1
                    x(index,:) = [time2(i:i+past-1);timeD2S2(i:i+past-1);timeD3S2(i:i+past-1)];%train
                    y(index,:) = [speed2(i:i+past-1);speedD2S2(i:i+past-1);speedD3S2(i:i+past-1)];
                elseif TableChoice==2
                    x(index,:) = [time1(i:i+past-1);timeD2S1(i:i+past-1);timeD3S1(i:i+past-1)];%train
                    y(index,:) = [speed1(i:i+past-1);speedD2S1(i:i+past-1);speedD3S1(i:i+past-1)];
                elseif TableChoice==3
                    x(index,:) = [time1(i:i+past-1);time2(i:i+past-1);timeD2S1(i:i+past-1);timeD2S2(i:i+past-1);timeD3S1(i:i+past-1);timeD3S2(i:i+past-1)];%train
                    y(index,:) = [speed1(i:i+past-1); speed2(i:i+past-1);speedD2S1(i:i+past-1);speedD2S2(i:i+past-1);speedD3S1(i:i+past-1);speedD3S2(i:i+past-1)];
                end
                
            end
            x1(index,:) = time2(i+past+future-1);%test
            y1(index,:) = speed2(i+past+future-1);
            p = polyfit(x(index,:),y(index,:),polyValue);
            yPred(index,:) = polyval(p,x1(index,:));
            %          figure
            %     plot(x(index,:),y(index,:),'o')
            %     hold on
            %     plot(x(index,:), polyval(p,x(index,:)))
            
            error(index,:) = (yPred(index,:)-y1(index,:))^2;
            %     plot(x1(index,:),y1(index,:),'*')
        end
        err(pastInd,futureInd)=sqrt(mean(error));
        clear x y x1 y1 p yPred error;
    end
end
% figure;hold on
color = {'r-o','g-o','b-o'};
% subplot(1,3,TableChoice)
if Day==1
    temp=0;
elseif Day==12
    temp=3;
elseif Day==123
    temp=6;
end
subplot(3,3,temp+TableChoice)
hold on

for ii = 1:length(futureVal)
    
    plot(pastVal',err(:,ii),color{ii}, 'LineWidth',2)
%      legend('1','2','3')
%      xlabel('#Past Samples')
%      ylabel('RMSE')
end
xlim([3,6])
 ylim([0,40])


% digits(4)
% latexdoc = latex(vpa(sym(err)))
% figure
% plot(x(index,:),y(index,:),'o')
% hold on
% plot(x(index,:), polyval(p,x(index,:)))
%2. Predict seg2 given seg1 past data




%3. Predict seg2 given seg1 and seg2 both past data