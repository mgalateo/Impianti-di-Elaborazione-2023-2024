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



figure;
title('Boxplot 1000');
subplot(1, 2, 1);
boxplot([colonna_c1]);
subplot(1, 2, 2);
boxplot([colonna_m1]);
saveas(gcf, 'Test_Var_1000_corpi.png');

figure;
title('Boxplot 100K');
subplot(1, 2, 1);
boxplot([colonna_c2]);
subplot(1, 2, 2);
boxplot([colonna_m2]);
saveas(gcf, 'Test_Var_100K_corpi.png');

figure;
title('Boxplot 1KK');
subplot(1, 2, 1);
boxplot([colonna_c3]);
subplot(1, 2, 2);
boxplot([colonna_m3]);
saveas(gcf, 'Test_Var_1K_corpi.png');

fprintf("Test Varianza 1000 corpi:\n");
[h1, p1] = vartest2(colonna_c1, colonna_m1);
if h1
    disp('Le varianze dei due campioni sono statisticamente diverse.');
else
    disp('Le varianze dei due campioni sono statisticamente equivalenti.');
end
fprintf('Valore p associato al test: %.4f\n\n', p1);

fprintf("Test Varianza 100000 corpi:\n");
[h2, p2] = vartest2(colonna_c2, colonna_m2);
if h2
    disp('Le varianze dei due campioni sono statisticamente diverse.');
else
    disp('Le varianze dei due campioni sono statisticamente equivalenti.');
end
fprintf('Valore p associato al test: %.4f\n\n', p2);

fprintf("Test Varianza 1000000 corpi:\n");
[h3, p3] = vartest2(colonna_c3, colonna_m3);
if h3
    disp('Le varianze dei due campioni sono statisticamente diverse.');
else
    disp('Le varianze dei due campioni sono statisticamente equivalenti.');
end
fprintf('Valore p associato al test: %.4f\n\n', p3);


