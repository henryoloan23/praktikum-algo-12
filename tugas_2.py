import pandas as pd
df = pd.read_csv(r'D:\ZCODING\percobaan\Negara.csv')


rata = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()


print('DATA NEGARA, BENUA, SEMUANYA DAH LENGKAP')
print(df)
print('=========================================================')
print(rata)
print('=========================================================')
print(std)
