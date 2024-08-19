% Projeto final -  Segmentação de colon de camundongos
% 
% Author: Igor Soares Colonna - igorcolonna@poli.ufrj.br
%         Renata Porciuncula Baptista - r.baptista@poli.ufrj.br
% Orientador: Joao Carlos Machado - jcm@peb.ufrj.br
% Date: 16 August 2019, v1.1 
%        07 September 2019, v2.0
%          16 August 2024, v3.0

function [masksActivated,...
         volTotalEstimated,...
         volMasks] = segmentationUSImagesIG(optionClosedFunction, ...
                                        ratioPixelMeter, distanceBetweenLayer,...
                                        images_filename, rootImages, ...
                                        GT_filename, rootMask,...
                                        type_filter,...
                                        level_processing,...
                                        stringTumorLayer,...
                                        IDX_LAYER,...
                                        save_option,...
                                        activeContour, root) 
    clc;
    tic;
    % Warningss
    warning('off', 'Images:initSize:adjustingMag'); % turning off warning size image
    warning('off', 'images:activecontour:vanishingContour'); %turning off warning about active contour

    % Briefing about the code
    fprintf('--------------------------------------------------------\n\n');
    fprintf('               SEGMENTATION US SCRIPT                   \n\n');
    fprintf('Author: Igor Soares Colonna, Renata Baptista\n')   ;
    fprintf('Email: igorcolonna@poli.ufrj.br, r.baptista@poli.ufrj.br\n');
    fprintf('v3.0 - 16/08/2024 \n');
    fprintf('--------------------------------------------------------\n\n');

    PATH = which('segmentationUSImagesIG');
    PATH = erase(PATH,'\segmentationUSImagesIG.m');
    % ---------------------- TREATING OPTIONAL ARGUMENTS
    %if ~exist('save_option','var')
    %  save_option = false;
    %end
    if ~exist('type_init','var')
      type_init = 'hull';
    end
    if  ~exist('level_processing', 'var')
        level_processing = 2;
    end
    

       
    % ------------------------ PATHS, INITIALIZATION
    % Root path 
    % Constants
    INITIAL_MASK = 1;
    %NB_IMG = size(images_filename, 1);

    % Load data
    fprintf('Loading images:\n')
    %tic;

    % Data
    images = imReadArray(images_filename, rootImages, false);
    imagesNoTreatment = imReadArrayNoTreatment(rootImages);
    masks = 255*imReadArray(GT_filename, rootMask, true);
    
%     imageFiles = dir(rootImages);
%     nfiles = length(imageFiles);
%     
%     for ii=1:nfiles
%         currentfilename = imageFiles(ii).name;
%         currentIMG = imread(currentfilename);
%         images{ii} = currentIMG;
%     end
    
%     figure(1)
%     maskteste1=squeeze(masks(1,:,:));
%     imshow (maskteste1)
    
    idxMasksToNotCompute = getIndexFromName(images_filename,GT_filename);
    steps_vector = diff(idxMasksToNotCompute);
    idxMaskToCompute = setdiff(1:size(images_filename,1), idxMasksToNotCompute);
    
%     idxMasksToNotCompute
%     idxMaskToCompute
    
    % Constant
    NB_MASK = size(masks, 1);

    % Output
    masksInterpolated = zeros(size(images));
    masksActivated = zeros(size(images));
    %toc;
    
    %% Filtering
    fprintf('\nFiltering images:\n')
    %tic;
    if strcmp(type_filter,'None')
         disp(['User opt for not filter images'])
    else
       images = filterArray(images, type_filter);
    end
    %toc;
    %% Interpolating
    % first, getting contours
    masksGrad = imGradientArray(masks);
    %fprintf('idxMaskToNotCompute: %d\n', idxMasksToNotCompute);
    %fprintf('steps_vector: %d\n', steps_vector);
    %fprintf('\nInterpolating images between well defined masks:\n')
    %tic;
    % coordinates of non null
    cum_step = 0;
    for iMask = 1:NB_MASK - 1
        maskCurrent = squeeze(masksGrad(iMask,:,:));
        maskNext = squeeze(masksGrad(iMask+1,:,:));
        % Finding points non null mask Current
        [Xcur, Ycur] = ind2sub(size(maskCurrent), find(maskCurrent));
        [Xnext, Ynext] = ind2sub(size(maskNext), find(maskNext));

        Zcur = ones(size(Xcur)) * (INITIAL_MASK + cum_step);
        cum_step = cum_step+abs(steps_vector(iMask));
        Znext = ones(size(Xnext)) * (INITIAL_MASK + cum_step);

        %%%%%%%%%%
        
        if save_option == true
            cd(root)
            aux1='Mask';
            aux3='.tif';
            aux2=sprintf('%04d', idxMasksToNotCompute(iMask)-1);
            filename=strcat(aux1,aux2,aux3);
            
            imgTemp = imagesNoTreatment{idxMasksToNotCompute(iMask)};
            
            %maskTemp = masks(iMask,:,:);
            maskTemp = squeeze(masks(iMask,:,:));
            maskTemp = uint8(maskTemp);
            %imwrite(maskTemp,'maskTemp.tif')
            
            bw = bwperim(maskTemp,8);
            
            se = strel('line',10,0);
            bw = imdilate(bw,se);
%             figure(1)
%             imshow(maskTemp)
            %imgTemp = squeeze(imgTemp(:,:,1));
            %figure(2)
            %imshow(imgTemp)
            %maskTemp = squeeze(maskTemp(:,:,1));
        
            filtro = imgTemp.*(maskTemp/255);
            %imwrite(filtro,'filtro.tif')
            %filtro = times(imgTemp, maskTemp/255);
            imgTemp = imgTemp - filtro;
            %imwrite(imgTemp, 'imgTemp-filtro.tif')
            
            zeropict = zeros(size(filtro),class(filtro));
            redpict = cat(3,filtro,zeropict, zeropict);
            redpict2 = cat(3,maskTemp.*255,zeropict,zeropict).* 0.3;
            boundpict = cat(3,bw.*255,zeropict,zeropict);
            
            %result = imgTemp+redpict+redpict2+boundpict;
            result = imgTemp+redpict+redpict2;
            imwrite(result,filename);
            %imwrite(result,filename);
            
            %imwrite(squeeze(masks(iMask,:,:)),filename);
          
            %Lugar aonde fica os codigos do matlab
            cd(PATH)
            %cd('C:\Users\Usuario\Downloads\fiji-win64\Fiji.app\IIWM\matlab')
        end
        
        
        for idxPt=1:size(Xcur,1) % for each point non null in maskCur,
                              % find closest in mask Next
                              % then determine all the points on the line
                              % between and draw then as one in the
                              % maskInterpolated
            ptA = [Xcur(idxPt), Ycur(idxPt), Zcur(idxPt)];
            closestB = findClosestPoint(ptA, [Xnext, Ynext, Znext]);
            coordinates = getCoordinatesOnTheLine(ptA, closestB, steps_vector(iMask));
            XYZ = round(coordinates);

            % linear indexing to change all points at once
            ind = sub2ind(size(masksInterpolated), XYZ(:,3),XYZ(:,1),XYZ(:,2));  
            masksInterpolated(ind) = 255;

        end
    end
    %toc;
    
    % Salvando a ultima mascara inserida
    
    if save_option == true
        cd(root)
        aux1='Mask';
        aux3='.tif';
        aux2=sprintf('%04d', idxMasksToNotCompute(iMask+1)-1);
        filename=strcat(aux1,aux2,aux3);
        
        imgTemp = imagesNoTreatment{idxMasksToNotCompute(iMask+1)};
        %maskTemp = masks(iMask+1,:,:);
        maskTemp = squeeze(masks(iMask+1,:,:));
        maskTemp = uint8(maskTemp);
        
        bw = bwperim(maskTemp,8);
        se = strel('line',10,0);
        bw = imdilate(bw,se);
        %imgTemp = squeeze(imgTemp(:,:,1));
        %maskTemp = squeeze(maskTemp(:,:,1));
        filtro = imgTemp.*(maskTemp/255);
        %filtro = times(imgTemp, maskTemp/255);
        imgTemp = imgTemp - filtro;
            
        zeropict = zeros(size(filtro),class(filtro));
        redpict = cat(3,filtro,zeropict, zeropict);
        redpict2 = cat(3,maskTemp.*255,zeropict,zeropict).* 0.3;
        boundpict = cat(3,bw.*255,zeropict,zeropict);
        
        %result = imgTemp+redpict+redpict2+boundpict;
        result = imgTemp+redpict+redpict2;
        %imwrite(result,filename);
        imwrite(result,filename);
        
        %imwrite(squeeze(masks(iMask+1,:,:)),filename);
          
        %Lugar aonde fica os codigos do matlab
        cd(PATH)
        %cd('C:\Users\Usuario\Downloads\fiji-win64\Fiji.app\IIWM\matlab')
    end
    % Works well, problem is not continous

    %% Closing the mask to initialize active contour
    fprintf('\nClosing initial contour:\n')
    %tic;
    closedContour = zeros(size(images));
    %idxMaskToCompute 
    count_mask=1;
    n_iterations = 100;
    for idx = idxMaskToCompute 
        img = squeeze(masksInterpolated(idx,:,:));
        %closedContour(idx,:,:) = generateClosedContour(img, optionClosedFunction);
        %MODIFICADO EM 10/03/2021s
        %imshow(img);
        closedContour(idx,:,:) = generateClosedContour5(img, optionClosedFunction);
%         figure(1)
%         imshow(squeeze(closedContour(idx,:,:)),[])
        if activeContour == true
%             size(imagesNoTreatment{idxMaskToCompute(count_mask)})
%             size(squeeze(closedContour(idx,:,:)))
            closedContour(idx,:,:) = activecontour(imagesNoTreatment{idxMaskToCompute(count_mask)}, squeeze(closedContour(idx,:,:)), n_iterations,'edge','ContractionBias',0);
%             bw = bwperim(squeeze(closedContour(idx,:,:)),8);
%             se = strel('line',10,0);
%             bw = imdilate(bw,se);
            %Bounds = visboundaries(squeeze(closedContour(idx,:,:)),'Color','g');
            %bw = activecontour(imagesNoTreatment(idxMaskToCompute(count_mask - 1)), closedContour(idx,:,:), n_iterations);
%             figure(2)  
%             imshow(squeeze(closedContour(idx,:,:)),[])
        end
        
        %imshow(img)
        %size(closedContour(idx,:,:))
        
          %alterado em 5/03/2021
      % cd ('C:\Users\DELL\Desktop\mask')
      if save_option == true
          cd (root)
          %cd ('D:\Documentos\Igor Colonna\Teste matlab\Arquivos imagens\Salvar mascaras')
          aux1='Mask';
          aux3='.tif';
          aux2=sprintf('%04d',[idxMaskToCompute(count_mask)-1]);
          filename=strcat(aux1,aux2,aux3);
          indexMask = idxMaskToCompute(count_mask);
          imgTemp = imagesNoTreatment{indexMask};
          maskTemp = squeeze(closedContour(idx,:,:));
          
          bw = bwperim(squeeze(closedContour(idx,:,:)),8);
          se = strel('line',10,0);
          bw = imdilate(bw,se);
%           figure(idx)
%           imshow(maskTemp)
%           figure(5)
%           imshow(imgTemp)
          %maskTemp = squeeze(closedContour(idx,:,:));
          
          %imgTemp = squeeze(imgTemp(:,:,1));
          %figure(6)
          %imshow(imgTemp)
          %maskTemp = squeeze(maskTemp(:,:,1));
          maskTemp = uint8(maskTemp);
          %figure(6)
          %imshow(maskTemp)
          
          filtro = imgTemp.*(maskTemp);
          %filtro = times(imgTemp, maskTemp/255);
          imgTemp = imgTemp - filtro;
            
          zeropict = zeros(size(filtro),class(filtro));
          
          redpict = cat(3,filtro,zeropict, zeropict);
          redpict2 = cat(3,maskTemp.*255,zeropict,zeropict).* 0.3;
          boundpict = cat(3,bw.*255,zeropict,zeropict);
%           figure(4)
%           imshow(boundpict)
          %result = imgTemp+redpict+redpict2+boundpict;
          result = imgTemp+redpict+redpict2;
%           figure(5)
%           imshow(result)
          %imwrite(result,filename);
          imwrite(result,filename);
          
          %imwrite(squeeze(closedContour(idx,:,:)),filename);
          count_mask=count_mask+1;
          %cd('C:\Rodrigo\Doutorado\Códigos\codigo_modi')
          %cd('D:\Documentos\Igor Colonna\Teste matlab')
          
          %Lugar aonde fica os codigos do matlab
          cd(PATH)
          %cd('C:\Users\Usuario\Downloads\fiji-win64\Fiji.app\IIWM\matlab')
          %cd('C:\Users\Usuario\Downloads\Programas para imagem_3D-20220215T161323Z-001\Programas para imagem_3D\ImageJ.app\plugins\IIWM\matlab')
          %cd('C:\Users\Usuario\Downloads\Programas para imagem_3D-20220215T161323Z-001\Programas para imagem_3D\ImageJ.app\matlab')
      end
      
   %#################### FIM DA PARTE PARA SALVAR MÁSCARAS
   
    end
    %toc;
    
   
    %% Visualizing final results

    for idx = idxMaskToCompute 

        % Principal variables

        contour = squeeze(closedContour(idx,:,:));
        image = squeeze(images(idx,:,:));
                       
    end
    
%% Computing area
    fprintf('\nComputing volumes:\n')
    
    masksComputed = zeros(size(idxMaskToCompute,2), size(image,1), size(image,2));
    %imshow(masksComputed) %1-03-2021 mostrar as máscaras 

count = 1;
    for idx = idxMaskToCompute
        masksComputed(count,:,:) = closedContour(idx,:,:);
        count = count+ 1;
    end
    
    %sum(sum(closedContour(idx,:,:)))
%     figure(3)
%     imshow(squeeze(closedContour(idx,:,:)))
    
    [volTotalEstimated, arrayVolEstimated] = computeVolumeFromMasks(masksComputed,...
                                                                    distanceBetweenLayer,...
                                                                    ratioPixelMeter);



    fprintf('\t Estimated computed: %.4f mm3 \n', volTotalEstimated*1e9);
     
     %mask_ref_int=masks(NB_MASK-1,:,:);
     %mask_ref=abs(1-squeeze(mask_ref_int)/255);

    %[volMasks, ~] = computeVolumeFromMasks(mask_ref,...
     %                                      distanceBetweenLayer,...
      %                                     ratioPixelMeter);
                                       
      masks1 = masks((1:end-1),:,:)/255;
      size(masks);
      size(masks1);
      [volMasks, ~] = computeVolumeFromMasks(masks1,...
                                           distanceBetweenLayer,...
                                           ratioPixelMeter);



fprintf('\t Vol mask passed to the algorithm computed: %.4f mm3 \n', volMasks*1e9);
   

vol_total=volTotalEstimated+volMasks;

fprintf('\t Vol total: %.4f mm3 \n', vol_total*1e9);

% TESTE FORMA DIFERENTE DE CALCULAR

dados_masksComputed = computeAreaFromMasks(masksComputed, ratioPixelMeter);
dados_masksRef = computeAreaFromMasks(masks, ratioPixelMeter);

n_masksComputed = size(masksComputed);


quantMasks = size(GT_filename);
indexMasks = [];

for count=1:quantMasks(1)
    
    index = str2num( regexprep( GT_filename(count,:), {'\D*([\d\.]+\d)[^\d]*', '[^\d\.]*'}, {'$1 ', ' '} ) )+1;
    indexMasks = [indexMasks, index];
end

n_masksRef = size(indexMasks);

dados_full = zeros(1,indexMasks(end));


for kk=1:n_masksRef(2)
    dados_full(indexMasks(kk)) = dados_masksRef(kk);
end

dados_full(idxMaskToCompute) = dados_masksComputed(1,:);
volumeTotal = NewComputeVolumeFromMasks(dados_full, distanceBetweenLayer);

fprintf('\t Volume total(new method): %.4f mm3 \n', volumeTotal);

%disp(dados_full)
   
    toc;
end