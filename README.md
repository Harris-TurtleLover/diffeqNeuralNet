# diffeqNeuralNet


## What is this?
This is a project that uses a TensorFLow neural network to solve a differential equation.

## What is it predicting?
It is a physical system of a pendulum where the pivot point of the pendulum is oscillating to the left and right following a cosine function.

<a href="https://i.imgur.com/2OjknMh.gif"><img src="https://i.imgur.com/2OjknMh.gif" title="The System"/></a>

The equation of motion of the angle theta was found by using the Euler–Lagrange equation.

<a href="https://i.imgur.com/sz7ewp1.png"><img src="https://i.imgur.com/sz7ewp1.png" title="The Equation"/></a>

Omega is the frequency of the oscillator, A is the oscillators amplitude, and L is the length of the pendulum 
## How the network was trained
Solutions to the equation was estimeted with Euler's method of intergration. Initial conditions were randomized and data points for theta were obtained incrementing time by 0.001 and each scenario went for 1000 total time steps. The initial conditions were inserted into the starting nodes and the network tries to minimize the custom loss function.
## What is the custom loss function?
It is the magnitude of the difference between the actual theta minus the predicted theta all squared. As this loss function approaches zero the nural network becomes more accurate.

### Resonance
An interesting aspect of this system is if the pivot point is oscillating at a frequency equal to that of the pendulum the oscillator will continously add energy to the pendulum causing it to go higher and higher until the frequency of the pendulum deviates from the small angle approximation of frequency (sqrt(g/L)). 

<a href="https://i.imgur.com/V7oLyv3.gif"><img src="https://i.imgur.com/V7oLyv3.gif" title="Resonance"/></a>
