import matplotlib.pyplot as plt
# saraksts ar gada videjam temperaturam no 2010 liddz 2020 gadam
temps_2010 = [1.3, 7.3, 7.2, 11.0, 13.5, 11.3, 12.3, 12.7, 6.0, 7.0, 5.3, 1.1]
temps_2015 = [0.9, 5.7, 3.1, 8.7, 13.1, 11.0, 10.9, 15.8, 16.6, 6.2, 1.9, 3.6]
temps_2020 = [1.3, 2.9, 7.9, 14.8, 15.1, 11.0, 18.8, 16.7, 8.8, 8.0, 3.9, 1.5]
months = list( range(1, 13))
plt.plot(months, temps_2010, months, temps_2015, months, temps_2020)
plt.legend([2010, 2015, 2020])
plt.title("Temperaturas")
plt.xlabel("Menesi")
plt.ylabel("Temperatura")
plt.show()
