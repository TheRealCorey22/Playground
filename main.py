new_users = ['master-boom-ching', 'wobble23', 'chunkus22', 'ALWAYS YELLING']
old_users = []

def greetUser(names):

    for name in names:
        msg = f"Welcome, {(name).title()}!"
        print(msg)


def userMigration():
    while new_users[:]:
        old_user = (new_users[:].pop())
        print(f"{old_user} is old now!")
        old_users.append(old_user)       

greetUser(new_users)

userMigration()