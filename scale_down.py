import rasterio
from PIL import Image
import numpy as np
import cv2

# NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif
# NFREC_Quincy_DSSAT_10_2_2024_x5_20m_dem.tif
with rasterio.open("NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif") as dataset:
    dataset_crs = dataset.crs
    blue = dataset.read(1)
    green = dataset.read(2)
    red = dataset.read(3)
    re = dataset.read(4)
    nir = dataset.read(5)

d_b = {}
d_g = {}
d_r = {}
d_re = {}
d_nir = {}
for i in range(0, len(red), 10):
    d_b[i] = []
    d_g[i] = []
    d_r[i] = []
    d_re[i] = []
    d_nir[i] = []
    for j in range(0, len(red[0]), 10):
        d_g[i].append(green[i][j])
        d_b[i].append(blue[i][j])
        d_r[i].append(red[i][j])
        d_re[i].append(re[i][j])
        d_nir[i].append(nir[i][j])

img = {"green": [], "blue": [], "red": [], "re": [], "nir": []}
for key in d_b:
    img["blue"].append(d_b[key])
    img["green"].append(d_g[key])
    img["red"].append(d_r[key])
    img["re"].append(d_re[key])
    img["nir"].append(d_nir[key])

img["blue"] = np.array(img["blue"])
img["green"] = np.array(img["green"])
img["red"] = np.array(img["red"])
img["re"] = np.array(img["re"])
img["nir"] = np.array(img["nir"])

new_dataset = rasterio.open(
    r"C:\Users\casez\Documents\IMG\vegetative_processing\tmp\new.tif",
    "w",
    driver="GTiff",
    height=7907 // 10,
    width=17694 // 10,
    count=5,
    crs="+proj=latlong",
    dtype=type(img["blue"][0][0]),
)
new_dataset.write(img["blue"], 1)
new_dataset.write(img["green"], 2)
new_dataset.write(img["red"], 3)
new_dataset.write(img["re"], 4)
new_dataset.write(img["nir"], 5)
new_dataset.close()
