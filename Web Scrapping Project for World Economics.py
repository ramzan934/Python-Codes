
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables = pd.read_html(URL)
df = tables[3]

df.columns = range(df.shape[1])
df = df[[0, 2]]
df = df.iloc[1:11, :]

df.columns = ['Country', 'GDP (Million USD)']

# Convert to integer
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert million to billion
df['GDP (Billion USD)'] = df['GDP (Million USD)'] / 1000

# Round values
df['GDP (Billion USD)'] = np.round(df['GDP (Billion USD)'], 2)

# Drop old column (optional)
df.drop(columns=['GDP (Million USD)'], inplace=True)

print(df)

df.to_csv('./Largest_economics.csv')

