#!/usr/bin/env python
# coding: utf-8

# # List of largest companies in the United States by revenue

# https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)      # now we tried to connect to the destination url page
print(page)
soup = BeautifulSoup(page.text, 'html')   # Now soup contains all the information of the destination url page in html shape format!
print(soup.prettify())


# #### How to select our preffered table in HTML?
# #### After checking the Inspect section of url & searching "table", I found that the "table" is representing the starting point of HTML code and totally we have 4 tables in this url in current date (Today is July 18, 2024). Now we can select our preffered table by indexing method using Pandas.

# In[39]:


table2 = soup.find_all('table', class_='wikitable sortable')[0]
# or --> table2 = soup.find_all('table')[1]
table2


# #### According to the last step we can see the Table headers are between "th" So we should write below query to drop it by list comprehention method.

# In[40]:


table2_header = table2.find_all('th')
table2_header


# #### List comprehention method

# In[41]:


table2_header = [title.text for title in table2_header]
print(table2_header)


# In[42]:


table2_header = [title.strip() for title in table2_header]
print(table2_header)


# #### Now we just need to insert this list in a Dataframe!

# In[7]:


import pandas as pd


# In[11]:


df = pd.DataFrame(columns=table2_header)
df


# #### Now is the time for pulling the rows:

# In[17]:


column_data = table2.find_all('tr')[1:]
column_data


# In[32]:


for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
df


# #### Well done ! Now it's done and you're ready to export your table to cvs, excel & so on.

# In[ ]:


df.to_csv(r'Your path/df.csv')

