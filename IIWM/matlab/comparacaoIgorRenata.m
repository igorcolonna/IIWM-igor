

AreaIgor = [2.0271 2.2103    2.3603    2.5266    2.7206 3.0040    3.2334    3.4070    3.6084    3.8275 4.1216   4.4145    4.6402    4.8802    5.1412 5.4746   5.7849 6.0112    6.2539    6.5133 6.8855    7.2142    7.4517    7.7011 8.0254]
AreaRenata = 10 * [0.2027 0.2210 0.2360 0.2527 0.2721 0.3004 0.3233 0.3407 0.3608 0.3827 0.4122 0.4414 0.4640 0.4880 0.5141 0.5475 0.5785 0.6011 0.6254 0.6513 0.6886 0.7214 0.7452 0.7701 0.8025]             

RaioIgor = sqrt(AreaIgor/pi)
RaioRenata = sqrt(AreaRenata/pi)
quantDados = size(AreaIgor);
distance = 0.0088692;
volumeTotal = 0;
for count=1:quantDados(2)
        if count+1 <= quantDados(2)
            volumeTotal = volumeTotal + ((pi*distance)/3)*((RaioIgor(count)^2) + (RaioIgor(count)*RaioIgor(count+1)) + (RaioIgor(count+1)^2));
        end
end

VolumeIgor = volumeTotal

VolumeRenata = sum(AreaRenata(1:end-1))*distance
    
    
    