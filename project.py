##project 

class Chatbot:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggeing = False 

        self.main()


    def main(self):
        user_input = input('''
                       1. press 1 to sign up 
                       2. press 2 to login
                       3. press 3 write a post 
                       4. press 4 to message a friend 
                    5. press 5 to exit ''')
        
        if user_input == "1":
            self.signup()
        elif user_input == '2':
            self.login()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else :
            exit() 

    def signup(self):
        user_email = input("enter your username here--->   ")
        pass_word  = input("enter your password here--->   ")
        self.username = user_email
        self.password = pass_word
        print("you have successfully signed up")
        print("\n")
        self.main()
    
    def login(self):
        if self.username == "" or self.password == "":
            print("please signup by pressing 1 first")
        else:
            uname= input("enter your username here--->")
            pwd= input("enter your password here--->")
            if self.username == uname and self.password == pwd:
                print("you have successfully logged in")
                self.loggeing = True
            else:
                print("please enter the correct username and password")
        print("\n")
        self.main()

obj  = Chatbot()
            
        