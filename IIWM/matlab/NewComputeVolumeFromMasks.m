function [volumeTotal] = NewComputeVolumeFromMasks(dados,distance)

    quantDados = size(dados);
    raiosMasks = sqrt(dados/pi);
    volumeTotal = 0;
    
    for count=1:quantDados(2)
        if count+1 <= quantDados(2)
            volumeTotal = volumeTotal + ((pi*distance*1000)/3)*((raiosMasks(count)^2) + (raiosMasks(count)*raiosMasks(count+1)) + (raiosMasks(count+1)^2));
        end
    end

end

