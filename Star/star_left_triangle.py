#!/usr/bin/env python
# coding: utf-8

# ##  왼쪽으로 치우친 삼각형 출력
# * 중첩반복문을 이용하여 왼쪽으로 치우친 삼각형 형태의 별 입력해보기

# In[10]:


n = int(input('원하는 행(세로)의 수를 입력하시오: ')) # 사용자가 원하는 값 입력받기

for i in range(n): # 행
    for j in range(n): # 열
        if(i>=j):
            print('*', end='')# 별 출력, end에 ''를 지정하여 줄 바꿈을 하지 않음
    print() # 다음줄로 넘기는 코드, print는 출력 후 기본적으로 다음 줄로 넘김

