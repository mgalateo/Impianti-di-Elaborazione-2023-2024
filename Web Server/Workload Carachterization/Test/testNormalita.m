clc;
clear;
% Specifica il percorso del file XLSX
file_path = "LLc.xlsx";

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

componentiNormali=[]

disp('\n');
disp(componentiNormali);

% Specifica il percorso completo del file di output
nome_file = 'output.txt';

% Attiva la registrazione dell'output nella command window
diary(nome_file);

for i = 1:7
    % Accedi alla colonna
    colonna = data(:, i);
    % Esegui il test di Lilliefors
    [h, p, stat] = lillietest(colonna);
    
    % Visualizza i risultati
    fprintf(['componente n %d', i])
    disp (i)
    disp(['H0: I dati provengono da una distribuzione normale']);
    disp(['p-value: ', num2str(p)]);
    disp(['Statistiche del test: ', num2str(stat)]);
    if h
        disp('Il test rigetta l ipotesi nulla a livello di significatività del 5%.');
    else
        disp('Il test non rigetta l ipotesi nulla a livello di significatività del 5%.');
        disp('La componente Principale è NORMALE')
        
        componentiNormali = [componentiNormali, text(i)];
    end
end





% Disattiva la registrazione dell'output
diary off;

