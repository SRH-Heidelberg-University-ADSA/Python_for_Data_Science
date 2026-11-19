data = {
    "name": ["alice", "bob", "carol"],
    "age": [30, 25, 35],
    "city": ["berlin", "munich", "hamburg"],
}

import sys

print(sys.path)
import pandas

df = pandas.DataFrame(data)
# print(df)

# df = pandas.read_csv()

# print(df.head(1))
# print(df.tail())

# print(df.shape)
# print(df.describe())
# print(df.columns)
# print(df.dtypes)
# print(df.info())

# print(df["name"])

print(df)

# print(df.loc[0])
# print(df.iloc[0])

filter = df[df["age"] >= 30]
print(filter)

# loc vs iloc for indexing
# print(filter.loc[1])
print(filter.iloc[1])

# cleaning
# df.isnull()
# df.isnull().sum()
# df['age'].duplicated()

# df.dropna()
# df.dropna(subset=['age'])
# df['age'].fillna(df['age'].mean())

# df.drop_duplicates() # exact duplicate
# df.drop_duplicates(subset=['name'])

# data type
# df['age'] = df['age'].astype(int)
# df['joined_date']=pandas.to_datetime(df['joined_date'])


# df.drop(columns=['age'], inplace=True)
# df.drop(index=2, inplace=True)

# df.groupby('city')['age']
#
#
# virtual env:
# venv
# conda   open source package version + python version
# poetry  open source package version + python version + which package manager
# pipenv
#
