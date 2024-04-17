import pandas as pd

data = pd.read_csv('divorces_data.csv')
data = data.dropna()

df = pd.DataFrame(data)

region = input("Enter a region: ")
filtered = df[(df['region'.lower()] == region) & (df['Residence'] == 'Total')]


if filtered.empty:
    print("Wrong region!")
   
else:
    print(filtered['region'],filtered['date'],filtered['divorce_count'])
    divorce_count = []

    for count in filtered['divorce_count']:
        d = int(count)
        divorce_count.append(d)

    total = sum(divorce_count)

    print('Total divorces in ' + region + ' from 2000 to 2022 is:', total)