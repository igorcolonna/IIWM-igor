package com.mycompany.imagej;

// Importações necessárias para o funcionamento do programa
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.AdjustmentEvent;
import java.awt.event.AdjustmentListener;
import java.io.File;
import java.util.ArrayList;

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
public class Process_Pixels implements Command, AdjustmentListener, ActionListener {

    // Componentes de interface e variáveis necessárias
    private JPanel contentPane;
    private ImageIcon s[];
    private JLabel l;
    private JLabel currImg;
    private ArrayList<String> filesList; // Lista de arquivos de imagem
    private ArrayList<Integer> indexes = new ArrayList<Integer>(); // Lista de índices selecionados
    private JScrollPane scrollPane;
    private Integer currentImage = null;
    private final Integer SKIP_IMAGES = 10;
    private SegmentationUSImageID model;
    static ImageJ ij;
    private JDialog check = new JDialog();
    static String path = new File("").getAbsolutePath();
    static final String MACRO_PATH = (path + "\\IIWM\\macros");

    // Método para exibir o diálogo de configuração
    private SegmentationUSImageID showDialog() {
        DialogUtils gd = new DialogUtils("IIWM");

        // Configurações disponíveis para o usuário
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
        return getParams(gd); // Retorna os parâmetros configurados
    }

    // Método para obter os parâmetros inseridos pelo usuário
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

    // Método para selecionar imagens para o processamento
    public void SelecIMG() {
        check.setTitle("Selecione as Imagens");
        check.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
        check.setModal(true);
        Dimension d = new Dimension(600, 500);
        check.setMinimumSize(d);

        int quant = filesList.size();

        contentPane = new JPanel(new BorderLayout());
        contentPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        JPanel boxes = new JPanel(new GridLayout(0, 2, 3, 0)); // Layout para os checkboxes de seleção
        scrollPane = new JScrollPane(boxes);
        scrollPane.setPreferredSize(new Dimension(250, Integer.MIN_VALUE));
        contentPane.add(scrollPane, BorderLayout.WEST);

        JPanel imagens = new JPanel();
        imagens.setLayout(new BoxLayout(imagens, BoxLayout.PAGE_AXIS));

        s = new ImageIcon[quant];
        for (int count = 0; count < quant; count++) {
            s[count] = new ImageIcon(filesList.get(count));
        }

        l = new JLabel("", SwingConstants.CENTER);
        imagens.add(l, BorderLayout.CENTER);

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

        JScrollBar scrollBar = new JScrollBar(JScrollBar.HORIZONTAL);
        scrollBar.setVisibleAmount(1);
        scrollBar.setMaximum(filesList.size());
        scrollBar.setMinimum(0);

        scrollBar.addAdjustmentListener(this);
        imagens.add(scrollBar);

        contentPane.add(imagens);
        check.add(contentPane);
        check.pack();
        l.setIcon(getResizedImageIcon(s[0]));
        check.setLocationRelativeTo(null);

        // Adiciona checkboxes para selecionar as imagens
        for (int i = 0; i < quant; i++) {
            String label = "Imagem " + i;
            JCheckBox checkBox = new JCheckBox(label);
            boxes.add(checkBox);
        }

        check.setVisible(true);
    }

    // Método para redimensionar as imagens exibidas no diálogo
    private ImageIcon getResizedImageIcon(ImageIcon originalIcon) {
        Rectangle r = contentPane.getBounds();
        int width = r.width;
        int height = r.height;
        Image img = originalIcon.getImage();
        Image resizedImg = img.getScaledInstance(width - 250, height - 84, Image.SCALE_SMOOTH);
        return new ImageIcon(resizedImg);
    }

    // Método chamado quando o valor do scrollbar é alterado
    @Override
    public void adjustmentValueChanged(AdjustmentEvent e) {
        l.setIcon(getResizedImageIcon(s[e.getValue()]));
        currImg.setText("Imagem " + String.valueOf(e.getValue()));
    }

    // Método chamado quando o botão "Confirmar" é pressionado
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
                            indexes.add(index); // Adiciona os índices das imagens selecionadas
                        }
                    }
                }
            }
            System.out.println(indexes);
            check.dispose(); // Fecha o diálogo após a confirmação
        }
    }

    // Método para chamar o MatLab com os parâmetros do modelo
    private void callMatlab() {
        try {
            MatLab.callMatlab(model, ij);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Método para abrir a próxima imagem (não está sendo usado no momento)
    public void openNextImage() {
        if (currentImage == null) {
            currentImage = 0;
        }
        if (filesList != null) {
            if (currentImage >= filesList.size()) {
                openImage(filesList.get(filesList.size() - 1));
                callMatlab();
            } else {
                openImage(filesList.get(currentImage));
                currentImage += SKIP_IMAGES;
            }
        }
    }

    // Método para abrir uma imagem no ImageJ
    private void openImage(String path) {
        ImagePlus image = IJ.openImage(path);
        image.show();
    }

    // Método principal que executa as ações com base nas configurações do modelo
    private void execute() {
        if (model.getCropImages()) {
            IJ.runMacroFile(MACRO_PATH + "\\OpenAndCrop.ijm",
                    model.getRootImages());
        }
        if (model.getOpenLiveWire()) {
            filesList = getFilesInPathAsList(model.getRootImages());
            SelecIMG(); // Seleciona as imagens para processamento
            String argument = model.getRootImages() + ";" + model.getRootMask() + ";" + indexes;
            IJ.runMacroFile(MACRO_PATH + "\\MacroCreateMask.ijm",
                    argument);
            callMatlab();
            filesList = getFilesInPathAsList(model.getRootImages());
        } else {
            callMatlab();
        }
    }

    // Método para obter os arquivos de um diretório como uma lista
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

    // Método principal que inicia o plugin no ImageJ
    public static void main(String[] args) throws Exception {
        ij = new ImageJ();
        ij.launch(args);
        ij.command().run(Process_Pixels.class, true);
    }

    // Método que é executado quando o comando é chamado
    @Override
    public void run() {
        model = showDialog();

        if (model != null) {
            execute();
        }
    }
}
