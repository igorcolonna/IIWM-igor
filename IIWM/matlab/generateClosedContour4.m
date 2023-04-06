function [closedImg] = generateClosedContour4(img, method)
%Generate Closed contour 
% Method: convex hull

  % Initialize output
  closedImg = zeros(size(img));
  
  if strcmp(method,'hull')
      
   [Xcnt_int, Ycnt_int] = ind2sub(size(img), find(img));%coordenadas XY da máscara 1
   

XY=[Xcnt_int Ycnt_int];

imag=zeros(1000,1000);

ind=sub2ind(size(imag),XY(:,1),XY(:,2));
imag(ind)=1;


[size_init,~]=size(Xcnt_int);



r = round(mean(Xcnt_int));
c = round(mean(Ycnt_int));

%Aqui, determinar coordenadas polares, ordenar pelo angulo e depois achar
%as coordenadas retangulares.

 [theta, rho] = cart2pol(Xcnt_int-r, Ycnt_int-c);
 
  % Ording by theta
     % sort A in descending order (decreasing A values) 
     % and keep the sort index in "sortIdx"
     [theta, sortIdx] = sort(theta, 'descend');
 
   % sort B using the sorting index
    rho = rho(sortIdx);
            
 % Come back to cartesian instruction
     %[Xorder, Yorder] = pol2cart(theta, rho);
     %ALTERADO EM 18/06/2020 PARA GERAR MÁSCARA TOTALMENTE COMPACTA
     %###################
     [Xorder_int1, Yorder_int1] = pol2cart(theta, rho);
     Xorder_int2=[Xorder_int1' Xorder_int1(1) Xorder_int1(2) Xorder_int1(3) Xorder_int1(4) Xorder_int1(5)];
     Yorder_int2=[Yorder_int1' Yorder_int1(1) Yorder_int1(2) Yorder_int1(3) Yorder_int1(4) Yorder_int1(5)];
      
     Xorder=Xorder_int2';
     Yorder=Yorder_int2';
     %ATÉ AQUI FOI A ALTERAÇÃO FEITA EM 18/06/2020
     %#################
     Xcnt = (round(Xorder + r))';
     Ycnt = (round(Yorder + c))';


 dX=max(Xcnt)-min(Xcnt);
 dY=max(Ycnt)-min(Ycnt);
 
 extp=10;
 
  oX=min(Xcnt)-extp/2;
  oY=min(Ycnt)-extp/2;
    
    
    
    if dX>=dY
        size_n=dX+extp;
    else size_n=dY+extp;
    end


masks_contour = zeros(size_n,size_n);


XYZ=[(Xcnt-oX)' (Ycnt-oY)'];

ind_1 = sub2ind(size(masks_contour),XYZ(:,1),XYZ(:,2));  

masks_contour(ind_1) = 1;

    
    masks_full = zeros(size_n,size_n);
   
   [~,n_dados]=size(Xcnt);
  
   
for kk=1:1:n_dados-1
     masks_full_int = zeros(size_n,size_n);
     XXX_1=[r-oX Xcnt(kk)-oX Xcnt(kk+1)-oX];
     YYY_1=[c-oY Ycnt(kk)-oY Ycnt(kk+1)-oY];%AQUI ESTÁ A MODIFICAÇÃO em Ycnt(kk+1)
           
     XYZ_1=[XXX_1' YYY_1'];
    ind_2 = sub2ind(size(masks_full_int),XYZ_1(1:3,1),XYZ_1(1:3,2));
    masks_full_int(ind_2) = 1;
     masks_full=masks_full+bwconvhull(masks_full_int);
end

     masks_full(masks_full>0) = 1;
     
     
         
 %Gerar a imagem com o tamanho inicial
 
 [size_mask,~]=size(masks_full);
  
 for countX=oX:oX+size_mask-1
     
     for countY=oY:oY+size_mask-1
         ind3=sub2ind(size(masks_full),countX-oX+1,countY-oY+1);
         ind4=sub2ind(size(closedImg),countX,countY);
         closedImg(ind4)=masks_full(ind3);
     end
 end
 
     
    %figure(4)
    %imshow([masks_contour masks_full])
    
    %figure(5)
    %imshow(closedImg)
    
    
 else 
     msg = 'This method is not implemented yet, try the following: hull';
     disp(msg);
     
  end

end

