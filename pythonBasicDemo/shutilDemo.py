import shutil
import zipfile
import tarfile
# 高级的 文件、文件夹、压缩包 处理模块

# f =open("shutil.xml","w")
# f.write("abbbbcd")
# f.close()
#
# # 将文件内容拷贝到另一个文件中
# shutil.copyfile("shutil.xml","shutil2.xml")
#

# shutil.make_archive(base_name, format,…)

# 创建压缩包并返回文件路径，例如：zip、tar
# 压缩
z =zipfile.ZipFile('test.zip','w')
z.write("open.txt")
z.close()

# zipfile压缩&解压缩
z = zipfile.ZipFile('test.zip','r')
z.extractall(path='.')
z.close()