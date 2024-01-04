#!/usr/bin/bash

# 格式: bc [选项] [参数]

# bc -q  :表示进入且关闭提示信息
# bc     :表示进入且出现提示信息

echo "100*2" | bc
echo "1/3" | bc
echo "scale=3;1/3" | bc



# 对文件里面的算数进行计算，注意一行代表一个算数
# 格式： bc -q  文件名

bc -q yunsuan.txt


# 内置变量  scalse  ：指定精度，对计算结果指定保留小数，默认为0.

# 格式： scale=2 ：表示保留两位小数
