import json
import string
import random
def create_name():
    s = string.ascii_letters
    files_names = []
    name = ''
    for _ in range(random.randint(4,15)):
        name += random.choice(s)
    return name
def create_password():
    s = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(12):
        password += random.choice(s)
    return password

json_object = dict()
json_object["name"] =create_name()
json_object["age"] = random.randint(1,100)
json_object["email"] = str(json_object.get("name"))+"@gmail.com"
json_object["password"] = create_password()

json_object = json.dumps(json_object)
with open("test1.txt","a", encoding= "utf-8") as file:
    file.write(json_object + "\n")
with open("test1.txt","r", encoding= "utf-8") as file:
    print(file.read())





