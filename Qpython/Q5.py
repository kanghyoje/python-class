logs = [
        ("user1", "login"), 
        ("user2", "login"), 
        ("user1", "view"), 
        ("user1", "logout"), 
        ("user2", "view"), 
        ("user2", "logout"), 
        ("user1", "login")
        ]
users_dict = {"user1":0, "user2":0}

for user, log in logs:
  if user == "user1":
    if log == "login" or log == "view":
      users_dict[user] += 1

  elif user == "user2":
    if log == "login" or log == "view":
      users_dict[user] += 1

print(users_dict)

if users_dict["user1"] > users_dict["user2"]:
  print("user1")
  if users_dict["user1"] >= 2:
    print(['user1'])
elif users_dict["user1"] < users_dict["user2"]:
  print("user2")
  if users_dict["user2"] >= 2:
    print(['user2'])
