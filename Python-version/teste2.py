from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QCheckBox
from PyQt5.QtWidgets import QPushButton, QStyleFactory



class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        QApplication.setStyle("Fusion")
        #self.setWindowFlags(Qt.FramelessWindowHint)
        font_id = QFontDatabase.addApplicationFont('C:/Users/igor_/OneDrive/Documents/GitHub/IIWM-igor/Python-version/fontes/Poppins-SemiBold.ttf')
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.setMaximumWidth(600)

        # Adiciona um layout vertical
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        # Cria os componentes
        lbl_opcao_funcao_fechamento = QLabel("Opção de Função de fechamento:",self)
        self.cmb_opcao_funcao_fechamento = QComboBox(self)
        self.cmb_opcao_funcao_fechamento.addItems(["hull", "linear"])
        lbl_tamanho_pixel = QLabel("Tamanho do Pixel [m]:",self)
        self.txt_tamanho_pixel = QLineEdit("0",self)
        lbl_comprimento_voxel = QLabel("Comprimento do Voxel [m]:",self)
        self.txt_comprimento_voxel = QLineEdit("0",self)
        lbl_imagens = QLabel("Imagens:",self)
        btn_imagens = QPushButton("Selecione um arquivo",self)
        btn_imagens.setObjectName("SelecIMG")
        btn_imagens.clicked.connect(self.btn_clicked)
        lbl_mascaras = QLabel("Máscaras:",self)
        btn_mascaras = QPushButton("Selecione um arquivo",self)
        btn_mascaras.setObjectName("SelecMASK")
        btn_mascaras.clicked.connect(self.btn_clicked)
        lbl_tipo_filtro = QLabel("Tipo do Filtro:",self)
        self.cmb_tipo_filtro = QComboBox(self)
        self.cmb_tipo_filtro.addItems(["None", "Median", "Wavelet"])
        lbl_nivel_processamento = QLabel("Nível de Processamento:",self)
        self.txt_nivel_processamento = QLineEdit("2",self)
        lbl_camada_tumor = QLabel("Camada do Tumor:",self)
        self.txt_camada_tumor = QLineEdit("Tumor",self)
        self.chk_index_camada = QCheckBox("Index da Camada",self)
        self.chk_salvar_conteudo = QCheckBox("Salvar Conteúdo",self)
        self.chk_editar_mascaras_livewire = QCheckBox("Editar máscaras com LiveWire",self)
        self.chk_cortar_imagens = QCheckBox("Cortar Imagens",self)
        self.chk_contorno_ativo = QCheckBox("Contorno Ativo",self)
        lbl_pasta_salvar = QLabel("Pasta para Salvar:",self)
        btn_pasta_salvar = QPushButton("Selecione uma pasta",self)
        btn_pasta_salvar.setObjectName("SelecSAVE")
        btn_pasta_salvar.clicked.connect(self.btn_clicked)
        btn_continuar = QPushButton("Continuar",self)
        btn_continuar.setObjectName("Continuar")
        btn_continuar.clicked.connect(self.btn_clicked)
        font = QFont(self.font_family)
        font.setPointSize(8)
        #font.setFamily("Heveltica")

        # Adiciona os componentes ao layout vertical
        layout.addWidget(lbl_opcao_funcao_fechamento)
        layout.addWidget(self.cmb_opcao_funcao_fechamento)
        layout.addWidget(lbl_tamanho_pixel)
        layout.addWidget(self.txt_tamanho_pixel)
        layout.addWidget(lbl_comprimento_voxel)
        layout.addWidget(self.txt_comprimento_voxel)
        layout.addWidget(lbl_imagens)
        layout.addWidget(btn_imagens)
        layout.addWidget(lbl_mascaras)
        layout.addWidget(btn_mascaras)
        layout.addWidget(lbl_tipo_filtro)
        layout.addWidget(self.cmb_tipo_filtro)
        layout.addWidget(lbl_nivel_processamento)
        layout.addWidget(self.txt_nivel_processamento)
        layout.addWidget(lbl_camada_tumor)
        layout.addWidget(self.txt_camada_tumor)
        layout.addWidget(self.chk_index_camada)
        layout.addWidget(self.chk_salvar_conteudo)
        layout.addWidget(self.chk_editar_mascaras_livewire)
        layout.addWidget(self.chk_cortar_imagens)
        layout.addWidget(self.chk_contorno_ativo)
        layout.addWidget(lbl_pasta_salvar)
        layout.addWidget(btn_pasta_salvar)
        layout.addWidget(btn_continuar)

        # Configurações adicionais
        self.setWindowTitle("Minha aplicação PyQt")
        self.setGeometry(100, 100, 600, 600)
        self.setFont(font)
    
    def btn_clicked(self):
        sender = self.sender()
        match sender.objectName():
            case "SelecIMG":
                filenames = QFileDialog.getOpenFileNames(self, 'Selecione as Imagens', '.', 'Image files (*.jpg)')
                self.imagens_selecionadas = filenames[0]
            case "SelecMASK":
                filenames = QFileDialog.getOpenFileNames(self, 'Selecione as Máscaras', '.', 'Image files (*.tif)')
                self.mascaras_selecionadas = filenames[0]
            case "SelecSAVE":
                foldername = QFileDialog.getExistingDirectory(self, 'Selecione a Pasta para Salvar')
                self.pasta_salvar = foldername
            case "Continuar":
                self.new_window = NewWindow()
                self.new_window.show()
                self.close()
                
class NewWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        # Configure a janela e o layout
        self.setWindowTitle("Nova Janela")
        layout = QVBoxLayout(self)

        # Adicione um rótulo e um botão
        label = QLabel("Nova Janela")
        button = QPushButton("Fechar Janela")
        button.clicked.connect(self.close)

        # Adicione os widgets ao layout
        layout.addWidget(label)
        layout.addWidget(button)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
