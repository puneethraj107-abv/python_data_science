#RANGE FUNC.
sum=0
for num in range(1,101):
    sum+=num
print(sum)

score = 0
for number in range(1,101):
    score = number

    if score % 3 == 0:
        score= "fizz"
        print(score)
    elif score % 5 == 0:
        score ="buzz"
        print(score)
    else:
        print(score)