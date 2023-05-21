def wrestle():
    n = int(input())
    giant_list = []
    strength_list = []

    for i in range(n):
        strength = 0
        list = input().split()
        if len(list) == 4:
            list[1] = int(list[1])
            list[2] = int(list[2])
            list[3] = int(list[3])
            giant_list.append(list)
        elif len(list) == 2:
            list[1] = int(list[1])
            for i in range(len(giant_list)):
                start = giant_list[i][2]
                end = giant_list[i][3]
                time = list[1]

                if time >= start and time <= end:
                    if giant_list[i][1] > strength:
                        strength = giant_list[i][1]
            strength_list.append(strength)
            giant_list = []

    for i in range(len(strength_list)):
        print(strength_list[i])


wrestle()
