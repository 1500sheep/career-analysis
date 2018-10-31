# CODE DESCRIPTION

**코드 설명**



## Indeedcrawling.py

- 사용 library : selenium , pymysql
  - selenium : Indeed site에서 data를 crawling하기 위해 사용!
    - chromedriver 사용 : chrome_options.add_argument('headless')를 하여 browser창을 직접적으로 띄우지 않고 background에서 작업 가능!
  - pymysql : indeed site에서 긁어온 job, city, state, url를 mysql에 저장하여 추후 url의 resume 데이터를 beautifulsoup으로 crawling 할 수 있게 작업
- error 발생 할 때 현재 작업을 저장하기 위해 추가적으로 current status를 저장하기 위한 index, data를 mysql table에 따로 저장





## Indeed.py

- 사용 library : BeautifulSoup, pymysql, pandas

  - pymysql : mysql database에 저장된 url을 이용해서 resume의 content를 긁어 올 수 있게 한다.
  - BeautifulSoup : url로 open하여 resume 데이터를 갖고 온다
  - pandas : crawling 한 resume데이터를 [job,city,state,content] 형식으로 담고 파일에 append 형식으로 저장한다.

  

## Column_count.py

- 사용 library : pyspark, pandas

  - pyspark : output 데이터를 rdd로 읽어 들인다

    1. strip()으로 양쪽의 while space 제거
    2. replace 로 " 제거
    3. map을 이용해서 (company,job) / (city,job) / (state,job) 로 변경
    4. 변경한 데이터를 reduceByKey로 wordcount 작업 진행 
    5. ((company,job),count) 형태의 데이터를  (company,job,count) 형태로 변경

  - pandas

    1.  (company,job,count) 형태의 rdd를 column명이 있는 pandas로 변경한다.
    2.  visualization을 위해 pandas 변수를 csv 파일로 저장한다.

    

## Analyze_word_v2.py

- c++과 c#, r등을 찾아내기 위해 토큰 단어에서 한번의 과정을 더 거친다.

- 크롤링된 데이터들을 이용하여 새로운 데이터 프레임(키값들, 단어, 빈도, 점수결과)을 생성한다.

- 사용 library : pandas, pyspark, nltk

  - pandas : csv파일을 읽어오고 csv파일 생성해서 내보낼 때 사용

  - pyspark : rdd를 생성할 때 사용

  - nltk : 자연어들로 연산을 할 때 사용

    - punkt : 단어와 문장을 각각 토큰화할 때 사용
    - stopwords : 불용어 처리에 사용      
    - wordnet : 형용사 구분에 사용
    - PorterStemmer : 어원이 같은 단어들을 합치기 위해 사용
    - sentiwordnet : 토큰화된 단어들의 점수를 가져올 때 사용

    

## find_word_v2.py

- Analyze_word_v2.py에서의 연산 결과 생성된 csv파일과 미리 만들어둔 단어 리스트를 비교하여 단어의 빈도수와 총 점수를 가진 csv를 출력한다.
- 사용 library : pandas, nltk
  - pandas : csv파일을 읽어오고 csv파일 생성해서 내보낼 때 사용
  - nltk : 자연어들로 연산을 할 때 사용
    - PorterStemmer : Analyze_word_v2.py에서 어원을 통해 분석했기 때문에 리스트 단어들 또한 스템 처리를 해서 비교하기 위해 사용



## Merge_file.py

- 자바 오버헤드 발생으로 큰 데이터를 올릴 수 없어 인덱스를 통해 나눠서한 데이터를 통합한다.
- 사용 library : pandas
  - pandas : csv파일을 읽어오고 csv파일 생성해서 내보낼 때와 데이터프레임을 합칠 때 사용
