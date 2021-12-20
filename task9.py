def homeWork():
    global max, min
    n = int(input())
    while True:
        numbers = [int(i) for i in input().split(' ')]
        if n == len(numbers):
            result = 0
            interMul = 1
            max = max(numbers)
            min = min(numbers)
            maxIndex = numbers.index(max)
            minIndex = numbers.index(min)

            if minIndex < maxIndex:
                for i in range(minIndex+1,maxIndex):
                    interMul *= numbers[i]

            elif minIndex > maxIndex:
                for i in range(maxIndex+1,minIndex):
                    interMul *= numbers[i]

            for j in numbers:
                if j>0:
                    result += j
            print(f'{result} {interMul}')
            break
        else:
            print("Try again !")

homeWork()
