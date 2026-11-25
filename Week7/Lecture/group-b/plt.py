import matplotlib.pyplot as pt

days = ["mon", "tue", "wed", "thu"]
delays = [20, 30, 10, 5]
pt.plot(days, delays, marker="o", linewidth=2)
pt.grid(True)
pt.title("delaoy of ICE123 for a week")
pt.xlabel("day of the week")
pt.ylabel("min delayed")
pt.tight_layout()
pt.show()


weeks = ["w1", "w2", "w3"]
delays = [2, 4, 6]

pt.bar(weeks, delays)
pt.title("week comparision")
pt.xlabel("weeks")
pt.ylabel("delayed days")
pt.show()

pt.scatter(weeks, delays)
pt.show()

ages = [
    18,
    22,
    25,
    25,
    28,
    30,
    31,
    33,
    35,
    35,
    36,
    38,
    40,
    40,
    42,
    45,
    48,
    50,
    52,
    55,
    60,
]
pt.hist(ages, bins=5, edgecolor="white")
pt.show()
