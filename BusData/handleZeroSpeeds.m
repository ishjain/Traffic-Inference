%handle zero speeds

function speed = handleZeroSpeeds(speed1,time1,SIZE)

state=1;
speed=speed1;
for i=1:SIZE-1
    s1 = speed1(i); s2 = speed1(i+1);
    if s1>0.5 && s2<0.5
        state=0;
        index1 = i; speedPrev=s1; timePrev = time1(i);
    elseif s1<0.5 && s2>0.5 && state==0
        speedcurr = speed1(i+1); timecurr = time1(i+1);
        p=polyfit([timePrev,timecurr],[speedPrev,speedcurr],1);
        for j=index1+1:i
            speed(j) = polyval(p,time1(j));
        end
        state=1;
    end
   
end

end