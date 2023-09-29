#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:19:50 2023

@author: dai
"""

import pandas as pd
import re

# def checkGen(row):
#     lst=['Action','Romance','Comedy','Thriller']
#     for gen in lst:
#         if row.find(gen)==-1:
#             return False
#     return True 
df= pd.read_csv("movies11.csv")
cols=df.columns
df1= pd.read_csv("movie12.csv", header=None)
df1.columns=cols
df2= pd.read_csv("movies13.csv", header=None)
df2.columns=cols

movies=pd.concat([df,df1, df2], ignore_index=True)

# movies=movies.loc[((movies['genres'].str.contains('Action')) & 
#                    (movies['genres'].str.contains('Romance')) &
#                    (movies['genres'].str.contains('Comedy')) &
#                    (movies['genres'].str.contains('Thriller'))), 'movieId':]


# movies=movies.loc[movies['genres'].apply(checkGen), 'movieId':]


# genres= pd.DataFrame(movies['genres'].str.get_dummies(sep='|'))
# avg= genres.sum()
# print(avg)

##Question2

list1=(movies.assign(genres = movies['genres'].str.split('|'))
          .explode('genres'))

genrelist=pd.DataFrame(list1.groupby('genres').count())

genrelist.drop('movieId', axis=1, inplace=True)
genrelist.rename(columns={'title':'count'}, inplace=True)
genrelist.sort_values('count', inplace=True, ascending=False)

import matplotlib.pyplot as plt

plt.pie(genrelist['count'],labels=genrelist.index,autopct='%1.1f%%',shadow=True,startangle=90, radius=4,textprops={'fontsize': 8})
plt.legend(labels=genrelist.index, loc='best')
plt.axis('equal')

plt.show()


