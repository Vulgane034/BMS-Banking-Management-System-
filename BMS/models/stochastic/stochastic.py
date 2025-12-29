import numpy as np

def simulate_gbm(S0, mu, sigma, n_steps):
    dt = 1
    S = [S0]
    for _ in range(n_steps-1):
        S.append(S[-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.random.normal() * np.sqrt(dt)))
    return np.array(S)

def simulate_ou(x0, mu, theta, sigma, n_steps):
    dt = 1
    x = [x0]
    for _ in range(n_steps-1):
        x.append(x[-1] + theta * (mu - x[-1]) * dt + sigma * np.random.normal() * np.sqrt(dt))
    return np.array(x)