import numpy as np
import matplotlib.pyplot as plt

class FuncionTrigonometrica:
    def __init__(self, tipo, amplitud=1, periodo=2*np.pi):
        self.tipo = tipo.lower()
        self.amplitud = amplitud
        self.periodo = periodo
        self._validar_tipo()

    def _validar_tipo(self):
        if self.tipo not in ['seno', 'coseno', 'tangente']:
            raise ValueError("Tipo debe ser 'seno', 'coseno' o 'tangente'.")

    def evaluar(self, x):
        omega = 2 * np.pi / self.periodo
        if self.tipo == 'seno':
            return self.amplitud * np.sin(omega * x)
        elif self.tipo == 'coseno':
            return self.amplitud * np.cos(omega * x)
        elif self.tipo == 'tangente':
            return self.amplitud * np.tan(omega * x)

    def graficar(self, x_min=-2*np.pi, x_max=2*np.pi, puntos=1000):
        x = np.linspace(x_min, x_max, puntos)
        y = self.evaluar(x)

        plt.figure(figsize=(10, 4))
        plt.plot(x, y, label=str(self))
        plt.title(f'Gráfica de {self.tipo.capitalize()} con A={self.amplitud}, T={self.periodo}')
        plt.xlabel('x (radianes)')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.legend()

        if self.tipo != 'tangente':
            plt.ylim(-1.5 * self.amplitud, 1.5 * self.amplitud)

        plt.show()

    def __str__(self):
        omega = 2 * np.pi / self.periodo
        return f"{self.amplitud}·{self.tipo}({omega:.2f}·x)"

    def valor_critico(self):
        if self.tipo in ['seno', 'coseno']:
            return self.amplitud, -self.amplitud
        elif self.tipo == 'tangente':
            return None