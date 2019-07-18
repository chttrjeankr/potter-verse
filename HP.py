import pandas as pd

# df = pd.DataFrame()

# spells = open('spells.txt')

# df = pd.DataFrame(map(lambda X: X.split('-').strip(),spells))
df = pd.DataFrame(map(lambda X: map(str.strip,X.split('-')),open('spells.txt')),columns = ['Spells','Reactions'])
# df.columns = ['Spells','Reactions']
print(df.head())
# for i in df['Spells'].to_list():
# 	print(i in df['Spells'].to_list())
while True:
	cast = input()
	# print(cast)
	# new_df = df[df['Spells'] == cast]
	# print(df[df['Spells'].to_list())
	print(df[df['Spells'] == cast]['Reactions'].to_list()[0])
