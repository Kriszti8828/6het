import numpy as np
from scipy.stats import norm

class browngen:

    def __int__(self):
        pass

    def generate(self, S0, mu, sigma, T, N):
        dt = T / N
        X = np.exp((mu - sigma ** 2 / 2) * dt + sigma * np.random.normal(0, np.sqrt(dt), N))
        return S0 * np.cumprod(X)