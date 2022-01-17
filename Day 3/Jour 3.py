if __name__ == '__main__':
    f = open("day 3.txt", "r")

    data = f.read().split('\n')
    dataInt = []
    dataInt = [entry.strip() for entry in dataInt]
    string_data = dataInt

    # gamma = 0
    # epsilon = 0
    gamma, epsilon = '', ''
    for i in dataInt:
        blabla = [entry[i] for entry in data]
        if blabla.count('0') > len(data) / 2:
                gamma += '0'
                epsilon += '1'
        else:
                gamma += '1'
                epsilon += '0'

                int_dataInt = dataInt(map(int, string_data))
    multi = gamma * epsilon
    print(multi)
