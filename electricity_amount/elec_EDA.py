import numpy as np
import pandas as pd
import pandas_profiling

# EDA
import matplotlib.pyplot as plt
import seaborn as sns

# Learning algorithms
import sklearn
from sklearn.linear_model import *
from sklearn.cluster import KMeans

# model validation
from sklearn.model_selection import KFold

import warnings
import os
print(os.getcwd())  # 현재 디렉토리 확인
warnings.filterwarnings('ignore')

# 데이터 불러오기
train_df = pd.read_csv('electricity_amount/energy/train.csv', encoding='cp949')
test_df = pd.read_csv('electricity_amount/energy/test.csv', encoding='cp949')
sub = pd.read_csv('electricity_amount/energy/sample_submission.csv', encoding='cp949')

# 데이터 정보확인
train_df.info()
train_df.shape
train_df.columns