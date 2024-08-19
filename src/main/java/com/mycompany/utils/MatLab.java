package com.mycompany.utils;

import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.StringWriter;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

import javax.imageio.ImageIO;

import com.mathworks.engine.MatlabEngine;
import com.mycompany.model.SegmentationUSImageID;

import net.imagej.ImageJ;
import ij.IJ;
import ij.ImagePlus;
import ij.gui.MessageDialog;
import ij3d.Content;
import ij3d.Image3DUniverse;

public class MatLab {

    static String path = new File("").getAbsolutePath();
    static final String MATLAB_PATH = (path + "\\IIWM\\matlab");
    static final String MACRO_PATH = (path + "\\IIWM\\macros");
    
    static StringWriter writer = new StringWriter();
    static StringWriter writer2 = new StringWriter();
    static ImageJ ij;

    // Método principal para chamar o script MATLAB com os parâmetros configurados
    public static void callMatlab(SegmentationUSImageID model, ImageJ ij) {
        try {
            MatlabEngine ml = MatlabEngine.startMatlab();  // Inicia uma sessão MATLAB

            // Define o diretório de trabalho no MATLAB
            ml.eval("cd '" + MATLAB_PATH + "'");
            
            // Variáveis a serem passadas para o MATLAB
            Object[] variables = {
                model.getOcf(),
                model.getRpm(),
                model.getDbl(),
                getFilesInPath(model.getRootImages()),
                (model.getRootImages().toCharArray()),
                getFilesInPath(model.getRootMask()),
                (model.getRootMask().toCharArray()),
                model.getTypeFilter(),
                model.getLevelProcessing(),
                model.getStringTumorLayer(),
                model.isIdxLayer(),
                model.isSave(),
                model.isActiveContour(),
                (model.getRoot().toCharArray())
            };
            
            // Executa a função MATLAB para segmentação de imagens
            ml.feval("segmentationUSImagesIG", writer, writer2, variables);
            
            // Exibe uma caixa de diálogo com o resultado da segmentação
            new MessageDialog(null, "Resultado da Segmentação", writer.toString());
            
            // Limpa o buffer do StringWriter
            writer.getBuffer().setLength(0);
            
            // Gera o arquivo final TIFF e o abre
            makeFinaltiff(model.getRoot());
            openImage(model.getRoot() + "\\final.tif", model.getRpm(), model.getDbl());
            
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

    // Método para somar imagens usando um script MATLAB
    public static void sumImages(char[] filePath, char[][] masknames, char[] maskPath, char[] savePath, double distance) {
        try {
            MatlabEngine ml = MatlabEngine.startMatlab();  // Inicia uma sessão MATLAB

            ml.eval("cd '" + MATLAB_PATH + "'");
            Object[] variables = { filePath, masknames, maskPath, savePath, distance };
            
            // Executa a função MATLAB para somar as imagens
            ml.feval("sumImages", writer, writer2, variables);
            new MessageDialog(null, "Resultado da Soma de Imagens", writer.toString());
            
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

    // Método para abrir uma imagem no ImageJ e configurar a calibração espacial
    private static void openImage(String path, double unitXY, double unitZ) {
        ImagePlus image = IJ.openImage(path);
        unitXY = unitXY * 1000;
        unitZ = unitZ * 1000;

        image.getCalibration().setUnit("mm");
        image.getCalibration().pixelWidth = image.getCalibration().pixelHeight = unitXY;
        image.getCalibration().pixelDepth = unitZ;
        
        // Abre a imagem em uma janela 3D no ImageJ
        Image3DUniverse univ = new Image3DUniverse();
        Content c = univ.addVoltex(image);  // Adiciona a imagem como volume

        univ.getCanvas();
        univ.show();  // Mostra a janela 3D
    }

    // Método para criar o arquivo final TIFF usando um macro do ImageJ
    public static void makeFinaltiff(String path) {
        IJ.runMacroFile(MACRO_PATH + "\\make3Dimage.ijm", path);
    }

    // Método para converter uma imagem BufferedImage em ByteBuffer
    public static ByteBuffer convertImage(BufferedImage image) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ImageIO.write(image, "TIFF", baos);
        return ByteBuffer.wrap(baos.toByteArray());
    }

    // Método para obter os arquivos de um diretório como uma matriz de char
    private static char[][] getFilesInPath(String path) {
        ArrayList<char[]> _files = new ArrayList<>();

        File folder = new File(path);
        File[] files = folder.listFiles();

        if (files != null) {
            for (File file : files) {
                if (file != null) {
                    _files.add((file.getName().toCharArray()));
                }
            }
        }

        return _files.toArray(new char[0][0]);
    }
}
