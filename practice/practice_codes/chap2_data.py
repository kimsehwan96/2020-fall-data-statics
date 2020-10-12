import numpy as np
import pandas as pd

pd.set_option('precision', 3) # DataFrame의 출력을 소수점 이하 3자리로 제한

df = pd.read_csv('../data/ch2_scores_em.csv', index_col = 'student number')


print(df.head()) # df의 처음 5행을 표시

'''
                english  mathematics
student number                      
1                    42           65
2                    69           80
3                    56           63
4                    41           63
5                    57           76
'''

# 학번 순서대로 10명의 영어 점수를 array 데이터 구조 scores에 저장

scores = np.array(df['english'])[:10]

print(scores)

# [42 69 56 41 57 48 65 49 65 58]

# 데이터 프레임 scores_df 작성

scores_df = pd.DataFrame({'scores' : scores}, 
                            index=pd.Index(['A','B','C','D','E',
                            'F','G','H','I','J'],
                            name = 'student'))

print(scores_df)

'''
         scores
student        
A            42
B            69
C            56
D            41
E            57
F            48
G            65
H            49
I            65
J            58
'''

# sum(scores)이 len(scores)이 n에 대응

print(sum(scores)/len(scores))
print(np.mean(scores))
print(scores_df.mean())

'''
55.0
55.0
scores    55.0
dtype: float64
'''

#최빈값

print(pd.Series([1, 1, 1, 2, 2, 3]).mode())

'''
0    1
dtype: int64
'''

# 편차

mean = np.mean(scores)

deviation = scores - mean #각 데이터가 평균으로부터 떨어져 있는 정도

#분산과 표준 편차
summary_df = scores_df.copy()
summary_df['deviation'] = deviation

print(summary_df)
'''
         scores  deviation
student                   
A            42      -13.0
B            69       14.0
C            56        1.0
D            41      -14.0
E            57        2.0
F            48       -7.0
G            65       10.0
H            49       -6.0
I            65       10.0
J            58        3.0
'''

# 분산

print(np.mean(deviation ** 2)) # 편차 제곱의 평균이 분산이다.

'''
86.0
'''

