# %%
import pandas as pd
import csv

wiki = pd.read_csv('EuroParl/Translated Wikipedia Biographies - EN_DE.csv', encoding='UTF-8')
wiki.head()
#%%
src = wiki['sourceText']
tgt = wiki['translatedText']
print(src.head())
export_csv = src.to_csv (r'EuroParl/src-test.txt' , index = None, header = False, quoting=csv.QUOTE_NONE, escapechar="\\")
export_csv = tgt.to_csv (r'EuroParl/tgt-test.txt' , index = None, header = False, quoting=csv.QUOTE_NONE, escapechar="\\")

# %%
