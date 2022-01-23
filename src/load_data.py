import argparse
import pandas as pd
import get_data as gt

def load_and_save(config_path):
    df=gt.get_data(config_path)
    new_cols=[col.replace(' ','_') for col in df.columns]
    config=gt.read_param(config_path)
    des_path=config['load_data']['raw_dataset_csv']
    df.to_csv(des_path,sep=',',index=False,header=new_cols)

if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed_arg=arg.parse_args()
    load_and_save(config_path=parsed_arg.config)