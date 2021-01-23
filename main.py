from vpython import *
import time
import random
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


theta = 0
thetadot = 0
l = 0.2
g = 9.8
A = 0.05
omega = 5
t = 0
dt = 0.001


# fx = gcurve(color=color.blue)


def function1(time):
    num = 0.0
    thet = 0
    thetdot = 0
    delt = 0.001
    while num < time:
        thetddot = -(g / l) * sin(thet) + (A / l) * omega ** 2 * cos(omega * num) * cos(thet)
        thetdot = thetdot + thetddot * delt
        thet = thet + thetdot * delt
        num = num + delt
    return thet


def pendulum_function2(time):
    num = 0.0
    thet = 0
    delt = 0.001
    thetddot = 0
    while num < time:
        thetddot = -(g / l) * sin(thet) + (A / l) * omega ** 2 * cos(omega * num) * cos(thet)
        num = num + delt
    return thetddot


def pendulum_loss(y_true, y_pred):
    inp1 = y_true
    inp2 = y_pred
    return (pendulum_function2(inp1) - pendulum_function2(inp2)) ** 2


x = []
y = []

for i in range(1000):
    ra = random.uniform(0, 5)
    x.append(ra)
    y.append(function1(ra))

x = np.array(x)
y = np.array(y)

np.reshape(x, (-1, 4))

tf.keras.backend.set_floatx('float64')

model = keras.Sequential([
    keras.layers.Dense(1, activation='linear'),
    keras.layers.Dense(12, activation='linear'),
    keras.layers.Dense(12, activation='linear'),
    keras.layers.Dense(12, activation='linear'),
    keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer='adam',
              loss='mean_absolute_percentage_error',
              metrics='mean_absolute_percentage_error',)

model.fit(x, y, epochs=10, batch_size=1)


model.save('first_model')
new_model = tf.keras.models.load_model('first_model')

prediction = model.predict([[0.21793312599435977, 0.019836378356533985, 21.45892175603604, 0.4829995271006352]])
print(prediction)


jiggle = box(pos=vector(A * cos(omega * t), 0.1, 0), size=vector(0.03, 0.02, 0.02))
mass = sphere(pos=jiggle.pos + vector(l * sin(theta), -l * cos(theta), 0), radius=0.01, color=color.yellow,
              make_trail=True)
stick = cylinder(pos=jiggle.pos, axis=mass.pos - jiggle.pos, radius=0.002)
start = time.time()
while t < 5:
    rate(1000)
    thetaddot = -(g / l) * sin(theta) + (A / l) * omega ** 2 * cos(omega * t) * cos(theta)
    thetadot = thetadot + thetaddot * dt
    theta = theta + thetadot * dt
    t = t + dt
    jiggle.pos = vector(A * cos(omega * t), 0.1, 0)
    mass.pos = jiggle.pos + vector(l * sin(theta), -l * cos(theta), 0)
    stick.pos = jiggle.pos
    stick.axis = mass.pos - jiggle.pos


stop = time.time()
print(stop - start)
