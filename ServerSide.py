from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np

with open("Model/model.json") as json_file:
    model = model_from_json(json_file.read())
    model.load_weights("Model/weight.h5")

img_width, img_height = 150, 150

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

img = image.load_img(
    "/home/ps/chest_xray/chest_xray/test/PNEUMONIA/person1616_virus_2802.jpeg",
                target_size = (img_width, img_height))

x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)

images = np.vstack([x])
classes = model.predict_classes(images, batch_size = 1)

print(classes)
