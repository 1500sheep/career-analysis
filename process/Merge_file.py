####################################################################
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

basic_folder = '/home/hwan/PycharmProjects/Normalization/splited_word/'
read_name1 = basic_folder + 'words_content_dataanalyst.csv'
read_name2 = basic_folder + 'words_content_dataarchitect.csv'

first = pd.read_csv(read_name1, index_col=0)
first.columns = ['job','company','city','state','word','frequency','score','result']
second = pd.read_csv(read_name2, index_col=0)
second.columns = ['job','company','city','state','word','frequency','score','result']
output = first.append(second, ignore_index=True)

read_name2 = basic_folder + 'words_content_dataengineer_bigdataengineer.csv'
second = pd.read_csv(read_name2, index_col=0)
second.columns = ['job','company','city','state','word','frequency','score','result']
output = output.append(second, ignore_index=True)

read_name2 = basic_folder + 'words_content_dataengineer_bigdataengineer10000.csv'
second = pd.read_csv(read_name2, index_col=0)
second.columns = ['job','company','city','state','word','frequency','score','result']
output = output.append(second, ignore_index=True)

read_name2 = basic_folder + 'words_content_softengineer.csv'
second = pd.read_csv(read_name2, index_col=0)
second.columns = ['job','company','city','state','word','frequency','score','result']
output = output.append(second, ignore_index=True)

read_name2 = basic_folder + 'words_content_softwareembedded_softwaredeveloper.csv'
second = pd.read_csv(read_name2, index_col=0)
second.columns = ['job','company','city','state','word','frequency','score','result']
output = output.append(second, ignore_index=True)

read_name2 = basic_folder + 'words_content_warehouseengineer_machinelearningengineer_deeplearningengineer.csv'
second = pd.read_csv(read_name2, index_col=0)
second.columns = ['job','company','city','state','word','frequency','score','result']
output = output.append(second, ignore_index=True)

write_name = '/home/hwan/PycharmProjects/Normalization/' + 'select_all.csv'
output = output.sort_values(['job', 'word', 'result'], ascending=[True, True, False])
output.to_csv(write_name)
print(output)