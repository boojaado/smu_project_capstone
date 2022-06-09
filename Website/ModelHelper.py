import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePrediction(self, Returns, Volatility, Node, Date, Sit, INV, DNG, QNG, HHDiffit, Ft, COT):
        Returns = 0
