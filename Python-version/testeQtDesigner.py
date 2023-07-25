from PyQt5.QtCore import Qt, QPointF, QLineF, QRectF
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QLabel, QStackedWidget,QScrollArea,QWidget, QGraphicsScene, QGraphicsView,QVBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase, QPen
from PIL import Image
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import qtmodern.styles
import qtmodern.windows
import os
import glob


class MainWindow(QtWidgets.QMainWindow):

    mode = "light"

    #private
    _txt_tamanho_pixel = ""
    _txt_pasta_salvar = ""
    _txt_selecao_mascaras = ""
    _txt_nivel_processamento = ""
    _txt_camada_tumor = ""
    _txt_comprimento_voxel = ""
    _txt_selecao_imagens = ""

    _cmb_opcao_funcao_fechamento = ""
    _cmb_tipo_de_filtro = ""

    _chk_editar_mascaras_livewire = ""
    _chk_salvar_conteudo = ""
    _chk_index_camada = ""
    _chk_cortar_imagens = ""
    _chk_contorno_ativo = ""

    _folder_path_img = ""
    _filenames_img = []
    _folder_path_mask = ""
    _filenames_mask = []
    _folder_path_save = ""

    _checkboxes_selecao_masks = []

    _rect = [0,0,0,0]
    _image_height = 0

    def __init__(self):
        super().__init__()
        # Carrega a interface de usuário a partir do arquivo .ui
        ui_file = os.path.join(os.path.dirname(__file__), 'MainScreen.ui')
        uic.loadUi(ui_file, self)
        child_widgets = self.findChildren(QtWidgets.QMainWindow)
        self.stackedWidget = self.findChild(QStackedWidget, "appBody")
        self.scrollbar = self.findChild(QtWidgets.QScrollBar, "horizontalScrollBar")
        self.scrollbar_crop = self.findChild(QtWidgets.QScrollBar, "scrollbar_crop")
        self.last_mouse_pos = None
        self.selection_start_pos = None
        self.selection_rect_item = None

        self.plotWidget = pg.GraphicsLayoutWidget()
        self.view = self.plotWidget.addViewBox()
        self._roi_item = pg.RectROI([100, 100], [200, 200], pen=(0, 9))
        print(self.stackedWidget)

        #self.scrollbar.sliderMoved.connect(self.atualizaImagem)

        #self.atualizaImagem(0)
        
        
    def btn_style(self):
        sender = self.sender().isChecked()
        if sender:
            self.setStyleSheet(qtmodern.styles.dark(app))
        else:
            self.setStyleSheet(qtmodern.styles.light(app))

    def button_clicked(self):
        menu = self.findChild(QtWidgets.QGridLayout, "gridMenuPrincipal")
        sender = self.sender().objectName()
        if sender in ("btn_selecao_imagens", "btn_selecao_mascaras", "btn_pasta_salvar"):

            folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Selecione uma pasta", "", QtWidgets.QFileDialog.ShowDirsOnly)
            if folder_path:

                if sender == "btn_selecao_imagens":
                    self._folder_path_img = folder_path
                    menu.itemAt(21).widget().setText(self._folder_path_img)                   #seta o caminho da pasta com as imagens
                    self._txt_selecao_imagens = menu.itemAt(21).widget().text()               #guarda em uma variavel privada esse caminho
                    filenames = os.listdir(self._folder_path_img)
                    filenames = [f for f in filenames if f.lower().endswith(".jpg") or f.lower().endswith(".jpeg")]
                    filenames.sort()
                    self._filenames_img.clear()
                    self._filenames_img = filenames
                    print(self._filenames_img)

                elif sender == "btn_selecao_mascaras":
                    self._folder_path_mask = folder_path
                    menu.itemAt(9).widget().setText(self._folder_path_mask)                   #seta o caminho da pasta com as imagens
                    MainWindow._txt_selecao_mascaras = menu.itemAt(9).widget().text()        #guarda em uma variavel privada esse caminho
                    filenames = os.listdir(self._folder_path_img)
                    filenames = [f for f in filenames if f.lower().endswith(".tif") or f.lower().endswith(".tiff")]
                    filenames.sort()
                    self._filenames_mask.clear()
                    self._filenames_mask = filenames
                    print(self._filenames_mask)

                elif sender == "btn_pasta_salvar":
                    self._folder_path_save = folder_path
                    menu.itemAt(4).widget().setText(self._folder_path_save)
                    MainWindow._txt_pasta_salvar = menu.itemAt(4).widget().text() 

            else:
                QtWidgets.QMessageBox.information(self, "Informação", "Nenhuma pasta selecionada.")

        elif sender == "btn_ajuda":
            pass
        
        elif sender == "btn_crop":
            for image in self._filenames_img:
                pil_image = Image.open(self._folder_path_img +"/"+ image)
                pil_image = pil_image.crop((self._rect[0],self._rect[1], self._rect[2], self._rect[3]))
                pil_image.save(self._folder_path_img +"/"+ image)
            self.stackedWidget.setProperty("currentIndex", 1)

        elif sender == "btn_continuar":
            self.recebeDados()
            self.criaCheckboxes()
            if self._chk_cortar_imagens:
                self.stackedWidget.setProperty("currentIndex", 2)
            elif self._chk_editar_mascaras_livewire:
                self.stackedWidget.setProperty("currentIndex", 1)
            else:
                pass
                #self.enviaDados()
            self.criaPlotWidget()
            #print(self.stackedWidget.children())

            #self.plotWidget = self.stackedWidget.findChild(QWidget, "plotWidget")
            self.scrollbar_crop.setMaximum(self._filenames_img.__len__()-1)
            self.scrollbar.setMaximum(self._filenames_img.__len__()-1)
    
    def criaPlotWidget(self):
        widgetContainer = self.stackedWidget.findChild(QWidget, "plotWidget")
        layout = QVBoxLayout(widgetContainer)
        layout.addWidget(self.plotWidget)
        widgetContainer.setLayout(layout)

    def atualizaImagem(self, value):
        sender = self.sender().objectName()
        index = value
        if sender == "scrollbar_mask":
            #print(index)
            print(self._folder_path_img +"/"+ self._filenames_img[index])
            imagem = QtGui.QPixmap(self._folder_path_img + "/" + self._filenames_img[index])
            img = self.findChild(QLabel, "currentImg")
            img.setPixmap(imagem)

        elif sender == "scrollbar_crop":
            self.view.clear()
            print(index)
            pil_image = Image.open(self._folder_path_img +"/"+ self._filenames_img[index])
            pil_image = pil_image.rotate(-90, expand=True)
            self._image_height = pil_image.height
            image_data = np.array(pil_image)
            image_item = pg.ImageItem()
            self.view.addItem(image_item)
            image_item.setImage(image_data)
            self._roi_item.addScaleHandle([1, 1], [0, 0])
            self._roi_item.sigRegionChanged.connect(self.update_roi)
            self.view.addItem(self._roi_item)

            QtWidgets.QApplication.processEvents()

    # Função de atualização do ROI
    def update_roi(self):
        pos = self._roi_item.pos()
        size = self._roi_item.size()
        x, y = pos.x(), pos.y()
        w, h = size.x(), size.y()

        # Verifica se a largura e altura são diferentes e ajusta para que sejam iguais
        if w != h:
            # Calcula o tamanho mínimo entre largura e altura
            min_size = min(w, h)
            
            # Ajusta a largura e altura para serem iguais
            if w > h:
                self._roi_item.setSize([min_size, min_size])
            else:
                self._roi_item.setSize([min_size, min_size])

        self._rect[0] = x
        self._rect[1] = y+h
        self._rect[2] = x+w
        self._rect[3] = self._image_height - y
        print("ROI selecionado:", x, y, w, h, self._image_height)

    # LISTA INDEXES
    # txt_tamanho_pixel = 0
    # txt_pasta_salvar = 4
    # txt_selecao_mascaras = 9
    # txt_nivel_processamento = 11
    # txt_camada_tumor = 12
    # txt_comprimento_voxel = 16
    # txt_selecao_imagens = 21
    #
    # cmb_opcao_funcao_fechamento = 10
    # cmb_tipo_de_filtro = 15
    # 
    # chk_editar_mascaras_livewire = 22
    # chk_salvar_conteudo = 23  
    # chk_index_camada = 24
    # chk_cortar_imagens = 25
    # chk_contorno_ativo = 26

    def criaCheckboxes(self):
        # Cria checkboxes
        print("chk")
        scrollArea = self.stackedWidget.findChild(QWidget,"Page2").findChild(QScrollArea,"scrollArea")
        scrollAreaWidget = scrollArea.findChild(QWidget, "scrollAreaCHKs")
        
        if scrollAreaWidget is not None:
        # Remove todos os widgets do gridLayout
            for i in reversed(range(scrollAreaWidget.layout().count())):
                widgetToRemove = scrollAreaWidget.layout().itemAt(i).widget()
                scrollAreaWidget.layout().removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)

        row = 0
        col = 0
        for filename in self._filenames_img:
            nome_arquivo, extensao = os.path.splitext(filename)
            checkbox = QtWidgets.QRadioButton(nome_arquivo)
            checkbox.setProperty("autoExclusive", False)
            self._checkboxes_selecao_masks.append(checkbox)
            scrollAreaWidget.layout().addWidget(checkbox,row,col)
            col+=1
            if col == 3:
                col = 0
                row+=1
        
        scrollAreaWidget.adjustSize()
    
    def recebeDados(self):
        menu = self.findChild(QtWidgets.QGridLayout, "gridMenuPrincipal")
        # MainWindow._txt_tamanho_pixel = menu.itemAt(0).widget().text()
        # MainWindow._txt_pasta_salvar = menu.itemAt(4).widget().text()
        # MainWindow._txt_selecao_mascaras = menu.itemAt(9).widget().text()
        # MainWindow._txt_nivel_processamento = menu.itemAt(11).widget().text()
        # MainWindow._txt_camada_tumor = menu.itemAt(12).widget().text()
        # MainWindow._txt_comprimento_voxel = menu.itemAt(16).widget().text()
        # MainWindow._txt_selecao_imagens = menu.itemAt(21).widget().text()

        MainWindow._cmb_opcao_funcao_fechamento = menu.itemAt(10).widget().currentText()
        MainWindow._cmb_tipo_de_filtro = menu.itemAt(15).widget().currentText()

        MainWindow._chk_editar_mascaras_livewire = menu.itemAt(22).widget().isChecked()
        MainWindow._chk_salvar_conteudo = menu.itemAt(23).widget().isChecked()
        MainWindow._chk_index_camada = menu.itemAt(24).widget().isChecked()
        MainWindow._chk_cortar_imagens = menu.itemAt(25).widget().isChecked()
        MainWindow._chk_contorno_ativo = menu.itemAt(26).widget().isChecked()

        print(menu)
        print(self._txt_selecao_imagens)

    # def mousePressEvent(self, event):
    #     if event.buttons() & Qt.LeftButton:
    #         self.selection_start_pos = self.graphicsView.mapToScene(event.pos())

    #         # Remove a seleção anterior, se existir
    #         if self.selection_rect_item:
    #             self.scene.removeItem(self.selection_rect_item)
    #             self.selection_rect_item = None

    # def mouseMoveEvent(self, event):
    #     if event.buttons() & Qt.LeftButton and self.selection_start_pos is not None:
    #         current_pos = self.graphicsView.mapToScene(event.pos())
    #         self.draw_selection_rect(self.selection_start_pos, current_pos)

    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton and self.selection_start_pos is not None:
    #         end_pos = self.graphicsView.mapToScene(event.pos())
    #         self.draw_selection_rect(self.selection_start_pos, end_pos)

    #         # Realize as ações necessárias com a seleção aqui
    #         # Por exemplo, obter as coordenadas da seleção retangular:
    #         selection_rect = QRectF(self.selection_start_pos, end_pos)
    #         print("Seleção retangular:", selection_rect.x(), selection_rect.y(), selection_rect.width(), selection_rect.height())

    # def draw_selection_rect(self, start_pos, end_pos):
    #     # Remove a seleção anterior, se existir
    #     if self.selection_rect_item:
    #         self.scene.removeItem(self.selection_rect_item)

    #     pen = QPen(Qt.red, 1, Qt.DashLine)
    #     rect = QRectF(start_pos, end_pos)
    #     self.selection_rect_item = self.scene.addRect(rect, pen)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    qtmodern.styles.light(app)
    #app.setStyle("Fusion")
    font_id = QFontDatabase.addApplicationFont('C:/Users/igor_/OneDrive/Documents/GitHub/IIWM-igor/Python-version/fontes/Poppins-SemiBold.ttf')
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    window = MainWindow()
    # qtmodern.styles.light(app)
    # if window.mode == "dark":
    #     qtmodern.styles.dark(app)
    # else:
    #     qtmodern.styles.light(app)
    #window.show()
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    
    app.exec_()
