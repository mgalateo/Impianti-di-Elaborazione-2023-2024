clc;
clear;
% Specifica il percorso del file XLSX
file_path1 = 'LLc.xlsx';
file_path2 = 'LL_Primo_c.xlsx';


% Leggi i dati dal file XLSX 1
[data1, text1, raw1] = xlsread(file_path1);

% Leggi i dati dal file XLSX 2
[data2, text2, raw2] = xlsread(file_path2);

colonna1 = data1(:, 3);
colonna2 = data2(:, 3);


% Calcola la varianza delle colonne
h = vartest2(colonna1,colonna2);


% Stampa i risultati
fprintf('valore di h per il vartest2 -> %.4f\n Le due distribuzioni sono omoschedastiche', h);

