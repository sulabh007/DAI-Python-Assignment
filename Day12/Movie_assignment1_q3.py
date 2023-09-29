#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:59:39 2023

@author: dai
"""
import pandas as pd
import matplotlib.pyplot as plt

################################Q3######################################

df= pd.read_csv("movies11.csv")
cols=df.columns
df1= pd.read_csv("movie12.csv", header=None)
df1.columns=cols
df2= pd.read_csv("movies13.csv", header=None)
df2.columns=cols

movies=pd.concat([df,df1, df2], ignore_index=True)

rating_dfs= pd.read_csv("rating11.csv")
rating_df= rating_dfs.groupby('movieId')['rating'].mean()

movie_rating=pd.merge(movies, rating_df, right_on=['movieId'],left_on=['movieId'])


######################################Q4############################################################
list1=(movie_rating.assign(genres = movie_rating['genres'].str.split('|'))
          .explode('genres'))



genre_avg= list1.groupby('genres')['rating'].mean()



plt.pie(genre_avg,labels=genre_avg.index,autopct='%1.1f%%',shadow=True,startangle=90, radius=4,textprops={'fontsize': 8})
plt.legend(labels=genre_avg.index, loc='best')
plt.axis('equal')

plt.show()

#####################################Q5##################################################

rating_movie_df= rating_dfs.groupby('rating')['movieId'].count()

# plt.pie(rating_movie_df,labels=rating_movie_df.index,autopct='%1.1f%%',shadow=True,startangle=90, radius=4,textprops={'fontsize': 8})
# plt.legend(labels=rating_movie_df.index, loc='best')
# plt.axis('equal')

rating_movie_df.plot(kind='bar')
plt.title("Number of movies Vs ratings")

plt.show()