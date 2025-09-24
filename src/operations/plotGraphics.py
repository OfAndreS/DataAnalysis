# Em plotGraphics.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class plotPD:

    @staticmethod
    # Correção: Renomeie os parâmetros para maior clareza
    def plotTopObjs(x_data, y_data, x_label: str, y_label: str):

        fig, ax = plt.subplots()
        # Use os novos nomes de parâmetros
        ax.bar(x_data, y_data)
        ax.grid(True)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        # ax.legend() # A legenda não é necessária para um gráfico de barras simples como este
        plt.show()