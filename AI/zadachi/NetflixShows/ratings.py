import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('zadachi/NetflixShows/imdb.csv')

# Split genres into individual rows
genre_d = data['genre'].str.split(', ').explode().reset_index(drop=True)

# Initialize a dictionary to store total ratings and counts for each genre
genre_ratings = {}

# Iterate over each row in the DataFrame to accumulate ratings for each genre
for index, row in data.iterrows():
    rating = float(row['rating'])  # Convert rating to float
    genres = row['genre'].split(', ')  # Split genres into a list
    for genre in genres:

        # setdefault() proverqva dali ima takuv kluch ( genre), i ako nqma slaga default value ( [] ) koqto tuke e 0.
        # Ako ima, toi vrushta stoinostta na tozi kluch
        # Sled tova dobavqme kum lista koito e [] , sus append( stoinostta koqto iskame da dobavim)
        genre_ratings.setdefault(genre, []).append(rating)  # Append rating to genre

for x in genre_ratings:
    rating = sum(genre_ratings[x]) / len(genre_ratings[x])
    genre_ratings[x] = rating
   # genre_ratings.update(rating)
  
decimal_places = 2

# Iterate over each key-value pair in the dictionary
for key, value in genre_ratings.items():
    # Round the float value to the specified number of decimal places
    rounded_value = round(value, decimal_places)
    # Update the value in the dictionary with the rounded value
    genre_ratings[key] = rounded_value

# Convert the dictionary to a DataFrame
final = pd.DataFrame(list(genre_ratings.items()), columns=['genre', 'average_rating'])

# Sort the DataFrame by average rating in descending order
final = final.sort_values(by='average_rating', ascending=False)

# Print the resulting DataFrame
final.plot('genre', 'average_rating', kind='bar', title='Most preffered genre', figsize=(10, 10))
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

