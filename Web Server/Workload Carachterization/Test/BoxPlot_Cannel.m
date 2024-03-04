clc;
clear;

% Carica i dati dal file XLSX
data = xlsread('LL_Primo_c.xlsx');  % Sostituisci con il percorso corretto del tuo file
data2 = xlsread('LLc.xlsx');
% Ottieni il numero di colonne
num_colonne = size(data, 2);
num_colonne2 = size(data2, 2);

% Crea un boxplot per ogni colonna
figure;


for colonna = 1:num_colonne
    % Seleziona la colonna di interesse
    colonna_corrente = data(:, colonna);

    % Crea un subplot per ogni colonna
    subplot(3, 3, colonna);
    boxplot(colonna_corrente);
    title(['Colonna ' num2str(colonna)]);
    ylabel('Valore');
end

% Imposta il layout dei subplots
sgtitle('Boxplot Componenti LL1c');


figure; 



for colonna = 1:num_colonne2
    % Seleziona la colonna di interesse
    colonna_corrente = data2(:, colonna);

    % Crea un subplot per ogni colonna
    subplot(3, 3, colonna);
    boxplot(colonna_corrente);
    title(['Colonna ' num2str(colonna)]);
    ylabel('Valore');
end

sgtitle('Boxplot Componenti LL');


