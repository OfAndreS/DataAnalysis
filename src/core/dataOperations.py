# Em operations.py

import pandas as pd  # type: ignore
import numpy as np   # type: ignore

from core import dataProcessing as dtPr
from core import dataVisualization as dtVi
class dataOperations:
    
    def __init__(self, csvPathFile : str, dataFrame : pd.DataFrame):
        self.csvPathFile = csvPathFile
        self.dataFrame = dataFrame
    
    def precoLimpo(self):
        precoLimpoStr = (
            self.dataFrame['preco_unitario'].astype(str)
            .str.replace('$', '', regex=False) 
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
        self.dataFrame['preco_unitario_limpo'] = precoLimpoStr
        self.dataFrame['preco_unitario_limpo'] = self.dataFrame['preco_unitario_limpo'].astype(float)

        return self.dataFrame
    
    def printColumnsNames(self, removeItem : str = None): 
        
        print("| Colunas Disponíveis:\n|")
        
        colunas = self.dataFrame.columns
        colunas = np.array(colunas.astype(str))
        
        if (removeItem != None):
            indexToRemove = np.where(colunas == removeItem)
            colunas = np.delete(colunas, indexToRemove)
        
        for index, nome_coluna in enumerate(colunas):
            finalIndex = index + 1
            print(f"| [ {finalIndex} ] - {nome_coluna}")
            
        return len(colunas)

    def selectColumns(self, removeItem : str = None):
        
        finalIndex = self.printColumnsNames(removeItem) 
        
        colunasIndex = self.dataFrame.columns
        colunasIndex = np.array(colunasIndex.astype(str))
        
        if (removeItem != None):
            indexToRemove = np.where(colunasIndex == removeItem)
            colunasIndex = np.delete(colunasIndex, indexToRemove)
        
        while(True):
            try:
                userInput = int(input("| Escolha: "))
                
                if (userInput <= 0 or userInput > finalIndex):
                    print("| Escolha um número válido! ")
                else:
                    break
            
            except ValueError: 
                print("| Opção Inválida! Digite um número. ")
                
        return colunasIndex[userInput - 1]
    
    def createCustomGrupby(self):
        
        mydtPr = dtPr.dataProcessing()
        mydtVi = dtVi.dataVisualization()
        
        print("| SELECIONAR ÍNDICE PARA PLOTAGEM: \n")
        xAxis = self.selectColumns()
        
        print("\n| SELECIONAR OS VALORES PARA PLOTAGEM: \n")
        yAxis = self.selectColumns(xAxis)
        
        print(f"\n| Seleção: Agrupar por '{xAxis}' e analisar '{yAxis}'")
        mySeriesGrupBy = mydtPr.getTopProdutos(self.dataFrame, xAxis, yAxis, 5)
        
        print(mySeriesGrupBy)
        
        x = mySeriesGrupBy.astype(str).sort_index()
        
        mydtVi.plotTopObjs(x, mySeriesGrupBy.values, 'a', 'b')
        
        