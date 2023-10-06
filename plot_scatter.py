import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits.axisartist as axisartist

if __name__ == '__main__':
    X = np.asarray(
        [10, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8, 10, 11, 11, 10, 11, 12, 10, 14, 15, 12, 12, 14, 16, 3, 5, 9, 8, 7, 4,  3, ])
    Y = np.asarray(
        [12, 2, 5, 6, 5, 7, 8, 6, 5, 7, 8, 13, 10, 14, 9, 11, 15, 10, 14, 15, 12, 12, 17, 15, 4, 5, 9, 8, 7, 4,  3, ])

    fig = plt.figure(figsize=(7, 7))
    ax = axisartist.Subplot(fig, 111)
    fig.add_axes(ax)
    ax.axis["bottom"].set_axisline_style("-|>", size=1.5)
    ax.axis["left"].set_axisline_style("-|>", size=1.5)
    # 通过set_visible方法设置绘图区的顶部及右侧坐标轴隐藏
    ax.axis["top"].set_visible(False)
    ax.axis["right"].set_visible(False)
    ax.yaxis.set_major_locator(plt.NullLocator())
    ax.xaxis.set_major_locator(plt.NullLocator())
    plt.scatter(x=X, y=Y, color='red')
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    # plt.gca().get_xaxis().set_visible(False)
    # plt.gca().get_yaxis().set_visible(False)
    # sns.despine()
    plt.savefig('scatter.png')  # 保存图片
    plt.show()
