clear;
clc;

% Specifica il percorso del file XLSX
file_path1 = 'LLc.xlsx';
file_path2 = 'PCAc.xlsx';


% Leggi i dati dal file XLSX 1
[data1, text1, raw1] = xlsread(file_path1);

% Leggi i dati dal file XLSX 2
[data2, text2, raw2] = xlsread(file_path2);

colonna1 = data1(:, 1);
colonna2 = data2(:, 1);

% Esegui il test t di Student
[h, p, ci, stats] = ttest2(colonna1, colonna2);

% Visualizza i risultati
disp('Componenti 1');
disp(['H0: I due campioni provengono dalla stessa distribuzione']);
disp(['p-value: ', num2str(p)]);
disp(['Intervallo di confidenza: [', num2str(ci(1)), ', ', num2str(ci(2)), ']']);
disp(['Statistiche del test: ', num2str(stats.tstat)]);

% Confronta il livello di significatività
alpha = 0.05;
if p < alpha
    disp('Il test rigetta l ipotesi nulla a livello di significatività del 5%.');
    disp('I due campioni non provengono dalla stessa distribuzione.');
else
    disp('Il test non rigetta l ipotesi nulla a livello di significatività del 5%.');
    disp('I due campioni provengono dalla stessa distribuzione.');
end