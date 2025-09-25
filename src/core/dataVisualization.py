
# plotGraphics.py

import matplotlib.pyplot as plt # type: ignore

class dataVisualization:

    @staticmethod

    def plotTopObjs(x_data, y_data, x_label: str, y_label: str):

        fig, ax = plt.subplots()
        ax.bar(x_data, y_data)
        ax.grid(True)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        plt.show()