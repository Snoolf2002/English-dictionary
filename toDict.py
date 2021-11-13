with open('./sources/baseUnits.txt') as readBase:
  ls = readBase.read().split()
# lengthEngWords = len(ls)

# Inglizcha so'zlarni key o'zbchasini value sifatida dict ga joylassh
dictEng = {}
for i in range(0, len(ls), 2):
  dictEng[ls[i]] = list(ls[i+1].split(','))

# O'zbekcha so'zlarni list shaklida yozib olish
uzbWords = []
for i in dictEng.values():
  for j in i:
    uzbWords.append(j)

# Uzbekcha so'zlarni key inglizchasini value sifatida dict ga joylash
dictUzb = {}
for i in uzbWords:
  for j in dictEng.keys():
    if i in dictEng[j]:
      dictUzb[i]=j