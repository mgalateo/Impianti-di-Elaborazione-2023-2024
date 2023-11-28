clear;
clc;

% Specifica il percorso del file XLSX
file_path = 'LLc.xlsx';

% Leggi i dati dal file XLSX
[data, text, raw] = xlsread(file_path);


componentiNormali=[]

for i = 1:9
    % Accedi alla colonna
    colonna = data(:, i);
    % Esegui il test di Lilliefors
    [h, p, stat] = lillietest(colonna);
    
    % Visualizza i risultati
    disp(['componente n ', i])
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

disp('\n');
disp(componentiNormali);
