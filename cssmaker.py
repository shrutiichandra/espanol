#!/usr/bin/env python
# coding: utf-8

# In[1]:



# In[9]:


def prepend(_list):
    str = "#" + '{0}'
    _list = list(map(str.format, _list))
    return _list


# In[26]:


def getColumn(df, colName):
    colList = df[colName].values
    colList = prepend(colList)
    return colList   


# In[32]:


def readCsv(file):
    import pandas as pd
    df = pd.read_csv(file)
    return df


# In[35]:


def getTenseColor():
    df = readCsv("colormap.csv")
    tense = getColumn(df, "tense")
    color = getColumn(df, "color")
    return tense, color


# In[33]:


def do():
    df = readCsv("colormap.csv")
    tense_mood = getColumn(df, "tense")
    colors = getColumn(df, "color")
    css_content = ""
    for tense, col in zip(tense_mood, colors):
        css_content += tense + "{ background: " + col + ";}\n"
    with open('colormap.css', 'w') as file:
        file.write(css_content)
