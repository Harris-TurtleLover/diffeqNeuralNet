# diffeqNuralNet


## What is this?
This is a project that uses a TensorFLow neural network to solve a differential equation.

## What is it predicting?
It is a physical system of a pendulum where the pivot point of the pendulum is occilating to the left and right following a cosine function.
![The System](https://imgur.com/a/M5x0Kcp)
The equation of motion of the angle theta was found by using the Euler–Lagrange equation.
## How was the network trained?
Solutions to the equation was estimeted with Euler's method of intergration. Initial conditions were randomized and data points for theta were obtained incrementing time by 0.001 and each scenario went for 1000 total time steps. The initial conditions were inserted into the starting nodes and the network tries to minimize the custom loss function.
## What is the custom loss function?
It is the magnitude of the difference between the actual theta minus the predicted theta all squared. As this loss function approaches zero the nural network becomes more accurate.

# Resonance
In interesting situation of this system is if the pivot point is occilating at a frequency equal to that of the pendulum the occilator will continously add energy to the pendulum causing it to go higher and higher until the frequency of the pendulum deviates from the small angle approximation of frequency (sqrt(g/L)). 
![resonance](https://imgur.com/V7oLyv3)
