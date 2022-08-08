// dose3d.cpp : This file contains the 'mexFunction' function. Program execution begins and ends there.
//
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
inline T gauss2d(T x, T y, T A, T mux, T muy, T sigma)
{
    if ((sigma < 1e-10))
    {
        return 0.0;
    }
    else
    {
		T half_1_sigma2 = 0.5 * pow(1.0 / sigma, 2.0);
		return A * M_1_PI * half_1_sigma2 * exp(-half_1_sigma2 * (pow((x - mux), 2.0) + pow((y - muy), 2.0)));
    }
}
template<class T>
inline T gauss2d_2(T x, T y, T A1, T mux1, T muy1, T sigma1, T A2, T mux2, T muy2, T sigma2)
{
    if ((sigma1 < 1e-10) | (sigma2 < 1e-10))
    {
        return 0.0;
    }
    else
    {
        T half_1_sigma2_1 = 0.5 * pow(1.0 / sigma1, 2.0);
        T half_1_sigma2_2 = 0.5 * pow(1.0 / sigma2, 2.0);
        return A1 * M_1_PI * half_1_sigma2_1 * exp(-half_1_sigma2_1 * (pow((x - mux1), 2.0) + pow((y - muy1), 2.0))) +
            A2 * M_1_PI * half_1_sigma2_2 * exp(-half_1_sigma2_2 * (pow((x - mux2), 2.0) + pow((y - muy2), 2.0)));
    }
}

template<class T>
inline T dot2(T v1, T v2,T u1, T u2)
{
    return v1*u1 + v2*u2;
}

template<class T>
inline T mvn2d(T x, T y, T A, T mux, T muy, T sigma1, T sigma2, T beta)
{
    if ((sigma1 < 1e-10) | (sigma2 < 1e-10))
    {
        return 0.0;
    }
    else
    {
        T sigma11 = sigma1*sigma1;
        T sigma12 = 0;
        T sigma21 = 0;
        T sigma22 = sigma2*sigma2;
        T det = sigma11 * sigma22 - sigma12 * sigma21;

        // invsere of corvariance matrix 
        T a =  sigma22/det;
        T b = -sigma12/det;
        T c = -sigma21/det;
        T d =  sigma11/det;

        // v = Rot([x - mux;y - muy])
        T v1 = std::cos(beta)*(x - mux) - std::sin(beta)*(y - muy);
        T v2 = std::sin(beta)*(x - mux) + std::cos(beta)*(y - muy);
        // v' * M^-1 * v
        T u1 = a * v1 + b * v2;
        T u2 = c * v1 + d * v2;
        T exponant = -0.5*dot2(v1, v2, u1, u2);
        T scale = (A*0.5*M_1_PI)/sqrt(abs(det));

        return scale * exp(exponant);
    }
}

template<class T>
void dose3d(std::vector<T> X, std::vector<T> Y, T* para, T* dose3d, int Nx, int Ny, int Nz)
{
#pragma omp parallel for firstprivate(X,Y,Nx,Ny,Nz)
    for (int nz = 0; nz < Nz; ++nz)
    {
        T A1     = para[nz * 4];
        T mux1   = para[nz * 4 + 1];
        T muy1   = para[nz * 4 + 2];
        T sigma1 = para[nz * 4 + 3];
        for (int ny = 0; ny < Ny; ++ny)
        {
            T y{ Y[ny] };
            for (int nx = 0; nx < Nx; ++nx)
            {
                T x{ X[nx] };
                int idx3d{ nx + ny * Nx + nz * (Nx * Ny) };
                dose3d[idx3d] = gauss2d(x, y, A1, mux1, muy1, sigma1);
            }
        }
    }
}

template<class T>
void dose3d_2(std::vector<T> X, std::vector<T> Y, T* para, T* dose3d, int Nx, int Ny, int Nz)
{
#pragma omp parallel for firstprivate(X,Y,Nx,Ny,Nz)
    for (int nz = 0; nz < Nz; ++nz)
    {
		T A1     = para[nz * 8];
		T mux1   = para[nz * 8 + 1];
		T muy1   = para[nz * 8 + 2];
		T sigma1 = para[nz * 8 + 3];
		T A2     = para[nz * 8 + 4];
		T mux2   = para[nz * 8 + 5];
		T muy2   = para[nz * 8 + 6];
		T sigma2 = para[nz * 8 + 7];
        for (int ny = 0; ny < Ny; ++ny)
        {
            T y{ Y[ny] };
            for (int nx = 0; nx < Nx; ++nx)
            {
                T x{ X[nx] };
                int idx3d{ nx + ny * Nx + nz * (Nx * Ny) };
				dose3d[idx3d] = gauss2d_2(x, y, A1, mux1, muy1, sigma1, A2, mux2, muy2, sigma2);
            }
        }
    }
}
template<class T>
void dose3d_N_iso(std::vector<T> X, std::vector<T> Y, std::vector<T>  para, T* dose3d, int Nx, int Ny, int Nz, int N_gaussian)
{
#pragma omp parallel for firstprivate(X,Y,Nx,Ny,Nz,para)
    for (int nz = 0; nz < Nz; ++nz)
    {
        for (int ny = 0; ny < Ny; ++ny)
        {
            T y{ Y[ny] };
            for (int nx = 0; nx < Nx; ++nx)
            {
                T x{ X[nx] };
                int idx3d{ nx + ny * Nx + nz * (Nx * Ny) };
                T temp {};
                for(int ng = 0; ng < N_gaussian; ++ng)
                {
                    T A1     = para[nz * N_gaussian * 4 + 4 * ng];
                    T mux1   = para[nz * N_gaussian * 4 + 4 * ng + 1];
                    T muy1   = para[nz * N_gaussian * 4 + 4 * ng + 2];
                    T sigma1 = para[nz * N_gaussian * 4 + 4 * ng + 3];
                    temp += gauss2d(x, y, A1, mux1, muy1, sigma1);
                }
                dose3d[idx3d] = temp;
            }
        }
    }
}

template<class T>
void dose3d_N(std::vector<T> X, std::vector<T> Y, std::vector<T>  para, T* dose3d, int Nx, int Ny, int Nz, int N_gaussian)
{
#pragma omp parallel for firstprivate(X,Y,Nx,Ny,Nz,para)
    for (int nz = 0; nz < Nz; ++nz)
    {
        for (int ny = 0; ny < Ny; ++ny)
        {
            T y{ Y[ny] };
            for (int nx = 0; nx < Nx; ++nx)
            {
                T x{ X[nx] };
                int idx3d{ nx + ny * Nx + nz * (Nx * Ny) };
                T temp {};
                for(int ng = 0; ng < N_gaussian; ++ng)
                {
                    T A     = para[nz * N_gaussian * 6 + 6 * ng];
                    T mux   = para[nz * N_gaussian * 6 + 6 * ng + 1];
                    T muy   = para[nz * N_gaussian * 6 + 6 * ng + 2];
                    T sigma1= para[nz * N_gaussian * 6 + 6 * ng + 3];
                    T sigma2= para[nz * N_gaussian * 6 + 6 * ng + 4];
                    T beta  = para[nz * N_gaussian * 6 + 6 * ng + 5];
                    temp += mvn2d(x, y, A, mux, muy, sigma1, sigma2, beta);
                }
                dose3d[idx3d] = temp;
            }
        }
    }
}

void mexFunction(int nlhs, mxArray* plhs[], int nrhs, const mxArray* prhs[]) {
    double *X;
    double *Y;
    double *para;
    X = mxGetPr(prhs[0]);
    Y = mxGetPr(prhs[1]);
    para = mxGetPr(prhs[2]);

    const mwSize *dim_X = mxGetDimensions(prhs[0]);
    const mwSize *dim_Y = mxGetDimensions(prhs[1]);
    const mwSize *dim_para = mxGetDimensions(prhs[2]);
    int Nx = static_cast<int>(dim_X[0]*dim_X[1]);
    int Ny = static_cast<int>(dim_Y[0]*dim_Y[1]);
    int N_para = static_cast<int>(dim_para[0]*dim_para[1]);

    int Nz = static_cast<int>(*mxGetPr(prhs[3]));
    int N_gaussian = static_cast<int>(*mxGetPr(prhs[4]));

    std::vector<double> X_vec(Nx), Y_vec(Ny);
    std::copy(X, X + Nx, X_vec.begin());
    std::copy(Y, Y + Ny, Y_vec.begin());

    const mwSize size[3]{ mwSize(Nx), mwSize(Ny), mwSize(Nz) };
    plhs[0] = mxCreateNumericArray(3, size, mxDOUBLE_CLASS, mxREAL);
    double* dose3d_ptr{};
    dose3d_ptr = (double*)mxGetPr(plhs[0]);
    if(N_para == Nz*N_gaussian*6)
    {
        std::vector<double> para_vec(6*N_gaussian*Nz);
        std::copy(para, para + 6*N_gaussian*Nz, para_vec.begin());
        dose3d_N(X_vec, Y_vec, para_vec, dose3d_ptr, Nx, Ny, Nz, N_gaussian);
        
    }
    else if(N_para == Nz*N_gaussian*4)
    {
        std::vector<double> para_vec(4*N_gaussian*Nz);
        std::copy(para, para + 4*N_gaussian*Nz, para_vec.begin());
        dose3d_N_iso(X_vec, Y_vec, para_vec, dose3d_ptr, Nx, Ny, Nz, N_gaussian);
    }
    else
    {
        mexPrintf("N_gaussian(%d)*Nz(%d) not match para size(%d)!\n",N_gaussian,Nz,N_para);
    }
}
