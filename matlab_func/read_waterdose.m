if contains(pwd,'matlab_func')
    path = '..';
else
    path = '.';
end
% read infinity small proton pencil beam, beam width = 0
E = 25:180;
Nx = 51;
Ny = 51;
Nz = 360;
dx = 0.1;
dy = 0.1;
dz = 0.1;
idds = zeros(Nz,length(E));
cnt = 1;
x = ((1:Nx) - (Nx+1)/2)*dx;
Ne = length(E);
% generate system matrix with different xy position,different energy
% A = sparse(Nx*Ny*Nz,Ne*Nx*Ny);
% A = sparse(Nx*Ny,Nx*Ny*Nz);
gauss_para = zeros(8*Ne,Nz);
Loss = zeros(Ne,1);
tic;
for e = 180%E
    load([path,'/output/waterDose',num2str(e),'.mat'],'totalDose');
    [gauss_para_o,Dose_o,loss] = fit3dDose_v3(x,totalDose);
    gauss_para(((cnt-1)*8+1):cnt*8,:) = gauss_para_o;
    Loss(cnt) = loss;
    cnt = cnt + 1;
end
toc;
% save('gauss_para.mat','gauss_para','Ne','Nz','Loss');
% save('waterIDDs.mat','idds','E','dz');
%% determine thres ratio by sparsity
cnt = 1;
sparsity = zeros(10,1);
load([path,'/output/waterDose',num2str(180),'.mat'],'totalDose');
for thres = linspace(1e-3,1e-4,10)
    stencil = totalDose;
    thres = thres*max(totalDose,[],"all");
    stencil(stencil<thres) = 0;
    sparsity(cnt) = nnz(stencil);
    cnt = cnt + 1;
end
sparsity = sparsity./numel(totalDose);
plot(sparsity);