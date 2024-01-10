import csv

import json

import pandas as pd

from pandas.io.json import json_normalize

def json_csv():

  with open('한국어 대화 요약/Training/[라벨]한국어대화요약_train/개인및관계.json') as data_file:
    data=json.load(data_file)
    df = json_normalize(data['data'])
    df.to_csv('개인및관계.csv',index=False)

  return

def main(): 
  json_csv() 

main()