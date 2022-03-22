import multiprocessing
import os

def copy_work(file_name,source_dir,dest_dir):
    # 拼接路径
    source_path=source_dir+"/"+file_name

    dest_path=dest_dir+"/"+file_name

    # 打开原文家，创建目标文件
    with open(source_path,"rb") as source_file:
        with open(dest_path,"wb") as dest_file:
            while True:
                # 读取文件数据
                file_data=source_file.read(1024)
                if file_data:
                    dest_file.write(file_data)
                else:
                    break
        dest_file.close()
    source_file.close()



if __name__ == '__main__':
    # 定义变量，保存源文件，目标文件
    source_dir="source_dir"
    dest_dir="dest_dir"

    try:
        # 创建目录
        os.mkdir(dest_dir)
    except Exception as e:
        print(e)
    # 获取所有源文件夹中的文件
    file_list=os.listdir(source_dir)

    # 创建进程池
    pool=multiprocessing.Pool(3)

    # 拷贝文件
    for file_name in file_list:
        pool.apply_async(copy_work,args=(file_name,source_dir,dest_dir))

    # 关闭进程池
    pool.close()
    # 设置等待进程池
    pool.join()

