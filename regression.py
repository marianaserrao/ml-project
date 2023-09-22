import numpy as np
import pandas as pd

x_train = np.load('data/X_train_regression1.npy')
x_train_df = pd.DataFrame(x_train.T)
print(x_train_df)