% % help funciton of dose3d_mex
% % generate 3d dose with gaussian fucntion layer by layer
% % author : shuang zhou civerjia@gmail.com
% x = (-30:30)'*1.3672;
% y = x;
% z = (1:220)'*1.3672;
% Nx = length(x);
% Ny = Nx;
% Nz = length(z);
% N_gaussian = 1;% number of gaussian function, should be > 0
% para = [A1,mux1,muy1,sigma1, A2,mux2,muy2,sigma2,...], for isotropic
% para = [A1,mux1,muy1,sigma1,sigma2,beta1, A2...], for anisotropic
% dose_mex = dose3d_mex(x,y,para, Nx,Ny,Nz,N_gaussian);
