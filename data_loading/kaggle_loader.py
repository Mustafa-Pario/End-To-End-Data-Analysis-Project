# import kaggle

# def download_data():
#     # download dataset from kaggle
#     !kaggle datasets download ankitbansal06/retail-orders -f orders.csv

import os

def download_data():
    print("Starting download...")
    os.system("kaggle datasets download ankitbansal06/retail-orders -f orders.csv")
    print("Download finished!")

