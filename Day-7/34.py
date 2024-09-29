# Print first 25 prime numbers


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def find_first_n_primes(count):
#     prime_numbers = []
#     num = 2
#     while len(prime_numbers) < count:
#         if is_prime(num):
#             prime_numbers.append(num)
#         num += 1
#     return prime_numbers

# # Find the first 25 prime numbers
# user = 25
# prime_numbers = find_first_n_primes(user)
# print(prime_numbers)

def prime(number):
    prime_numebr=[]
    num=2
    while(len(prime_numebr)<number):
        is_true=True
        if num<2:
            is_true=False
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_true=False
                break
        if is_true:
            prime_numebr.append(num)
        num+=1
    return prime_numebr
print(prime(25))
