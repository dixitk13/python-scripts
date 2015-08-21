__author__ = 'Dixit_Patel'
import math

def get_above_average(marks):
    avg = 0
    sum = 0
    for x in marks:
        sum = sum + int(x);


    avg = sum / len(marks)

    count = 0
    for x in marks:
        if x > avg:
            count = count + 1

    return math.ceil(float(count)/len(marks) * 100)

if __name__ == "__main__":
    #print('hi')
    marks =  [20,23,7]
    print(get_above_average(marks))