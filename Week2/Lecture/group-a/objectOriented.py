a1 = {"rooms": 2, "rent": 700, "city": "heidelberg"}
print(type(a1))


if 1 == "1":
    print("yes")
else:
    print("no")

a1 = 0

# all = [a1,]
limit_apartment = 500


class Apartment:
    limit = 500

    def __init__(self, passed_rooms, passed_rent, passed_city):

        self.rooms = passed_rooms
        self.city = passed_city
        self.rent = passed_rent

    def change_rent(self, new_rent):

        self.rent = new_rent

    def modify_limit(clss, new_limit):
        clss.limit = new_limit


a = Apartment(1, 700, "he")
b = Apartment(2, 900, "m")
# Apartment.moidfy_limit()
# Apartment.limit = "700"
print(a.city)
a.rent = "900"
a.change_rent(900)
print(a.limit)

a.include_utilites = 700
print(a.limit)
print(b.limit)

print(dir(a))
z = 1
print(dir(z))
