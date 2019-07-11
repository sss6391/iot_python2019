import os
os.chdir("info_data")
result = os.popen("dir")
print(result.read())
