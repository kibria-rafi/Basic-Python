user_name = ["healthMin", "relifeMin", "FoodMin"]
password = ["123health", "456relief", "789food"]
admin = {"imadmin": "123"}

u1, u2, u3 = user_name
p1, p2, p3 = password

d = {u1: p1, u2: p2, u3: p3}


def checkUser(username, password, d):
    if username in d and d[username] == password:
        return "valid user"
    else:
        return "invalid user"


def checkAdmin(aUsername, aPassword, ad):
    if aUsername in ad and ad[aUsername] == aPassword:
        return "valid admin"
    else:
        return "invalid admin"


def addNewUser(newUser, newPass, aU, aP, ad):
    if checkAdmin(aU, aP, ad) == "valid admin":
        d.update({newUser: newPass})
        return "new user added"
    else:
        return "invalid access"


print(checkUser("jishan", "1234", d))
print(checkAdmin("imadmin", "123", admin))
print(addNewUser("rifat", "987", "imadmin","123",admin))