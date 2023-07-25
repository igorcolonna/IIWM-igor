import cv2
import numpy as np
import os
from skimage.segmentation import active_contour

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        seed_points.append((x, y))

# Carrega a imagem
pasta_imagens = 'C:/Users/igor_/Downloads/Teste_IIWM/imagem'

filenames = os.listdir(pasta_imagens)

# Filtra os nomes de arquivo para incluir apenas arquivos com extensão .jpg ou .jpeg
filenames = [f for f in filenames if f.lower().endswith(".jpg") or f.lower().endswith(".jpeg")]

# Ordena a lista de nomes de arquivo
filenames.sort()

if len(filenames) == 0:
    print("Nenhuma imagem encontrada na pasta.")
    exit()

imagens = [os.path.join(pasta_imagens, filename) for filename in filenames]

image = cv2.imread(imagens[0])

original_image = image.copy()

#roi = cv2.selectROI("teste",image)

# Exibe a imagem e permite que o usuário selecione o ROI retangular
# Exibe a imagem e permite que o usuário selecione o ROI retangular
x, y, w, h = cv2.selectROI("Selecione o ROI", image, fromCenter=False)

# Calcula o tamanho do lado do quadrado perfeito
size = max(w, h)

# Calcula as coordenadas do ROI quadrado
x_square = x
y_square = y
w_square = size
h_square = size

# Verifica se a seleção é um quadrado perfeito
if w != h:
    # Ajusta as coordenadas do ROI para um quadrado perfeito
    diff = abs(w - h) // 2
    if w > h:
        y_square -= diff
        h_square = w_square
    else:
        x_square -= diff
        w_square = h_square

# Desenha o ROI quadrado na imagem
cv2.rectangle(image, (x_square, y_square), (x_square + w_square, y_square + h_square), (0, 255, 0), 2)

# Exibe a imagem com o ROI quadrado
cv2.imshow("ROI Quadrado", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Redimensiona a imagem para facilitar a interação do usuário
scale_percent = 50  # Define a escala de redimensionamento
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# Cria uma janela para exibir a imagem
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

seed_points = []
is_drawing = False

while True:
    cv2.imshow('image', image)
    key = cv2.waitKey(1) & 0xFF

    # Se a tecla 'r' for pressionada, redefine os pontos de semente
    if key == ord('r'):
        image = original_image.copy()
        seed_points = []

    # Se a tecla 'c' for pressionada, realiza a segmentação
    elif key == ord('c'):
        if len(seed_points) >= 3:
            # Converte os pontos de semente para um array do NumPy
            seed_points_arr = np.array(seed_points, dtype=np.int32)
            
            # Executa o algoritmo Live Wire para segmentação
            snake = active_contour(image, seed_points_arr, alpha=0.015, beta=10, gamma=0.001)

            # Desenha o contorno da segmentação na imagem original
            cv2.polylines(original_image, np.int32([snake]), True, (0, 255, 0), 2)
            
            # Exibe a imagem segmentada
            cv2.imshow('segmented image', original_image)
    
    # Se a tecla 'q' for pressionada, encerra o programa
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
