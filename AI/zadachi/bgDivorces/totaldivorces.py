import pandas as pd

data = pd.read_csv('divorces_data.csv')
data = data.dropna()

df = pd.DataFrame(data)

filtered = df[(df['region_code'] == "BG") & (df['Residence'] == 'Total')]
print(filtered)
divorce_count = []

for count in filtered['divorce_count']:
    d = int(count)
    divorce_count.append(d)

total = 0

for i in divorce_count:
    total += i

print( 'Total divorces in Bulgaria from 2000 to 2022 is: ',total)
