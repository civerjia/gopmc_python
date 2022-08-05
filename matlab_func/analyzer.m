%% read scene
if contains(pwd,'matlab_func')
    path = '..';
else
    path = '.';
end
load([path,'/output/MLSICscene.mat']);
load([path,'/output/MLSICdose.mat']);
%%
MLSIC_3Ddose = totalDose(:,:,MLSIC(2:end));
f = figure;
% x_ROI = 210:310;
% y_ROI = 210:310;
x_ROI = 1:size(MLSIC_3Ddose,1);
y_ROI = 1:size(MLSIC_3Ddose,2);
subplot(1,3,1)
imagesc(MLSIC_3Ddose(x_ROI,y_ROI,2));
subplot(1,3,2)
imagesc(MLSIC_3Ddose(x_ROI,y_ROI,30));
subplot(1,3,3)
imagesc(MLSIC_3Ddose(x_ROI,y_ROI,60));
%%
f = figure;
% subplot(3,1,1)
% imagesc(squeeze(MLSIC_3Ddose(x_ROI,260,:)));
% subplot(3,1,2)
% imagesc(squeeze(MLSIC_3Ddose(x_ROI,270,:)));
% subplot(3,1,3)
% imagesc(squeeze(MLSIC_3Ddose(x_ROI,280,:)));
subplot(3,1,1)
imagesc(squeeze(MLSIC_3Ddose(260,x_ROI,:)));
subplot(3,1,2)
imagesc(squeeze(MLSIC_3Ddose(270,x_ROI,:)));
subplot(3,1,3)
imagesc(squeeze(MLSIC_3Ddose(280,x_ROI,:)));
%% IDD
depth = ((1:size(MLSIC_3Ddose,3))-1)*0.15;
f = figure;
plot(depth,squeeze(sum(sum(MLSIC_3Ddose,1),2)));
xlabel('Depth (cm)')
ylabel('Dose(a.u.)')
grid on
grid minor
% exportgraphics(f,[path,'/output/','IDD.png'],'Resolution',600)
%% re-interporate to detector size
% x_ct = ((1:512) - 256.5)*0.126953;
x_ct = ((160:360)-1 - 256.5)*0.126953;
y_ct = x_ct;
x_mlsic = ((1:128)-64.5)*0.2;
y_mlsic = x_mlsic;
z_ct = ((1:size(MLSIC_3Ddose,3))-1)*0.15;
temp = zeros(length(x_mlsic),length(x_mlsic),size(MLSIC_3Ddose,3));

[X_ct,Y_ct] = meshgrid(x_ct,y_ct);
[X_mlsic,Y_mlsic] = meshgrid(x_mlsic,y_mlsic);

for i = 1:size(MLSIC_3Ddose,3)
    temp(:,:,i) = interp2(X_ct,Y_ct,squeeze(MLSIC_3Ddose(:,:,i)),X_mlsic,Y_mlsic,'linear',0);
end
MLSIC_det = zeros(length(x_mlsic),length(x_mlsic),floor(size(MLSIC_3Ddose,3)/2));
for i = 1:2:floor(size(MLSIC_3Ddose,3)/2)*2
    MLSIC_det(:,:,(i+1)/2) = temp(:,:,i) + temp(:,:,i+1);
end
z = ((1:size(MLSIC_det,3))-1)*0.3;
save('pRG2.mat',"MLSIC_det",'x_mlsic','z');
target = permute(MLSIC_det,[3,1,2]);
% save('target2.mat','target')
%% create simulated measure data
x_meas = sum(MLSIC_det(:,:,1),1);
y_meas = sum(MLSIC_det(:,:,2),2);
[z1_meas,z2_meas] = get_z_meas(MLSIC_det);
[z1_meas2,z2_meas2,z1,z2] = get_z_meas2(MLSIC_det);
%%
f = figure;
plot(x_meas);hold on
plot(y_meas);
legend('X','Y')
grid on
grid minor
exportgraphics(f,[path,'/output/','xy_meas.png'],'Resolution',600)
%%
f = figure;
subplot(3,2,1)
imagesc(z1_meas)
title('z1')
subplot(3,2,2)
imagesc(z2_meas)
title('z2')
subplot(3,2,3)
imagesc(z1_meas2)
title('z1 new')
subplot(3,2,4)
imagesc(z2_meas2)
title('z2 new')
subplot(3,2,5)
imagesc(z1)
title('z1 gt')
subplot(3,2,6)
imagesc(z2)
title('z2 gt')
% exportgraphics(f,[path,'/output/','z_meas.png'],'Resolution',600)
%%
Nz = 1;
N_gauss = 1;
para0 = [1,0,0,1.5,0.2,0*pi/180];
dose_mex = dose3d_mex(x_mlsic,y_mlsic,para0,Nz,N_gauss);
%%
function [z1_meas,z2_meas] = get_z_meas(MLSIC_det)
space = 8;
z1_meas = zeros(8,size(MLSIC_det,3)/2-1);
z2_meas = z1_meas;
idx = reshape(1:128,space,[]);
for i = 3:2:size(MLSIC_det,3)
    z1 = sum(MLSIC_det(:,:,i),1);
    z2 = sum(MLSIC_det(:,:,i+1),2);
    z1_meas(:,(i+1)/2-1) = sum(z1(idx),2);
    z2_meas(:,(i+1)/2-1) = sum(z2(idx),2);
end
end

function [z1_meas,z2_meas,z1_gt,z2_gt] = get_z_meas2(MLSIC_det)
space = 4;
z1_meas = zeros(8,size(MLSIC_det,3)/2-1);
z2_meas = z1_meas;
z1_gt = zeros(128,size(MLSIC_det,3)/2-1);
z2_gt = z1_gt;
temp = reshape(1:128,space,[]);
temp1 = temp';
idx = reshape(temp1,8,[]);
for i = 3:2:size(MLSIC_det,3)
    z1 = sum(MLSIC_det(:,:,i),1);
    z2 = sum(MLSIC_det(:,:,i+1),2);
    z1_gt(:,(i+1)/2-1) = z1';
    z2_gt(:,(i+1)/2-1) = z2;
    z1_meas(:,(i+1)/2-1) = sum(z1(idx),2);
    z2_meas(:,(i+1)/2-1) = sum(z2(idx),2);
end
end