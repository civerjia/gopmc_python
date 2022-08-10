target2 = permute(target,[2,3,1]);
x = ((1:128)'-64.5)*0.2;
xy = [x,x];
N_gaussian = 9;
fun = @(para,xy) dose3d_mex(xy(:,1),xy(:,2),para,1,N_gaussian);
lb = repmat([0,-12.7,-12.7,1e-5,1e-5,0]',N_gaussian,1);% A,mux,muy,sigma1,sigma2,beta
ub = repmat([1e2,12.7,12.7,20,20,2*pi]',N_gaussian,1);% A,mux,muy,sigma, A,mux,muy,sigma
para0 = [];
for i = 1:N_gaussian
    r = 3;
    beta = 360*rand(1)*pi/180;
    para0 = [para0;[1,r*rand(1),r*rand(1),1,1,beta]'];
end
profile2d = target2(:,:,32);% < 40
options = optimoptions('lsqcurvefit','display','none',...
        'FunctionTolerance',1e-6,'OptimalityTolerance',1e-6,'StepTolerance',1e-6);
[para_o,resnorm] = lsqcurvefit(fun,para0,xy,profile2d,lb,ub,options);
disp(resnorm);
f = figure('Position',[10,10,900,250]);
subplot(1,3,1)
imagesc(fun(para_o,xy))
subplot(1,3,2)
imagesc(profile2d)
subplot(1,3,3)
imagesc(profile2d-fun(para_o,xy))