import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image
import uuid
import os

remoteImageURL = os.environ['remoteImageURL']
imageSaveLocation = os.environ['imageSaveLocation']

class theAlgo:
    def __init__(self, img_width=512, img_height=512+128):
        keras.mixed_precision.set_global_policy("mixed_float16")
        self.model = keras_cv.models.StableDiffusion(img_width, img_height)

    def generate(self, prompt):
        if prompt is None:
            return 0

        start_time = time.time()

        images = self.model.text_to_image(prompt, batch_size=1)

        name = "".join(prompt.split(" ")) + str(uuid.uuid4())
        img_location = "%s%s.png" % (imageSaveLocation, name)

        Image.fromarray(images[0]).save(img_location)

        new_img_location = "%s%s.png" % (remoteImageURL, name)

        total_time = time.time() - start_time
        print("total_time: ", total_time)

        return new_img_location
