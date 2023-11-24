clc;
clear;

%% Read the data
data = xlsread("Dati.xlsx");
pca_data = xlsread('PCA.xlsx');
cluster_data = xlsread('Cluster.xlsx');
N_pca = size (pca_data,2); % number of principal components
N_cluster = max (cluster_data); % number of clusters

%% Total Deviance
data_norm = zscore(data);
DEV_TOT = sum(sum((data_norm-mean(data_norm,1)).^2)); % total deviance

%% PCA Deviance
DEV_PCA = sum(sum((pca_data-mean(pca_data,1)).^2)); % deviance after pca
DEV_PCA_per = DEV_PCA/DEV_TOT; % percentage deviance after pca

%% Cluster Deviance
W = zeros (N_cluster,1); % deviance intra (within) clusters
B = zeros (N_cluster,1); % deviance inter (between) clusters
for i = 1: N_cluster
   index = find(cluster_data==i); % find the index of cluster i
   n_ele = size(index, 1); % number of samples of the cluster i
   centroid = mean(pca_data(index,:),1); 
   W(i) = sum(sum((centroid-pca_data(index,:)).^2));
   B(i)= n_ele*sum((centroid-mean(pca_data,1)).^2);
end

W = sum(W); % total deviance intra (within) cluster
B = sum(B); % total deviance inter (between) cluster
(W+B)/DEV_PCA % check if W+B is equal to the deviance after pca

DEV_PCA_CL_per = (B/DEV_TOT); % percentage deviance after pca & clustering
DEV_LOST_per = (1-DEV_PCA/DEV_TOT)+(W/DEV_TOT); % percentage deviance lost after pca & clustering 
%DEV_LOST_per2 = (1-DEV_PCA/DEV_TOT)+ DEV_PCA_per * W/DEV_PCA; % equivalent formula

% Apri il file in modalità di scrittura
fid = fopen('variabili_31.txt', 'w');
 
% Ottieni la lista delle variabili nel workspace
workspace_vars = whos;
 
% Ciclo attraverso le variabili nel workspace
for i = 1:length(workspace_vars)
    var_name = workspace_vars(i).name;
    
    % Verifica se la variabile è una matrice a più dimensioni
    if ~ismatrix(eval(var_name))
        continue; % Ignora le matrici a più dimensioni
    end
    
    % Scrivi nel file il nome della variabile e il suo valore
    fprintf(fid, '%s = ', var_name);
    
    % Ottieni il valore della variabile
    var_value = eval(var_name);
    
    % Scrivi nel file il valore della variabile
    if isnumeric(var_value) || islogical(var_value)
        fprintf(fid, '%g', var_value);
    elseif ischar(var_value)
        fprintf(fid, '%s', var_value);
    else
        % Puoi aggiungere altre condizioni per gestire diversi tipi di variabili
        fprintf(fid, 'Non posso salvare questo tipo di variabile');
    end
    
    fprintf(fid, '\n'); % Vai a capo dopo ogni variabile
end
 
% Chiudi il file
fclose(fid);