clc;
clear;
close all;

% Carica i dati dal file XLSX
data_claudio = xlsread('Medie.xlsx');  % Sostituisci con il percorso corretto del tuo file
data_mauro1 = readtable('1000_mauro.csv');
data_mauro2 = readtable('100000_mauro.csv');
data_mauro3 = readtable('1000000_mauro.csv');
clc;


colonna_c1 = data_claudio(:, 1);
colonna_c2 = data_claudio(:, 2);
colonna_c3 = data_claudio(:, 3);
colonna_m1 = table2array(data_mauro1);
colonna_m2 = table2array(data_mauro2);
colonna_m3 = table2array(data_mauro3);

colonne = [colonna_c1, colonna_c2, colonna_c3, colonna_m1];
colonne2=[colonna_m2, colonna_m3];

[num_righe, num_colonne] = size(colonne);
[num_righe2, num_colonne2] = size(colonne2);
%t=1.96;
t = abs(tinv(0.025,14))
t2= abs(tinv(0.025,44))
campioni=zeros(1,num_colonne+num_colonne2);
medie=zeros(1,num_colonne+num_colonne2);

for colonna = 1:num_colonne
    colonna_corrente = colonne(:, colonna);
    media=0;
    dev=0;
    errore=0;

    media=mean(colonna_corrente);
    dev=std(colonna_corrente);
    errore= media * 0.05;

    campioni(colonna)=(t*dev/errore)^2;
    medie(colonna)=media;
    
end

for colonna = 1:num_colonne2
    colonna_corrente = colonne2(:, colonna);
    media=0;
    dev=0;
    errore=0;

    media=mean(colonna_corrente);
    dev=std(colonna_corrente);
    errore= media * 0.05;

    campioni(colonna+4)=(t2*dev/errore)^2;
    medie(colonna+4)=media;
    
end

campioni
format longG;
medie