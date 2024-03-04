clc;
clear; 

% Lettura File
data = xlsread('PCAc.xlsx');
num_colonne = size(data, 2);


% Vettore Risultati
risultati_test = zeros(1, num_colonne);

% Livello di significatività
alpha = 0.05;

% Ciclo for per applicare Shapiro-Wilk ad ogni componente
for componente = 1:num_colonne
    componente_corrente = data(:, componente);

    % test di Shapiro-Wilk
    [h, p, w] = swtest(componente_corrente);

    % risultato del test
    risultati_test(componente) = p;

    % Visualizza i risultati del test per ogni componente
    if risultati_test(componente) >= alpha
        fprintf('componente %d - p-value: %.4f | La componente è Normale. \n', componente, risultati_test(componente));
    else 
        fprintf('componente %d - p-value: %.4f | La componente non è Normale. \n', componente, risultati_test(componente));
    end
    
end

fprintf('\n');
fprintf('Componenti Normali: \nComponenti: ');

% Visualizza i risultati del test per ogni componente e interpreta
for componente = 1:num_colonne
    if risultati_test(componente) >= alpha
        fprintf('%d,', componente);
    end
end