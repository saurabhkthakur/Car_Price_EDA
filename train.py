import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as mse
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def run(fold):
    # read the training data with fold
    df = pd.read_csv('reg_stratified.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    df_test = df[df.kfold == 4].reset_index(drop=True)

    # training data is where data is not equal fold
    df_train = df[(df.kfold != fold) & (df.kfold != 4)].reset_index(drop=True)
    # validation data is where data is equal fold
    df_valid = df[(df.kfold == fold) & (df.kfold != 4)].reset_index(drop=True)

    feature = df.drop(['kfold', 'priceUSD'], axis=1).columns

    test_feat = df.drop(['kfold', 'priceUSD'], axis=1).columns

    X_test = df_test[test_feat].values
    y_test = df_test['priceUSD'].values

    x_train = df_train[feature].values
    y_train = df_train['priceUSD'].values

    x_valid = df_valid[feature].values
    y_valid = df_valid['priceUSD'].values

    clf = RandomForestRegressor(n_estimators=150, max_depth=4, random_state=42)

    clf.fit(x_train, y_train)

    pred = clf.predict(x_valid)

    accuracy = np.sqrt(mse(y_valid, pred))

    test_pred = clf.predict(X_test)

    print(f"Fold={fold}, Accuracy = {accuracy} ")

    print(np.sqrt(mse(y_test, test_pred)))


    return accuracy


if __name__ == "__main__" :

    count = 0
    for i in range(4):
        count += run(i)

    print("The accuracy is ",count / 4)








