import hashlib
import os, time
from multiprocessing import Pool, Manager

q = Manager().Queue()  # 创建队列


def copy_file_task(name, old_folder_name, new_folder_name):
    '''此函数用来读写文件内容'''
    # 如果源文件夹不存在，直接返回
    if not os.path.exists(old_folder_name):
        print('文件夹 %s 不存在！' % old_folder_name)
        return None
    # 如果目标路径不存在，则尝试创建
    if not os.path.exists(new_folder_name):
        try:
            os.mkdir(new_folder_name)
        except NotImplementedError:
            print('创建文件夹 %s 错误！' % new_folder_name)
            return None
    try:
        with open(old_folder_name + '/' + name, 'rb') as fr, open(new_folder_name + '/' + name, 'wb') as fw:
            content = fr.read()
            fw.write(content)
            q.put(name)  # 把复制完的文件名扔到队列里
    except:
        print('读写出错误！')


def hashFile(name):
    '''对文件做hash,用来判断文件是否一致'''
    h = hashlib.sha256()
    # 打开一个文件
    with open(name, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()  # 哈希结果


def main():
    old_folder_name = input('请输入文件夹的名字：')
    new_folder_name = old_folder_name + '-副本'

    # 如果目标文件夹已经存在的情况下，注意这里不能覆盖
    while os.path.isdir(new_folder_name):
        new_folder_name = new_folder_name + '-副本'

    # os.mkdir(new_folder_name)  # 创建一个新文件夹
    file_names = os.listdir(old_folder_name)  # 将旧文件夹内的文件名字放在列表中

    pool = Pool(5)  # 创建一个拥有五个进程的进程池

    for name in file_names:
        pool.apply_async(copy_file_task, args=(
            name, old_folder_name, new_folder_name))  # 将任务添加到进程池

    pool.close()

    num = 0  # 用来记录当前完成文件的个数
    all_num = len(file_names)  # 文件名列表的长度，统计有多少个文件
    while num < all_num:
        file_name = q.get()  # 等待从队列中获取文件名
        num += 1
        copy_rate = num / all_num * 100

        # 做哈希值的检测,验证复制的文件有没有出错
        old_file_name = old_folder_name + '/' + file_name
        new_file_name = new_folder_name + '/' + file_name

        if hashFile(old_file_name) == hashFile(new_file_name):
            print('%s 文件拷贝成功' % old_file_name)
        else:
            print('%s 文件拷贝失败' % old_file_name)

        print('复制的进度为：%.1f%%' % copy_rate)
        # time.sleep(0.5)

    pool.join()
    print("\n已完成文件复制！")


if __name__ == '__main__':
    main()
