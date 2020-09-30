#!/usr/bin/env python
# coding: utf-8

# ## Observable Trends
# 
# - Between 576 of players, 84% male and 14% female, which means it is designed mainly for male. This big group of men assigned 1,967 of total purchase value. As a result, we can understand this game isn’t a favorite female game so if the designers want to attract female, they should add more female characteristics in their game. 
# - The range age (20-24) have 44 of total players and the total purchase value of this range is 1,114 which is a huge amount. So, we see this game is more designed for this group. The second position is for (15-19) that is 18% of total portion, also we can notice the big difference between first and second position.
# - “Final Critic “and “Oathbreaker, Last Hope of the Breaking Storm” are the most popular and profitable items among all 179 items. For future, developers and designers of this game could planning for add more similar items in this game to increase their profit.

# In[124]:


# Dependencies and Setup
import pandas as pd

# File to Load
find_path = "Resource/02-Homework_04-Pandas_HeroesOfPymoli_Resources_purchase_data.csv"


# In[3]:


# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(find_path)
purchase_data.head(2)


#  ## Player Count
#  - Total Number of Players

# In[113]:


total_number_players = len(purchase_data["SN"].unique())
total_number_players_data_frame = pd.DataFrame({"Total Players":[total_number_players]})
total_number_players_data_frame


# ## Purchasing Analysis (Total)
# - Number of Unique Items
# 
# - Average Purchase Price
# 
# - Total Number of Purchases
# 
# - Total Revenue

# In[114]:


number_unique_items = len(purchase_data["Item Name"].unique())
number_unique_items


# In[6]:


average_price = purchase_data["Price"].mean()
average_price


# In[7]:


number_purchases = len(purchase_data.index)
number_purchases


# In[8]:


total_revenue = purchase_data["Price"].sum()
total_revenue


# In[9]:


pd.options.display.float_format = '${:,.2f}'.format
summary_data_frame = pd.DataFrame (
    {"Number of Unique Items" : [number_unique_items] ,
    "Average Price" : [average_price] , 
    "Number of Purchases" : [number_purchases] ,
    "Total Revenue" : [total_revenue ]
})
summary_data_frame


# ##  Gender Demographics
# - Percentage and Count of Male Players
# - Percentage and Count of Female Players
# - Percentage and Count of Other / Non-Disclosed

# In[10]:


male_playes = purchase_data.loc[(purchase_data["Gender"] == "Male") , :]
clean_male_playes = male_playes["SN"].unique()
count_male_playes = len(clean_male_playes)
count_male_playes


# In[11]:


percent_male_playes = (count_male_playes/total_number_players)*100
percent_male_playes


# In[12]:


female_playes = purchase_data.loc[(purchase_data["Gender"] == "Female") , :]
clean_female_playes = female_playes["SN"].unique()
count_female_playes = len(clean_female_playes)
count_female_playes


# In[13]:


percent_female_playes = (count_female_playes/total_number_players)*100
percent_female_playes


# In[14]:


other_playes = purchase_data.loc[(purchase_data["Gender"] == "Other / Non-Disclosed") , :]
clean_other_playes = other_playes["SN"].unique()
count_other_playes = len(clean_other_playes)
count_other_playes


# In[15]:


percent_other_playes = (count_other_playes/total_number_players)*100
percent_other_playes


# In[16]:


pd.options.display.float_format = '{:,.2f}%'.format
fill_data = {"Total Count" : [count_male_playes , count_female_playes , count_other_playes ] ,
    "Percentage of Players" : [percent_male_playes , percent_female_playes , percent_other_playes ] ,     
}
labels = ['Male', 'Female', 'Other / Non-Disclosed']
gender_data_frame = pd.DataFrame(fill_data, index=labels)
gender_data_frame


# ## Purchasing Analysis (Gender)
# - Purchase Count
# - Average Purchase Price
# - Total Purchase Value
# - Average Purchase Total per Person by Gender

# In[17]:


male_purchase_count = len(male_playes)
male_purchase_count


# In[18]:


ave_male_purch = male_playes["Price"].mean()
ave_male_purch


# In[19]:


total_male_purch = male_playes["Price"].sum()
total_male_purch


# In[20]:


ave_male_purch_per = total_male_purch/count_male_playes
ave_male_purch_per


# In[21]:


female_purchase_count = len(female_playes)
female_purchase_count


# In[22]:


ave_female_purch = female_playes["Price"].mean()
ave_female_purch


# In[23]:


total_female_purch = female_playes["Price"].sum()
total_female_purch


# In[24]:


ave_female_purch_per = total_female_purch/count_female_playes
ave_female_purch_per


# In[25]:


other_purchase_count = len(other_playes)
other_purchase_count


# In[26]:


ave_other_purch = other_playes["Price"].mean()
ave_other_purch


# In[27]:


total_other_purch = other_playes["Price"].sum()
total_other_purch


# In[28]:


ave_other_purch_per = total_other_purch/count_other_playes
ave_other_purch_per


# In[29]:


pd.options.display.float_format = '${:,.2f}'.format
fill_data = {"Purchase Count" : ["",female_purchase_count , male_purchase_count , other_purchase_count ] ,
    "Average Purchase Price" : ["",ave_female_purch , ave_male_purch , ave_other_purch ] , 
    "Total Purchase Value" : ["",total_female_purch , total_male_purch , total_other_purch ] ,         
    "Avg Total Purchase per Person" : ["",ave_female_purch_per , ave_male_purch_per , ave_other_purch_per ] , 
}
labels = ['Gender','Female', 'Male', 'Other / Non-Disclosed']
purchasing_analysis_data_frame = pd.DataFrame(fill_data, index=labels)
purchasing_analysis_data_frame


# ##  Age Demographics
# - Purchase Count
# - Average Purchase Price
# - Total Purchase Value
# - Average Purchase Total per Person by Age Group

# In[33]:


ad_bins = [0, 9, 14, 19, 24, 29, 34, 39, 60]
ad_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
pd.cut(purchase_data["Age"], ad_bins, labels=ad_labels)


# In[36]:


purchase_data["Range Age"] = pd.cut(purchase_data["Age"], ad_bins, labels=ad_labels)
purchase_data


# In[43]:


grouped_range_age = purchase_data.groupby("Range Age")


# In[52]:


total_count_age = grouped_range_age["SN"].nunique()
total_count_age


# In[56]:


pd.options.display.float_format = '{:,.2f}%'.format
percentage_players_age = (total_count_age/total_number_players)*100
percentage_players_age


# In[60]:


age_demographics_data_frame = pd.DataFrame({"Total Count": total_count_age, "Percentage of Players": percentage_players_age})
age_demographics_data_frame


# ##  Purchasing Analysis (Age)
# - Purchase Count
# - Average Purchase Price
# - Total Purchase Value
# - Average Purchase Total per Person by Age Group

# In[63]:


purchase_count_age = grouped_range_age["Price"].count()
purchase_count_age


# In[65]:


average_purchase_price_age = grouped_range_age["Price"].mean()
average_purchase_price_age


# In[66]:


total_purchase_value_age = grouped_range_age["Price"].sum()
total_purchase_value_age


# In[72]:


avg_total_purchase_person_age = total_purchase_value_age/total_count_age
avg_total_purchase_person_age


# In[90]:


pd.options.display.float_format = '${:,.2f}'.format
age_purchasing_analysis_data_frame = pd.DataFrame({"Purchase Count": purchase_count_age,
                                                   "Average Purchase Price": average_purchase_price_age,
                                                   "Total Purchase Value": total_purchase_value_age,
                                                   "Avg Total Purchase per Person": avg_total_purchase_person_age})
age_purchasing_analysis_data_frame


# ## Top Spenders
# dentify the the top 5 spenders in the game by total purchase value, then list (in a table):
# 
# - SN
# - Purchase Count
# - Average Purchase Price
# - Total Purchase Value

# In[120]:


grouped_purchase_data = purchase_data.groupby("SN")
grouped_purchase_data.count().head()


# In[91]:


purchase_count_spenders = grouped_purchase_data["Price"].count()
purchase_count_spenders


# In[92]:


average_purchase_price_spenders = grouped_purchase_data["Price"].mean()
average_purchase_price_spenders


# In[93]:


total_purchase_value_spenders = grouped_purchase_data["Price"].sum()
total_purchase_value_spenders


# In[119]:


spenders_data_frame = pd.DataFrame({"Purchase Count": purchase_count_spenders,
                                        "Average Purchase Price": average_purchase_price_spenders,
                                        "Total Purchase Value": total_purchase_value_spenders})
spenders_data_frame.head()


# In[118]:


top_spenders_data_frame = spenders_data_frame.sort_values("Total Purchase Value", ascending=False)
top_spenders_data_frame.head()


# ##  Most Popular Items
# Identify the 5 most popular items by purchase count, then list (in a table):
# 
# - Item ID
# - Item Name
# - Purchase Count
# - Item Price
# - Total Purchase Value

# In[99]:


item_group = purchase_data.groupby(["Item ID","Item Name"])


# In[100]:


purchase_count_item = item_group["Price"].count()
purchase_count_item


# In[104]:


item_price = total_purchase_value/purchase_count_item
item_price


# In[101]:


total_purchase_value = item_group["Price"].sum()
total_purchase_value


# In[121]:


popular_item_data_frame = pd.DataFrame({"Purchase Count": purchase_count_item,
                                        "Item Price": item_price,
                                        "Total Purchase Value": total_purchase_value})
popular_item_data_frame.head()


# In[122]:


top_popular_item_data_frame = popular_item_data_frame.sort_values("Purchase Count", ascending=False)
top_popular_item_data_frame.head()


# ## Most Profitable Items
# Identify the 5 most profitable items by total purchase value, then list (in a table):
# 
# - Item ID
# - Item Name
# - Purchase Count
# - Item Price
# - Total Purchase Value

# In[123]:


top_profitable_item_data_frame = top_popular_item_data_frame.sort_values("Total Purchase Value", ascending=False)
top_profitable_item_data_frame.head()

