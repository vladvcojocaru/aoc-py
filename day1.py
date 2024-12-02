from re import split

def solution():
    with open("input/day1.txt") as f:
        index = 2
        list1, list2 = [], []
        list_dict = {}
        total_distance = []
        total_apparitions = 0

        for x in f:
            item1, item2 = x.split(maxsplit=1)
            list1.append(int(item1))
            list2.append(int(item2))

            if int(item1) not in list_dict:
                list_dict[int(item1)] = 0



        sorted_l1 = sorted(list1)
        sorted_l2 = sorted(list2)

        for i in range(len(list1)):
            if int(list2[i]) in list_dict.keys():
                list_dict[int(list2[i])] += 1

            total_distance.append(abs(sorted_l1[i] - sorted_l2[i]))


        for key, value in list_dict.items():
            total_apparitions += key * value


    print(f"total distance: {sum(total_distance)}\ntotal aparitions: {total_apparitions}")


if __name__ == "__main__":
    solution()
