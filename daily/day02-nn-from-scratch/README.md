# Day 2 — Neural Network From Scratch (XOR)

This project implements a tiny neural network **entirely from scratch using NumPy**, without relying on PyTorch, JAX, or any autograd framework. The goal is to build intuition for how forward passes, nonlinear activation functions, loss computation, backpropagation, and gradient-based weight updates actually work.

It is the second entry in a long‑term daily project series aimed at building deep intuition for machine learning, AI infrastructure, and systems engineering.

---

## Project Overview

This project contains:

- A fully manual implementation of a **2 → 4 → 1 multilayer perceptron**
- A **forward pass** (linear → ReLU → linear → sigmoid)
- A **binary cross‑entropy loss function**
- A **manual backpropagation routine** using the chain rule
- A **training loop** that updates weights and biases using gradient descent
- A visualization of the **loss curve during training**

The model is trained to learn the XOR function, a classic example of a problem that cannot be solved with a linear model and requires nonlinearity.

---

## Architecture

The network structure:

```
Input (2 dims)
   ↓
Linear layer (2 → 4)
   ↓
ReLU activation
   ↓
Linear layer (4 → 1)
   ↓
Sigmoid activation
```

- **Hidden layer:** 4 neurons, ReLU
- **Output layer:** 1 neuron, sigmoid
- **Loss:** Binary cross entropy (BCE)
- **Training:** 5000 steps of gradient descent with learning rate 0.1

---

## What Each Part of the Code Does

- **`__init__`**  
  Initializes all weights and biases.  
  - `W1`, `b1`: input → hidden  
  - `W2`, `b2`: hidden → output  
  All weights are randomly initialized; biases start at zero.

- **`forward`**  
  Computes predictions by performing:
  - matrix multiplications  
  - adding biases  
  - applying ReLU and sigmoid nonlinearities  

- **`backward`**  
  Manually computes gradients of the loss w.r.t. weights and biases using the chain rule:
  - propagates error from output → hidden → input  
  - computes gradients for `W1`, `b1`, `W2`, `b2`  
  - performs parameter updates using gradient descent  

- **`train`**  
  Repeats forward → loss → backward → update for 5000 iterations while logging the loss.

- **Main block**  
  Defines the XOR dataset, trains the model, plots the loss curve, and prints final predictions.

---

## Insights I Learned

- Neural networks are ultimately just matrix multiplications with nonlinearities layered between them.
- Backpropagation is not magic; it is the chain rule applied consistently across layers.
- ReLU is essential — without nonlinearity, XOR cannot be solved.
- The loss curve reflects whether gradients are flowing correctly.
- Weight updates are literally small numerical nudges applied thousands of times.
- This tiny MLP operates on exactly the same principles as modern LLMs—just scaled down by billions of parameters.

---

## ▶How to Run

```bash
pip install -r requirements.txt
python3 nn_from_scratch.py
```

This will generate `loss_curve.png` and print the model’s predictions on the XOR dataset.

---

## Example Output

Final predictions (approximate):

```
[[0.006]
 [0.999]
 [0.999]
 [0.006]]
```

This corresponds to the correct XOR mapping.

---