import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense

model = Sequential()

model.add(
    LSTM(
        50,
        return_sequences=True,
        input_shape=(60,1)
    )
)

model.add(LSTM(50))

model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse"
)

model.save("models/lstm.h5")