import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Sample data: latitude and longitude of cities
cities = {
    'New York': (40.7128, -74.0060),
    'Los Angeles': (34.0522, -118.2437),
    'Chicago': (41.8781, -87.6298),
    'Houston': (29.7604, -95.3698),
    'Phoenix': (33.4484, -112.0740)
}

# Create a new figure with a GeoAxes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Plotting the map
ax.stock_img()
ax.coastlines()

# Plotting cities
for city, (lat, lon) in cities.items():
    ax.plot(lon, lat, 'o', transform=ccrs.Geodetic(), label=city)

# Add a legend
ax.legend()

# Set title and display the plot
ax.set_title('Cities Plot on Map')
plt.show()