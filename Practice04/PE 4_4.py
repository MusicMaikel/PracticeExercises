def new_password (oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else:
        return False

res = new_password('vakProg17', 'pyton17')
print(res)
print(new_password('huProg17', 'huProg17'))
print(new_password('vakProg17', 'Pro17'))
