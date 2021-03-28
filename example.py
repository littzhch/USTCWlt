# an example of using ustcwlt

import ustcwlt

name = input("name:")
password = input("password:")
wa = ustcwlt.WltAccount(name, password)

try:
    wa.login()
except ustcwlt.LoginError as err:
    print(err)
    exit()
    
print(wa.get_info())
wa.set_connection(8, 0)
print("connected")
input("press any key to quit")
wa.logout()
