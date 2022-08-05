if contains(pwd,'matlab_func')
    path = '..';
else
    path = '.';
end
%% read scene
load([path,'/output/MLSICscene.mat']);
load([path,'/output/MLSICdose.mat']);
%% write image
fileID = fopen([path,'/Phantom/geo_phantom.img'],'w+');
fwrite(fileID,scene,'short');
fclose(fileID);
%% read image
fileID = fopen([path,'/output/totalDose.img'],'r');
temp = fread(fileID,'float');
dose = reshape(temp,size(scene));
fclose(fileID);
%% read phantom image
fileID = fopen([path,'/Phantom/geo_phantom.img'],'r');
temp = fread(fileID,'int16');
phantom = reshape(temp,size(scene));%size(scene)
fclose(fileID);
%%
f = figure;
plot(squeeze(sum(sum(dose,1),2)));
hold on
plot(squeeze(scene(256,256,:)));
plot(squeeze(mean(mean(scene(200:300,200:300,:),1),2)))
legend('IDD','HU','mean HU')
%%
plot(squeeze(sum(sum(totalDose,1),2)))
hold on
plot(squeeze(scene(256,256,:)));
plot(squeeze(mean(mean(scene(200:300,200:300,:),1),2)))
%%
system('appgopmc_dose.exe --config ./Phantom/pencilbeam.cfg');