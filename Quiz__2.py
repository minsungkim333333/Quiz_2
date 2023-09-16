er = {"usd": 1320, "jpy": 950, "cny": 182}
money = [13, 200, 13]
dollar = er["usd"]*money[0]
yen = er["jpy"]*money[1]
yuan = er["cny"]*money[2]
print(dollar, yen, yuan)
print("철수가 가지고 있는 돈의 원화 가치는 %d 원 입니다." % (dollar+yen+yuan))
