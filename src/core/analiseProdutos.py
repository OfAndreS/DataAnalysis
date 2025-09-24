import pandas as pd

class aProdutos:

    @staticmethod
    def getTopProdutos(myDF : pd.DataFrame, a : str, b : str, num : int):

        return myDF.groupby(a)[b].sum().sort_values(ascending=False).head(num)
    
    
    @staticmethod
    def myFunc():
        # myDF = generateDataFrame(FILEPATH)
        # myOp = op.Operations(FILEPATH, myDF)
        # myAp = ap.aProdutos()

        # myOp.precoLimpo()
        """
        topTenP = myAp.getTopProdutos(myOp.dataFrame, 'id_produto', 'preco_unitario_limpo', 5)
        topFiveProdutosVolume = myAp.getTopProdutos(myOp.dataFrame, 'id_produto', 'quantidade', 5)
        topFiveDataVenda = myAp.getTopProdutos(myOp.dataFrame, 'data_venda', 'quantidade', 5)
        topFiveClientesFaturamento = myAp.getTopProdutos(myOp.dataFrame, 'id_cliente', 'preco_unitario_limpo', 5)

        x = myOp.dataFrame['data_venda'].sort_values()

        print(myOp.dataFrame)
        print(x)
        """