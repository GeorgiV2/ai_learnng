import pandas as pd

data = pd.read_csv('Popular_Spotify_Songs.csv', encoding='ISO-8859-1')
dates = {}
months = {"Winter": 0,"Spring": 0, "Summer": 0, "Fall": 0}
for index, row in data.iterrows():
    month = row['released_month']
    track_name = row['track_name']
    if track_name not in dates:
        dates[track_name] = { 'released_month': []}
    dates[track_name]['released_month'].append(month)

for track in dates:
    #Extract the first released month for the track
    first_month = dates[track]['released_month'][0]
    
    first_month = int(first_month)

    #Update the season based on the release month
    if first_month in [1, 2, 12]:
        dates[track]['released_month'] = "Winter"
        months['Winter'] += 1
    elif first_month in [3, 4, 5]:
        dates[track]['released_month'] = "Spring"
        months['Spring'] += 1
    elif first_month in [6, 7, 8]:
        dates[track]['released_month'] = "Summer"
        months['Summer'] += 1
    elif first_month in [9, 10, 11]:
        dates[track]['released_month'] = "Fall"
        months['Fall'] += 1

#Making a DataFrame for songs count on every month and sorting it to see which season has the most songs released
df = pd.DataFrame.from_dict(months, orient='index', columns=['Count'])
sorted_df = df.sort_values("Count",ascending=False)


print(sorted_df)
  