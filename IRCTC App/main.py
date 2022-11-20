import admin
import user
x = admin.Admin().adminLogIn("bob", "bob")

y = user.User().searchTrainsByNo("47154")
for i in y:
    print(i)
