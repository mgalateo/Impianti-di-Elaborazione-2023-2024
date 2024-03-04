clear all;
close all;
clc;

BGL_interarrivals= importdata("BGL/interarrivals.txt");
Mercury_interarrivals= importdata("Mercury/interarrivals.txt");

% Calcola le empRel per il set di dati BGL
[y_bgl, t_bgl] = cdfcalc(BGL_interarrivals);
empTTF_bgl = y_bgl(2:end);
empRel_bgl = 1 - empTTF_bgl;

% Calcola le empRel per il set di dati Mercury
[y_mercury, t_mercury] = cdfcalc(Mercury_interarrivals);
empTTF_mercury = y_mercury(2:end);
empRel_mercury = 1 - empTTF_mercury;

% Confronto delle empRel
plot(t_bgl, empRel_bgl, '-o', t_mercury, empRel_mercury, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
legend('BGL empRel', 'Mercury empRel');


% Calcola l'integrale delle empRel per il set di dati BGL
integral_bgl = trapz(t_bgl, empRel_bgl);

% Calcola l'integrale delle empRel per il set di dati Mercury
integral_mercury = trapz(t_mercury, empRel_mercury);

disp(['Integrale dell affidabilita per BGL: ', num2str(integral_bgl)]);
disp(['Integrale dell affidabilita per Mercury: ', num2str(integral_mercury)]);