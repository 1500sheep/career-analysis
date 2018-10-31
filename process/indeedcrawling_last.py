import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (WebDriverException,
                                NoSuchElementException)
import datetime
import os.path
import pymysql
# from pyvirtualdisplay import Display
INDEED_URL = 'https://www.indeed.com/q-Indeed-jobs.html'

# display = Display(visible=0,size=(800,600))
# display.start()

conn = pymysql.connect(host='localhost',user='root',password='2018',db='indeed',charset='utf8')
curs = conn.cursor()


# return commit_data_array
binary_chrom = '/home/project/project_lastest/chromedriver'
start_time = time.time()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('현재 시작 : ',now)


chrome_options = Options()
#개발자 전용 접근제한 걸릴 경우 방지 코드
chrome_options.add_argument("-incognito")
# chrome_options.add_argument("--disable-extensions")
# head 없이 주는것!
chrome_options.add_argument("headless")
browser = webdriver.Chrome(binary_chrom, chrome_options=chrome_options)
#browser = webdriver.PhantomJS(binary_phantom)
browser.get(INDEED_URL)
time.sleep(1)


keep_searching = True


start_city = 1
current_url=""
pageNum = 0

def crawlingPage(current_page,current_url,pageNum,search_job,search_city,search_state):
    if current_page*10 > pageNum:
        return
    if current_page*10 >= 1000:
        return

    search_url = current_url
    if current_page != 0:
        search_url += "&start=" + str(current_page * 10)
    browser.get(search_url)
    try:
        research_Col = browser.find_element_by_id("resultsCol").find_elements_by_class_name("result")
        for a in research_Col:
            b = a.find_element_by_tag_name("h2").find_element_by_tag_name("a")
            url =b.get_attribute("href")
            sql = "insert into url_crawling(job,city,state,url) values(%s,%s,%s,%s)"
            curs.execute(sql,(search_job,search_city,search_state,url))
    except NoSuchElementException:
        print("NoSuchElementException : ",search_url)
        return

    crawlingPage(current_page+1,current_url,pageNum,search_job,search_city,search_state)


def crawlingData(search_job,start_city):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('진행 시작 : ', now)
    if start_city ==-1:
        return

    sql = "select id,city,state from cities_usa where id=" + str(start_city)
    curs.execute(sql)
    search_city_list = curs.fetchone()
    search_city = search_city_list[1]
    search_state = search_city_list[2]

    print("***********************city name: ", search_city)

    search_ = browser.find_element_by_name('q')
    search_.clear()

    search_.send_keys(search_job)

    search_where = browser.find_element_by_name('l')
    search_where.clear()

    search_where.send_keys(search_city + "," + search_state)

    search_click = browser.find_element_by_xpath("//*[@type='submit']")
    search_click.submit()

    current_url = browser.current_url

    pageNum = 0

    try:
        pageNum = browser.find_element_by_id("searchCount")
        pageNum = pageNum.text.split(" ")[3]
        pageNum = int(pageNum.replace(",", ""))
        print("pageNum",pageNum)

    except NoSuchElementException:
        print("searched nothing in ",search_city)
        if start_city >=200:
            start_city = -2
            sql = "update cities_index set current_index = " + str(1)
        else:
            sql = "update cities_index set current_index = " + str(start_city + 1)

        curs.execute(sql)
        conn.commit()
        crawlingData(search_job,start_city + 1)


    crawlingPage(0,current_url,pageNum,search_job,search_city,search_state)

    if start_city >= 200:
        start_city = -2
        sql = "update cities_index set current_index = " + str(1)
    else:
        sql = "update cities_index set current_index = " + str(start_city + 1)

    curs.execute(sql)
    conn.commit()
    crawlingData(search_job,start_city+1)





while keep_searching:
    sql = "select current_index from jobs_index"
    curs.execute(sql)
    current_index = curs.fetchone()[0]
    current_index = int(current_index)
    print("***********************job index : ", current_index)

    if current_index>39:
        keep_searching = False
        conn.close()
        break

    # user id 갖고 오는!
    sql = "select name from jobs where id=" + str(current_index)
    curs.execute(sql)
    search_word = curs.fetchone()[0]
    search_word = str(search_word)
    print("***********************job's name : ", search_word)

    sql = "select current_index from cities_index"
    curs.execute(sql)
    cities_index = curs.fetchone()[0]
    cities_index = int(cities_index)
    print("***********************citiy's index : ", cities_index)

    crawlingData(str(search_word),cities_index)

    sql = "update jobs_index set current_index = "+str(current_index+1)
    curs.execute(sql)
    conn.commit()



print("taking time : ",time.time()-start_time)

