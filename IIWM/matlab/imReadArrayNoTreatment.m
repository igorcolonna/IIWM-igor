function [array_output] = imReadArrayNoTreatment(root_path)
    myFolder = root_path;
    if ~isfolder(myFolder)
      errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);
      uiwait(warndlg(errorMessage));
      return;
    end
    filePattern = fullfile(myFolder, '*.jpg');
    jpegFiles = dir(filePattern);
    for k = 1:length(jpegFiles)
      baseFileName = jpegFiles(k).name;
      fullFileName = fullfile(myFolder, baseFileName);
      %fprintf(1, 'Now reading %s\n', fullFileName);
      imageArray = imread(fullFileName);
      imageArray = squeeze(imageArray(:,:,1));
      array_output{k} = imageArray;
      %imshow(imageArray);  % Display image.
      %drawnow; % Force display to update immediately.
    end
end