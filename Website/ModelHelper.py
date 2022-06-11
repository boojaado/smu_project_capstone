import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePrediction(self, Returns, Volatility, Node, Sit, INV, DNG, QNG, HHDiffit, Ft, COT, cott, icot, idng, dngt):
        
        Node_Midwest = 0
        Node_Mountain = 0
        Node_Pacific = 0
        Node_SouthCentral = 0
        
        Returns = 0
        Volatility = 0
        Sit = 0
        INV = 0
        DNG = 0
        QNG = 0
        HHDiffit = 0
        Ft = 0
        COT = 0
        cott = 0
        icot = 0
        idng = 0
        dngt = 0

        #parse node
        if (Node == 1):
            Node_Midwest = 1
        elif (Node == 3):
            Node_Mountain = 1
        elif (Node == 2):
            Node_Pacific = 1
        elif (Node == 4):
            Node_SouthCentral = 1
        else:
            pass

        input_pred = [[Returns, Volatility, Sit, INV, DNG, QNG, HHDiffit, Ft, COT, cott, icot, idng, dngt, Node_Midwest, Node_Mountain, Node_Pacific, Node_SouthCentral]]

        filename = 'finalized_model.sav'
        model_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = model_load.predict_proba(X)
        preds_singular = model_load.predict(X)

        return preds_singular[0]


