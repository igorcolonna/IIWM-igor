package com.mycompany.imagej;


import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.AdjustmentEvent;
import java.awt.event.AdjustmentListener;
import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.SwingConstants;
import javax.swing.border.BevelBorder;
import javax.swing.border.CompoundBorder;
import javax.swing.border.LineBorder;

import com.mycompany.listener.ImageListener;
import com.mycompany.model.SegmentationUSImageID;
import com.mycompany.utils.DialogUtils;
import com.mycompany.utils.MatLab;


import ij.IJ;
import net.imagej.ImageJ;

import ij.ImagePlus;
import ij.gui.GenericDialog;
import ij.gui.ImageCanvas;
import javassist.compiler.ast.NewExpr;

import org.forester.development.neTest;
import org.ojalgo.access.Access1D.IndexOf;
import org.scijava.command.Command;
import org.scijava.plugin.Plugin;
import ij.gui.ImagePanel;


@Plugin(type = Command.class, headless = true, menuPath = "Plugins>IIWM")
public class Process_Pixels implements Command,AdjustmentListener,ActionListener {

	private JPanel contentPane;
	private ImageIcon s[];
	private JLabel l;
	private JLabel currImg;
	private int quantidade;
	private ArrayList<String> filesList;
	private ArrayList<Integer> indexes = new ArrayList<Integer>(); 
	private JScrollPane scrollPane;
	private Integer currentImage = null;
	private final Integer SKIP_IMAGES = 10;
	private SegmentationUSImageID model;
	static ImageJ ij;
	private JDialog check = new JDialog();
	static String path = new File("").getAbsolutePath();
	static final String MACRO_PATH = (path + "\\IIWM\\macros");
	
	

	private SegmentationUSImageID showDialog() {
		DialogUtils gd = new DialogUtils("IIWM");

		gd.addChoice("Opção de Função de Fechamento - teste", new String[] { "hull", "linear" }, "hull");
		gd.addNumericField("Tamanho do pixel [m]", 6E-6, 0);
		gd.addNumericField("Comprimento do Voxel [m]", 25E-6, 0);
		gd.addDirectoryField("Imagens", "");
		gd.addDirectoryField("Imagens com Máscara", "");
		gd.addChoice("Tipo do Filtro", new String[] { "None", "Median", "Wavelet" }, "None");
		gd.addStringField("Nível de Processamento", "2");
		gd.addStringField("Camada do Tumor", "Tumor");
		gd.addCheckbox("Index da Camada", true);
		gd.addCheckbox("Salvar Conteúdo", true);
		gd.addCheckbox("Editar máscaras com LiveWire", true);
		gd.addCheckbox("Cortar imagens", true);
		gd.addCheckbox("Contorno Ativo", false);
		gd.addDirectoryField("Pasta para Salvar", "");

		gd.showDialog();
		if (gd.wasCanceled()) {
			return null;
		}
		return getParams(gd);
	}

	private SegmentationUSImageID getParams(DialogUtils gd) {
		SegmentationUSImageID model = new SegmentationUSImageID();

		model.setOcf(gd.getNextChoice());
		model.setRpm(gd.getNextNumber());
		model.setDbl(gd.getNextNumber());
		model.setRootImages(gd.getNextString());
		model.setRootMask(gd.getNextString());
		model.setTypeFilter(gd.getNextChoice());
		model.setLevelProcessing(gd.getNextString());
		model.setStringTumorLayer(gd.getNextString());
		model.setIdxLayer(gd.getNextBoolean());
		model.setSave(gd.getNextBoolean());
		model.setOpenLiveWire(gd.getNextBoolean());
		model.setCropImages(gd.getNextBoolean());
		model.setActiveContour(gd.getNextBoolean());
		model.setRoot(gd.getNextString());

		return model;
	}

	//##############################################
	
	
//	private void SelecIMG() {
//	
//		//////////////// Painel Principal //////////
//		check.setLayout(new FlowLayout());
//		contentPane = new JPanel();
//		////////////////////////////////////////////
//		
//		/////////////// Checkboxes /////////////////
//		
//		Integer quant = filesList.size();
//		String[] labels = new String[quant];
//		boolean defaultValues[] = new boolean[quant];
//		Arrays.fill(defaultValues, false);
//		for(int i = 0; i < quant; i++) {
//			labels[i] = "Imagem " + String.valueOf(i);
//		}
//		//int rows = quant/2;
//		int rows = 10;
//		//int cols = quant/2;
//		int cols = (int) Math.ceil((double) quant/rows);
//		System.out.println(cols);
////		if ((quant % 2) != 0) {
////			rows++;
////		}
//		check.addCheckboxGroup(rows, cols, labels, defaultValues);
//		
//		////////////////////////////////////////////
//		
//		check.add(contentPane);
//		contentPane.setLayout(new BorderLayout(0, 0));
//		
//		//////////////////////////////////////////
//		
//		//////////////////Painel das Imagens \\\\\\\\\\\\\\\\\\\\
//				
//		JPanel imagens = new JPanel();
//		imagens.setBorder(new CompoundBorder(new LineBorder(new Color(0, 0, 0)), new BevelBorder(BevelBorder.RAISED, null, null, null, null)));
//		contentPane.add(imagens, BorderLayout.CENTER);
//		imagens.setLayout(new BorderLayout(5, 5));
//		
//		currImg = new JLabel("Imagem 0");
//		currImg.setMinimumSize(new Dimension(30, 5));
//		currImg.setMaximumSize(new Dimension(40, 10));
//		currImg.setFont(new Font("Verdana", Font.BOLD, 15));
//		currImg.setHorizontalAlignment(SwingConstants.CENTER);
//		imagens.add(currImg, BorderLayout.NORTH);
//		
//		JScrollBar scrollBar = new JScrollBar();
//		scrollBar.setVisibleAmount(1);
//		scrollBar.setMaximum(filesList.size());
//		scrollBar.setMinimum(0);
//		scrollBar.setOrientation(JScrollBar.HORIZONTAL);
//		scrollBar.addAdjustmentListener(this);
//		imagens.add(scrollBar, BorderLayout.SOUTH);
//		
//		s = new ImageIcon[quant];
//		
//		for(int count = 0; count < quant; count++) {
//			s[count] = new ImageIcon(filesList.get(count));
//		}
//		
//		l = new JLabel("");
//		imagens.add(l, BorderLayout.CENTER);
//		l.setIcon(s[0]);
//		
//		////////////////////////////////////////////////////////
//		
//		check.hideCancelButton();
//		check.showDialog();
//
//		for (Integer i = 0; i < quant; i++) {
//			if(check.getNextBoolean() == true) {
//				indexes.add(i);
//			}
//        }
//		
//	}
//		
//
//	@Override
//	public void adjustmentValueChanged(AdjustmentEvent e) {
//		// TODO Auto-generated method stub
//		l.setIcon(s[e.getValue()]);
//		currImg.setText("Imagem " + String.valueOf(e.getValue()));
//		
//		System.out.println(e.getValue());
//		
//		
//	}
//
//	@Override
//	public void actionPerformed(ActionEvent e) {
//		// TODO Auto-generated method stub
//		
//	}
		
	//##################################################
	
	
	public void SelecIMG() {
        check.setTitle("Selecione as Imagens");
        check.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
        check.setModal(true);

        //filesList = getFilesInPathAsList("C:\\Users\\igor_\\Downloads\\Teste_IIWM\\imagem");
        int quant = filesList.size();
        quantidade = quant;

        contentPane = new JPanel(new BorderLayout());
        contentPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        JPanel boxes = new JPanel(new GridLayout(0, 2, 3, 0));
        scrollPane = new JScrollPane(boxes);
        scrollPane.setPreferredSize(new Dimension(250, Integer.MIN_VALUE));
        contentPane.add(scrollPane, BorderLayout.WEST);
        
        JPanel imagens = new JPanel();
        imagens.setLayout(new BoxLayout(imagens, BoxLayout.PAGE_AXIS));

        s = new ImageIcon[quant];
        for (int count = 0; count < quant; count++) {
            s[count] = new ImageIcon(filesList.get(count));
        }

        l = new JLabel("");
        imagens.add(l);
        l.setIcon(s[0]);

        currImg = new JLabel("Imagem 0");
        currImg.setMinimumSize(new Dimension(30, 5));
        currImg.setMaximumSize(new Dimension(40, 10));
        currImg.setFont(new Font("Verdana", Font.BOLD, 15));
        currImg.setHorizontalAlignment(SwingConstants.CENTER);
        contentPane.add(currImg, BorderLayout.NORTH);

        JPanel buttons = new JPanel();
        contentPane.add(buttons, BorderLayout.SOUTH);
        buttons.setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));

        JButton okButton = new JButton("Confirmar");
        buttons.add(okButton);
        okButton.addActionListener(this);

//        continuarButton = new JButton("Continuar");
//        buttons.add(continuarButton);
//        continuarButton.addActionListener(this);

        JScrollBar scrollBar = new JScrollBar(JScrollBar.HORIZONTAL);
        scrollBar.setVisibleAmount(1);
        scrollBar.setMaximum(filesList.size());
        scrollBar.setMinimum(0);
        //scrollBar.setOrientation(JScrollBar.HORIZONTAL);
        scrollBar.addAdjustmentListener(this);
        //scrollPane.setHorizontalScrollBar(scrollBar);
        imagens.add(scrollBar);

        contentPane.add(imagens);
        check.add(contentPane);
        check.pack();
        check.setLocationRelativeTo(null);
        
        for (int i = 0; i < quant; i++) {
            String label = "Imagem " + i;
            JCheckBox checkBox = new JCheckBox(label);
            boxes.add(checkBox);
        }
        
        check.setVisible(true);
    }

    @Override
    public void adjustmentValueChanged(AdjustmentEvent e) {
        l.setIcon(s[e.getValue()]);
        currImg.setText("Imagem " + String.valueOf(e.getValue()));
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("Confirmar")) {
            indexes.clear();
            Component viewport = scrollPane.getViewport().getView();
            if (viewport instanceof JPanel) {
                JPanel boxes = (JPanel) viewport;
                for (Component component : boxes.getComponents()) {
                    if (component instanceof JCheckBox) {
                        JCheckBox checkBox = (JCheckBox) component;
                        if (checkBox.isSelected()) {
                            int index = boxes.getComponentZOrder(checkBox);
                            indexes.add(index);
                        }
                    }
                }
            }
            System.out.println(indexes);
            check.dispose();
        }
    }
	
	private void callMatlab()  {

		try {
			MatLab.callMatlab(model, ij);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void openNextImage() {                   // nao esta sendo usado
		if(currentImage == null) {
			currentImage = 0;
		}
		if(filesList != null) {
			if (currentImage >= filesList.size()) {
				openImage(filesList.get(filesList.size() - 1));
				callMatlab();
			} else {
				openImage(filesList.get(currentImage));
				currentImage+= SKIP_IMAGES;
			}
		}
	}

	private void openImage(String path) {
		ImagePlus image = IJ.openImage(path);
		image.show();
	}
		

	private void execute() {
			
//			System.out.println(new File("").getAbsolutePath());
		
			if(model.getCropImages()) {
				IJ.runMacroFile(MACRO_PATH + "\\OpenAndCrop.ijm", 
						model.getRootImages());
			}
			if (model.getOpenLiveWire()) {
				//IJ.runMacroFile("D:\\Documentos\\Igor_Colonna\\ProjetoImagem3d\\Programas_para_imagem_3D\\ImageJ.app\\macros\\ViewImages.ijm", model.getRootImages());
				filesList = getFilesInPathAsList(model.getRootImages());
				SelecIMG();
				String argument = model.getRootImages() + ";" + model.getRootMask() + ";" + indexes;
				IJ.runMacroFile(MACRO_PATH +"\\MacroCreateMask.ijm",
								 argument);
				callMatlab();
				filesList = getFilesInPathAsList(model.getRootImages());
				//openNextImage();
			} else {
				callMatlab();
			}
	}
	
	private ArrayList<String> getFilesInPathAsList(String path) {
		ArrayList<String> _files = new ArrayList<String>();
	
		File folder = new File(path);
		File[] files = folder.listFiles();

		if (files != null) {
			for (File file : files) {
				 if (file != null) {
					 _files.add(path + "\\" + (file.getName()));
				}
			}
		}

		return _files;
	}
	
	public static void main(String[] args) throws Exception {
		ij = new ImageJ();
		ij.launch(args);
		ij.command().run(Process_Pixels.class, true);
	}

	@Override
	public void run() {
		model = showDialog();

//		ImageListener listener = new ImageListener(this, model);
//		ImagePlus.addImageListener(listener);

		 if (model != null) {
			execute();
		}
		
	}

}
