
# plotGraphics.py

import matplotlib.pyplot as plt # type: ignore

class dataVisualization:

    @staticmethod
    def plotTopObjs(x_data, y_data, x_label: str, y_label: str):

        fig, ax = plt.subplots()
        ax.bar(x_data, y_data)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.grid(True)
        plt.show()
    
    @staticmethod
    def plotLineObjs(x_data, y_data, x_label: str, y_label: str):
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.grid(True)
        plt.show()