from __future__ import absolute_import
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Conv2D, ZeroPadding2D



def layers(input_shape):
    return [
        ZeroPadding2D((3, 3), input_shape=input_shape),
        Conv2D(64, (7, 7), padding='valid'),
        Activation('relu'),

        ZeroPadding2D((2, 2)),
        Conv2D(64, (5, 5)),
        Activation('relu'),

        ZeroPadding2D((2, 2)  ),
        Conv2D(64, (5, 5)  ),
        Activation('relu'),

        ZeroPadding2D((2, 2)  ),
        Conv2D(48, (5, 5)  ),
        Activation('relu'),

        ZeroPadding2D((2, 2) ),
        Conv2D(48, (5, 5)),
        Activation('relu'),

        ZeroPadding2D((2, 2)  ),
        Conv2D(32, (5, 5)  ),
        Activation('relu'),

        ZeroPadding2D((2, 2)  ),
        Conv2D(32, (5, 5)  ),
        Activation('relu'),

        Flatten(),
        Dense(1024),
        Activation('relu'),
    ]
