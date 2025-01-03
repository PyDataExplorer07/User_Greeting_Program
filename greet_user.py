from datetime import datetime

Username = input("Enter Your Name : ")
def greet_user(Username):
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    print(f"{greeting}! {Username} Hope you're having a great time!")

greet_user(Username)