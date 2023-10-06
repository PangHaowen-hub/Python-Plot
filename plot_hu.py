import os
import matplotlib.pyplot as plt
import SimpleITK as sitk
import seaborn as sns
from PIL import Image
import pandas as pd


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def image_hist(image_list, slice_num):
    img_sitk_img_0 = sitk.ReadImage(image_list[0])
    img_arr_0 = sitk.GetArrayFromImage(img_sitk_img_0)
    temp = img_arr_0[slice_num, :, :]
    temp = (temp + 1000) / 2000 * 255
    T = Image.fromarray(temp.astype('uint8'))
    T.show()
    data = {}
    name = ['NCCT', 'CECT', 'CycleGAN', 'Pix2Pix', 'Pix2PixHD', 'Ours']
    for i in range(len(image_list)):
        img_sitk_img = sitk.ReadImage(image_list[i])
        img_arr = sitk.GetArrayFromImage(img_sitk_img)
        img_arr = img_arr[slice_num, :, :].reshape(-1, 1).squeeze()
        data[name[i]] = img_arr
    frame = pd.DataFrame(data)

    plt.figure(figsize=(10, 6.18))
    sns.histplot(frame, element="poly", fill=False, legend=True, binwidth=10)
    plt.xlim(-1000, 1000)
    # plt.xlim(-250, 500)
    plt.ylim(0, 10000)

    plt.yticks(fontproperties='Times New Roman', size=15, weight='bold')
    plt.xticks(fontproperties='Times New Roman', size=15, weight='bold')
    plt.xlabel("Hounsfield Unit", fontsize=15, fontweight='bold')
    plt.ylabel("Count", fontsize=15, fontweight='bold')
    plt.savefig('CECT2NCCT.svg')
    plt.show()


if __name__ == '__main__':
    path = r'F:\my_code\NCCT2CECT\figure\fig7\031_cect2ncct'
    slice_num = 232
    image_list = get_listdir(path)
    image_list.sort()
    image_hist(image_list, slice_num)
