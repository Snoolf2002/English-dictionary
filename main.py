from functionDictionary import chekAnswerEng, chekAnswerUzb, lsUzb, lsEng
import random

correctAnswers = 0
wrongAnswers = 0

request = input("Eng-Uzb(1), Uzb-Eng(2): ")
while request!='1' and request!='2':
  request = input("Eng-Uzb(1), Uzb-Eng(2): ")

if request=='1':
  for i in range(2*len(lsEng)):
    keyWord = random.choice(lsEng)
    print(keyWord)
    answerUzb = input()
    ans = chekAnswerUzb(answerUzb, keyWord)
    if ans=="Correct!!!":
      correctAnswers+=1
    else:
      wrongAnswers+=1
    print(ans)
else:
  for i in range(2*len(lsUzb)):
    value = random.choice(lsUzb)
    print(value)
    answerEng = input()
    ans = chekAnswerEng(answerEng, value)
    if ans=="Correct!!!":
      correctAnswers+=1
    else:
      wrongAnswers+=1
    print(ans)

print(f"You answered {correctAnswers} correct {wrongAnswers} incorrect answers.")
