a = [900, "h", False, 800, "m", True]

b = {"rent": 900, "location": "h", "varification": False}

# c = {
#    "rent":"400"
# }
# a =[b]


class Apartment:
    limit = 5000

    def __init__(self, passed_rent, passed_location, passed_verification):
        self.rent = passed_rent
        self.location = passed_location
        self.verification = passed_verification

    def change_rent(self, new_rent):
        self.rent = new_rent

    # def change_limit(cls,)


apartment_1 = Apartment(400, "h", False)
print(apartment_1.rent)
apartment_2 = Apartment(700, "m", False)
apartment_1.rent = "900"
print(apartment_1.rent)
# apartmenit_1.change_rent(900)
print(apartment_1.limit)
apartment_1.limit = 7000
print(apartment_2.limit)

apartment_1.something = 5000
# Apartment.
print(type(apartment_1))

b = "srh"

print(dir(b))
