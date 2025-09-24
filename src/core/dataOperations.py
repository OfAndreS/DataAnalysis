# Em operations.py

import pandas as pd  # type: ignore
import numpy as np   # type: ignore

class Operations:
    def __init__(self, csvPathFile : str, dataFrame : pd.DataFrame):
        self.csvPathFile = csvPathFile
        self.dataFrame = dataFrame
    
    def printColumnsNames(self): 
        print("| Colunas Disponíveis:")
        colunas = self.dataFrame.columns
        for index, nome_coluna in enumerate(colunas):
            print(f"| [ {index + 1} ] - {nome_coluna}")

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