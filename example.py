# an example of using ustcwlt

import ustcwlt


wa = ustcwlt.WltAccount("name", "123456")

try:
    wa.login()
except ustcwlt.LoginError as err:
    print(err)
    exit()
    
print(wa.get_info())

wa.set_preference(8, 0)
wa.set_connection()
print("connected")

input("press any key to quit")
wa.logout()
