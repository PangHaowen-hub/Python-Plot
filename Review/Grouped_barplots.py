import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# 统一设置字体
plt.rcParams["font.family"] = "Times New Roman"
# 统一设置字体大小
plt.rcParams['font.size'] = 20


x_labels = ['2018', '2019', '2020', '2021', '2022', '2023']
y_creation = [4, 4, 9, 16, 19, 11]
y_translation = [9, 17, 32, 40, 44, 43]
legend_labels = ['Creation', 'Translation']
y = [y_creation, y_translation]
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(facecolor='white')

x_loc = np.arange(6)
# x轴上每个刻度上能容纳的柱子的总的宽度设为0.8
total_width = 0.8
# 由y值可以看出x轴每个刻度上一共有3组数据, 也即3个柱子
total_num = 2
# 每个柱子的宽度用each_width表示
each_width = total_width / total_num
if total_num % 2 == 0:
    x1 = x_loc - (total_num / 2 - 1) * each_width - each_width / 2
else:
    x1 = x_loc - ((total_num - 1) / 2) * each_width
x_list = [x1 + each_width * i for i in range(total_num)]
print(x_list)

for i in range(0, len(y)):
    ax.bar(x_list[i], y[i], width=each_width, label=legend_labels[i])
ax.set_xticks(x_loc)
ax.set_xticklabels(x_labels)
ax.grid(True, ls=':', color='b', alpha=0.3)

fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.96), frameon=False, ncol=5, handlelength=0.9, handleheight=0.9, fontsize=14)
fig.tight_layout()
fig.subplots_adjust(top=0.9)
plt.savefig('Grouped_bar.png')  # 保存图片
plt.show()