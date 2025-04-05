import numpy as np
import matplotlib.pyplot as plt
import random

matan = [4, 5, 5, 4, 5]
linal = [5, 5, 4, 5, 4, 5]
gos = [4, 4, 5, 5, 4, 5, 5]
hist = [5, 4, 5, 4, 5]

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.step(range(len(matan)), matan, 'r', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('Матанализ')
plt.grid()

plt.subplot(2, 2, 2)
plt.step(range(len(linal)), linal, 'b', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('Линейная алгебра')
plt.grid()

plt.subplot(2, 2, 3)
plt.step(range(len(gos)), gos, 'g', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('Государственность')
plt.grid()

plt.subplot(2, 2, 4)
plt.step(range(len(hist)), hist, 'm', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('История')
plt.grid()

plt.tight_layout()
plt.show()