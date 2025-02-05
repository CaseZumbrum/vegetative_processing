import rasterio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap
from typing import Callable
from color_map import cmap



def generate_image(raster: np.ndarray, cm: Colormap) -> Image.Image:
    """generate_image converts a raster image into a PIL image

    Args:
        x (np.ndarray): 2D array of values [-1,1], assumed that a vegetative index has already been applied
        cm (Colormap): function that takes in a value [-1,1] and returns a [red, green, blue] rgb value

    Returns:
        Image.Image: PIL image object that corresponds to the raster with the colormap applied
    """
    print(f"min: {np.nanmin(raster)}, max: {np.nanmax(raster)}")

    (x,y) = raster.shape
    image = np.zeros(shape=(x,y,3))
    for index, val  in np.ndenumerate(raster):
        image[index] = cmap(val)

    return Image.fromarray((image[:, :, :3]).astype(np.uint8))

def index_run(image_path: str, index_function: Callable[[np.ndarray, np.ndarray], np.ndarray], color_map: Colormap) -> Image.Image:
    """ runs the vegetative index workflow

    Args:
        image_path (str): valid path on system to GEOtiff orthomosaic
        index_function (Callable[[np.ndarray, np.ndarray], np.ndarray]): index function that will be called on the orthomosaic
        color_map (Colormap): function that takes in a value [-1,1] and returns a [red, green, blue] rgb value

    Returns:
        Image.Image: PIL image object corresponding to the orthomosaic with the colormap applied
    """
    with rasterio.open(image_path) as dataset:
        dataset_crs = dataset.crs
        blue = dataset.read(1)
        green = dataset.read(2)
        red = dataset.read(3)
        re = dataset.read(4)
    red = red.astype('int16')
    green = green.astype('int16')
    v = np.vectorize(index_function)
    return generate_image(v(red, green), color_map)

if __name__ == "__main__":
    from gndvi import GNDVI

    AG_PATH = "C:/Users/AgriBugs/Documents/vegetative_processing/ag_output"
    SAVE_PATH = "temp.png"
    COLOR_MAP = plt.get_cmap("RdYlGn")

    img = index_run(AG_PATH + "/orthomosaic.tif", GNDVI, COLOR_MAP)


    img.save(SAVE_PATH)