import pandas as pd

data = pd.read_csv('zadachi/Spotify/Popular_Spotify_Songs.csv', encoding='ISO-8859-1')
authors = {}

for index, row in data.iterrows():
    name = row['artist(s)_name']
    track_name = row['track_name']
    playlist = str(row['in_spotify_playlists'])  # Convert to string
    if name not in authors:
        authors[name] = {'track_name': [], 'playlists': []}
    authors[name]['track_name'].append(track_name)
    authors[name]['playlists'].append(playlist)

# Create a DataFrame from the dictionary
df = pd.DataFrame([(name, track, playlist) for name, info in authors.items() for track, playlist in zip(info['track_name'], info['playlists'])],
                  columns=['artist(s)_name', 'track_name', 'in_spotify_playlists'])

# Convert 'in_spotify_playlists' column to integer
df['in_spotify_playlists'] = df['in_spotify_playlists'].astype(int)

# Sort the DataFrame by the 'in_spotify_playlists' column
sorted_df = df.sort_values(by='in_spotify_playlists', ascending=False)

print(data.columns)
#print(sorted_df[['track_name','in_spotify_playlists']])
