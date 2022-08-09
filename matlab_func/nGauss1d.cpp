#define _USE_MATH_DEFINES
#include <array>
#include <vector>
#include <cmath>
#include <iostream>
#include <omp.h>
#include "mex.h"

template<class T>
inline T gauss1d(T x, T A, T mu, T sigma)
{
    T c{ M_SQRT1_2 * sqrt(M_1_PI) / sigma };
    return A * c * exp(-0.5 * pow((x - mu) / sigma, 2.0));
}


template<class T>
inline T dot2(T v1, T v2,T u1, T u2)
{
    return v1*u1 + v2*u2;
}

template<class T>
void dose3d_N(std::vector<T> X, std::vector<T>  para, T* ouput, int Nx, int N_gaussian)
{
#pragma omp parallel for firstprivate(X,para,Nx,N_gaussian)
    for (int nx = 0; nx < Nx; ++nx)
    {
        T x{ X[nx] };
        T temp {};
        for(int ng = 0; ng < N_gaussian; ++ng)
        {
            T A     = para[nz * N_gaussian * 4 + 4 * ng];
            T mu    = para[nz * N_gaussian * 4 + 4 * ng + 1];
            T sigma = para[nz * N_gaussian * 4 + 4 * ng + 2];
            T c = para[nz * N_gaussian * 4 + 4 * ng + 3];// constant term
            temp += gauss1d(x, A, mu, sigma) + c;
        }
        ouput[nx] = temp;
    }
}

void mexFunction(int nlhs, mxArray* plhs[], int nrhs, const mxArray* prhs[]) {
    double *X;
    double *para;
    X = mxGetPr(prhs[0]);
    para = mxGetPr(prhs[1]);

    const mwSize *dim_X = mxGetDimensions(prhs[0]);
    const mwSize *dim_para = mxGetDimensions(prhs[1]);
    int Nx = static_cast<int>(dim_X[0]*dim_X[1]);
    int N_para = static_cast<int>(dim_para[0]*dim_para[1]);
    int N_gaussian = static_cast<int>(*mxGetPr(prhs[2]));

    std::vector<double> X_vec(Nx);
    std::copy(X, X + Nx, X_vec.begin());

    const mwSize size[2]{ dim_X[0], dim_X[1] };
    plhs[0] = mxCreateNumericArray(2, size, mxDOUBLE_CLASS, mxREAL);
    double* output_ptr{};
    output_ptr = (double*)mxGetPr(plhs[0]);
    if(N_para == N_gaussian*4)
    {
        std::vector<double> para_vec(4*N_gaussian);
        std::copy(para, para + 4*N_gaussian, para_vec.begin());
        dose3d_N_iso(X_vec, para_vec, output_ptr, Nx, N_gaussian);
    }
    else
    {
        mexPrintf("N_gaussian(%d)*4 not match para size(%d)!\n",N_gaussian,N_para);
    }
}
