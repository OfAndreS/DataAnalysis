import pandas as pd
import numpy as np

from core import analiseProdutos as ap
from operations import operations as op
from operations import plotGraphics as pg

FILEPATH = '../Data/AllSells.csv'

def printHead():
    print("\n\n|  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n")


def generateDataFrame(filePath : str):

    return pd.read_csv(filePath)

def startMenu(dataFrame : pd.DataFrame):
    printHead()

    myOp = op.Operations(FILEPATH, dataFrame)
    myAp = ap.aProdutos()

    while(True):

        printHead()
        print("| ( 1 ) - Plotar um Gráfico: ")
        print("| ( 2 ) - Lista Opção de plotagem: ")
        print("| ( 0 ) - Terminar Execução")

        userInput = str(input("| Escolha: "))
        match userInput:
            case '1':
                topFiveProdutosVolume = myAp.getTopProdutos(myOp.dataFrame, 'id_produto', 'quantidade', 5)
                topFiveProdutosVolume.sort_values(inplace=True)
                xAxisLabel = topFiveProdutosVolume.index.astype(str)
                yAxisLabel = topFiveProdutosVolume.values
                pg.plotPD.plotTopObjs(xAxisLabel, yAxisLabel, "Produto", "Quantidade")
            case '2':
                myOp.printColumnsNames()
            case '0':
                printHead()
                print("| Terminando...")
                printHead()
                return
            case _:
                print("| Opção Inválida ")

        printHead()

if __name__ == "__main__":
    myDF = generateDataFrame(FILEPATH)
    startMenu(myDF)
    print(np.array(myDF.columns))







    
