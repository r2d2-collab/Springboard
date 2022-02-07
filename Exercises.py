def print_loop_method():
        print("print_loop_method")
        i = 1
        while(i<=10):
             print(i)
             i+=1

def sumit_method():
        print("sumit_method")
        x= 0
        # s = int(input("Enter number"))
        s = 5
        for i in range(1, s+1, 1):
            x+=i
        print("Sum = ",x)


def times_method():
        print("times_method")
        # x= int(input("Enter number"))
        x = 6
        for i in range(1, 15, 1):
            #x+=i
            print(i,"times =",x,"is",x*i)


def List_print_method():
        print("List_print_method")
        numbers = [10,20,30,40,50,60]
        for i in numbers:
                 print(i)


def length_of_string_method():
        print("length_of_string_method")
        i = 989565623232568
        print(len(str(i)))

def reverse_from_list_method():
        print("reverse_from_list_method")
        numbers = [10,20,30,40,50,60]
        new_numbers = reversed(numbers)
        for i in new_numbers:
             print(i)


def method_1():
        print("method_1")
        for i in range(-20,0,1):
             print(i)

        for i in range(-20,0,1):
              print(i)
        else:
             print("Done")


def method_2():
        print('method_2')
        begin = 10
        end = 80
        for i in range(begin,end +1):
            if i >1:
                for n in range(2,i):
                    if (i%n) == 0:
                        break
                else:
                    print(i)



def reverse_method1():
    print('reverse_method1')
    n = 6140314
    reverse = 0
    while n >0:
        remainder = n%10
        reverse = (reverse*10)+remainder
        n=n//10
        print (reverse)


def cubeit_method():
        # n=int(input("Number ?"))
        print('cubeit_method')
        n=5
        for i in range(1,n,+1):
            print(i,i**3)


def main():
    cubeit_method()
    print_loop_method()
    sumit_method()
    times_method()
    List_print_method()
    length_of_string_method()
    reverse_from_list_method()
    method_1()
    method_2()
    reverse_method1()
    length_of_string_method()
    length_of_string_method()



if __name__ == "__main__":
    main()
