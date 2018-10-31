'''city state 추가 career과 content 사이에'''
import sys
import urllib.request as req
import urllib.parse as parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame
from urllib.error import HTTPError
import csv
# display = Display(visible=0,size=(800,600))
# display.start()
import pymysql
conn = pymysql.connect(host='localhost',user='root',password='2018',db='indeed',charset='utf8')
curs = conn.cursor()

### 빈 데이터프레임 생성
df = DataFrame(columns=("jobs", "url","company", "location", "content"))



''' 만들 것
#같은 직업을 가진 것 행들을 새로운 데이터프레임에 복사
df_temp = df
#이 데이터프레임에서 url을 이용해 중복제거
df_drop_duplicated_data = df_temp.drop_duplicates(['name'],keep='first')
'''
### 파일 읽어옴
basic_folder = '/home/project/project_lastest/output/'
#read_name = basic_folder + 'testforntlk.csv'
#df_origin = pd.read_csv(read_name)

### 파일 저장 경로/이름
#basic_folder = 'C:/Users/User/Desktop/'
write_name = basic_folder + 'result_content.csv'
### 임시
#textfile = open('C:/Users/User/Desktop/indeedurl_dataengineer.txt')

def findfromhtml(job,url):
    ### url 받아옴
    #url =
    # error 500  예외처리
    try:
        html = req.urlopen(url)
    except HTTPError as e:
        print("에러발생 : ",e)
        return
        #df = df.append({"jobs": "NULL", "company": "NULL", "city": "NULL", "state": "NULL", "content": "NULL"}, ignore_index=True)

    else:
        soup = BeautifulSoup(html, 'html.parser')

        ### html에서 찾아옴
        ############################################
        # job
        ###########################################

        ############################################
        # company
        ############################################
        company = soup.select_one(".company")
        if company is not None:
            company = company.string
        
        ############################################
        # summary
        ############################################
        summary = soup.select_one(".summary")
        if summary is not None:
            summary = summary.text
       
        #print("summary : ", summary.text)

        location= soup.select_one(".location")
        if location is not None:
            location = location.string

        # 찾은 데이터 데이터프레임에 추가
        #df = df.append({"jobs":job,"url":url, "company":company.string, "location": location.string,"content":summary.text}, ignore_index=True)

        print("job : ",job,"\turl : ",url,"\tcompany : ",company,"\tlocation : ",location)

        data = [job,url,company,location,summary]
        # # 10번째마다 저장
        # if _index%10==0:
        #     print("savefile")
        with open(write_name,'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        return


# 함수 시작
current_job="big data engineer"

df_url = pd.read_sql('select job,url from url_crawling where job=\''+str(current_job)+'\' and id > '+str(4336), con=conn)
df2 = df_url.drop_duplicates()

print("job : "+current_job+" count : ",df2.count())
for index,row in df2.iterrows():
    findfromhtml(row['job'],row['url'])

   
