import requests
import numpy as np
from tensorflow import keras

# Charger MNIST
(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()

# Prendre la première image du jeu de test
image = x_test[0].reshape(784).astype("float32").tolist()
label = y_test[0]

# Envoi à l'API
url = "http://127.0.0.1:5000/predict"
response = requests.post(url, json={"image": image})

print("Label attendu :", label)
print("Réponse API :", response.json())
