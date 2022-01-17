if __name__ == '__main__':
    f = open("day 3.txt", "r")

    data = f.read().split('\n')
    dataInt = []
    dataInt = [entry.strip() for entry in dataInt]
    O2List = []
    CO2List = []

    for i in data:
        O2List.append(i)
        CO2List.append(i)


    # HERE BEGINS THE O2 WINNOWING

    numIndex = 0
    bitIndex = 0

    while bitIndex in range(len(data[numIndex])):

        myO2OnesinColumnTally = 0
        while numIndex in range(len(O2List)):# possible
            if O2List[numIndex][bitIndex]=='1':
                myO2OnesinColumnTally += 1

            numIndex += 1

        myO2ZerosinColumnTally = len(O2List) - myO2OnesinColumnTally

        if myO2OnesinColumnTally>myO2ZerosinColumnTally:
            print(f'The most common bit in column {bitIndex} is 1.')

        else:
            print(f'The most common bit in colum {bitIndex} is 0.')

        numIndex = 0
        while numIndex in range(len(O2List)):
            if myO2OnesinColumnTally>=myO2ZerosinColumnTally: # THIS IS WHERE THE PROBLEM ISs
                myIndex = 0
                myListSize = len(O2List)
                while myIndex<myListSize and myListSize>=2:
                    if O2List[myIndex][bitIndex]=='0':
                        O2List.pop(myIndex)
                    else:
                        myIndex += 1

                    myListSize = len(O2List)


            else:
                myIndex = 0
                myListSize = len(O2List)
                while myIndex<myListSize and myListSize>=2:
                    if O2List[myIndex][bitIndex]=='1':
                        O2List.pop(myIndex)
                    else:
                        myIndex += 1

                    myListSize = len(O2List)

            numIndex += 1

        numIndex = 0

        bitIndex += 1



    # HERE BEGINS THE CO2 NARROWING

    numIndex = 0
    bitIndex = 0

    while bitIndex in range(len(data[numIndex])):

            myCO2OnesinColumnTally = 0
            while numIndex in range(len(CO2List)):# possible
                if CO2List[numIndex][bitIndex]=='1':
                    myCO2OnesinColumnTally += 1

                numIndex += 1

            myCO2ZerosinColumnTally = len(CO2List) - myCO2OnesinColumnTally

            if myCO2OnesinColumnTally>myCO2ZerosinColumnTally:
                print(f'The most common bit in column {bitIndex} is 1.')

            else:
                print(f'The most common bit in column {bitIndex} is 0.')

            numIndex = 0
            while numIndex in range(len(CO2List)):

                if myCO2OnesinColumnTally<myCO2ZerosinColumnTally:

                    myIndex = 0
                    myListSize = len(CO2List)
                    while myIndex<myListSize and myListSize>=2:
                        if CO2List[myIndex][bitIndex]=='0':
                            CO2List.pop(myIndex)
                        else:
                            myIndex += 1

                        myListSize = len(CO2List)

                else:

                    myIndex = 0
                    myListSize = len(CO2List)
                    while myIndex<myListSize and myListSize>=2:
                        if CO2List[myIndex][bitIndex]=='1':
                            CO2List.pop(myIndex)
                        else:
                            myIndex += 1

                        myListSize = len(CO2List)

                numIndex += 1

            numIndex = 0

            bitIndex += 1


    binO2 = O2List[0]
    finalO2 = 0
    powerOfTwo = 1
    for bit in range(len(binO2)-1, -1, -1):
        try:
            next = int(binO2[bit])
            finalO2 += powerOfTwo*next
            powerOfTwo = powerOfTwo*2
        except:
            pass

    binCO2 = CO2List[0]
    finalCO2 = 0
    powerOfTwo = 1
    for bit in range(len(binCO2)-1, -1, -1):
        try:
            next = int(binCO2[bit])
            finalCO2 += powerOfTwo*next
            powerOfTwo = powerOfTwo*2
        except:
            pass



    print(f"MY O2 GENERATOR RATING IS {O2List}, {finalO2} AND MY "
            f"CO2 SCRUBBER RATING IS {CO2List}, {finalCO2}.")

    powerConsumption = finalO2*finalCO2

    print(f"My power consumption is allegedly {powerConsumption}.")



