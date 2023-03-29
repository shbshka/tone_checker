import pandas
import pandas as pd
import numpy as np

words_pos = pd.read_csv("pos.csv", sep=",", header=None)
words_neg = pd.read_csv("neg.csv", sep=",", header=None)

words_pos.drop(columns=[0], inplace=True)
words_neg.drop(columns=[0], inplace=True)

df_pos = pandas.DataFrame(words_pos)
df_neg = pandas.DataFrame(words_neg)

words_pos = np.array(df_pos[1].values).flatten()
words_neg = np.array(df_neg[1].values).flatten()




