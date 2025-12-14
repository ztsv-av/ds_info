import numpy as np

# GD

class GradientDescent:
    def __init__(self, lr=1e-2):
        self.lr = float(lr)

    def step(self, params, grads):
        for p, g in zip(params, grads):
            p -= self.lr * g

# Adam

class Adam:
    def __init__(self, lr=1e-3, betas=(0.9, 0.999), eps=1e-8):
        self.lr = float(lr)
        self.beta1 = float(betas[0])
        self.beta2 = float(betas[1])
        self.eps = float(eps)

        self.t = 0
        self.m = None
        self.v = None

    def _init_state(self, params):
        self.m = [np.zeros_like(p) for p in params]
        self.v = [np.zeros_like(p) for p in params]

    def step(self, params, grads):
        if self.m is None:
            self._init_state(params)

        self.t += 1
        b1, b2 = self.beta1, self.beta2

        for i, (p, g) in enumerate(zip(params, grads)):
            self.m[i] = b1 * self.m[i] + (1.0 - b1) * g
            self.v[i] = b2 * self.v[i] + (1.0 - b2) * (g * g)

            m_hat = self.m[i] / (1.0 - (b1 ** self.t))
            v_hat = self.v[i] / (1.0 - (b2 ** self.t))

            p -= self.lr * m_hat / (np.sqrt(v_hat) + self.eps)


class Adam:
    def __init__(self, lr=1e-3, beta_1=0.9, beta_2=0.999, eps=1e-8):
        self.lr = float(lr)
        self.beta_1 = float(beta_1)
        self.beta_2 = float(beta_2)
        self.eps = float(eps)
        self.t = 0
        self.m = None
        self.v = None
    
    def _init_state(self, params):
        self.m = [np.zeros_like(p) for p in params]
        self.v = [np.zeros_like(p) for p in params]
    
    def step(self, params, grads):
        if self.m == None:
            self._init_state(params)
        
        self.t += 1

        for i, (p, g) in enumerate(zip(params, grads)):
            self.m[i] = self.beta_1 * self.m[i] + (1.0 - self.beta_1) * g
            self.v[i] = self.beta_2 * self.v[i] + (1.0 - self.beta_2) * (g * g)

            m_hat = self.m[i]/(1.0 - self.beta_1**self.t)
            v_hat = self.v[i]/(1.0 - self.beta_2**self.t)

            p -= self.lr * m_hat/(np.sqrt(v_hat) + self.eps)

# AdamW

class AdamW:
    def __init__(self, lr=1e-3, beta_1=0.9, beta_2=0.999, eps=1e-8, weight_decay=1e-2):
        self.lr = float(lr)
        self.beta_1 = float(beta_1)
        self.beta_2 = float(beta_2)
        self.eps = float(eps)
        self.weight_decay = weight_decay
        self.t = 0
        self.m = None
        self.v = None
    
    def _init_state(self, params):
        self.m = [np.zeros_like(p) for p in params]
        self.v = [np.zeros_like(p) for p in params]
    
    def step(self, params, grads):
        if self.m == None:
            self._init_state(params)
        
        self.t += 1

        for i, (p, g) in enumerate(zip(params, grads)):
            if self.weight_decay != 0.0:
                p -= self.lr * self.weight_decay * p

            self.m[i] = self.beta_1 * self.m[i] + (1.0 - self.beta_1) * g
            self.v[i] = self.beta_2 * self.v[i] + (1.0 - self.beta_2) * (g * g)

            m_hat = self.m[i]/(1.0 - self.beta_1**self.t)
            v_hat = self.v[i]/(1.0 - self.beta_2**self.t)

            p -= self.lr * m_hat/(np.sqrt(v_hat) + self.eps)
