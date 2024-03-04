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


mean(colonna_m1)