import pandas as pd

print("Extract the data")

data = {
    'Id': [101, 102, 103],
    'name': ['Ram', 'Sham', 'Raju'],
    'age': [20, 30, 40]
}

df = pd.DataFrame(data)

print(df)
