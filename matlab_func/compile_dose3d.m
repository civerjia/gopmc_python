use_openmp = 1;
if ismac && use_openmp
    % Code to run on Mac platform
    mex  CXXFLAGS='$CXXFLAGS -fopenmp' dose3d_mex.cpp
elseif isunix && use_openmp
    % Code to run on Linux platform
    mex  CXXFLAGS='$CXXFLAGS -fopenmp' dose3d_mex.cpp
elseif ispc && use_openmp
    % Code to run on Windows platform
    %mex  COMPFLAGS="$COMPFLAGS /openmp" *.cpp
    openmp_flag = 'COMPFLAGS="$COMPFLAGS /openmp"';
    avx_flag = 'CXXOPTIMFLAGS="\$CXXOPTIMFLAGS -mavx2"';
    src_path = './dose3d_mex.cpp';
    mex('-output','dose3d_mex',openmp_flag,avx_flag,src_path) 
    mexcuda('-output', 'dose3d_gpu','-R2018a','dose3d.cu');
else
    mex  dose3d_mex.cpp
end
% avx2 or avx512 are not set,
% if you compile with avx2, this function can even more faster
% the cpp file is suggest to compile with vs2019 + intel oneAPI(intel
% compiler) + openmp + avx2
