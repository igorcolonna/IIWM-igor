import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.util.ArrayList;

public class TesteDialog extends JDialog implements AdjustmentListener, ActionListener {

    private JPanel contentPane;
    private ArrayList<String> filesList;
    private ImageIcon s[];
    private JLabel l;
    private JScrollPane scrollPane;
    private int quantidade;
    private JLabel currImg;
    private ArrayList<Integer> indexes = new ArrayList<>();
    private JButton continuarButton;

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    TesteDialog dialog = new TesteDialog();
                    dialog.setVisible(true);
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
                    _files.add(path + File.separator + file.getName());
                }
            }
        }

        return _files;
    }

    public TesteDialog() {
        setTitle("Teste Dialog");
        setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
        setModal(true);

        filesList = getFilesInPathAsList("C:\\Users\\igor_\\Downloads\\Teste_IIWM\\imagem");
        int quant = filesList.size();
        quantidade = quant;

        contentPane = new JPanel(new BorderLayout());
        contentPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        JPanel boxes = new JPanel(new GridLayout(0, 2, 3, 0));
        //JScrollPane scrollPane = new JScrollPane(boxes);
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
        //contentPane.add(l, BorderLayout.CENTER);
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
        add(contentPane);
        pack();
        setLocationRelativeTo(null);
        
        for (int i = 0; i < quant; i++) {
            String label = "Imagem " + i;
            JCheckBox checkBox = new JCheckBox(label);
            boxes.add(checkBox);
        }
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
            dispose();
        }
    }

}

