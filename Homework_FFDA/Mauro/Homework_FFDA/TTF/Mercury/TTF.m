clear all;
close all;
clc;

load interarrivals.txt
[y,t]=cdfcalc(interarrivals);
empTTF=y(2 :size(y,1));
empRel= 1 - empTTF;
plot(t,empTTF,'-o',t, empRel,'-o');
xlabel('time [s]'); ylabel('p');
legend('emp TTF', 'emp Rel');

%[h,p,k] = kstest2(empRel,fittedmodel(t))