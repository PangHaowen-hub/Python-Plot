import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

file_path = r'G:\Lobectomy\shengjing\RML_nii\RM.xls'

percent = pd.read_excel(io=file_path, sheet_name=3, header=None)


value = percent.values[:, 1:]

percent_Data = pd.DataFrame(value * 100)

plt.boxplot(percent_Data,  labels=['RU', 'RM', 'RL', 'LU',  'LL'], patch_artist=True)
# plt.ylim(-2, 2)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f%%'))
plt.savefig('RML_percent_shengjing.png')  # 保存图片
plt.show()
