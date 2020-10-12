import pandas as pd

df = pd.read_csv('../data/ch1_sport_test.csv', index_col='학생번호')

print(df)

'''
      학년    악력  윗몸일으키기  점수  순위
학생번호                          
1      1  40.2      34  15   4
2      1  34.2      14   7  10
3      1  28.8      27  11   7
4      2  39.0      27  14   5
5      2  50.9      32  17   2
6      2  36.5      20   9   9
7      3  36.6      31  13   6
8      3  49.2      37  18   1
9      3  26.0      28  10   8
10     3  47.4      32  16   3
'''


print(df['악력'])

'''
학생번호
1     40.2
2     34.2
3     28.8
4     39.0
5     50.9
6     36.5
7     36.6
8     49.2
9     26.0
10    47.4
Name: 악력, dtype: float64
'''

#DataFrame의 크기는 shape이라는 인스턴스 변수 참조

print(df.shape)
# (10, 5)
# 데이터(레코드 수) 10개, 변수 개수 5 (컬럼 수)