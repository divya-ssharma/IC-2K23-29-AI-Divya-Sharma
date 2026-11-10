import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'age': [22, 25, np.nan, 28, 24, 26],
    'marks': [78, 85, 90, np.nan, 70, 88],
    'placed': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())

# df = df.dropna()

df['age'] = df['age'].fillna(df['age'].mean())
df['marks'] = df['marks'].fillna(df['marks'].median())

df['placed'] = df['placed'].map({'Yes': 1, 'No': 0})

print(df)
print(df.describe())

plt.figure()
plt.hist(df['marks'], bins=5)
plt.savefig('marks_hist.png')
plt.close()

plt.figure()
plt.scatter(df['age'], df['marks'])
plt.savefig('age_marks.png')
plt.close()

print("ok")
