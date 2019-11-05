# English в цифры. five hundred and fifty five
import re
import sys
from threading import Thread


def main():
    s = str(input())
    # s = 'one one'
    # s = "  fIve hundred and  fifty five  ".lower().strip()
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
           "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "seventeen": 17,
           "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
           "seventy": 70,
           "eighty": 80,
           "ninety": 90}
    res = re.split(r" ", s)
    result = []
    # print(res)
    i = 0
    for item in res:
        if item == "" or item == "and":
            continue
        if item == "hundred":
            result[int(len(result)) - 1] *= 100
            continue
        if dic.get(item) == None:
            raise SystemExit('Error: \"' + item + '\"' + '\n' + "А чего ты ожидал? Говно на входе - говно на выходе")

        result.append(dic.get(item))
        i += 1
    l = len(result)
    # print(l)
    answer = 0
    for i in range(l):
        answer = answer + int(result[i])
    for i in range(l - 1):
        if result[i] < result[i + 1]:
            raise SystemExit("Ошибка: Число большей разрядности идет за числом меньшей разрядности: ")
            # + str(result[i]) + " " + str(result[i + 1]))
        if result[i] == result[i + 1]:
            sys.exit()
            raise SystemExit("Ошибка: Введено два одинаковых числа: ")
            # + result[i] + "," + result[i + 1])
        if l > 1:
            if result[i] < 10 and result[i + 1] < 10:
                raise SystemExit("Ошибка: Введено два числа единичного формата: ")
                # + result[i] + "," + result[i + 1])
            if result[i] < 100 and result[i + 1] < 100:
                raise SystemExit("Ошибка: Введено два числа десятичного формата: ")
    # for i in range(l):
    #         answer += result[i]

    # for c, item in enumerate(result):
    #     cc = c + 1
    #     if result[c] < result[cc]:
    #         print("Ошибка: Число большей разрядности идет за числом меньшей разрядности")
    #     if result[c] == result[cc]:
    #         print("Ошибка: Введено два одинаковых числа")
    print("Распознанные данные(для debug'a:" + result)
    print(answer)
thread1 = Thread(target=main())
num = 1
while num < 10:
    thread1.start()
    thread1.join()
