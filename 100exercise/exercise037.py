class mode_test:
    def __init__(self,list):
        self.list = list

    def sort(list):
        for i in range(len(list)):
            min = i
            for j in range(i + 1, len(list), 1):
                if list[j] < list[min]:
                    min = j
            tem = list[min]
            list[min] = list[i]
            list[i] = tem
        return list


if __name__ == '__main__':
    num = int(input('输入多少位数：'))

    list  = []
    for i in range(num):
        list.append(int(input('输入第'+str(i+1)+'位数：')))
    list =  sort(list)
    print(list)
