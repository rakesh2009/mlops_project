import pandas as pd
import argparse
import os
import get_data as gt
from sklearn.model_selection import train_test_split

def split_and_saved_data(config_path):
    config=gt.read_param(config_path)
    train_data_path=config['split_data']['train_path']
    test_data_path = config['split_data']['test_path']
    raw_data_path = config['load_data']['raw_dataset_csv']
    random_state=config['base']['random_state']
    split_ratio=config['split_data']['test_size']
    df=pd.read_csv(raw_data_path,sep=',')
    train,test=train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,sep=',')
    test.to_csv(test_data_path,sep=',')

if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed_args=arg.parse_args()
    split_and_saved_data(config_path=parsed_args.config)
