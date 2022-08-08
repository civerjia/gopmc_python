function [gauss_para_o,Dose_o] = fit3dDose_v3(x,Dose_i)

if size(x,1) == 1
    x = x';
end
N_gaussian = 2;
[Dose_o,gauss_para_o] = gauss3d_dose(Dose_i,x,x,N_gaussian);
end

function [Dose_o,gauss_para_o] = gauss3d_dose(Dose3D,x,y,N_gaussian)
xy = [x,y];
idd = squeeze(sum(sum(Dose3D,1),2));
Nz = size(Dose3D,3);
gauss3d = @(para,xy) dose3d_mex(xy(:,1),xy(:,2),para,1,N_gaussian);
if N_gaussian ==2
lb = [0,0,0,1e-3, 0,0,0,1e-3]';% A,mux,muy,sigma, A,mux,muy,sigma
ub = [10,0,0,80, 10,0,0,80]';% A,mux,muy,sigma, A,mux,muy,sigma
% para = [1,0,0,5, 1e-2,0,0,5]';% A,mux,muy,sigma, A,mux,muy,sigma
gauss_para_o = zeros(8,size(Dose3D,3));
elseif N_gaussian ==1
lb = [0,0,0,1e-3]';% A,mux,muy,sigma
ub = [10,0,0,80]';% A,mux,muy,sigma
% para = [1,0,0,5]';% A,mux,muy,sigma
gauss_para_o = zeros(4,size(Dose3D,3));
end


% Dose_o = zeros(size(Dose3D));
% [m,n,~] = size(Dose3D);
valid = idd >= 4e-4*max(idd);
idx = 1:length(idd);
valid_idx = idx(valid);
for i = valid_idx
    profile2d = squeeze(Dose3D(:,:,i));
    if N_gaussian ==2
        para = [1.7*idd(i),0,0,5, 1e-2,0,0,5];
    else
        para = [1.7*idd(i),0,0,5];% A,mux,muy,sigma
    end
    options = optimoptions('lsqcurvefit','display','none',...
        'FunctionTolerance',1e-10,'OptimalityTolerance',1e-10,'StepTolerance',1e-10);
    [para_o,resnorm] = lsqcurvefit(gauss3d,para,xy,profile2d,lb,ub,options);
    gauss_para_o(:,i) = para_o;
    
end
Dose_o = dose3d_mex(xy(:,1),xy(:,2),gauss_para_o,Nz,N_gaussian);

end

