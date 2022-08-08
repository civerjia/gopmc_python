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
Ne = length(E);
% generate system matrix with different xy position,different energy
% A = sparse(Nx*Ny*Nz,Ne*Nx*Ny);
A = sparse(Nx*Ny,Nx*Ny*Nz);
tic;
for e = 100%E
    load([path,'/output/waterDose',num2str(e),'.mat'],'totalDose');
    stencil = totalDose;
    thres = 3e-4*max(totalDose,[],"all");
    stencil(stencil<thres) = 0;
    %idds(:,cnt) = squeeze(sum(totalDose,[1,2]));
    row = [];
    col = [];
    val = [];
    for ix = ((1:2:Nx)-(Nx+1)/2)
        nx = ix + (Nx+1)/2;
        temp = circshift(stencil,ix,2);
        for iy = ((1:2:Ny)-(Ny+1)/2)
            ny = iy + (Ny+1)/2;
            idx = ny + (nx-1)*Ny;
            temp = circshift(temp,iy,1);
            %A(:,cnt) = sparse(temp(:));
            [r,c,v] = find(temp(:));
            row = [row;r];
            col = [col;c*idx];
            val = [val;v];
            cnt = cnt + 1;
        end
    end
    %
end
toc;
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