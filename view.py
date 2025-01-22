import rasterio
from PIL import Image
import numpy as np
import cv2

# NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif
# NFREC_Quincy_DSSAT_10_2_2024_x5_20m_dem.tif
with rasterio.open("NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif") as dataset:
    dataset_crs = dataset.crs
    print(dataset.shape)
    blue = dataset.read(1)
    green = dataset.read(2)
    red = dataset.read(3)

pic = Image.fromarray(red, "L")
pic.show()
