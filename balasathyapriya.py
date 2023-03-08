# -*- coding: utf-8 -*-
"""Balasathyapriya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zPlB7dZcBhDaENUZH2qeMj23SrGt3JkW

EXPLORATORY DATA ANALYSIS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/train.csv.xls')

df.info()

"""DELETING THE COLUMNS WITH MORE NUMBER OF NULL VALUES


"""

df2 = df.drop(['Unnamed: 17', 'Unnamed: 18'], axis =1)

df2.info()

"""STATISTICAL DESCRIPTION OF THE DATA"""

df2.describe()

"""FILLING THE ROWS WITH THE NULL VALUES"""

df2.fillna(0)

df2.info()

df2 = df2.fillna(0)

df2.info()

"""CHANGING DATA TYPES FOR NUMERIC DATA"""

df2['Trend_day_count']= df2['Trend_day_count'].astype(float)

df2 = df2.fillna(0)

df2.info()

df2['like dislike disabled']= df2['like dislike disabled'].astype(bool)
df2['comment_disabled']= df2['comment_disabled'].astype(bool)
df2['tag appered in title']= df2['tag appered in title'].astype(bool)

df2.fillna(0)

df2.info()

"""visualization"""

sns.boxplot(df2['subscriber'])



sns.distplot(df2['dislike'])

sns.catplot(x="comment_count",y="comment_disabled",data=df2,kind="bar",height=4)

sns.catplot(x="Trend_tag_count",y="Tag_count",data=df2,kind="bar",height=4)

sns.barplot(x= df2['Video_id'].head(), y= df2['Trend_day_count'].head())
sns.lineplot(x= df2['Video_id'].head(), y= df2['Trend_day_count'].head())

sns.countplot(x ='like dislike disabled', data=df2)

sns.countplot(x ='comment_disabled', data=df2)

sns.countplot(x ='tag appered in title', data=df2)

sns.violinplot(df2.Trend_day_count,df2.Trend_tag_count)

sns.regplot(x = df2.Trend_day_count, y = df2.Trend_tag_count)

sns.heatmap(data = df2.corr(), annot = True, linewidth=0.5,cmap = 'Blues', cbar = True,vmin=-1, vmax=1)

