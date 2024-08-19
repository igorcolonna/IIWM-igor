% Projeto final -  Segmenta��o de colon de camundongos
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
            
            maskTemp = squeeze(masks(iMask,:,:));
            maskTemp = uint8(maskTemp);              
            
            bw = bwperim(maskTemp,8);
            
            se = strel('line',10,0);
            bw = imdilate(bw,se);
        
            filtro = imgTemp.*(maskTemp/255);
            imgTemp = imgTemp - filtro;
            
            zeropict = zeros(size(filtro),class(filtro));
            redpict = cat(3,filtro,zeropict, zeropict);
            redpict2 = cat(3,maskTemp.*255,zeropict,zeropict).* 0.3;
            boundpict = cat(3,bw.*255,zeropict,zeropict);
            
            %result = imgTemp+redpict+redpict2+boundpict;                   %Salvar com uma borda maior (melhor vizualiza��o no 3D)
            result = imgTemp+redpict+redpict2;                              %Salvar sem uma borda maior (melhor fidelidade da geometria)
            imwrite(result,filename);      
          
            %Lugar aonde fica os codigos do matlab
            cd(PATH)
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

        maskTemp = squeeze(masks(iMask+1,:,:));
        maskTemp = uint8(maskTemp);
        
        bw = bwperim(maskTemp,8);
        se = strel('line',10,0);
        bw = imdilate(bw,se);

        filtro = imgTemp.*(maskTemp/255);

        imgTemp = imgTemp - filtro;
            
        zeropict = zeros(size(filtro),class(filtro));
        redpict = cat(3,filtro,zeropict, zeropict);
        redpict2 = cat(3,maskTemp.*255,zeropict,zeropict).* 0.3;
        boundpict = cat(3,bw.*255,zeropict,zeropict);
        
        %result = imgTemp+redpict+redpict2+boundpict;                       %Salvar com uma borda maior (melhor vizualiza��o no 3D)
        result = imgTemp+redpict+redpict2;                                  %Salvar sem uma borda maior (melhor fidelidade da geometria)

        imwrite(result,filename);
          
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
        
        % DEBUG - para vizualizar como esta o contorno pr� contorno ativo, use a linha abaixo:
        % imshow(squeeze(closedContour(idx,:,:)),[])
        
        if activeContour == true
            closedContour(idx,:,:) = activecontour(imagesNoTreatment{idxMaskToCompute(count_mask)}, squeeze(closedContour(idx,:,:)), n_iterations,'edge','ContractionBias',0);
            
        % DEBUG - para vizualizar como esta o contorno p�s contorno ativo, use a linha abaixo:
        % imshow(squeeze(closedContour(idx,:,:)),[])
            
        end
        
      if save_option == true
          cd (root)
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
          
          maskTemp = uint8(maskTemp);
          
          filtro = imgTemp.*(maskTemp);
          
          imgTemp = imgTemp - filtro;
            
          zeropict = zeros(size(filtro),class(filtro));
          
          redpict = cat(3,filtro,zeropict, zeropict);
          redpict2 = cat(3,maskTemp.*255,zeropict,zeropict).* 0.3;
          boundpict = cat(3,bw.*255,zeropict,zeropict);
          
          %result = imgTemp+redpict+redpict2+boundpict;                     %Salvar com uma borda maior (melhor vizualiza��o no 3D)
          result = imgTemp+redpict+redpict2;                                %Salvar sem uma borda maior (melhor fidelidade da geometria)
          imwrite(result,filename);
          
          count_mask=count_mask+1;
          
          %Lugar aonde fica os codigos do matlab
          cd(PATH)
      end
      
   %#################### FIM DA PARTE PARA SALVAR M�SCARAS
   
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
    %imshow(masksComputed) %1-03-2021 mostrar as m�scaras 

count = 1;
    for idx = idxMaskToCompute
        masksComputed(count,:,:) = closedContour(idx,:,:);
        count = count+ 1;
    end

    
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

   
    toc;
end