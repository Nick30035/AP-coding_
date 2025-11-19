a = 100
b = 0
if b > a:"student did not turn in homework"
print("b is greater than a,student did not turn in homework")
a = 0
b = 100
if a > b:"student did turn in homework"
print("a is greater than b,student did turn in homework")





def reverseString(word):
    text = word[::-1]
    print(text)

reverseString('cat')



def pdCheck():
    print("Please enter a number")
    number= input()
    values = []

    while number != 'q':
        values.append(int(number))
        print(values)
        print("please enter a number")
        number = input()
    else:
     print('doing calculation') 
     total = sum(values)
    print(total)

    pdCheck()