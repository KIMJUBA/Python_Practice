#!/usr/bin/env python
# coding: utf-8

# ##  원하는 직사각형 모양으로 별 출력하기
# * 중첩반복문을 이용하여 직사각형 형태의 별 입력해보기

# In[8]:


x, y = map(int, input('원하는 행(세로)의 수와 열(가로)의 수를 입력하시오: ').split()) # 사용자가 원하는 값 입력받기

for i in range(x): # 행
    for j in range(y): # 열
        print('*', end='') # 별 출력, end에 ''를 지정하여 줄 바꿈을 하지 않음
    print() # 다음줄로 넘기는 코드, print는 출력 후 기본적으로 다음 줄로 넘김

