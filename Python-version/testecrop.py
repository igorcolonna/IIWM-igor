import os
import pyqtgraph as pg
import numpy as np
from PIL import Image
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

# Caminho da pasta contendo as imagens
folder_path = 'C:/Users/igor_/Downloads/Teste_IIWM/imagem'

# Lista os arquivos na pasta
filenames = os.listdir(folder_path)

# Filtra apenas os arquivos de imagem suportados (por exemplo, .jpg, .jpeg, .png)
image_extensions = ['.jpg', '.jpeg', '.png']
image_files = [f for f in filenames if os.path.splitext(f)[1].lower() in image_extensions]

# Ordena os arquivos por nome
image_files.sort()

# Definir o tamanho da janela
window_size = 600

# Criação do aplicativo Qt
app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True, title="Selecione o ROI")
win.resize(window_size, window_size)  # Definir as dimensões quadradas
view = win.addViewBox()

# Variável global para o ROI
roi_item = None
roi_item = pg.RectROI([100, 100], [200, 200], pen=(0, 9))
# Função para carregar e exibir a próxima imagem
def load_next_image():
    global roi_item  # Referencia a variável global
    
    # Verifica se há mais imagens para exibir
    if len(image_files) == 0:
        print("Todas as imagens foram exibidas.")
        return
    
    # Remove a imagem anterior (se houver)
    view.clear()
    
    # Carrega a próxima imagem
    image_file = image_files.pop(0)
    image_path = os.path.join(folder_path, image_file)
    pil_image = Image.open(image_path)
    
    # Rotaciona a imagem em 90 graus anti-horário
    pil_image = pil_image.rotate(-90, expand=True)
    
    # Converte a imagem PIL para um array numpy
    image_data = np.array(pil_image)
    
    # Criação da imagem
    image_item = pg.ImageItem()
    view.addItem(image_item)
    image_item.setImage(image_data)
    
    # Adiciona uma região retangular inicial para seleção
    
    roi_item.addScaleHandle([1, 1], [0, 0])
    roi_item.sigRegionChanged.connect(update_roi)
    view.addItem(roi_item)
    
    # Atualiza a interface gráfica
    QtWidgets.QApplication.processEvents()

# Função de atualização do ROI
def update_roi():
    pos = roi_item.pos()
    size = roi_item.size()
    x, y = pos.x(), pos.y()
    w, h = size.x(), size.y()

    # Verifica se a largura e altura são diferentes e ajusta para que sejam iguais
    if w != h:
        # Calcula o tamanho mínimo entre largura e altura
        min_size = min(w, h)
        
        # Ajusta a largura e altura para serem iguais
        if w > h:
            roi_item.setSize([min_size, min_size])
        else:
            roi_item.setSize([min_size, min_size])

    print("ROI selecionado:", x, y, w, h)

# Janela principal
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("Selecione o ROI")
        
        # Botão para carregar a próxima imagem
        self.next_image_button = QtWidgets.QPushButton("Próxima Imagem")
        self.next_image_button.clicked.connect(load_next_image)
        
        # Configuração do layout
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.next_image_button)
        layout.addWidget(win)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Inicia o aplicativo Qt e exibe a janela principal
main_window = MainWindow()
main_window.show()

# Carrega a primeira imagem
load_next_image()

# Executa o aplicativo Qt
app.exec_()
