function [gauss_para_o,Dose_o,loss] = fit3dDose_v3(x,Dose_i)

if size(x,1) == 1
    x = x';
end
N_gaussian = 2;
[Dose_o,gauss_para_o,loss] = gauss3d_dose(Dose_i,x,x,N_gaussian);
end

function [Dose_o,gauss_para_o,loss] = gauss3d_dose(Dose3D,x,y,N_gaussian)
xy = [x,y];
idd = squeeze(sum(sum(Dose3D,1),2));
Nz = size(Dose3D,3);
if gpuDeviceCount > 0
    gauss3d = @(para,xy) double(dose3d_gpu(single(xy(:,1)),single(xy(:,2)),single(para),1,N_gaussian));
else
    gauss3d = @(para,xy) dose3d_mex(xy(:,1),xy(:,2),para,1,N_gaussian);
end
if N_gaussian ==2
    %  sigma = 0 will return 0
    lb = [0,0,0,0, 0,0,0,0]';% A,mux,muy,sigma, A,mux,muy,sigma
    ub = [10,0,0,80, 10,0,0,80]';% A,mux,muy,sigma, A,mux,muy,sigma
    % para = [1,0,0,5, 1e-2,0,0,5]';% A,mux,muy,sigma, A,mux,muy,sigma
    gauss_para_o = zeros(8,size(Dose3D,3));
elseif N_gaussian ==1
    lb = [0,0,0,0]';% A,mux,muy,sigma
    ub = [10,0,0,80]';% A,mux,muy,sigma
    % para = [1,0,0,5]';% A,mux,muy,sigma
    gauss_para_o = zeros(4,size(Dose3D,3));
end
dS = (x(2)-x(1))*(y(2)-y(1));

c = 1/(2*pi);
% Dose_o = zeros(size(Dose3D));
% [m,n,~] = size(Dose3D);
valid = idd > 4e-4*max(idd);
idx = 1:length(idd);
valid_idx = idx(valid);
loss = zeros(Nz,1);
for i = valid_idx
    profile2d = squeeze(Dose3D(:,:,i));
    A = idd(i)*dS;% area
    maxv = max(profile2d,[],'all');
    sigma0 = sqrt(A*c/maxv);
    if N_gaussian ==2
        para = [A,0,0,sigma0, 1e-2,0,0,1];
    else
        para = [A,0,0,sigma0];% A,mux,muy,sigma
    end
    options = optimoptions('lsqcurvefit','display','none',...
        'FunctionTolerance',1e-6,'OptimalityTolerance',1e-6,'StepTolerance',1e-6);
    [para_o,resnorm] = lsqcurvefit(gauss3d,para,xy,profile2d,lb,ub,options);
    gauss_para_o(:,i) = para_o;
    loss(i) = resnorm;
    
end
Dose_o = dose3d_mex(xy(:,1),xy(:,2),gauss_para_o,Nz,N_gaussian);
loss = mean(loss(valid_idx));
end

