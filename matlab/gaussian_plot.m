x = 0:10/100:10;
sigmas = 0.5:0.5:1.5;
mu = 5;
ys = [];
for sigma = sigmas
    y = (1/sqrt(2*pi*sigma^2))*exp(-(x-mu).^2/(2*sigma^2))
    plot (x,y)
    ys = [ys;y]
    
end 
plot(x,ys)


