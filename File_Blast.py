from unrar import rarfile#需要安装unrar和一个windows的插件
import itertools

def make_pwd(min,max,word = '123456789'):
    while min <= max:
        iter = itertools.product(word,repeat=min)
        for i in iter:
            yield ''.join(i)#生成器,join生成str
        min += 1

def Un_RAR(pwd,out_path,file):
    try:
        file.extractall(out_path, pwd=pwd)
        return True
    except:#密码错误
        return False

def make_file(file_path,out_path):
    file = rarfile.RarFile(file_path)
    return file,file_path,out_path

def start_(min,max,word):
    print('Start to run...')
    for pwd in make_pwd(min,max,word):
        if Un_RAR(pwd,out_put_file_path,file):
            print(f'Password is {pwd}')
            break
        else:
            print(f"isn't {pwd}" )


if __name__ == '__main__':
    file,file_path,out_put_file_path = make_file(r"xxx",r'yyy')#创建文件xxx为压缩包位置,yyy为输出位置

    inf = float("inf")#无穷
    min = 4
    max = 4
    word = r'''1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''

    start_(min,max,word)
