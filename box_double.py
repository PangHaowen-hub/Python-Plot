import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

file_path = r'G:\Lobectomy\dalian\RUL\RU.xls'

LL_before = pd.read_excel(io=file_path, sheet_name=0, header=None)
LL_after = pd.read_excel(io=file_path, sheet_name=1, header=None)

LL_before_value = LL_before.values[:, 1:]
LL_after_value = LL_after.values[:, 1:]
LL_before = pd.DataFrame(LL_before_value)
LL_after = pd.DataFrame(LL_after_value)

width = 0.7
x1 = list((1, 5, 9, 13, 17))
x2 = list((2, 6, 10, 14, 18))

plt.boxplot(LL_before, positions=x1, widths=width, patch_artist=True,
            boxprops={'color': 'black', 'facecolor': 'pink'})
plt.boxplot(LL_after, positions=x2, widths=width, patch_artist=True,
            boxprops={'color': 'black', 'facecolor': 'yellow'})
plt.xticks(ticks=[1.5, 5.5, 9.5, 13.5, 17.5], labels=['RU', 'RM', 'RL', 'LU', 'LL'])
plt.xlim(-0.5, 20)

rect1 = patches.Rectangle((0, 0), 1, 1, facecolor='pink')
rect2 = patches.Rectangle((0, 0), 1, 1, facecolor='yellow')
plt.ylim(0, 2500000)

plt.legend((rect1, rect2), ('before', 'after'), ncol=1)
plt.savefig('RUL_dalian.png')  # 保存图片
plt.show()
