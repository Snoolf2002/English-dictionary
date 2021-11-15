from functionDictionary import chekAnswerEng, chekAnswerUzb, lsUzb, lsEng
import random

correctAnswers = 0
wrongAnswers = 0
wrongAnswersList = []

request = input("Eng-Uzb(1), Uzb-Eng(2): ")
while request!='1' and request!='2':
  request = input("Eng-Uzb(1), Uzb-Eng(2): ")

if request=='1':
  wrongAnswersList = lsEng
  for i in range(len(lsEng)):
    if len(lsUzb)==0:
      break
    keyWord = random.choice(lsEng)
    print(keyWord)
    answerUzb = input()
    ans = chekAnswerUzb(answerUzb, keyWord)
    if ans=="Correct!!!":
      correctAnswers+=1
      wrongAnswersList.remove(keyWord)
    else:
      wrongAnswers+=1
    print(ans)
else:
  wrongAnswersList = lsEng
  for i in range(len(lsUzb)):
    if len(lsUzb)==0:
      break
    value = random.choice(lsUzb)
    print(value)
    answerEng = input()
    ans = chekAnswerEng(answerEng, value)
    if ans=="Correct!!!":
      correctAnswers+=1
      wrongAnswersList.remove(value)
    else:
      wrongAnswers+=1
    print(ans)

print(f"You answered {correctAnswers} correct {wrongAnswers} incorrect answers.")

# Xatolar bilan ishlash uchun qism
correctAnswers = 0
wrongAnswers = 0

request2 = input("Xatolar bilan ishlashni hohlaysizmi? Ha(1)/Yo'q(2): ")
while request2!='1' and request2!='2':
  request2 = input("Ha(1)/Yo'q(2): ")

while len(wrongAnswersList)!=0:
  if request2=='1' and request=="1":
    for i in range(2*len(wrongAnswersList)):
      if len(wrongAnswersList)==0:
        break
      keyWord = random.choice(wrongAnswersList)
      print(keyWord)
      answerUzb = input()
      ans = chekAnswerUzb(answerUzb, keyWord)
      if ans=="Correct!!!":
        wrongAnswersList.remove(keyWord)
        correctAnswers+=1
      else:
        wrongAnswers+=1
      print(ans)
  elif request2=='1' and request=="2":
    for i in range(2*len(wrongAnswersList)):
      if len(wrongAnswersList)==0:
        break
      value = random.choice(wrongAnswersList)
      print(value)
      answerEng = input()
      ans = chekAnswerEng(answerEng, value)
      if ans=="Correct!!!":
        correctAnswers+=1
        wrongAnswersList.remove(value)
      else:
        wrongAnswers+=1
      print(ans)
  print(f"You answered {correctAnswers} correct {wrongAnswers} incorrect answers.")
print("Congratulation!!!")