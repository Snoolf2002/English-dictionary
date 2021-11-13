from toDict import dictEng, dictUzb

# lsEng ga inglizcha so'zlarni list sifatida qabul qilyapmiz
lsEng = list(dictEng.keys())

# Inglizcha so'z beriladi tarjimasi tekshiriladi
def chekAnswerUzb(answer, keyWord):
  if answer in dictEng[keyWord]:
    return "Correct!!!"
  else:
    return "Wrong answer!"




# lsUzb ga o'zbekcha so'zlarni list sifatida qabul qilyapmiz
lsUzb = list(dictUzb)

# O'zbekcha so'z beriladi tarjimasi tekshiriladi
def chekAnswerEng(answer, value):
  if answer in dictUzb[value]:
    return True
  else:
    return False