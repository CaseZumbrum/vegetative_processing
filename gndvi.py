import rasterio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif
# NFREC_Quincy_DSSAT_10_2_2024_x5_20m_dem.tif
with rasterio.open("NFREC_Quincy_DSSAT_10_2_2024_Altum_20m.tif") as dataset:
    dataset_crs = dataset.crs
    blue = dataset.read(1)
    green = dataset.read(2)
    red = dataset.read(3)
    re = dataset.read(4)
    nir = dataset.read(5)


cm = plt.get_cmap("RdYlGn")

gndvi = ((nir - green) / (nir + green) + 1) / 2
image = cm(gndvi)
pic = Image.fromarray((image[:, :, :3] * 255).astype(np.uint8))
pic.show()
