import pandas as pd # type: ignore

class dataProcessing:

    @staticmethod
    def getTopProdutos(myDF : pd.DataFrame, a : str, b : str, num : int):

        return myDF.groupby(a)[b].sum().sort_values(ascending=False).head(num)
    
    @staticmethod
    def generateDataFrameFromCSV(filePath : str):
        return pd.read_csv(filePath)
        