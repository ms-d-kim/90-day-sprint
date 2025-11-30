import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


class PIDController:
    def __init__(self, Kp: float, Ki: float, Kd: float, dt: float, integral_limit: Optional[float] = None):
        """
        Simple PID Controller.

        Kp: proportional gain
        Ki: integral gain
        Kd: derivative gain
        dt: time step (seconds)
        integral_limit: clamp for integral term to avoid 'windup'
        """
        # store parameters
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.integral_limit = integral_limit

        # internal state
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        """Reset internal state (integral + previous error)."""
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, setpoint: float, measurement: float) -> float:
        """
        Compute the PID control signal for the current measurement.
        """
        # error between target and current value
        error = setpoint - measurement

        # proportional term
        P = self.Kp * error

        # integral term (accumulate error over time)
        self.integral += error * self.dt

        # clamp integral to avoid windup
        if self.integral_limit is not None:
            self.integral = max(
                -self.integral_limit,
                min(self.integral, self.integral_limit)
            )

        I = self.Ki * self.integral

        # derivative term (rate of change of error)
        derivative = (error - self.prev_error) / self.dt
        D = self.Kd * derivative

        # save current error for next step
        self.prev_error = error

        # total control signal
        u = P + I + D
        return u


def simulate_pid(
    Kp: float,
    Ki: float,
    Kd: float,
    total_time: float = 5.0,
    dt: float = 0.01,
    setpoint: float = 1.0,
    mass: float = 1.0,
    friction: float = 0.2,
):
    """
    Simulate a 1D point mass controlled by a PID controller.
    """

    controller = PIDController(
        Kp=Kp,
        Ki=Ki,
        Kd=Kd,
        dt=dt,
        integral_limit=10.0,
    )

    num_steps = int(total_time / dt)

    # state: position x, velocity v
    x = 0.0
    v = 0.0

    time_history = np.zeros(num_steps)
    x_history = np.zeros(num_steps)
    v_history = np.zeros(num_steps)
    u_history = np.zeros(num_steps)

    for i in range(num_steps):
        t = i * dt

        # control signal from PID
        u = controller.compute(setpoint=setpoint, measurement=x)

        # physics: F = u - friction * v, a = F / m
        a = (u - friction * v) / mass

        # integrate acceleration -> velocity -> position
        v = v + a * dt
        x = x + v * dt

        time_history[i] = t
        x_history[i] = x
        v_history[i] = v
        u_history[i] = u

    return time_history, x_history, v_history, u_history


def main():
    total_time = 5.0
    dt = 0.01
    setpoint = 1.0

    # PID gains
    Kp = 4.0
    Ki = 0.0
    Kd = 0.0

    t, x, v, u = simulate_pid(
        Kp=Kp,
        Ki=Ki,
        Kd=Kd,
        total_time=total_time,
        dt=dt,
        setpoint=setpoint,
        mass=1.0,
        friction=0.4,
    )

    # position vs time
    plt.figure()
    plt.plot(t, x, label="position x(t)")
    plt.axhline(setpoint, linestyle="--", label="setpoint")
    plt.xlabel("Time (s)")
    plt.ylabel("Position")
    plt.title(f"PID Response (Kp={Kp}, Ki={Ki}, Kd={Kd})")
    plt.legend()
    plt.grid(True)

    # control signal vs time
    plt.figure()
    plt.plot(t, u, label="control u(t)")
    plt.xlabel("Time (s)")
    plt.ylabel("Control Signal")
    plt.title("Control Signal Over Time")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()