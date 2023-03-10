import pandas as pd   
import matplotlib.pyplot as plt 
df = pd.read_csv('countries_of_the_world.csv') 

df['Birthrate'].fillna('-1',inplace=True)
df['Deathrate'].fillna('-1',inplace=True)

def convert(Birthrate):
    if Birthrate == '0':
        return 0
    return float(Birthrate.replace(',','.'))

def conver2(Deathrate):
    if Deathrate == '0':
        return 0
    return float(Deathrate.replace(',','.'))

df['Birthrate'] = df['Birthrate'].apply(convert)
df['Deathrate'] = df['Deathrate'].apply(conver2)


rozdaemost = df[df['Region'] > 'ASIA (EX. NEAR EAST)']['Birthrate'].mean()
smertnost = df[df['Region'] > 'ASIA (EX. NEAR EAST)']['Deathrate'].mean()

print(rozdaemost/smertnost)

a = pd.Series(data = [rozdaemost, smertnost], index = ['Рождаемость','Смертность'])
a.plot(kind='pie')
plt.show()
#рождаемость в ASIA (EX. NEAR EAST) больше чем смертность