% Specifica il percorso del file XLSX
file_path = 'LLc.xlsx';

% Leggi i dati dal file XLSX
[data, text, raw] = xlsread(file_path);

% 'data' contiene i dati numerici
% 'text' contiene i dati di testo
% 'raw' contiene tutti i dati nel formato originale del foglio di lavoro

% Ad esempio, puoi stampare i dati numerici
disp('Dati numerici:');
disp(data);

% Puoi anche stampare i dati di testo
disp('Dati di testo:');
disp(text);
