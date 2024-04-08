import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample DataFrame
np.random.seed(0)
dates = pd.date_range('2022-01-01', periods=100)
df = pd.DataFrame({
    'Date': dates,
    'Value': np.random.randn(100).cumsum()
})

# Plotting with Pandas
df.plot(x='Date', y='Value', kind='line', title='Line Plot with Pandas', figsize=(10, 6))
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Plotting with Seaborn
plt.figure(figsize=(10, 6))
sns.set_style('whitegrid')  # Set seaborn style
sns.lineplot(data=df, x='Date', y='Value')
plt.title('Line Plot with Seaborn')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
