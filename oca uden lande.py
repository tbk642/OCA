import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 1])
ypoints = np.array([1, 0])
plt.plot(xpoints, ypoints, color='black')
plt.text(0.2, 0.9, "OCA-line", size=12)
plt.text(0.2, 0.2, "Costs dominate benefits", size=12)
plt.text(0.5, 0.6, "Benefits dominate costs", size=12)
plt.ylabel('Share of output variance explained by regional shocks - Costs')
plt.xlabel('Share of intraregional trade - Benefits')
plt.show()
