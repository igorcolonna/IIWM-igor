% Copies all the files from one folder to another folder.
clc;    % Clear the command window.
workspace;  % Make sure the workspace panel is showing.
format compact;

% Define input and output folders.
% CHANGE THESE FOLDER NAMES!!!!!!
inputFolder = 'C:\Users\Usuario\Documents\igor_imagens_teste\teste_mts_testes\imagem';
outputFolder = uigetdir(pwd);
if strcmp(outputFolder, inputFolder)
	errorMessage = sprintf('Error: the output folder must be different than the input folder');
	uiwait(warndlg(errorMessage));
	return;
end

% Check to see that both folders exist.
if ~isdir(inputFolder)
	errorMessage = sprintf('Error: The following input folder does not exist:\n%s', inputFolder);
	uiwait(warndlg(errorMessage));
	return;
end
if ~isdir(outputFolder)
	errorMessage = sprintf('Error: The following output folder does not exist:\n%s', outputFolder);
	uiwait(warndlg(errorMessage));
	return;
end

% Get a list of files to copy.
filePattern = fullfile(inputFolder, '*.*'); % All files.
% filePattern = fullfile(inputFolder, '*.m'); % m-files.
fileNamesToTransfer = dir(filePattern);
numFiles = length(fileNamesToTransfer);
% Do the copying.
for k = 1 : numFiles
	% Get the base file name.
	baseFileName = fileNamesToTransfer(k).name;
	% Create the full input and output filenames.
	fullInputFileName = fullfile(inputFolder, baseFileName);
	fullOutputFileName = fullfile(outputFolder, baseFileName);
	fprintf(1, 'Now copying file #%d of %d: %s to %s\n', ...
		k, numFiles, fullInputFileName, fullOutputFileName);
	copyfile(fullInputFileName, fullOutputFileName);
end
uiwait(msgbox('Done copying files!', 'modal'));