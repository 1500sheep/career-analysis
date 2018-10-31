
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from decimal import *
basic_folder = '/home/project/Untitled Folder/'
read_name = basic_folder + 'select_all.csv'
pd.set_option('max_colwidth', 800)
df = pd.read_csv(read_name, index_col=0)
df.columns = ['job','company','city','state','word','frequency','score','result']
df.fillna('_')

print(df)



import nltk
stemmer = nltk.stem.PorterStemmer()
def filetolist(text, _df):
    read_name = basic_folder + text + '.csv'
    __df = pd.read_csv(read_name)
    __df.columns = ['word']
    __df = __df.drop_duplicates('word', keep='last')
    list = __df.values.tolist()
    flat_list = [item for sublist in list for item in sublist]

    df_words = DataFrame(columns=("col_index", "word", "frequency", "score", "result"))
    write_name = basic_folder + text + '_' + _df.columns[0] + '.csv'
    for i in range(len(flat_list)):
        word_in_list = flat_list[i].lower()
        after_stem = stemmer.stem(word_in_list)
        for j in _df.index:
            # 리스트의 단어를 통해 csv에서 이 단어를 포함하는 문자열이 있는지 확인
            #print(_df)
            try:
                word_in_df = _df[j:j + 1].word.item()
                if after_stem in word_in_df:
                    # 문자열에서 빈도와 결과점수 가져와서 통합
                    df_words = df_words.append({"col_index": _df.loc[_df['word'] == word_in_df, _df.columns[0]].item(),
                                              "word": word_in_list,
                                              "frequency": _df.loc[_df['word'] == word_in_df, 'frequency'].item(),
                                               "score": 0,
                                               "result": _df.loc[_df['word'] == word_in_df, 'result'].item()},
                                              ignore_index=True)
            except:
                pass
        df_words.to_csv(write_name)

    df_words = df_words.groupby(['col_index', 'word']).agg({'frequency': np.sum, 'score': np.sum, 'result': np.sum})
    df_words = df_words[["frequency", "score", "result"]]
    df_words = df_words.sort_values(['col_index', 'word', 'result'], ascending=[True, True, False])
    df_words.to_csv(write_name)
    print('    ' + text+ ' finished')
    return 0



###
#job
print('job table started')
Temp = df
Temp = Temp.drop(['company','city','state'], axis=1)
#filetolist('ability_words', Temp)
#filetolist('Resume_words', Temp)
#filetolist('Programming_for_software_developer', Temp)
#filetolist('programming_for_software_engineer', Temp)
#filetolist('programming_for_data_engineer', Temp)
#filetolist('programming_for_data_analyst', Temp)
#filetolist('programming_for_big_data', Temp)
#filetolist('Programming_for_software_developer', Temp)
print('job table finished')

###
#company
print('company table started')
Temp = df
Temp = Temp.drop(['job','city','state'], axis=1)
#filetolist('ability_words', Temp)
#filetolist('Resume_words', Temp)
#filetolist('Programming_for_software_developer', Temp)
#filetolist('programming_for_software_engineer', Temp)
#filetolist('programming_for_data_engineer', Temp)
#filetolist('programming_for_data_analyst', Temp)
#filetolist('programming_for_big_data', Temp)
#filetolist('Programming_for_software_developer', Temp)
print('company table finished')

###
#city
print('city table started')
Temp = df
Temp = Temp.drop(['company','job','state'], axis=1)
filetolist('ability_words', Temp)
filetolist('Resume_words', Temp)
#filetolist('Programming_for_software_developer', Temp)
#filetolist('programming_for_software_engineer', Temp)
#filetolist('programming_for_data_engineer', Temp)
#filetolist('programming_for_data_analyst', Temp)
#filetolist('programming_for_big_data', Temp)
#filetolist('Programming_for_software_developer', Temp)
print('city table finished')

###
#state
print('state table started')
Temp = df
Temp = Temp.drop(['company','city','job'], axis=1)
#filetolist('ability_words', Temp)
#filetolist('Resume_words', Temp)
#filetolist('Programming_for_software_developer', Temp)
#filetolist('programming_for_software_engineer', Temp)
#filetolist('programming_for_data_engineer', Temp)
#filetolist('programming_for_data_analyst', Temp)
#filetolist('programming_for_big_data', Temp)
#filetolist('Programming_for_software_developer', Temp)
print('state table finished')


###
#result

























