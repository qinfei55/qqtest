
from filecmp import dircmp

def my_dircmp(dirobj):
    if (dirobj.left_only or  dirobj.right_only or dirobj.diff_files): ##是否两边的文件名/目录名相同，文件的内容相同
        print(dirobj.left, '<-->', dirobj.right, ": False")
        return False
    elif not dirobj.subdirs: #如果不存在子目录，则文件夹相同
        print(dirobj.left, '<-->', dirobj.right, ": True")
        return True

    else: #比较子目录，如果有1个子目录不同，则返回失败
        for sub,dcmp in dirobj.subdirs.items():
            if not my_dircmp(dcmp):
                print(dirobj.left, '<-->', dirobj.right, ":False")
                return False
        print(dirobj.left, '<-->', dirobj.right, ": True")
        return True

d=dircmp('1','2')
my_dircmp(d)



