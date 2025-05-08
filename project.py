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
        
        if user_input == '1':
            pass 
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else :
            exit() 


obj  = Chatbot()
            
        