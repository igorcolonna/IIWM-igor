directory = getArgument();
print(directory);
pasta = newArray(3);
pasta = split(directory, ";");
name = "";
Dialog.create("Salvar mascara");
Dialog.addString("Nome do arquivo", name);
indexes = substring(pasta[2], 1, lastIndexOf(pasta[2], "]"));
print(indexes);
indexes = split(indexes, ",");
filelist = getFileList(pasta[0]);
//print(pasta[0]);	
//print(lengthOf(filelist)); 
for (i = 0; i < lengthOf(filelist); i++ ) {
	for(index = 0; index < (indexes.length); index++){
		if(parseInt(indexes[index]) == i){
			//if (endsWith(filelist[i], ".tif")) {
			print("entrou no if de file"); 
        	open(pasta[0] + File.separator + filelist[i]);
        	waitForUser("Use o LiveWire para selecionar a areae clique em OK");
        	run("Create Mask");
        	//Dialog.show()
        	//name = Dialog.getString();
        	if(i < 10){
        		name = "mask00" + i;
        	}else if (i < 100){
        		name = "mask0" + i;
        	}else{
        		name = "mask" + i;
        	}
        	
        	saveAs("Tiff", pasta[1] + File.separator + name);
        	run("Close All");
    
        		//print("testedentro");
			//} 
		//print("testefora");
		}
		
	}
    print("index= " + index);
    print("i= " + i);
}
//if(File.nameWithoutExtension != filelist[lengthOf(filelist)-1]){
//	open(pasta[0] + File.separator + filelist[lengthOf(filelist)-1]);
//	waitForUser("Use o LiveWire para selecionar a areae clique em OK");
//    run("Create Mask");
//    Dialog.show()
//    name = Dialog.getString();
//    saveAs("Tiff", pasta[1] + File.separator + name);
//}
print("terminou");
