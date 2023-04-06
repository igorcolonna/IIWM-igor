clear all

method = 'hull';

img = imread('imagem-errado.tif');

imshow(img);

closedContour = generateClosedContour5(img, method);

imshow(closedContour);
