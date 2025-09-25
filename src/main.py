import pandas as pd    # type: ignore
import numpy as np     # type: ignore

from core import dataProcessing as dtPr
from core import dataOperations as dtOp
from core import dataVisualization as dtVi

from utility import consoleUI as ui

# Implementar o seletor de arquivos
FILEPATH = '../Data/AllSells.csv'


def startMenu():

    mydtPr = dtPr.dataProcessing()
    mydtOp = dtOp.dataOperations(FILEPATH, mydtPr.generateDataFrameFromCSV(FILEPATH))
    mydtOp.precoLimpo()

    ui.printLogo()

    while(True):

        ui.printStartMenu()

        userInput = str(input("| Escolha: "))
        match userInput:
            case '1':
                ui.printHead()
                mydtOp.createCustomGrupby()
                
            case '2':
                ui.printHead()
                mydtOp.printColumnsNames()
                
            case '0':
                ui.printExit()
                return
            
            case _:
                print("| Opção Inválida! ")

if __name__ == "__main__":
    startMenu()