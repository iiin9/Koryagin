# English в цифры. five hundred and fifty five
import re
import sys


def main():
    s = str(input())
    # s = 'one one'
    # s = "  fIve hundred and  fifty five  ".lower().strip()
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
           "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "seventeen": 17,
           "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
           "seventy": 70, "eighty": 80, "ninety": 90}
    res = re.split(r" ", s)
    result = []
    for item in res:
        if item == "" or item == "and":
            continue
        if item == "hundred":
            if result[int(len(result)) - 1] < 10:
                result[int(len(result)) - 1] *= 100
            else:
                return 'Ошибка: \"hundred\"'
            continue
        if dic.get(item) is None:
            return 'Error: \"' + item + '\"' + '\n' + "А чего ты ожидал? Говно на входе - говно на выходе"
            # raise SystemExit('Error: \"' + item + '\"' + '\n' + "А чего ты ожидал? Говно на входе - говно на выходе")
        result.append(dic.get(item))
    print("Распознанные данные(для debug'a:" + str(result))
    l = len(result)
    answer = 0
    for i in range(l):
        answer = answer + int(result[i])
    for i in range(l - 1):
        if(l>1 and int(result[i]) == 10 or int(result[i]) == 11 or int(result[i]) == 12 or int(result[i]) == 13 or int(result[i]) == 14 or int(result[i]) == 15 or int(result[i]) == 16 or int(result[i]) == 17 or int(result[i]) == 18 or int(result[i]) == 19):
            return 'Ошибка: \"' + str(result[i+1]) + '\"'
        if (result[i] < result[i + 1] and result[i] < 10 and result[i+1] > 9):
            return ("Ошибка: Число большей разрядности идет за числом меньшей разрядности: "
                    + str(result[i]) + " " + str(result[i + 1]))
        if (result[i] < result[i + 1] and result[i] < 100 and result[i] > 9 and result[i + 1] > 99):
            return ("Ошибка: Число большей разрядности идет за числом меньшей разрядности: "
                    + str(result[i]) + " " + str(result[i + 1]))
        if result[i] == result[i + 1]:
            # 10 20 числа одинакового формата
            return "Ошибка: Введено два одинаковых числа: "
                   #+ str(result[i]) + " " + str(result[i + 1]))
        if l > 1:
            if result[i] < 10 and result[i + 1] < 10:
                return "Ошибка: Введено два числа единичного формата: " + str(result[i]) + " " + str(result[i + 1])
            if result[i] < 100 and result[i + 1] < 100 and result[i] > 10 and result[i + 1] > 10:
                if result[0] < 100:
                    return "Ошибка: Введено два числа десятичного формата: " + str(result[i]) + " " + str(result[i + 1])

    print(answer)


num = 1
while num == 1:
    print(main())
