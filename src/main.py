import pandas as pd    # type: ignore
import numpy as np     # type: ignore

from core import dataProcessing as dtPr
from core import dataOperations as dtOp
from core import dataVisualization as dtVi

from utility import consoleUI as ui

FILEPATH = '../Data/AllSells.csv'

def printHead():
    print("\n\n|  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n")


def generateDataFrame(filePath : str):

    return pd.read_csv(filePath)

def startMenu(dataFrame : pd.DataFrame):
    printHead()

    myOp = dtOp.Operations(FILEPATH, dataFrame)
    myAp = dtPr.aProdutos()

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
                dtVi.plotPD.plotTopObjs(xAxisLabel, yAxisLabel, "Produto", "Quantidade")
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
    







    
