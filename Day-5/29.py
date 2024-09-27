# Print all the armstrong numbers in the range of 100 to 1000

def results(num):
    digits=list(map(int,(str(num))))
    len_digits=len(digits)
    sum_digits=sum(digit ** len_digits for digit in digits)
    return sum_digits == num

def print_100_1k(number:int):
    for num in range(100,number+1):
        if results(num):
            print(num)

if __name__=="__main__":
    print_100_1k(1000)