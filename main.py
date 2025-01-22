import rasterio
from PIL import Image
import numpy as np
import cv2

# NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif
# NFREC_Quincy_DSSAT_10_2_2024_x5_20m_dem.tif
with rasterio.open("NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif") as dataset:
    dataset_crs = dataset.crs
    print(dataset.shape)
    blue = dataset.read(1) / 32768
    green = dataset.read(2) / 32768
    red = dataset.read(3) / 32768

img: list[list[tuple[float, float, float]]] = []
for i in range(0, len(blue)):
    img.append([])
    for j in range(0, len(blue[0])):
        img[i].append((red[i][j], blue[i][j], green[i][j]))

img = np.array(img)
pic = Image.fromarray(img, "L")
pic.show()
cv2.imshow("image", img)
cv2.waitKey()
exit()

d = {}
for i in range(0, len(red), 1):
    d[i] = []
    for j in range(0, len(red[0]), 1):
        d[i].append(red[i][j])
        print(red[i][j])

img = []
for key in d:
    img.append(d[key])

img = np.array(img)

pic = Image.fromarray(img, "L")
pic.show()
