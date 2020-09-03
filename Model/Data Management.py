import pandas as pd
import re
import folium
from dateutil.parser import parse
import cpi


housingDataFrame = pd.read_csv('Market_Data.csv')
housingDataFrame = housingDataFrame.dropna()
locationColumn = housingDataFrame['LOCATION_open_data']
locationList = []
lat = []
lon = []
for location in locationColumn:
    locationList.insert(len(locationList), re.sub('[()]', '', location))

for location in locationList:
    combo = location.split(", ")
    lat.insert(len(lat), combo[0])
    lon.insert(len(lon), combo[1])

housingDataFrame['LAT'] = lat
housingDataFrame['LON'] = lon

housingDataDict = []
for row in housingDataFrame.itertuples():
    if row[3] != 'No Sales History' or row[7] != 'No Sales History' and row[3] != '$1':
        housingDict = {'Date_Sold': row[2],
                       'Price': row[3],
                       'Total_Value': row[7],
                       'Census_Tract': row[11],
                       'Block_Group': row[12],
                       'SBL': row[13],
                       'Address': row[14],
                       'Neighborhood': row[15],
                       'Latitude': row[17],
                       'Longitude': row[18],
                       'Prior_Owner': row[6],
                       'Year': 0
                       }
        housingDataDict.insert(len(housingDataDict), housingDict)

for obj in housingDataDict:
    obj['Price'] = re.sub('[$]', '', obj['Price'])
    obj['Price'] = re.sub('[ ]', '', obj['Price'])
    obj['Price'] = float(obj['Price'].replace(',', ''))
    obj['Total_Value'] = re.sub('[$]', '', obj['Total_Value'])
    obj['Total_Value'] = re.sub('[ ]', '', obj['Total_Value'])
    obj['Total_Value'] = re.sub('[()]', '', obj['Total_Value'])
    obj['Total_Value'] = float(obj['Total_Value'].replace(',', ''))

for obj in housingDataDict:
    date = str(parse(obj['Date_Sold']).date())
    date = date[0:4]
    obj['Year'] = int(date)

housingDataDict = [i for i in housingDataDict if (i['Year'] <= 2020)]

m = folium.Map(location=[42.839278777194686, -78.80483461698972], zoom_start=12)

for index in range(0, len(housingDataDict)):
    if housingDataDict[index]['Neighborhood'] == 'MLK Park':
        folium.Circle(
            (housingDataDict[index]['Latitude'], housingDataDict[index]['Longitude']),
            popup="Address: " + housingDataDict[index]['Address'] + '\n' + 'Neighborhood: ' + housingDataDict[index]['Neighborhood'] + '\n' + 'Date Sold: ' + housingDataDict[index]['Date_Sold'] + '\n' + 'Prior Owner: ' +housingDataDict[index]['Prior_Owner'] + '\n' + 'Price: ' + str(housingDataDict[index]['Price']),
            radius=housingDataDict[index]['Price'] / 5000,
            color='red',
            fill=False
        ).add_to(m)

    if housingDataDict[index]['Neighborhood'] == 'Lower West Side':
        folium.Circle(
            (housingDataDict[index]['Latitude'], housingDataDict[index]['Longitude']),
            popup="Address: " + housingDataDict[index]['Address'] + '\n' + 'Neighborhood: ' + housingDataDict[index]['Neighborhood'] + '\n' + 'Date Sold: ' + housingDataDict[index]['Date_Sold'] + '\n' + 'Prior Owner: ' + housingDataDict[index]['Prior_Owner'] + '\n' + 'Price: ' + str(housingDataDict[index]['Price']),
            radius=housingDataDict[index]['Price'] / 5000,
            color='green',
            fill=False
        ).add_to(m)

    if housingDataDict[index]['Neighborhood'] == 'Fruit Belt':
        folium.Circle(
            (housingDataDict[index]['Latitude'], housingDataDict[index]['Longitude']),
            popup="Address: " + housingDataDict[index]['Address'] + '\n' + 'Neighborhood: ' + housingDataDict[index]['Neighborhood'] + '\n' + 'Date Sold: ' + housingDataDict[index]['Date_Sold'] + '\n' + 'Prior Owner: ' +housingDataDict[index]['Prior_Owner'] + '\n' + 'Price: ' + str(housingDataDict[index]['Price']),
            radius=housingDataDict[index]['Price'] / 5000,
            color='purple',
            fill=False
        ).add_to(m)

    if housingDataDict[index]['Neighborhood'] == 'Ellicott':
        folium.Circle(
            (housingDataDict[index]['Latitude'], housingDataDict[index]['Longitude']),
            popup="Address: " + housingDataDict[index]['Address'] + '\n' + 'Neighborhood: ' + housingDataDict[index]['Neighborhood'] + '\n' + 'Date Sold: ' + housingDataDict[index]['Date_Sold'] + '\n' + 'Prior Owner: ' +housingDataDict[index]['Prior_Owner'] + '\n' + 'Price: ' + str(housingDataDict[index]['Price']),
            radius=housingDataDict[index]['Price'] / 5000,
            color='blue',
            fill=False
        ).add_to(m)

    if housingDataDict[index]['Neighborhood'] == 'Pratt-Willert':
        folium.Circle(
            (housingDataDict[index]['Latitude'], housingDataDict[index]['Longitude']),
            popup="Address: " + housingDataDict[index]['Address'] + '\n' + 'Neighborhood: ' + housingDataDict[index]['Neighborhood'] + '\n' + 'Date Sold: ' + housingDataDict[index]['Date_Sold'] + '\n' + 'Prior Owner: ' +housingDataDict[index]['Prior_Owner'] + '\n' + 'Price: ' + str(housingDataDict[index]['Price']),
            radius=housingDataDict[index]['Price'] / 5000,
            color='brown',
            fill=False
        ).add_to(m)

    if housingDataDict[index]['Neighborhood'] == 'West Side':
        folium.Circle(
            (housingDataDict[index]['Latitude'], housingDataDict[index]['Longitude']),
            popup="Address: " + housingDataDict[index]['Address'] + '\n' + 'Neighborhood: ' + housingDataDict[index]['Neighborhood'] + '\n' + 'Date Sold: ' + housingDataDict[index]['Date_Sold'] + '\n' + 'Prior Owner: ' +housingDataDict[index]['Prior_Owner'] + '\n' + 'Price: ' + str(housingDataDict[index]['Price']),
            radius=housingDataDict[index]['Price'] / 5000,
            color='pink',
            fill=False
        ).add_to(m)

m.save('2020.html')
