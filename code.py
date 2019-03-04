# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
#Code starts here
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))



# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',
np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries= data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
#print(top_countries)
top_countries.drop(top_countries.index[-1],inplace=True)
#print(top_countries)

def top_ten(topcountries, colname):
    country_list=[]
    top_ten=topcountries.nlargest(10,colname)
    country_list=top_ten['Country_Name'].tolist()
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

#print(top_10_summer)
#print(top_10_winter)
#print(top_10)

common=[x for x in top_10_summer if x in top_10_winter and x in top_10]
print(common)






# --------------
#Code starts here
#print(top_10)
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
#print(summer_df)

fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,30))
ax_1.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax_1.set_xlabel("Country",fontsize = 20)
ax_1.set_ylabel("Total Medals",fontsize = 20)
ax_1.set_title("Summer Games",fontsize = 20)

ax_2.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
ax_2.set_xlabel("Country",fontsize = 20)
ax_2.set_ylabel("Total Medals",fontsize = 20)
ax_2.set_title("Winter Games",fontsize = 20)

ax_3.bar(top_df['Country_Name'],top_df['Total_Medals'])
ax_3.set_xlabel("Country",fontsize = 20)
ax_3.set_ylabel("Total Medals",fontsize = 20)
ax_3.set_title("All Games",fontsize = 20)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df['Country_Name'].loc[summer_df['Golden_Ratio'].idxmax()]

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df['Country_Name'].loc[winter_df['Golden_Ratio'].idxmax()]

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df['Country_Name'].loc[top_df['Golden_Ratio'].idxmax()]

print(top_country_gold)




# --------------
#Code starts here
data_1=data.drop(data.index[-1],inplace=False)



data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)
most_points=data_1['Total_Points'].max()
best_country=data_1['Country_Name'].loc[data_1['Total_Points'].idxmax()]
print(most_points)
print(best_country)



# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel(best_country)
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()



