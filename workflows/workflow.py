import matplotlib.pyplot as plt
from agisoft_workflow import agisoft_run
from index_workflow import index_run
from gndvi import GNDVI

IMAGES_PATH = "C:/Users/AgriBugs/Documents/vegetative_processing/prop_images/x5-20241122T175142Z/x5"
AG_PATH = "C:/Users/AgriBugs/Documents/vegetative_processing/ag_output"
SAVE_PATH = "temp.png"
COLOR_MAP = plt.get_cmap("RdYlGn")

agisoft_run(IMAGES_PATH, AG_PATH)

img = index_run(AG_PATH + "/orthomosaic.tif", GNDVI, COLOR_MAP)


img.save(SAVE_PATH)