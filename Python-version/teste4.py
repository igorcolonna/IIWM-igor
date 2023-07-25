import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

src = cv.imread('C:\\Users\\igor_\\OneDrive\\Pictures\\Teste_IIWM\\imagem\\imagem0115.jpg')
# src = cv.resize(src, (1024, 1024))  # Uncomment this line if you need to resize the image

tool = cv.segmentation_IntelligentScissorsMB()
tool.setEdgeFeatureCannyParameters(32, 100)
tool.setGradientMagnitudeMaxLimit(200)
tool.applyImage(src)

hasMap = False

def build_map(x, y):
    global hasMap
    if 0 <= x < src.shape[1] and 0 <= y < src.shape[0]:
        print(x, y)
        print('buildMap')
        tool.buildMap((x, y))
        hasMap = True

def draw_contour(event, x, y, flags, param):
    global hasMap
    if event == cv.EVENT_MOUSEMOVE and hasMap and 0 <= x < src.shape[1] and 0 <= y < src.shape[0]:
        dst = src.copy()
        contour = cv.Mat()
        tool.getContour((x, y), contour)
        contours = cv.MatVector()
        contours.push_back(contour)
        color = (0, 255, 0)  # BGR
        cv.polylines(dst, contours, isClosed=False, color=color, thickness=1)
        cv.imshow('canvasOutput', dst)
        contour.delete()

# Create Tkinter window
root = tk.Tk()
root.title('Intelligent Scissors')

# Convert the OpenCV image to PIL format
image = cv.cvtColor(src, cv.COLOR_BGR2RGB)
image = Image.fromarray(image)
image_tk = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=image_tk)
label.pack()

def on_click(event):
    x = event.x
    y = event.y
    build_map(x, y)

def on_mousemove(event):
    x = event.x
    y = event.y
    draw_contour(cv.EVENT_MOUSEMOVE, x, y, None, None)

# Bind mouse click and mouse move events
label.bind("<Button-1>", on_click)
label.bind("<B1-Motion>", on_mousemove)

# Start the Tkinter event loop
root.mainloop()

# After closing the Tkinter window, continue with OpenCV
cv.waitKey(0)
cv.destroyAllWindows()

# Don't forget to release resources
src.release()
tool.delete()
