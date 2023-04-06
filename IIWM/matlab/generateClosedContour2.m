function [closedImg] = generateClosedContour2(img, method)
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

Xcnt=[];
Ycnt=[];

for nn=1:1:size_init
    
    Xcnt=[Xcnt Xcnt_int(nn)];
    Ycnt=[Ycnt Ycnt_int(nn)];
    
end


r = round(mean(Xcnt));
c = round(mean(Ycnt));


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
 
 [size_Xcnt,~]=size(Xcnt_int);
 
 closedImg(Xcnt(1:size_Xcnt),Ycnt(1:size_Xcnt))=masks_full(Xcnt(1:size_Xcnt)-oX,Ycnt(1:size_Xcnt)-oY);
 
     
    figure(4)
    imshow([masks_contour masks_full])
    
  %  figure(5)
  %  imshow(closedImg)
    
    
 else 
     msg = 'This method is not implemented yet, try the following: hull';
     disp(msg);
     
  end

end

