% Automatic multiscale-based peak detection (AMPD) algorithm
% author : shuang zhou 740110712@qq.com
% Reference : Scholkmann, Felix, Jens Boss, and Martin Wolf.
% "An efficient algorithm for automatic peak detection in noisy periodic and
% quasi-periodic signals." Algorithms 5.4 (2012): 588-603.
% inputs:
%   x : 1D array
%   pad: padding size, scalar
%   mode : padding mode, 'both','pre','post'
%          if first or last peak is missing, set mode to 'pre' or 'post'
%          with a proper pad size
% outputs:
%   p : indices of peaks
% example:
% N = 1000;
% t = linspace(0,200,N);
% x = 2*cos(2*pi*300*t)+5*sin(2*pi*100*t)+1*randn(1,N);
% p = AMPD(x);
% plot(t,x);
% hold on
% plot(t(p),x(p),'ro');
function p = AMPD(x,pad,mode)
    if nargin == 2 
        mode = 'both';
        if(size(x,1) > size(x,2))
            x = padarray(x,[pad,0],-1e6,mode);
        else
            x = padarray(x,[0,pad],-1e6,mode);
        end
    elseif nargin == 3
        if(size(x,1) > size(x,2))
            x = padarray(x,[pad,0],-1e6,mode);
        else
            x = padarray(x,[0,pad],-1e6,mode);
        end
    else
        pad = 0;
    end
    N = length(x);
    L = ceil(N/2)-1;
    m = rand(L,N)+1;
    lambda = 1;
    row_cnt_max = 1;
    for k = 1:L
        row_cnt = 0;
        for i = (k+2):(N-k+1)
            if(((x(i-1) > x(i-1-k)) && (x(i-1) > x(i-1+k))))
                m(k,i) = 0;
                row_cnt = row_cnt+1;
            end
        end
        if row_cnt > row_cnt_max
            row_cnt_max = row_cnt;
            lambda = k;
        end
    end
    mr = m(1:lambda,:);
    sigma = std(mr,0,1);
    p = find(sigma==0)-1;
    p = p - pad;
end

