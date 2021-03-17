import ustcwlt


try:
    wa = ustcwlt.WltAccount("chi_zhang", "123456")
    wa.login()
except ustcwlt.LoginError as err:
    print(err)
