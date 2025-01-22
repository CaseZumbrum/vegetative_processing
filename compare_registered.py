from PIL import Image
import numpy as np

def f(y,x):
    try:
        if(np.all(x == 0)):
            return y
        else:
            return (np.int16((x[0]) + np.int16(y[0]))/2,(np.int16(x[1]) + np.int16(y[1]))/2,(np.int16(x[2]) + np.int16(y[2]))/2)
    except RuntimeWarning as w:
        print(x,y,w)
        return y


ref = np.array(Image.open("prop_images/ref.png"))
print("loaded first image")
registered = np.array(Image.open("prop_images/output.jpg"))
print("loaded second image")
output = np.zeros(ref.shape)
     
    
count = 0
for i in range(ref.shape[0]):
    count +=1
    for j in range(ref.shape[1]):
        output[i,j] = f(ref[i,j,:], registered[i,j,:])
        
Image.fromarray(output.astype(np.uint8)).save("test.png")



