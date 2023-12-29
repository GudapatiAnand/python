def is_prime(number):
    if number>1:
        for num in range(2,number):
            if number%num==0:
                return "Not a Prime number"
            return "Prime number"
        return "Not a Prime number"
d=int(input("Enter the number:"))
print(is_prime(d))