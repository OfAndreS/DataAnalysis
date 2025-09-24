
# plotGraphics.py

import matplotlib.pyplot as plt # type: ignore
import pandas as pd             # type: ignore
import numpy as np              # type: ignore

class plotPD:

    @staticmethod

    def plotTopObjs(x_data, y_data, x_label: str, y_label: str):

        fig, ax = plt.subplots()
        ax.bar(x_data, y_data)
        ax.grid(True)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        plt.show()