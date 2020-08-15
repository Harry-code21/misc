name,c =input("enter your name and a character separated by comma").split(",")
name=name.strip()
print(f"the length of name is {len(name)}")


print(f"character length :{name.strip().lower().count(c.strip().lower())}")




