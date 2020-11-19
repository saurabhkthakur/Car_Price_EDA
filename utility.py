import pandas as pd
import numpy as np
from sklearn import model_selection



def create_fold(data):
    '''

    :param data: input csv file (Dataframe)
    :return: DataFrame
    '''
    data['kfold'] = -1
    data = data.sample(frac=1).reset_index(drop=True)
    kf = model_selection.KFold(n_splits=5)

    for fold, (train_idx, val_idx) in enumerate(kf.split(X=data[['priceUSD']])):
        data.loc[val_idx, 'kfold'] = fold

    data.to_csv('train_folds1.csv')
    return data


def reg_startified_fold(data):
    '''

    :param data: input csv file (Dataframe)
    :return: DataFrame
    '''

# we create new column and fill it -1
    data['kfold'] = -1
# randomize the data
    data = data.sample(frac=1).reset_index(drop=True)
# calculating number of bins
    num_bins = np.floor(1 + np.log2(len(data)))
# column on which we want to validate
    data.loc[:, 'bins'] = pd.cut(x=data[['priceUSD']], bins=num_bins, labels=False)
# initiate kFold
    kf = model_selection.StratifiedKFold(n_splits=5)

    for fold, (train_idx, val_idx) in enumerate(kf.split(X=data['priceUSD'],y=data.bins.values)):
        data.loc[val_idx, 'kfold'] = fold
    data.drop('bins',axis=1,inplace=True)
    data.to_csv('reg_stratified.csv')
    return data


def root_mean_squared(y_true, y_pred):
    '''
    :param y_true:list of real values
    :param y_pred: list of predicted values
    :return: sqrt(mean_square)
    '''
    error = 0

    for yt, yp in zip(y_true,y_pred):
        error += (yt-yp)**2

        return np.sqrt(error/len(y_true))
