cd('C:\Users\Usuario\Documents\Vanessa\HPG1_Experimento1_01.02.2024')

A = imread('C:\Users\Usuario\Documents\Vanessa\HPG1_Experimento1_01.02.2024\segmento_tumor1\image0010.jpg');
mask = imread('C:\Users\Usuario\Documents\Vanessa\HPG1_Experimento1_01.02.2024\all_masks_teste_CF\Mask0010.tif');

bw = activecontour(A, mask, 100, 'edge','ContractionBias',0);

figure(1)
imshow(A)

figure(2)
imshow(mask)

figure(3)
imshow(bw)
