clc;
clear;
% Specifica il percorso del file XLSX
file_path1 = 'LLc.xlsx';
file_path2 = 'PCAc.xlsx';


% Leggi i dati dal file XLSX 1
[data1, text1, raw1] = xlsread(file_path1);

% Leggi i dati dal file XLSX 2
[data2, text2, raw2] = xlsread(file_path2);

colonna1 = data1(:, 6);
colonna2 = data2(:, 6);


% Calcola la varianza delle colonne
varianza1 = var(colonna1);
varianza2 = var(colonna2);

% Stampa i risultati
fprintf('Varianza della colonna 1: %.4f\n', varianza1);
fprintf('Varianza della colonna 2: %.4f\n', varianza2);
