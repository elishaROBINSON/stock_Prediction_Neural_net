

from os import listdir
from os.path import dirname, join, splitext

data_dir = join(dirname(__file__), "daily")
tickers = listdir(data_dir)
tickers = [splitext(x)[0].split("table_")[-1] for x in tickers]
f=open("new.txt","w")
for i in tickers :
	f.write(i.upper()+"\",\"")