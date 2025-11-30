# Day 1 — PID Controller Simulation (Robotics Control Fundamentals)

This project implements a PID (Proportional–Integral–Derivative) controller and uses it to control a simulated 1D point mass with friction. It is the first entry in a series of daily projects designed to build strong intuition for robotics, real-time systems, and AI infrastructure.

---

## Project Overview

This project contains:

- **A reusable PID controller class**
- **A physics simulation of a 1D point mass**
- **Plots showing closed-loop stability and controller behavior**

PID control is one of the most widely used techniques in robotics, mechanical systems, motor control, drone stabilization, and even thermal or load control in datacenters. Understanding PID behavior is foundational to everything in robotics and real-time AI systems.

---

## What This Project Demonstrates

### **1. Closed-loop control**
The PID controller observes the error between the target position and the current position and continuously corrects it.

### **2. System dynamics**
Physics (acceleration → velocity → position) is updated using Euler integration.

### **3. Controller behavior**
Different PID gains produce different system dynamics:
- **P**: fast response, but steady-state error  
- **PI**: removes bias, but can oscillate  
- **PD**: adds damping and reduces overshoot  
- **PID**: practical balance of speed + stability

---

## File Structure

```
day1-pid-controller/
├── pid_sim.py               # Main code: PID + physics simulation + plots
├── README.md                # Documentation
├── requirements.txt         # Dependencies for reproducibility
└── .gitignore               # Excludes venv, cache, and system files
```

---

## How to Run

```bash
# (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
python3 pid_sim.py
```

You should see:

- A **position vs time plot**, showing the mass approaching the setpoint  
- A **control signal plot**, showing how PID stabilizes the system  

---

## Example Behavior (Optional)

If you saved the plots as images:

```
pid_position.png
pid_control.png
```

You can embed them here later.

---

## Lessons Learned

- PID is the simplest and most widely used closed-loop controller in robotics  
- Integral windup must be clamped to avoid instability  
- Derivative smooths motion and reduces overshoot  
- Small changes in gains dramatically change response characteristics  
- Simulations like this build intuition before touching real robots or RL policies  

---

## What's Next (Day 2)

The next daily project explores:

- Building a tiny neural network **from scratch** (no PyTorch)  
- Understanding the forward pass and backpropagation  
- Training it on a simple task (XOR) to understand nonlinearity  

This daily series will gradually build toward reinforcement learning, robotics control, simulation, and AI infrastructure.
