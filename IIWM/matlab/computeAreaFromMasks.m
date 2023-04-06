function [arrayAreas] = computeAreaFromMasks(MasksToCalculate, ratioPixelMeter)
    
    countMasks = size(MasksToCalculate);
    arrayAreas = [];
    
    for count=1:countMasks(1)
       arrayAreas = [arrayAreas, (bwarea(MasksToCalculate(count,:))*ratioPixelMeter^2*1e6)];
       
    end
    %AreaIgor = arrayAreas
end