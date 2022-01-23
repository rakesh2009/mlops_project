import pandas as pd
import yaml
import argparse

def read_param(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config=read_param(config_path)
    data_src=config['data_source']['s3_source']
    df=pd.read_csv(data_src,sep=',')
    return df

if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed_arg=arg.parse_args()
    get_data(config_path=parsed_arg.config)


