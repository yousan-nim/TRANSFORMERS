import argparse
import time
import torch
import dill as pickle

# from utils import read_data, create_fields



def read_data(opt):
    if opt.src_data is not None:
        try:
            opt.src_data = open(opt.src_data).read().strip().split('\n')
            print(opt.src_data )
        except:
            print("error: '" + opt.src_data + "' file not found")
            quit()
    
    if opt.trg_data is not None:
        try:
            opt.trg_data = open(opt.trg_data).read().strip().split('\n')
        except:
            print("error: '" + opt.trg_data + "' file not found")
            quit()

















def main(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument('-src_data', required=True)
    parser.add_argument('-trg_data', required=True)
    parser.add_argument('-src_lang', required=True)
    parser.add_argument('-trg_lang', required=True)
    
    
    opt = parser.parse_args()
    
    
    
    read_data(opt)
#     SRC, TRG = create_fields(opt)
    
    
    
#     print(SRC)
    
    
    

    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    print("finish")
