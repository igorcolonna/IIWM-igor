import java.awt.EventQueue;

import javax.swing.JFrame;

import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import java.io.File;
import java.util.ArrayList;


import java.awt.BorderLayout;


import ij.gui.GenericDialog;
import ij.gui.MessageDialog;


import java.awt.Dialog;
import java.awt.Dialog.ModalExclusionType;

public class TesteFrame2 extends JFrame{

	private GenericDialog result = new GenericDialog("Resultado da Segmentação");
	private JPanel contentPane;
	
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TesteFrame2 frame = new TesteFrame2();
					//frame.setVisible(true);
					frame.pack();
					
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
	public TesteFrame2() {


		contentPane = new JPanel();

		contentPane.setLayout(new BorderLayout(5, 0));
		
		JTextArea textArea = new JTextArea("Test");
        textArea.setSize(800, 800);
        
		//MessageDialog message = new MessageDialog(null, "Resultado da Segmentação", "blablabla");
		
		JScrollPane scroll = new JScrollPane(textArea, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
		
		contentPane.add(scroll);
		
		result.add(contentPane);
		result.showDialog();

		
		/////////////////////////////////////////////
	
	}
}
