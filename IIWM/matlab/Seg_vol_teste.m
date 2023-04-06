 %Seg_vol.m
%Calcula o volume para uma sequência de imagens 2D com a região de
%interesse (tumor) circunscrita a um contorno obtido por segmentação linear

clear all
close all
%tic;
%Dados iniciais
optionClosedFunction='hull';
ratioPixelMeter=0.000006;
distanceBetweenLayer=0.000025;

IMG = dir('C:\Users\Usuario\Documents\igor_imagens_teste\testeTumor\imagens\*.jpg');
filename_array = vertcat(IMG.name);
MASK = dir('C:\Users\Usuario\Documents\igor_imagens_teste\testeTumor\mask\*.tif');
GT_filename = vertcat(MASK.name);
rootImages = 'C:\Users\Usuario\Documents\igor_imagens_teste\testeTumor\imagens';
rootMask='C:\Users\Usuario\Documents\igor_imagens_teste\testeTumor\mask';
% filename_array=['teste0000.tif';'teste0001.tif';'teste0002.tif';'teste0003.tif';'teste0004.tif';'teste0005.tif';'teste0006.tif';'teste0007.tif';'teste0008.tif';'teste0009.tif';
%     'teste0010.tif';'teste0011.tif';'teste0012.tif';'teste0013.tif';'teste0014.tif';'teste0015.tif';'teste0016.tif';'teste0017.tif';'teste0018.tif';'teste0019.tif';'teste0020.tif';
%     'teste0021.tif';'teste0022.tif';'teste0023.tif';'teste0024.tif'];

% filename_array=['imagens processadas 20000.tif';'imagens processadas 20001.tif';'imagens processadas 20002.tif';'imagens processadas 20003.tif';'imagens processadas 20004.tif';'imagens processadas 20005.tif';
%                'imagens processadas 20006.tif';'imagens processadas 20007.tif';'imagens processadas 20008.tif';'imagens processadas 20009.tif';'imagens processadas 20010.tif';'imagens processadas 20011.tif';
%                'imagens processadas 20012.tif';'imagens processadas 20013.tif';'imagens processadas 20014.tif';'imagens processadas 20015.tif';'imagens processadas 20016.tif';'imagens processadas 20017.tif';
%                'imagens processadas 20018.tif';'imagens processadas 20019.tif';'imagens processadas 20020.tif';'imagens processadas 20021.tif';'imagens processadas 20022.tif';'imagens processadas 20023.tif';
%                'imagens processadas 20024.tif'];

% filename_array = ['image000.jpg';'image001.jpg';'image002.jpg';'image003.jpg';'image004.jpg';'image005.jpg';'image006.jpg';'image007.jpg';
%                   'image008.jpg';'image009.jpg';'image010.jpg';'image011.jpg';'image012.jpg';'image013.jpg';'image014.jpg';'image014.jpg';
%                   'image015.jpg';'image016.jpg';'image017.jpg';'image018.jpg';'image019.jpg';'image020.jpg';'image021.jpg';'image022.jpg';
%                   'image023.jpg';'image024.jpg'];

%filename_array=['image0000.tif';'image0001.tif';'image0002.tif';'image0003.tif'];
%rootImages= 'D:\Documentos\Igor_Colonna\teste_juliana\conico-2.5_sem_crop';
%rootImages= 'D:\Documentos\Igor_Colonna\teste_juliana\cilindrico-0.5mm-segmento2.5mm_sem_crop_e_scale';
% rootImages = 'C:\Users\Usuario\Documents\igor_imagens_teste\teste_mts_testes\imagem';

%GT_filename=['Mask0000.tif';'Mask0001.tif';'Mask0002.tif'];
%GT_filename=['Mask0000.tif';'Mask0005.tif';'Mask0010.tif';'Mask0015.tif';'Mask0020.tif';'Mask0024.tif'];
%GT_filename=['Mask20000.tif';'Mask20010.tif';'Mask20020.tif';'Mask20024.tif'];
% GT_filename=['mask000.tif';'mask005.tif';'mask010.tif';'mask015.tif';'mask020.tif';'mask024.tif'];
%rootMask='D:\Documentos\Igor_Colonna\teste_juliana\conico_mask_sem_crop';
%rootMask='D:\Documentos\Igor_Colonna\teste_juliana\cilindrico-0.5mm_mask_sem_crop';
%rootMask='C:\Users\jcm\Arquivos_Trabalho\Alunos\Rodrigo Oliveira\Segmentacao\Imagens';
% rootMask='C:\Users\Usuario\Documents\igor_imagens_teste\teste_mts_testes\mask';


type_filter='median';
level_processing=2;
stringTumorLayer= 'void';
IDX_LAYER='void';
save_option= true;
activeContour = true;
% root='C:\Users\Usuario\Documents\igor_imagens_teste\teste_mts_testes\resultado';
root='C:\Users\Usuario\Documents\igor_imagens_teste\testeTumor\result';
%Fim dos dados iniciais

[masksActivated,...
    volTotalEstimated,...
    volMasks] = segmentationUSImagesIG(optionClosedFunction, ...
                                        ratioPixelMeter, distanceBetweenLayer,...
                                        filename_array, rootImages, ...
                                        GT_filename, rootMask,...
                                        type_filter,...
                                        level_processing,...
                                        stringTumorLayer,...
                                        IDX_LAYER,...
                                        save_option,...
                                        activeContour, root);


%toc;

