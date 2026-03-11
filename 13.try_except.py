try:
    age = int(input("How old are you?"))
except ValueError:
    print("please retry entering an integer for age")
    age=int(input("how old are you?"))

if age > 18:
    print("You can drive at age {age}.")
