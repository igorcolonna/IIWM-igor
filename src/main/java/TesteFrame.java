import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.AdjustmentEvent;
import java.awt.event.AdjustmentListener;
import java.awt.event.ComponentEvent;
import java.awt.event.ComponentListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

import javax.swing.ImageIcon;
import javax.swing.JCheckBox;

import java.awt.BorderLayout;
import java.awt.Checkbox;
import java.awt.CheckboxGroup;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Panel;

import javax.swing.JScrollBar;
import javax.swing.border.LineBorder;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import ij.gui.GenericDialog;

import java.awt.Color;
import java.awt.Dialog;
import java.awt.Dimension;
import javax.swing.SwingConstants;
import javax.swing.border.CompoundBorder;
import javax.swing.border.BevelBorder;
import java.awt.Font;
import java.awt.Dialog.ModalExclusionType;
import javax.swing.JButton;
import javax.swing.JScrollPane;

public class TesteFrame extends JFrame implements AdjustmentListener, ActionListener, ItemListener{

	private GenericDialog check = new GenericDialog("CheckBox");
	private JPanel contentPane;
	private ArrayList<String> filesList;
	private ImageIcon s[];
	private JLabel l;
	private ArrayList<Integer> indexes = new ArrayList<Integer>(); 
	private int quantidade;
	JLabel currImg;
	JOptionPane OK;
	
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TesteFrame frame = new TesteFrame();
					//frame.setVisible(true);
					frame.pack();
					System.out.println(System.getProperty("user.dir"));
					
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
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
	

	/**
	 * Create the frame.
	 */
	public TesteFrame() {
		
		setModalExclusionType(ModalExclusionType.NO_EXCLUDE);
		check.setBackground(new Color(255, 255, 0));

		check.setModalityType(Dialog.DEFAULT_MODALITY_TYPE);
		
		filesList = getFilesInPathAsList("C:\\Users\\igor_\\Downloads\\Teste_IIWM\\imagem");
		
		int quant = filesList.size();
		quantidade = quant;
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		contentPane = new JPanel();
		contentPane.setBackground(new Color(0, 255, 0));
		
		//contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		//setContentPane(contentPane);
		//contentPane.setLayout(new BorderLayout(5, 0));

		JScrollPane scrollPane = new JScrollPane();
		//scrollPane.setMaximumSize(new Dimension(500,500));
		//contentPane.add(scrollPane, BorderLayout.WEST);
		
		JPanel boxes = new JPanel();
		boxes.setBorder(new CompoundBorder(new LineBorder(new Color(0, 0, 0)), new BevelBorder(BevelBorder.RAISED, null, null, null, null)));
		
		boxes.setLayout(new GridLayout(0, 2, 3, 0));
		
		JPanel imagens = new JPanel();
		imagens.setBorder(new CompoundBorder(new LineBorder(new Color(0, 0, 0)), new BevelBorder(BevelBorder.RAISED, null, null, null, null)));
		contentPane.add(imagens, BorderLayout.CENTER);
		imagens.setLayout(new BorderLayout(5, 5));
		
		JScrollBar scrollBar = new JScrollBar();
		scrollBar.setVisibleAmount(1);
		scrollBar.setMaximum(filesList.size());
		scrollBar.setMinimum(0);
		scrollBar.setOrientation(JScrollBar.HORIZONTAL);
		scrollBar.addAdjustmentListener(this);
		imagens.add(scrollBar, BorderLayout.SOUTH);
		
		s = new ImageIcon[quant];
		
		for(int count = 0; count < quant; count++) {
			
			s[count] = new ImageIcon(filesList.get(count));
			
			
		}
		System.out.println(filesList);
		System.out.println(scrollBar.getMaximum());
		System.out.println(scrollBar.getUnitIncrement());

		l = new JLabel("");
		imagens.add(l, BorderLayout.CENTER);
		l.setIcon(s[0]);
		
		currImg = new JLabel("Imagem 0");
		currImg.setMinimumSize(new Dimension(30, 5));
		currImg.setMaximumSize(new Dimension(40, 10));
		currImg.setFont(new Font("Verdana", Font.BOLD, 15));
		currImg.setHorizontalAlignment(SwingConstants.CENTER);
		imagens.add(currImg, BorderLayout.NORTH);
		
		JPanel buttons = new JPanel();
		contentPane.add(buttons, BorderLayout.SOUTH);
		buttons.setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));
		
		JButton OkButton = new JButton("Confirmar");
		buttons.add(OkButton);
		
		OkButton.addActionListener(this);
		
		//////////////////////////////////////////////
		
		
		
		String[] labels = new String[quant];
		boolean defaultValues[] = new boolean[quant];
		Arrays.fill(defaultValues, false);
		for(int i = 0; i < quant; i++) {
			labels[i] = "Imagem " + String.valueOf(i);
			Checkbox checkbox = new Checkbox(labels[i]);
			boxes.add(checkbox);
		}
		
		scrollPane.setViewportView(boxes);
		contentPane.add(scrollPane, BorderLayout.WEST);
		
		check.add(contentPane);
		
		check.setSize(contentPane.getPreferredSize().width, contentPane.getPreferredSize().height);
		check.showDialog();

		
		/////////////////////////////////////////////
	
	}

	@Override
	public void adjustmentValueChanged(AdjustmentEvent e) {
		// TODO Auto-generated method stub
		l.setIcon(s[e.getValue()]);
		currImg.setText("Imagem " + String.valueOf(e.getValue()));
		System.out.println(e.getValue());
		
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getActionCommand() == "Confirmar") {
			for (Integer i = 0; i < quantidade; i++) {
				if(check.getNextBoolean() == true) {
					indexes.add(i);
				}
	        }
			
			//check.dispose();
		}
	}

	@Override
	public void itemStateChanged(ItemEvent e) {
		// TODO Auto-generated method stub
	}

}
