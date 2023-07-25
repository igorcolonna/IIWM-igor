# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QScrollBar, QSizePolicy, QStackedWidget, QStatusBar,
    QTabWidget, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"QWidget#centralwidget,QStatusBar,QMenuBar{\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel#PEB_logo{\n"
"	background: transparent;\n"
"}\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(500, 550))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.centralwidget.setFont(font1)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 200))
        self.header.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PEB_logo = QLabel(self.header)
        self.PEB_logo.setObjectName(u"PEB_logo")
        self.PEB_logo.setMaximumSize(QSize(105, 100))
        self.PEB_logo.setFont(font1)
        self.PEB_logo.setAutoFillBackground(False)
        self.PEB_logo.setFrameShape(QFrame.NoFrame)
        self.PEB_logo.setTextFormat(Qt.AutoText)
        self.PEB_logo.setPixmap(QPixmap(u"Resources/LUS_logo-fotor-bg-remover-20230525152913.png"))
        self.PEB_logo.setScaledContents(True)
        self.PEB_logo.setWordWrap(False)
        self.PEB_logo.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.PEB_logo)

        self.textBrowser = QTextBrowser(self.header)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFont(font1)
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.textBrowser)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_ajuda = QPushButton(self.header)
        self.btn_ajuda.setObjectName(u"btn_ajuda")
        self.btn_ajuda.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_ajuda, 0, Qt.AlignTop)

        self.Rbtn_style = QRadioButton(self.header)
        self.Rbtn_style.setObjectName(u"Rbtn_style")

        self.verticalLayout_3.addWidget(self.Rbtn_style, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)

        self.appBody = QStackedWidget(self.centralwidget)
        self.appBody.setObjectName(u"appBody")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.gridMenuPrincipal = QGridLayout(self.Page1)
        self.gridMenuPrincipal.setObjectName(u"gridMenuPrincipal")
        self.gridMenuPrincipal.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridMenuPrincipal.setContentsMargins(10, -1, 10, -1)
        self.txt_tamanho_pixel = QLineEdit(self.Page1)
        self.txt_tamanho_pixel.setObjectName(u"txt_tamanho_pixel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_tamanho_pixel.sizePolicy().hasHeightForWidth())
        self.txt_tamanho_pixel.setSizePolicy(sizePolicy2)
        self.txt_tamanho_pixel.setMinimumSize(QSize(0, 0))
        self.txt_tamanho_pixel.setFont(font1)
        self.txt_tamanho_pixel.setFrame(True)
        self.txt_tamanho_pixel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridMenuPrincipal.addWidget(self.txt_tamanho_pixel, 1, 1, 1, 1)

        self.lbl_tipo_filtro = QLabel(self.Page1)
        self.lbl_tipo_filtro.setObjectName(u"lbl_tipo_filtro")
        self.lbl_tipo_filtro.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_tipo_filtro, 5, 0, 1, 1)

        self.lbl_mascaras = QLabel(self.Page1)
        self.lbl_mascaras.setObjectName(u"lbl_mascaras")
        self.lbl_mascaras.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_mascaras, 4, 0, 1, 1)

        self.lbl_tamanho_pixel = QLabel(self.Page1)
        self.lbl_tamanho_pixel.setObjectName(u"lbl_tamanho_pixel")
        self.lbl_tamanho_pixel.setFont(font1)
        self.lbl_tamanho_pixel.setScaledContents(False)

        self.gridMenuPrincipal.addWidget(self.lbl_tamanho_pixel, 1, 0, 1, 1)

        self.txt_pasta_salvar = QLineEdit(self.Page1)
        self.txt_pasta_salvar.setObjectName(u"txt_pasta_salvar")
        self.txt_pasta_salvar.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.txt_pasta_salvar, 13, 1, 1, 1)

        self.lbl_imagens = QLabel(self.Page1)
        self.lbl_imagens.setObjectName(u"lbl_imagens")
        self.lbl_imagens.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_imagens, 3, 0, 1, 1)

        self.lbl_opcao_funcao_fechamento = QLabel(self.Page1)
        self.lbl_opcao_funcao_fechamento.setObjectName(u"lbl_opcao_funcao_fechamento")
        self.lbl_opcao_funcao_fechamento.setMinimumSize(QSize(0, 0))
        self.lbl_opcao_funcao_fechamento.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_opcao_funcao_fechamento.setFont(font1)
        self.lbl_opcao_funcao_fechamento.setFrameShadow(QFrame.Plain)
        self.lbl_opcao_funcao_fechamento.setTextFormat(Qt.PlainText)

        self.gridMenuPrincipal.addWidget(self.lbl_opcao_funcao_fechamento, 0, 0, 1, 1)

        self.btn_continuar = QPushButton(self.Page1)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.btn_continuar, 14, 1, 1, 1)

        self.lbl_pasta_salvar = QLabel(self.Page1)
        self.lbl_pasta_salvar.setObjectName(u"lbl_pasta_salvar")
        self.lbl_pasta_salvar.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_pasta_salvar, 13, 0, 1, 1)

        self.txt_selecao_mascaras = QLineEdit(self.Page1)
        self.txt_selecao_mascaras.setObjectName(u"txt_selecao_mascaras")
        sizePolicy2.setHeightForWidth(self.txt_selecao_mascaras.sizePolicy().hasHeightForWidth())
        self.txt_selecao_mascaras.setSizePolicy(sizePolicy2)
        self.txt_selecao_mascaras.setMinimumSize(QSize(0, 0))
        self.txt_selecao_mascaras.setFont(font1)
        self.txt_selecao_mascaras.setFrame(True)
        self.txt_selecao_mascaras.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridMenuPrincipal.addWidget(self.txt_selecao_mascaras, 4, 1, 1, 1)

        self.cmb_opcao_funcao_fechamento = QComboBox(self.Page1)
        self.cmb_opcao_funcao_fechamento.addItem("")
        self.cmb_opcao_funcao_fechamento.addItem("")
        self.cmb_opcao_funcao_fechamento.setObjectName(u"cmb_opcao_funcao_fechamento")
        sizePolicy2.setHeightForWidth(self.cmb_opcao_funcao_fechamento.sizePolicy().hasHeightForWidth())
        self.cmb_opcao_funcao_fechamento.setSizePolicy(sizePolicy2)
        self.cmb_opcao_funcao_fechamento.setMinimumSize(QSize(0, 0))
        self.cmb_opcao_funcao_fechamento.setMaximumSize(QSize(16777215, 16777215))
        self.cmb_opcao_funcao_fechamento.setFont(font1)
        self.cmb_opcao_funcao_fechamento.setEditable(False)
        self.cmb_opcao_funcao_fechamento.setMaxVisibleItems(2)
        self.cmb_opcao_funcao_fechamento.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.cmb_opcao_funcao_fechamento.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cmb_opcao_funcao_fechamento.setIconSize(QSize(16, 16))
        self.cmb_opcao_funcao_fechamento.setFrame(True)
        self.cmb_opcao_funcao_fechamento.setModelColumn(0)

        self.gridMenuPrincipal.addWidget(self.cmb_opcao_funcao_fechamento, 0, 1, 1, 1)

        self.txt_nivel_processamento = QLineEdit(self.Page1)
        self.txt_nivel_processamento.setObjectName(u"txt_nivel_processamento")
        sizePolicy2.setHeightForWidth(self.txt_nivel_processamento.sizePolicy().hasHeightForWidth())
        self.txt_nivel_processamento.setSizePolicy(sizePolicy2)
        self.txt_nivel_processamento.setMinimumSize(QSize(0, 0))
        self.txt_nivel_processamento.setFont(font1)
        self.txt_nivel_processamento.setFrame(True)
        self.txt_nivel_processamento.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridMenuPrincipal.addWidget(self.txt_nivel_processamento, 6, 1, 1, 1)

        self.txt_camada_tumor = QLineEdit(self.Page1)
        self.txt_camada_tumor.setObjectName(u"txt_camada_tumor")
        sizePolicy2.setHeightForWidth(self.txt_camada_tumor.sizePolicy().hasHeightForWidth())
        self.txt_camada_tumor.setSizePolicy(sizePolicy2)
        self.txt_camada_tumor.setMinimumSize(QSize(0, 0))
        self.txt_camada_tumor.setFont(font1)
        self.txt_camada_tumor.setFrame(True)
        self.txt_camada_tumor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridMenuPrincipal.addWidget(self.txt_camada_tumor, 7, 1, 1, 1)

        self.lbl_comprimento_voxel = QLabel(self.Page1)
        self.lbl_comprimento_voxel.setObjectName(u"lbl_comprimento_voxel")
        self.lbl_comprimento_voxel.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_comprimento_voxel, 2, 0, 1, 1)

        self.btn_selecao_imagens = QToolButton(self.Page1)
        self.btn_selecao_imagens.setObjectName(u"btn_selecao_imagens")
        self.btn_selecao_imagens.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.btn_selecao_imagens, 3, 2, 1, 1)

        self.cmb_tipo_de_filtro = QComboBox(self.Page1)
        self.cmb_tipo_de_filtro.addItem("")
        self.cmb_tipo_de_filtro.addItem("")
        self.cmb_tipo_de_filtro.addItem("")
        self.cmb_tipo_de_filtro.setObjectName(u"cmb_tipo_de_filtro")
        self.cmb_tipo_de_filtro.setMinimumSize(QSize(0, 0))
        self.cmb_tipo_de_filtro.setMaximumSize(QSize(16777215, 16777215))
        self.cmb_tipo_de_filtro.setFont(font1)
        self.cmb_tipo_de_filtro.setEditable(False)
        self.cmb_tipo_de_filtro.setMaxVisibleItems(2)
        self.cmb_tipo_de_filtro.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.cmb_tipo_de_filtro.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cmb_tipo_de_filtro.setIconSize(QSize(16, 16))
        self.cmb_tipo_de_filtro.setFrame(True)
        self.cmb_tipo_de_filtro.setModelColumn(0)

        self.gridMenuPrincipal.addWidget(self.cmb_tipo_de_filtro, 5, 1, 1, 1)

        self.txt_comprimento_voxel = QLineEdit(self.Page1)
        self.txt_comprimento_voxel.setObjectName(u"txt_comprimento_voxel")
        sizePolicy2.setHeightForWidth(self.txt_comprimento_voxel.sizePolicy().hasHeightForWidth())
        self.txt_comprimento_voxel.setSizePolicy(sizePolicy2)
        self.txt_comprimento_voxel.setMinimumSize(QSize(0, 0))
        self.txt_comprimento_voxel.setFont(font1)
        self.txt_comprimento_voxel.setFrame(True)
        self.txt_comprimento_voxel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridMenuPrincipal.addWidget(self.txt_comprimento_voxel, 2, 1, 1, 1)

        self.lbl_camada_tumor = QLabel(self.Page1)
        self.lbl_camada_tumor.setObjectName(u"lbl_camada_tumor")
        self.lbl_camada_tumor.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_camada_tumor, 7, 0, 1, 1)

        self.btn_pasta_salvar = QToolButton(self.Page1)
        self.btn_pasta_salvar.setObjectName(u"btn_pasta_salvar")
        self.btn_pasta_salvar.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.btn_pasta_salvar, 13, 2, 1, 1)

        self.btn_selecao_mascaras = QToolButton(self.Page1)
        self.btn_selecao_mascaras.setObjectName(u"btn_selecao_mascaras")
        self.btn_selecao_mascaras.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.btn_selecao_mascaras, 4, 2, 1, 1)

        self.lbl_nivel_processamento = QLabel(self.Page1)
        self.lbl_nivel_processamento.setObjectName(u"lbl_nivel_processamento")
        self.lbl_nivel_processamento.setFont(font1)

        self.gridMenuPrincipal.addWidget(self.lbl_nivel_processamento, 6, 0, 1, 1)

        self.txt_selecao_imagens = QLineEdit(self.Page1)
        self.txt_selecao_imagens.setObjectName(u"txt_selecao_imagens")
        sizePolicy2.setHeightForWidth(self.txt_selecao_imagens.sizePolicy().hasHeightForWidth())
        self.txt_selecao_imagens.setSizePolicy(sizePolicy2)
        self.txt_selecao_imagens.setMinimumSize(QSize(0, 0))
        self.txt_selecao_imagens.setFont(font1)
        self.txt_selecao_imagens.setFrame(True)
        self.txt_selecao_imagens.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridMenuPrincipal.addWidget(self.txt_selecao_imagens, 3, 1, 1, 1)

        self.chk_editar_mascaras_livewire = QRadioButton(self.Page1)
        self.chk_editar_mascaras_livewire.setObjectName(u"chk_editar_mascaras_livewire")
        self.chk_editar_mascaras_livewire.setFont(font1)
        self.chk_editar_mascaras_livewire.setAutoExclusive(False)

        self.gridMenuPrincipal.addWidget(self.chk_editar_mascaras_livewire, 10, 0, 1, 1)

        self.chk_salvar_conteudo = QRadioButton(self.Page1)
        self.chk_salvar_conteudo.setObjectName(u"chk_salvar_conteudo")
        self.chk_salvar_conteudo.setFont(font1)
        self.chk_salvar_conteudo.setAutoExclusive(False)

        self.gridMenuPrincipal.addWidget(self.chk_salvar_conteudo, 9, 0, 1, 1)

        self.chk_index_camada = QRadioButton(self.Page1)
        self.chk_index_camada.setObjectName(u"chk_index_camada")
        self.chk_index_camada.setFont(font1)
        self.chk_index_camada.setCheckable(True)
        self.chk_index_camada.setChecked(False)
        self.chk_index_camada.setAutoExclusive(False)

        self.gridMenuPrincipal.addWidget(self.chk_index_camada, 8, 0, 1, 1)

        self.chk_cortar_imagens = QRadioButton(self.Page1)
        self.chk_cortar_imagens.setObjectName(u"chk_cortar_imagens")
        self.chk_cortar_imagens.setFont(font1)
        self.chk_cortar_imagens.setAutoExclusive(False)

        self.gridMenuPrincipal.addWidget(self.chk_cortar_imagens, 11, 0, 1, 1)

        self.chk_contorno_ativo = QRadioButton(self.Page1)
        self.chk_contorno_ativo.setObjectName(u"chk_contorno_ativo")
        self.chk_contorno_ativo.setFont(font1)
        self.chk_contorno_ativo.setAutoExclusive(False)

        self.gridMenuPrincipal.addWidget(self.chk_contorno_ativo, 12, 0, 1, 1)

        self.appBody.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.gridLayout = QGridLayout(self.Page2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_livewire = QPushButton(self.Page2)
        self.btn_livewire.setObjectName(u"btn_livewire")

        self.gridLayout.addWidget(self.btn_livewire, 1, 0, 1, 1)

        self.frame = QFrame(self.Page2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.currentImg = QLabel(self.frame)
        self.currentImg.setObjectName(u"currentImg")
        sizePolicy1.setHeightForWidth(self.currentImg.sizePolicy().hasHeightForWidth())
        self.currentImg.setSizePolicy(sizePolicy1)
        self.currentImg.setFrameShape(QFrame.NoFrame)
        self.currentImg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.currentImg)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.Page2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaCHKs = QWidget()
        self.scrollAreaCHKs.setObjectName(u"scrollAreaCHKs")
        self.scrollAreaCHKs.setGeometry(QRect(0, 0, 227, 359))
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollAreaCHKs.sizePolicy().hasHeightForWidth())
        self.scrollAreaCHKs.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.scrollAreaCHKs)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea.setWidget(self.scrollAreaCHKs)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.scrollbar_mask = QScrollBar(self.Page2)
        self.scrollbar_mask.setObjectName(u"scrollbar_mask")
        self.scrollbar_mask.setSliderPosition(0)
        self.scrollbar_mask.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.scrollbar_mask, 1, 1, 1, 1)

        self.appBody.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.gridLayout_4 = QGridLayout(self.Page3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_crop = QPushButton(self.Page3)
        self.btn_crop.setObjectName(u"btn_crop")

        self.gridLayout_4.addWidget(self.btn_crop, 2, 0, 1, 1)

        self.scrollbar_crop = QScrollBar(self.Page3)
        self.scrollbar_crop.setObjectName(u"scrollbar_crop")
        self.scrollbar_crop.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.scrollbar_crop, 1, 0, 1, 1)

        self.plotWidget = QWidget(self.Page3)
        self.plotWidget.setObjectName(u"plotWidget")

        self.gridLayout_4.addWidget(self.plotWidget, 0, 0, 1, 1)

        self.appBody.addWidget(self.Page3)

        self.gridLayout_2.addWidget(self.appBody, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_ajuda.clicked.connect(MainWindow.button_clicked)
        self.Rbtn_style.toggled.connect(MainWindow.btn_style)
        self.btn_selecao_imagens.clicked.connect(MainWindow.button_clicked)
        self.btn_pasta_salvar.clicked.connect(MainWindow.button_clicked)
        self.btn_continuar.clicked.connect(MainWindow.button_clicked)
        self.btn_selecao_mascaras.clicked.connect(MainWindow.button_clicked)
        self.scrollbar_mask.sliderMoved.connect(MainWindow.atualizaImagem)
        self.scrollbar_crop.sliderMoved.connect(MainWindow.atualizaImagem)
        self.btn_crop.clicked.connect(MainWindow.button_clicked)

        self.appBody.setCurrentIndex(1)
        self.cmb_opcao_funcao_fechamento.setCurrentIndex(0)
        self.cmb_tipo_de_filtro.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IIWM Igor Python", None))
        self.PEB_logo.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Autor: Igor Soares Colonna</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: igorcolonna@poli.ufjr.br</p></body></html>", None))
        self.btn_ajuda.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.Rbtn_style.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.txt_tamanho_pixel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_tipo_filtro.setText(QCoreApplication.translate("MainWindow", u"Tipo de Filtro:", None))
        self.lbl_mascaras.setText(QCoreApplication.translate("MainWindow", u"M\u00e1scaras:", None))
        self.lbl_tamanho_pixel.setText(QCoreApplication.translate("MainWindow", u"Tamanho do Pixel [m]:", None))
        self.lbl_imagens.setText(QCoreApplication.translate("MainWindow", u"Imagens:", None))
        self.lbl_opcao_funcao_fechamento.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o de Fun\u00e7\u00e3o de fechamento:", None))
        self.btn_continuar.setText(QCoreApplication.translate("MainWindow", u"Continuar", None))
        self.lbl_pasta_salvar.setText(QCoreApplication.translate("MainWindow", u"Pasta para Salvar", None))
        self.txt_selecao_mascaras.setPlaceholderText("")
        self.cmb_opcao_funcao_fechamento.setItemText(0, QCoreApplication.translate("MainWindow", u"hull", None))
        self.cmb_opcao_funcao_fechamento.setItemText(1, QCoreApplication.translate("MainWindow", u"linear", None))

        self.cmb_opcao_funcao_fechamento.setCurrentText(QCoreApplication.translate("MainWindow", u"hull", None))
        self.txt_nivel_processamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2", None))
        self.txt_camada_tumor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tumor", None))
        self.lbl_comprimento_voxel.setText(QCoreApplication.translate("MainWindow", u"Comprimento do Voxel [m]:", None))
        self.btn_selecao_imagens.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.cmb_tipo_de_filtro.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_tipo_de_filtro.setItemText(1, QCoreApplication.translate("MainWindow", u"Median", None))
        self.cmb_tipo_de_filtro.setItemText(2, QCoreApplication.translate("MainWindow", u"Wavelet", None))

        self.cmb_tipo_de_filtro.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.txt_comprimento_voxel.setText("")
        self.txt_comprimento_voxel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_camada_tumor.setText(QCoreApplication.translate("MainWindow", u"Camada do Tumor:", None))
        self.btn_pasta_salvar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_selecao_mascaras.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_nivel_processamento.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel de Processamento:", None))
        self.txt_selecao_imagens.setPlaceholderText("")
        self.chk_editar_mascaras_livewire.setText(QCoreApplication.translate("MainWindow", u"Editar m\u00e1scaras com LiveWire", None))
        self.chk_salvar_conteudo.setText(QCoreApplication.translate("MainWindow", u"Salvar Conte\u00fado", None))
        self.chk_index_camada.setText(QCoreApplication.translate("MainWindow", u"Index da Camada", None))
#if QT_CONFIG(shortcut)
        self.chk_index_camada.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.chk_cortar_imagens.setText(QCoreApplication.translate("MainWindow", u"Cortar Imagens", None))
        self.chk_contorno_ativo.setText(QCoreApplication.translate("MainWindow", u"Contorno Ativo", None))
        self.btn_livewire.setText(QCoreApplication.translate("MainWindow", u"Continuar", None))
        self.currentImg.setText("")
        self.btn_crop.setText(QCoreApplication.translate("MainWindow", u"Recortar", None))
    # retranslateUi

