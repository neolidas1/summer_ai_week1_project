#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            user = ai_social_network.create_account()
            

        elif choice == "2":
            name = input("What account do you want to log in to? ")
            ai_social_network.get_current_user(name) 
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "6":
                    break
                elif inner_menu_choice == "1":
                    edditedName = input("Enter your new name, your original name was " + str(user.id) + ". New name: " )
                    edditedAge = input("Enter your new age, your originial name was " + str(user.year) + ". New age: ")
                    bio = input("What is your favorite animal? Favorite movie? Favorite book? Put down anything interesting about yourself down here! ")
                    user.id = edditedName 
                    user.year = edditedAge 
                elif inner_menu_choice == "2": 
                    requestedfriend = input("What is your friend's name: ")
                    print("Great! She is now in your list.")
                    break 
                elif inner_menu_choice == "3":
                    user.view_friends(user.friendlist)
                elif inner_menu_choice == "5":   
                    remove_friend = input("Who do you want to block? ")
                    user.remove_friend(remove_friend)

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()