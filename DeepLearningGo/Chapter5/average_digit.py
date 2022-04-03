import numpy as np
from load_mnist import load_data
from matplotlib import pyplot as plt
from sklearn import preprocessing

def average_digit(data, digit):
    filtered_data = [x[0] for x in data if np.argmax(x[1]) == digit]
    filtered_array = np.asarray(filtered_data)

    return np.average(filtered_array, axis=0)


train, test = load_data()
avg_eight = average_digit(train, 8)

img = (np.reshape(avg_eight, (28, 28)))
plt.imshow(img)
plt.show()

x_3 = preprocessing.normalize(train[2][0])
x_18 = preprocessing.normalize(train[17][0])

W = preprocessing.normalize(np.transpose(avg_eight))

# print(np.dot(W, x_3))
# print(np.dot(W, x_18))


def sigmoid_double(x):
    result = 1.0 / (1.0 + np.exp(-x))
    return result


def sigmoid(z):
    return np.vectorize(sigmoid_double)(z)


def predict(x, W, b):
    return sigmoid_double(np.dot(W, x) + b)


b = -45
predict_3 = predict(x_3, W, b)
predict_18 = predict(x_18, W, b)
# print(predict_3)
# print(predict_18)

def evaluate(data, digit, treshold, W, b):
    total_samples = 1.0 * len(data)
    correct_predictions = 0
    for x in data:
        if predict(x[0], W, b) > treshold and np.argmax(x[1]) == digit:
            correct_predictions += 1
        if predict(x[0], W, b) <= treshold and np.argmax(x[1]) != digit:
            correct_predictions += 1
    return correct_predictions / total_samples

print(evaluate(data=train, digit=8, treshold=0.5, W=W, b=b))
print(evaluate(data=test, digit=8, treshold=0.5, W=W, b=b))

eight_test = [x for x in test if np.argmax(x[1]) == 8]
print(evaluate(data=eight_test, digit=8, treshold=0.5, W=W, b=b))
