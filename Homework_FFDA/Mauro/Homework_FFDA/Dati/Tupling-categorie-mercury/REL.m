clear all;
close all;
clc;

DEV_interarrivals= importdata("tupling_DEV-200/interarrivals.txt");


% Calcola le empRel per il set di dati tg-DEV
[y_DEV, t_DEV] = cdfcalc(DEV_interarrivals);
empTTF_DEV = y_DEV(2:end);
empRel_DEV = 1 - empTTF_DEV;



% Confronto delle empRel
fig=plot(t_DEV, empRel_DEV, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
legend('DEV empRel');


% Calcola l'integrale delle empRel per il set di dati DEV
integral_DEV = trapz(t_DEV, empRel_DEV);

MTTF_DEV= num2str(integral_DEV);
text(0.5, 0.5, ['MTTF = ', MTTF_DEV], 'Units', 'normalized', 'FontSize', 12);

% Salva la figura come PNG
saveas(fig, 'DEVREL.png')


% Carica i dati per tupling_I-O-100
IO_interarrivals = importdata("tupling_I-O-100/interarrivals.txt");
[y_IO, t_IO] = cdfcalc(IO_interarrivals);
empTTF_IO = y_IO(2:end);
empRel_IO = 1 - empTTF_IO;
integral_IO = trapz(t_IO, empRel_IO);
figure;
plot(t_IO, empRel_IO, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
title('Curva di Affidabilità per tupling\_I-O-100');
MTTF_IO = num2str(integral_IO);
text(0.5, 0.5, ['MTTF = ', MTTF_IO], 'Units', 'normalized', 'FontSize', 12);


saveas(gcf, 'IO_Reliability.png');

% Carica i dati per tupling_MEM-200
MEM_interarrivals = importdata("tupling_MEM-200/interarrivals.txt");
[y_MEM, t_MEM] = cdfcalc(MEM_interarrivals);
empTTF_MEM = y_MEM(2:end);
empRel_MEM = 1 - empTTF_MEM;
integral_MEM = trapz(t_MEM, empRel_MEM);
figure;
plot(t_MEM, empRel_MEM, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
title('Curva di Affidabilità per tupling\_MEM-200');
MTTF_MEM = num2str(integral_MEM);
text(0.5, 0.5, ['MTTF = ', MTTF_MEM], 'Units', 'normalized', 'FontSize', 12);
saveas(gcf, 'MEM_Reliability.png');


% Carica i dati per tupling_NET-100
NET_interarrivals = importdata("tupling_NET-100/interarrivals.txt");
[y_NET, t_NET] = cdfcalc(NET_interarrivals);
empTTF_NET = y_NET(2:end);
empRel_NET = 1 - empTTF_NET;
integral_NET = trapz(t_NET, empRel_NET);
figure;
plot(t_NET, empRel_NET, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
title('Curva di Affidabilità per tupling\_NET-100');
MTTF_NET = num2str(integral_NET);
text(0.5, 0.5, ['MTTF = ', MTTF_NET], 'Units', 'normalized', 'FontSize', 12);
saveas(gcf, 'NET_Reliability.png');



% Carica i dati per tupling_PRO-150
PRO_interarrivals = importdata("tupling_PRO-150/interarrivals.txt");
[y_PRO, t_PRO] = cdfcalc(PRO_interarrivals);
empTTF_PRO = y_PRO(2:end);
empRel_PRO = 1 - empTTF_PRO;
integral_PRO = trapz(t_PRO, empRel_PRO);
figure;
plot(t_PRO, empRel_PRO, '-o');
xlabel('Tempo [s]'); ylabel('Probabilità');
title('Curva di Affidabilità per tupling\_PRO-150');
MTTF_PRO = num2str(integral_PRO);
text(0.5, 0.5, ['MTTF = ', MTTF_PRO], 'Units', 'normalized', 'FontSize', 12);
saveas(gcf, 'PRO_Reliability.png');









disp(['Integrale dell affidabilita per DEV: ', num2str(integral_DEV)]);
disp(['Integrale dell affidabilita per I-O: ', num2str(integral_IO)]);
disp(['Integrale dell affidabilita per MEM: ', num2str(integral_MEM)]);
disp(['Integrale dell affidabilita per NET: ', num2str(integral_NET)]);
disp(['Integrale dell affidabilita per PRO: ', num2str(integral_PRO)]);
