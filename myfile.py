def greet_user(name):
    print("Hello, " + name)

user_name = "Alice"
age = 25

if age > 18:
    greet_user(user_name)  # SyntaxError due to missing colon
else:
    print("You are too young.")
