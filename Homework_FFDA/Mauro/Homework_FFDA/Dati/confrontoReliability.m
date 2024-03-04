clear all;
close all;
clc;

C401_interarrivals= importdata("tupling_tg-C401-200/interarrivals.txt");
C238_interarrivals= importdata("tupling_tg-C238-200/interarrivals.txt");

% Calcola le empRel per il set di dati tg-C401
[y_C401, t_C401] = cdfcalc(C401_interarrivals);
empTTF_C401 = y_C401(2:end);
empRel_C401 = 1 - empTTF_C401;

% Calcola le empRel per il set di dati tg-C238
[y_C238, t_C238] = cdfcalc(C238_interarrivals);
empTTF_C238 = y_C238(2:end);
empRel_C238 = 1 - empTTF_C238;

% Confronto delle empRel
plot(t_C401, empRel_C401, '-o', t_C238, empRel_C238, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
legend('C401 empRel', 'C238 empRel');


% Calcola l'integrale delle empRel per il set di dati C401
integral_C401 = trapz(t_C401, empRel_C401);

% Calcola l'integrale delle empRel per il set di dati C238
integral_C238 = trapz(t_C238, empRel_C238);

disp(['Integrale dell affidabilita per C401: ', num2str(integral_C401)]);
disp(['Integrale dell affidabilita per C238: ', num2str(integral_C238)]);