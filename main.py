print("""\33[1mGreetings and welcome to Zoul's vault.\33[0m

Please enter the \33[4musername\33[0m and \33[4mPIN code\33[0m to gain access to Zoul's \33[1;31mTop Secret File\33[0m.\n""")

logged_in = False
new_password = None

while logged_in == False:
    username = input("Username: ").lower().capitalize()
    password = input("PIN code: ")

    if username != "Zoul":
        print("\n\33[31mInvalid username\33[0m")
        print("")

    elif username == "Zoul" and password == "240794":
        logged_in = True
        print("""
\33[32m---Logged in---\33[0m
\33[1mCongratulations!\33[0m

You have successfully gained access to Zoul's \33[1;31mTop Secret File\33[0m! Amazing!
Send Zoul a screenshot of this message and tell him the correct username and PIN code. He will buy you a \33[1;32mMcDonald's Ice-cream\33[0m!🍦

\33[3mThanks so much for supporting~!\33[0m🥰""")

    elif username == "Zoul" and password == new_password:
        logged_in = True
        print("""
\33[32m---Logged in---\33[0m
\33[1mWelcome!\33[0m

You have managed to log in to Zoul's \33[1;34mSecret File\33[0m!
Unfortunately, since you have forgotten Zoul's birthday, you will not receive any prizes.😢

Try again when you have figured out the real PIN code!🤭

\33[3mBye~\33[0m""")

    elif username == "Zoul" and password == "":
        print("\n\33[33mHint: ddmmyy\33[0m\n")
    
    elif username == "Zoul" and password != "240794":
        while new_password == None:
            forgot_password = input("\n\33[33mForgot PIN code?\33[0m Y/N\n").upper()
            if forgot_password == "Y":
                from pass_gen import *
                password = new_password
                
            elif forgot_password == "N":
                print("")
                break
            else:
                print("\nInvalid input")
    
    else:
        print("\n\33[31mInvalid username and Pin code\33[0m")
        print("")