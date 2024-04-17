import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('imdb.csv')


genre_d = data['genre'].str.split(', ').explode().reset_index(drop=True)


genre_ratings = {}


for index, row in data.iterrows():
    rating = float(row['rating'])  
    genres = row['genre'].split(', ')  
    for genre in genres:

        # setdefault() proverqva dali ima takuv kluch ( genre), i ako nqma slaga default value ( [] ) koqto tuke e 0.
        # Ako ima, toi vrushta stoinostta na tozi kluch
        # Sled tova dobavqme kum lista koito e [] , sus append( stoinostta koqto iskame da dobavim)
        genre_ratings.setdefault(genre, []).append(rating)  # Append rating to genre

for x in genre_ratings:
    rating = sum(genre_ratings[x]) / len(genre_ratings[x])
    genre_ratings[x] = rating
   
  
decimal_places = 2


for key, value in genre_ratings.items():
    
    rounded_value = round(value, decimal_places)
   
    genre_ratings[key] = rounded_value


final = pd.DataFrame(list(genre_ratings.items()), columns=['genre', 'average_rating'])


final = final.sort_values(by='average_rating', ascending=False)


final.plot('genre', 'average_rating', kind='bar', title='Most preffered genre', figsize=(10, 10))
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

