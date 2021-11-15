# %%
import pandas as pd
import numpy as np

src = []
tgt = []
with open('EuroParl/en_tokenized', encoding='UTF-8') as f:
    for line in f:
        src.append(line.rstrip())
with open('EuroParl/de_tokenized', encoding='UTF-8') as f:
    for line in f:
        tgt.append(line.rstrip())

print(len(src))
print(len(tgt))
#%%
src_df = pd.DataFrame(src, columns=['src'])
tgt_df = pd.DataFrame(tgt, columns=['tgt'])
sentence_pair = pd.concat([src_df, tgt_df], axis=1)

print(sentence_pair.head())
#%%
sentence_pair_filter = sentence_pair[
sentence_pair['src'].apply(lambda x: len(x)>0) &
sentence_pair['tgt'].apply(lambda x: len(x)>0)
  ]
#%%
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(sentence_pair_filter['src'], sentence_pair_filter['tgt'], test_size=0.2, random_state=1)

#%%

textfile = open("EuroParl/src-train.txt", "w", encoding='UTF-8')
for element in X_train:
    textfile.write(element + "\n")
textfile.close()

textfile = open("EuroParl/tgt-train.txt", "w", encoding='UTF-8')
for element in y_train:
    textfile.write(element + "\n")
textfile.close()

textfile = open("EuroParl/src-val.txt", "w", encoding='UTF-8')
for element in X_val:
    textfile.write(element + "\n")
textfile.close()

textfile = open("EuroParl/tgt-val.txt", "w", encoding='UTF-8')
for element in y_val:
    textfile.write(element + "\n")
textfile.close()
# %%
