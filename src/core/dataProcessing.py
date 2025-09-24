import pandas as pd # type: ignore

class aProdutos:

    @staticmethod
    def getTopProdutos(myDF : pd.DataFrame, a : str, b : str, num : int):

        return myDF.groupby(a)[b].sum().sort_values(ascending=False).head(num)
    
    