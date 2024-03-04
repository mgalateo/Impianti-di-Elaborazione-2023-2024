clear;
clc;

% Specifica il percorso del file XLSX
file_path1 = 'LLc.xlsx';
file_path2 = 'LL_Primo_c.xlsx';


% Leggi i dati dal file XLSX 1
[data1, text1, raw1] = xlsread(file_path1);

% Leggi i dati dal file XLSX 2
[data2, text2, raw2] = xlsread(file_path2);

colonna1 = data1(:, 4);
colonna2 = data2(:, 4);

% Esegui il test t di Student
[h, p, ci, stats] = ttest2(colonna1, colonna2);

% Confronta il livello di significatività

if h == 1
    disp('Il test rigetta l ipotesi nulla a livello di significatività del 5%.');
    disp('I due campioni non provengono dalla stessa distribuzione.');
    fprintf('P-Value: %d',p);
else
    disp('Il test non rigetta l ipotesi nulla a livello di significatività del 5%.');
    disp('I due campioni provengono dalla stessa distribuzione.');
    fprintf('P-Value: %d',p);
end