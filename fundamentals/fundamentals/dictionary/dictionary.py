person = {
    "first_name": "Yifan",
    "last_name": "Qiu",
    "age": 24,
    "is_organ_donor": False
}

person["email"] = "yif.chu22@gmail.com"

print(person)

person["email"] = "changing the inital email"

# syntax : if key not in dict:

if "email" not in person:
    person["email"] = "this is a better way to prevent replacing existing value"


print(person)

print(person["email"])  #to access value ""

person.pop("email")  # to remove a key

print(person)

del person["is_organ_donor"]  #another method to delete

print(person)

person["job"] = "none at the moment"

a = person.get("job")

print(a)

b = person.get("address")  #when accessing an nonexisting key, default output is None

print(b)