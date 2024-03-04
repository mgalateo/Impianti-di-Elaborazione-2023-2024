clear all;
close all;
clc;


% Definizione dei parametri
lambda2=0.01;
lambda1=lambda2;
% tasso di fallimento
t_max = 200;    % tempo massimo

% Creazione di un vettore di tempi
t = 0:0.1:t_max;

% Calcolo della reliability per il sistema 1
R1 = exp(-lambda1 * t);
reliability_parallel_1 = 1 - (1 - R1.^4).^2;

% Calcolo della reliability per il sistema 2
R2 = exp(-lambda2 * t);
reliability_parallel_2 = (1 - (1 - R2).^2).^4;

% Plot del grafico
figure;
plot(t, reliability_parallel_1, 'LineWidth', 2, 'DisplayName', 'Sistema 1');
hold on;
plot(t, reliability_parallel_2, 'LineWidth', 2, 'DisplayName', 'Sistema 2');
title('Grafico della Reliability nei Sistemi');
xlabel('Tempo');
ylabel('Reliability');
legend('show');
grid on;
