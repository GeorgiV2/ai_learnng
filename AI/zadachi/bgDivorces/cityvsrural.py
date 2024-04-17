import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('divorces_data.csv')

df = pd.DataFrame(data)
# Replace every '-' in the DataFrame with NaN
df = df.replace('-', pd.NA)

# Remove every NaN number from the DataFrame
df.dropna(inplace=True)

city = df[df['Residence'] == 'City/Urban']
rural = df[df['Residence'] == 'Rural']


sum_city = []
sum_rural = [] 

for count in city['divorce_count']:
    if count != 'x':
      d = int(count)
      sum_city.append(d)

for count in rural['divorce_count']:
    if count != 'x':
        d = int(count)
        sum_rural.append(d)

total_city = 0
total_rural = 0

for i in sum_city:
    total_city += i

for i in sum_rural:
    total_rural += i

categories = ['City', 'Rural']
values = [total_city, total_rural]

print(total_city, total_rural)

fig, ax = plt.subplots(figsize=(5, 5))

bars = ax.bar(categories, values, color='blue')

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height),
            ha='center', va='bottom')

ax.set_title('City vs Rural')
ax.set_xlabel('Category')
ax.set_ylabel('Total')
ax.set_ylim(0,1200000)

plt.show()