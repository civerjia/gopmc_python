use_openmp = 1;
if ismac && use_openmp
    % Code to run on Mac platform
    mex  CXXFLAGS='$CXXFLAGS -fopenmp' *.cpp
elseif isunix && use_openmp
    % Code to run on Linux platform
    mex  CXXFLAGS='$CXXFLAGS -fopenmp' *.cpp
elseif ispc && use_openmp
    % Code to run on Windows platform
    %mex  COMPFLAGS="$COMPFLAGS /openmp" *.cpp
    openmp_flag = 'COMPFLAGS="$COMPFLAGS /openmp"';
    avx_flag = 'CXXOPTIMFLAGS="\$CXXOPTIMFLAGS -mavx2"';
    src_path = './*.cpp';
    mex('-output','dose3d_mex',openmp_flag,avx_flag,src_path) 
else
    mex  *.cpp
end
% avx2 or avx512 are not set,
% if you compile with avx2, this function can even more faster
% the cpp file is suggest to compile with vs2019 + intel oneAPI(intel
% compiler) + openmp + avx2