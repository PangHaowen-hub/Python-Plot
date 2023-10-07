import seaborn as sns
import matplotlib.pyplot as plt


def read_info(str_list):
    out = []
    for i in str_list:
        out.append(float(i.split(' ')[-1]))
    return out


def read_list(txt_path):
    test = []
    train = []
    with open(txt_path, "r") as f:
        for line in f.readlines():
            if 'Test loss' in line:
                test.append(line.strip('\n'))
            elif 'Train loss' in line:
                train.append(line.strip('\n'))
    test = read_info(test)
    train = read_info(train)
    return train, test


if __name__ == '__main__':
    txt_name_0 = r'D:\my_code\Federated_Learning\Flower_NC2CE\2023-10-03-17-35-29\Client-0-2023-10-03-17-35-29.log'
    txt_name_1 = r'D:\my_code\Federated_Learning\Flower_NC2CE\2023-10-03-17-35-37\Client-0-2023-10-03-17-35-37.log'
    txt_name = r'D:\my_code\Federated_Learning\Flower_NC2CE\2023-10-03-15-48-14\Centralized-2023-10-03-15-48-14.log'

    train_Centralized, test_Centralized = read_list(txt_name)
    train_0, test_0 = read_list(txt_name_0)
    train_1, test_1 = read_list(txt_name_1)
    x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    sns.lineplot(data=train_Centralized, label='Centralized Train Loss')
    sns.lineplot(data=train_0, label='Client 0 Train Loss')
    sns.lineplot(data=train_1, label='Client 1 Train Loss')

    sns.lineplot(x=x, y=test_Centralized, label='Centralized Test Loss')
    sns.lineplot(data=test_0, label='Client 0 Test Loss')
    sns.lineplot(data=test_1, label='Client 1 Test Loss')
    plt.legend()
    plt.savefig('loss.png')  # 保存图片
    plt.show()
