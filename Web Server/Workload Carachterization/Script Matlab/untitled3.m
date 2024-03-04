clear;
clc;

% Specifica il percorso del file XLSX
file_path1 = 'LLc.xlsx';
file_path2 = 'PCAc.xlsx';


% Leggi i dati dal file XLSX 1
[data1, text1, raw1] = xlsread(file_path1);

% Leggi i dati dal file XLSX 2
[data2, text2, raw2] = xlsread(file_path2);



colonna1 = data1(:, 2);
colonna2 = data2(:, 2);

% Esegui il test t di Student
[p,h, stats] = ranksum(colonna1, colonna2);

% Stampa il risultato del test
fprintf('Il p-value del test di Wilcoxon è %.4f\n', p);

% Valuta l'ipotesi nulla
if h == 1
    fprintf('L''ipotesi nulla è rigettata a un livello di significatività del 5%%.\n');
else
    fprintf('L''ipotesi nulla non può essere rigettata a un livello di significatività del 5%%.\n');
end

% Visualizza le statistiche del test
disp('Statistiche del test:');
disp(stats);

