### DESCRIBE YOUR VISUALIZATION STEP
# Application
- Apache Zeppelin
  -여러가지 언어를 사용할 수 있어 협업에 용이하다
  -제플린 자체 기능으로 데이터 그래프화 가능

# PreProcessing
- process과정을 거친 csv파일을 load하여 나온 데이터 전처리 과정
- 모든 데이터를 시각화하기엔 너무 많다
- value(frequency or result)값에 따라 상위 10개만을 뽑아냄
<pre><code>
"%python
city_2 = pd.DataFrame(city, columns[city,frequency])
city_2 = city_2.sort_values(frequency,ascending=False)
city_2[frequency] = city_2.groupby(city)[frequency].transform('sum')
city_2 = city_2.drop_duplicates([city], keep=first)
city_h = city_2.head(10)
city_h = pd.DataFrame(city_h, columns[city])
city = pd.merge(city,city_h)
</code></pre>

# data nomarization
- result값은 모두 더한 값이기에 정규화 과정을 거친다
<pre><code>
"%python
city[new_result] = city[result] / city[frequency]
</code></pre>
