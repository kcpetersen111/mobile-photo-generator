import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image

class theAlgo:
    def __init__(self, img_width=512, img_height=512):
        keras.mixed_precision.set_global_policy("mixed_float16")
        self.model = keras_cv.models.StableDiffusion(img_width, img_height)

    def generate(self, prompt, batch_size=1):
        if prompt is None:
            return 0
        # In case we want to count de time
        start_time = time.time()

        images = self.model.text_to_image(prompt, batch_size)

        for i in range(len(images)):
            Image.fromarray(images[i]).save("%s%s.png" % (prompt, i+1))
        total_time = time.time() - start_time
        print("total_time: ", total_time)

        return 1
