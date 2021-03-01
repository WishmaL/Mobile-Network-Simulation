from Tests.User import User
import time
# The locations of the Base Stations


# Create 100 users
numberOfUser = 100

# users = [None] * numberOfUser
users = []

# for k in range(0, numberOfUser):
for k in range(0, 3):
    # Create different 10 users
    users.append(User(k))

    print("id = ",users[k].id)
    print("direction = ",users[k].direction)
    print("speed = ",users[k].speed)


print("------------ ------------ ------------ \n")

# following should start with (numberOfUser - 1)
sizeOfUsers = 2

# for testing
h = 1

# following should be while True
while h <= 10:

    # while useridx < len(users):
    for user in users:
        # if sizeUpdated:
        print("Size of the users list: ", len(users))
        print("\n")
        # each user is moved for 1 step
        print("users id = ", user.id)

        user.keepMove()

        # now if the boundary is reached user must be deleted and new user must be assigned
        if user.xValue > 10 or user.yValue > 10 or user.xValue < 0 or user.yValue < 0:
            # Remove the user
            users.remove(user)
            print("Size of the users list after remove: ", len(users))
            #       add a new user
            print("List updating")
            # create another user into the area
            sizeOfUsers += 1
            users.append(User(sizeOfUsers))
            print("test users id = ", user.id)
            sizeUpdated = True

        # Connect the user to a tower


        # disconnect the user Once the call is ended

    h += 1


