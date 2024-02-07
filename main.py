import numpy as np # linear algebra
import pandas as pd # data processing
from sklearn.pipeline import Pipeline # importing pipeline for preprocessing
from sklearn.preprocessing import OneHotEncoder # importing One Hot Encoder for Pre processing
from sklearn.compose import ColumnTransformer # used to Combine preprocessing steps


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from google.colab import files

df = pd.read_csv('flixpatrol.csv')

print(df.head(5))

df.shape

col_list=list(df.columns)
col_list

df.info()

df['Watchtime'] = pd.to_numeric(df['Watchtime'].str.replace(',', ''), errors='coerce')
df = df.dropna(subset=['Watchtime', 'Genre'])
df = df[df['Genre'].str.strip() != '']

plt.figure(figsize=(10, 10))
sns.boxplot(x='Genre', y='Watchtime', data = df, palette='bright')
plt.title('Distribution of Watchtime by Genre')
plt.xlabel('Type')
plt.ylabel('Watchtime (Million)')
plt.xticks(rotation=90)
plt.show()

top_10_shows = df.sort_values(by='Watchtime', ascending=False).head(10)
plt.figure(figsize=(14, 8))
sns.barplot(x='Watchtime', y='Title', data=top_10_shows, color='green')
plt.title('Top 10 Shows by Watchtime')
plt.xlabel('Watchtime (Million)')
plt.ylabel('Show Title')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Premiere', y='Watchtime', data=df, hue='Genre', palette='Set2')
plt.title('Premiere Year vs. Watchtime')
plt.xlabel('Premiere Year')
plt.ylabel('Watchtime (Million)')
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Genre', data=df, palette='pastel')
plt.title('Count of Shows by Genre')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


sns.pairplot(df[['Watchtime', 'Premiere', 'Genre']], hue='Genre', palette='dark', height=3)
plt.suptitle('Scatterplot Matrix of Watchtime, Premiere Year, and Genre', y=1.02)
plt.show()


correlation_matrix = df[['Watchtime', 'Premiere']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Watchtime'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Watchtime')
plt.xlabel('Watchtime (Million)')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(14, 8))
sns.violinplot(x='Genre', y='Watchtime', data=df, palette='husl')
plt.title('Distribution of Watchtime by Genre')
plt.xlabel('Genre')
plt.ylabel('Watchtime (Million)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Premiere', y='Watchtime', data=df, estimator='mean', ci=None, color='green')
plt.title('Average Watchtime Over the Years')
plt.xlabel('Premiere Year')
plt.ylabel('Average Watchtime (Million)')
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


