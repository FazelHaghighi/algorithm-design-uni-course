list = [1]


def prepend(value):
    list.insert(0, value)


def append(value):
    list.append(value)


def insert(index, value):
    list.insert(index, value)


def get_input():
    number = int(input())
    for i in range(number):
        index = input()
        value = i + 2
        if index == "begin":
            prepend(value=value)
        elif index == "end":
            append(value=value)
        elif index == "mid":
            if len(list) % 2 == 0:
                index = len(list) // 2
            else:
                index = (len(list) // 2) + 1

            insert(index=index, value=value)


get_input()
print(list)
