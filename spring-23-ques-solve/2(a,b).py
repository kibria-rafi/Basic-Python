userData = {"name": "rafi", "university": "diu", "sem": "5th"}
userData["sem"] = userData["sem"].replace("5th", "7th")


def chatGPT(data):
    print(f"hello {userData['name']}, how are u today?")
    
    res = input("you can ask me anything!\n")
    
    if res == "do you know me?":
        print(
            f"yes!, your are {userData['name']}. And you are from {userData['university']}. And you are in {userData['sem']} semester."
        )
      
    else:
        print("sorry i am unable to understand that!")
    q2 =input("ask me any question\n")
    if q2 == "Thanks for Your Information":
        print("thanks for your gratitute") 
    else:
        print("I dont know about that")     

chatGPT(userData)