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
import ij.process.StackConverter;
import ij3d.Content;
import ij3d.Image3DUniverse;

public class MatLab {
	
	
	static String path = new File("").getAbsolutePath();
	
	//static final String MATLAB_PATH = (path + "\\plugins\\IIWM\\matlab");
	static final String MATLAB_PATH = (path + "\\IIWM\\matlab");
	static final String MACRO_PATH = (path + "\\IIWM\\macros");
	
	static StringWriter writer = new StringWriter();
	static StringWriter writer2 = new StringWriter();
	static ImageJ ij;
	
	public static void callMatlab(SegmentationUSImageID model, ImageJ ij)  {
		
		try {
			MatlabEngine ml = MatlabEngine.startMatlab();
			
			ml.eval("cd '" + MATLAB_PATH + "'");
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
			
			ml.feval("segmentationUSImagesIG", writer, writer2, variables);
			//MessageDialog tela = new MessageDialog(null, "Resultado da Segmentação", writer.toString());
			
			//////////////// IMPRESSAO NA TELA /////////////////////////
			// FileWriter myWriter = new FileWriter("C:\\Users\\Usuario\\Documents\\igor_imagens_teste\\logs\\log.txt");
			// myWriter.write(writer.toString());
			// myWriter.close();
			new MessageDialog(null, "Resultado da Segmentação", writer.toString());
			writer.getBuffer().setLength(0);
			makeFinaltiff(model.getRoot());
			openImage(model.getRoot() + "\\final.tif", model.getRpm(), model.getDbl());
			
		} 
		catch (InterruptedException e) {
			e.printStackTrace();
		} catch (ExecutionException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	public static void sumImages( char[] filePath, char[][] masknames, char[] maskPath, char[] savePath, double distance)  {
		System.out.println(distance);
		try {
			MatlabEngine ml = MatlabEngine.startMatlab();

			ml.eval("cd '" + MATLAB_PATH + "'");
			Object[] variables = { filePath, masknames, maskPath, savePath, distance };
			
			ml.feval("sumImages", writer, writer2, variables);
			new MessageDialog(null, "Resultado da Soma de Imagens", writer.toString());
			
		} catch (InterruptedException e) {
			e.printStackTrace();
		} catch (ExecutionException e) {
			e.printStackTrace();
		}
	}
	
	
	private static void openImage(String path, double unitXY, double unitZ) {
		ImagePlus image = IJ.openImage(path);
		unitXY = unitXY * 1000;
		unitZ = unitZ * 1000;
		System.out.println(path);
		System.out.println(unitXY);
		System.out.println(unitZ);
		
		image.getCalibration().setUnit("mm");
		image.getCalibration().pixelWidth = image.getCalibration().pixelHeight = unitXY;
		image.getCalibration().pixelDepth = unitZ;
		
		Image3DUniverse univ = new Image3DUniverse();
		
		
		//Content c = univ.addMesh(image);
		Content c = univ.addVoltex(image);
			
		//sleep(5);
		univ.getCanvas();
	    
		//c.setTransparency((float) 0.4);
		univ.show();
	}
    
//	private static void sleep(int sec) {
//	    try {
//			Thread.sleep(sec * 1000);
//	    } catch(InterruptedException e) {
//			System.out.println(e.getMessage());
//	    }
//  }
	
	public static void makeFinaltiff(String path) {
		System.out.println(MACRO_PATH + "\\make3Dimage.ijm");
		IJ.runMacroFile(MACRO_PATH + "\\make3Dimage.ijm", path);
	}
	
	public static ByteBuffer convertImage(BufferedImage image) throws IOException
	{     
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		ImageIO.write( image, "TIFF", baos );
		
		return ByteBuffer.wrap(baos.toByteArray());
		
	}

	
	private static char[][] getFilesInPath(String path) {
		ArrayList<char[]> _files = new ArrayList<char[]>();
	
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
