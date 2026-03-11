def is_prime(num):
    divisibility_list=[]
    for n in range(1,num+1):
        if num%n==0:
            divisibility_list.append(n)
    if num==1 and num%1==0:
        return "1 is not a prime number"
    elif num in divisibility_list and num%1==0 and len(divisibility_list)==2:
        return f"{num} is a prime number {divisibility_list}"

    else:
        return f"{num} is not a prime number {divisibility_list}"

number=int(input("enter a number: "))
print(is_prime(number))