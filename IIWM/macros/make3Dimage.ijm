file = getArgument();
args = "open=" + file + " file=Mask sort";
print(args);
argsSave = file + File.separator + "final"
run("Image Sequence...",args);
saveAs("Tiff", argsSave);
close();