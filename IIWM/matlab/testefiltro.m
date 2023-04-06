[image000,~,alpha] = imread('image000.jpg');
[image3750,~,alpha3750] = imread('imagem3750.jpeg');
[image001,~,alpha01] = imread('image001.jpeg'); 
phantom000 = imread('phantom_alinhado0000.tif');

arrayIMG = imReadArrayNoTreatment('C:\Users\Usuario\Documents\igor_imagens_teste\teste_mts_testes\imagem');
arrayMask = imReadArrayNoTreatmentMask('C:\Users\Usuario\Documents\igor_imagens_teste\teste_mts_testes\mask');
Mask000 = imread('Mask000.tif');
Mask3750 = imread('Mask3750.tif');
Maskphantom = imread('Maskalinhado000.tif');

image000 = squeeze(image000(:,:,1));
Iarray000 = arrayIMG{1};
Marray000 = arrayMask{1};
%teste = rgb2gray(image000);
image3750 = squeeze(image3750(:,:,1));
image001 = squeeze(image001(:,:,1));
phantom000 = squeeze(phantom000(:,:,1));

teste = Iarray000.*(Marray000/255);
%teste = times(image000, (Mask000/255));
figure(1)
imshow(Iarray000)

zeropict = zeros(size(teste),class(teste));
%image000 = image000 - teste;
Iarray000 = Iarray000 - teste;
redpict = cat(3,teste,zeropict, zeropict);

figure(2)
imshow(redpict)

figure(3)
result = Iarray000+redpict; 
imshow(result)  