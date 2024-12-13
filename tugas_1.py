import pandas as pd
df = pd.read_csv(r'/content/Negara.csv')

# Select only numeric columns before calculating the mean
numeric_columns = df.select_dtypes(include=['number']).columns
rata = df.groupby(['Benua'])[numeric_columns].mean()  # Calculate mean for numeric columns only
std = df.groupby(['Benua'])[numeric_columns].std()   # Calculate std for numeric columns only


print('DATA NEGARA, BENUA, SEMUANYA DAH LENGKAP')
print(df)
print('Berikut Hasil Mean')
print(rata)
print('Standart Deviation')
print(std)