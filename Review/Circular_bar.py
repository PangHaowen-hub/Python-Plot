import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"
# 数据
np.random.seed(123)
group1 = [4, 12, 13, 2, 2]  # Classification
group2 = [8, 5, 3, 7]  # Segmentation
group3 = [6, 2, 3, 1]  # Other tasks
group4 = [47, 15, 2, 1]  # MRI
group5 = [57, 12, 2, 5]  # CT
group6 = [3, 3, 2]  # X-ray
group7 = [4, 2]  # PET
group8 = [1]  # US
group9 = [7, 9]  # NC-CE

groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9]
group_names = list('ABCDEFGHI')
group_colors = ['#ff706d', '#7baf06', '#01bfc5', '#cb7bf6', '#ff706d', '#7baf06', '#01bfc5', '#cb7bf6', '#7baf06']

# 画图
fig = plt.figure(figsize=(6, 6), dpi=300, facecolor='white')
ax = fig.add_subplot(projection='polar')

ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

radii = [0]
colors = ['white']
for g, c in zip(groups, group_colors):
    radii.extend(g)
    colors.extend([c] * len(g))
    radii.append(0)
    colors.append('white')
radii.pop()
colors.pop()

N = len(radii)
r_lim = 180
scale_lim = 50
scale_major = 10
bottom = 40
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = 2 * np.pi / (N + 9)

# 画出柱状图
ax.bar(theta, radii, width=width, bottom=bottom, color=colors)


# 画出刻度
def scale(ax, bottom, scale_lim, theta, width):
    t = np.linspace(theta - width / 2, theta + width / 2, 6)
    for i in range(int(bottom), int(bottom + scale_lim + scale_major), scale_major):
        ax.plot(t, [i] * 6, linewidth=1, color='gray', alpha=0.8)


# 画出刻度值
def scale_value(ax, bottom, theta, scale_lim):
    for i in range(int(bottom), int(bottom + scale_lim + scale_major), scale_major):
        ax.text(theta,
                i,
                f'{i - bottom}',
                fontsize=12,
                alpha=0.8,
                va='center',
                ha='center'
                )


s_list = []
g_no = 1
label = ['MRI', 'CT', 'X-ray', 'US', 'OCT',
         'MRI', 'CT', 'X-ray', 'US',
         'MRI', 'CT', 'X-ray', 'US',
         'MRI', 'CT', 'PET', 'US',
         'MRI', 'CBCT', 'X-ray', 'PET',
         'CT', 'X-ray', 'Others',
         'MRI', 'CT',
         'CT',
         'MRI', 'CT',
         ]
for t, r in zip(theta, radii):
    if r == 0:
        s_list.append(t)
        if t == 0:
            scale_value(ax, bottom, t, scale_lim)
        else:
            scale(ax, bottom, scale_lim, t, width)
    else:
        t2 = np.rad2deg(t)
        # 标出每根柱的名称
        ax.text(t, r + bottom + scale_major * 0.6,
                label[g_no - 1],
                fontsize=12,
                rotation=90 - t2 if t < np.pi else 270 - t2,
                rotation_mode='anchor',
                va='center',
                ha='left' if t < np.pi else 'right',
                color='black',
                clip_on=False
                )
        g_no += 1

s_list.append(2 * np.pi)

for i in range(len(s_list) - 1):
    t = np.linspace(s_list[i] + width, s_list[i + 1] - width, 50)
    ax.plot(t, [bottom - scale_major * 0.4] * 50, linewidth=1, color='black')
    ax.text(s_list[i] + (s_list[i + 1] - s_list[i]) / 2,
            bottom - scale_major * 1.2,
            group_names[i],
            va='center',
            ha='center'
            )

ax.set_rlim(0, bottom + scale_lim + scale_major)
ax.axis('off')
plt.savefig('circular_bar.png')  # 保存图片
plt.show()
