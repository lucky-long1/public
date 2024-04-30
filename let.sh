#!/usr/bin/bash

# 语法功能等价于((表达式))，let后面的整数运算表达式中变量不需要加$，特殊字符前也不需要加“\”

# 多个表达式之间使用空格 而不是"，"号

a=1
b=2

let c=a+b


# 变量++和++变量的区别

# 变量++，运算过后再+1
a=2
let b=a++
echo $a $b


# ++变量，+1再运算
c=2
let d=++c
echo $c $d


# 变量数值自增+2的表示方法
a=4
let a+=2
echo $a



# 乘法表示方法
b=2
let b*=6; echo $b