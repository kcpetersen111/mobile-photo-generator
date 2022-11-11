import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image

start_time = time.time()

keras.mixed_precision.set_global_policy("mixed_float16")
model = keras_cv.models.StableDiffusion()

while True:
    prompt = input("")

    if prompt is None:
        continue

    batch_size = 1

    start_time = time.time()

    images = model.text_to_image(name, batch_size)

    print("It took : %s seconds to run"% (time.time() - start_time))
