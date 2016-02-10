from os.path import dirname, join, splitext
from pybrain.datasets import SequentialDataSet
from itertools import cycle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import LSTMLayer
from pybrain.supervised import RPropMinusTrainer
from sys import stdout
import matplotlib.pyplot as plt
import numpy as np
import time as tm
from numba import jit
import random
from pybrain.supervised import BackpropTrainer
import pandas as pd
import os
pwd= os.popen("pwd").read().replace("\n","") 
@jit
def getdata(ticker1):
    data_dir = pwd+ "/daily"
    fname = join(data_dir, "table_%s.csv" % ticker1.lower())
    a=open(fname,'r')
    b=a.read().split()
    for i in b :
            x=i.split(',')
            data.append(float(x[2])) 
    return data

@jit
def train(data,name):
    ds = SequentialDataSet(1, 1)
    for sample, next_sample in zip(data, cycle(data[1:])):
        ds.addSample(sample, next_sample)
    net = buildNetwork(1, 200, 1, hiddenclass=LSTMLayer, outputbias=False, recurrent=True)

    trainer = RPropMinusTrainer(net, dataset=ds)
    train_errors = [] # save errors for plotting later
    EPOCHS_PER_CYCLE = 5
    CYCLES = 20
    EPOCHS = EPOCHS_PER_CYCLE * CYCLES
    store=[]
    for i in xrange(CYCLES):
        trainer.trainEpochs(EPOCHS_PER_CYCLE)
        train_errors.append(trainer.testOnData())
        epoch = (i+1) * EPOCHS_PER_CYCLE
        print("\r epoch {}/{}".format(epoch, EPOCHS))
        print tm.time()-atm
        stdout.flush() 
    for sample, target in ds.getSequenceIterator(0):
        store.append(net.activate(sample))
    abcd=pd.DataFrame(store)
    abcd.to_csv(pwd+"lstmdata/"+name+".csv",encoding='utf-8')
    print "result printed to file"
#
#plese download and add more names to the list also modify the list of the stock displayed in the stock_app.py
#
stock_dat=[ 'ECL', 'EW', 'FLS', 'GPC', 'HOG', 'INTU', 'JWN', 'LLL', 'MAS', 'MON', 'NEE', 'NYX', 'PEG', 'PPG', 'RHT', 'SJM', 'SWN', 'TMO', 'USB', 'WFM', 'XOM']

atm=tm.time()
data=[]

for i in stock_dat:
    data=getdata(i)
    print tm.time()-atm
    train(data,i)
    print tm.time()-atm