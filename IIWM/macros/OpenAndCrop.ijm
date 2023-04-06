file = getArgument();
//file = "C:\\Users\\Usuario\\Documents\\igor_imagens_teste\\teste_mts_testes\\imagem";
args = "open=" + file;
print(args);
print(File.nameWithoutExtension());
print(file);
run("Image Sequence...",args);
waitForUser("Recorte a parte desejada e clique em OK");
run("Crop");

filelist = getFileList(file);

argsSave = "select=" + file;
argsSave += " dir=" + file;
argsSave += " format=TIFF";
//argsSave += " name=" + File.getNameWithoutExtension(file);

argsSave += " digits=3";
print(argsSave);
run("Image Sequence... ");

for (i = 0; i < lengthOf(filelist); i++) {
	if(endsWith(filelist[i], ".jpeg")){
		File.delete(file + File.separator() + filelist[i]);
	}
}

wait(2000);
print("acabou");
close();