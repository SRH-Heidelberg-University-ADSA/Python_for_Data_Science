import matplotlib.pyplot as plt

days = ["mon", "tue", "wed", "thu"]
delay = [20, 30, 22, 5]

# plt.plot(days, delay, marker="o", linewidth=2)
# plt.title("delay during the week")
# plt.xlabel("Day of the week")
# plt.ylabel("minutes in delay")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

weeks = ["w1", "w2", "w3", "w4"]
delay = [3, 6, 3, 1]
# plt.bar(weeks, delay)
# plt.title("week delays")
# plt.xlabel("Delay by week")
# plt.ylabel("days delayed")
# plt.show()

# plt.scatter(days, delay)
# plt.xlabel("days of the week")
# plt.ylabel("delay in minutes")
# plt.show()


import matplotlib.pyplot as mt

ages = [18, 22, 25, 25, 30, 31, 33, 35, 35, 36, 38, 40, 40, 42, 45, 48, 50, 52, 55, 60]

mt.hist(ages, bins=5, color="blue", edgecolor="white")
mt.title("age distribution")
mt.xlabel("age distribution of the population")
mt.ylabel("number of citizen")
mt.show()
