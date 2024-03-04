clc;
clear;

% Carica i dati dal file XLSX
residui = xlsread('Medie.xlsx');  % Sostituisci con il percorso corretto del tuo file


% Seleziona le colonne di interesse di Claudio
residui1 = residui(:, 1);
residui2 = residui(:,2);
residui3 = residui(:,3); 

% Seleziona le colonne di interesse di Mauro
data_mauro1 = readtable('1000_mauro.csv');
data_mauro2 = readtable('100000_mauro.csv');
data_mauro3 = readtable('1000000_mauro.csv'); 

data_mauro1 = table2array(data_mauro1);
data_mauro2 = table2array(data_mauro2);
data_mauro3 = table2array(data_mauro3);

clc;

%figure; 
%boxplot([residui1])


[h, p, ci, stats] = ttest2(residui1, data_mauro1, 'Vartype', 'unequal');

% Visualizza i risultati
disp('Risultati del two-sample t-test unpooled Claudio1-Mauro1:');
disp(['Statistiche t = ', num2str(stats.tstat)]);
disp(['Valore p = ', num2str(p)]);
disp(['Intervallo di confidenza = [', num2str(ci(1)), ', ', num2str(ci(2)), ']']);

% Verifica l'ipotesi nulla
if h
    disp('L ipotesi nulla e rifiutata.');
else
    disp('L ipotesi nulla non e rifiutata.');
end

disp(' ');

[h, p, ci, stats] = ttest2(residui2, data_mauro2, 'Vartype', 'unequal');

% Visualizza i risultati
disp('Risultati del two-sample t-test unpoled Claudio2-Mauro2:');
disp(['Statistiche t = ', num2str(stats.tstat)]);
disp(['Valore p = ', num2str(p)]);
disp(['Intervallo di confidenza = [', num2str(ci(1)), ', ', num2str(ci(2)), ']']);

% Verifica l'ipotesi nulla
if h
    disp('L ipotesi nulla e rifiutata.');
else
    disp('L ipotesi nulla non e rifiutata.');
end

disp(' ');

[h, p, ci, stats] = ttest2(residui2, data_mauro2, 'Vartype', 'unequal');

% Visualizza i risultati
disp('Risultati del two-sample t-test unpoled Claudio3-Mauro3:');
disp(['Statistiche t = ', num2str(stats.tstat)]);
disp(['Valore p = ', num2str(p)]);
disp(['Intervallo di confidenza = [', num2str(ci(1)), ', ', num2str(ci(2)), ']']);

% Verifica l'ipotesi nulla
if h
    disp('L ipotesi nulla e rifiutata.');
else
    disp('L ipotesi nulla non e rifiutata.');
end


% % Creazione del boxplot
% figure;
% 
% % Boxplot per la varianza tra residui1 e data_mauro1
% subplot(3, 1, 1);
% boxplot([residui1, data_mauro1], 'Labels', {'Claudio', 'Mauro1'});
% title('Confronto Varianza - Colonna 1');
% 
% % Boxplot per la varianza tra residui2 e data_mauro2
% subplot(3, 1, 2);
% boxplot([residui2, data_mauro2], 'Labels', {'Claudio', 'Mauro2'});
% title('Confronto Varianza - Colonna 2');
% 
% % Boxplot per la varianza tra residui3 e data_mauro3
% subplot(3, 1, 3);
% boxplot([residui3, data_mauro3], 'Labels', {'Claudio', 'Mauro3'});
% title('Confronto Varianza - Colonna 3');
% 
% % Impostazioni aggiuntive per la visualizzazione
% ylabel('Valori');
% xlabel('Gruppi');
% sgtitle('Confronto Varianza tra Claudio e Mauro');















% colonna_mauro3 = table2array(data_mauro3);
% 
% % Esegui il two-sample t-test
% [h, p, ci, stats] = ttest2(colonna_corrente, colonna_mauro3, 'Vartype', 'unequal');
% 
% % Visualizza il risultato del test
% fprintf('Risultato del two-sample t-test:\n');
% fprintf('H0: Le medie sono uguali.\n');
% fprintf('H1: Le medie sono diverse.\n');
% fprintf('p-value: %.4f\n', p);
% 
% % Visualizza il boxplot
% figure;
% boxplot([colonna_corrente, colonna_mauro3], 'Labels', {'Claudio', 'Mauro3'});
% ylabel('Valore');
% title('Confronto tra Claudio e Mauro3');




% % Ottieni il numero di colonne
% num_colonne = size(data, 2);
% num_colonne2 = size(data2, 2);
% 
% % Crea un boxplot per ogni colonna
% figure;
% 
% 
% for colonna = 1:num_colonne
%     % Seleziona la colonna di interesse
%     colonna_corrente = data(:, colonna);
% 
%     % Crea un subplot per ogni colonna
%     subplot(3, 3, colonna);
%     boxplot(colonna_corrente);
%     title(['Colonna ' num2str(colonna)]);
%     ylabel('Valore');
% end
% 
% % Imposta il layout dei subplots
% sgtitle('Boxplot Componenti LL1c');
% 
% 
% figure; 
% 
% 
% 
% for colonna = 1:num_colonne2
%     % Seleziona la colonna di interesse
%     colonna_corrente = data2(:, colonna);
% 
%     % Crea un subplot per ogni colonna
%     subplot(3, 3, colonna);
%     boxplot(colonna_corrente);
%     title(['Colonna ' num2str(colonna)]);
%     ylabel('Valore');
% end
% 
% sgtitle('Boxplot Componenti LL');
% 
% 
