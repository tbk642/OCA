import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 1])
ypoints = np.array([1, 0])
plt.plot(xpoints, ypoints, color='black')
plt.text(0.2, 0.9, "OCA-line", size=12)

plt.scatter([0.25],[0.1587], color='blue')
plt.text(0.26, 0.18, "Argentina", color='blue')

plt.scatter([0.49],[0.02386], color='black')
plt.text(0.5, 0.04, "Paraguay")

plt.scatter([0.34],[0.1468], color='green')
plt.text(0.34, 0.09, "Uruguay",color='green')

plt.ylabel('Share of output variance explained by regional shocks - Costs')
plt.xlabel('Share of Intraregional Trade - Benefits')
plt.show()