#!/usr/bin/bash

VAR="world"  #变量与值之间不能有空格

echo "hello $VAR"

# 多行注释
: '          
name="li"
echo ${name}
echo $name
echo "$name"
echo '$name'
echo "${name}"
'

get_name(){
	echo "li"
}
echo "you are $(get_name)"
# -z:检测字符串长度是否为0；-n:检测字符串长度是否不为0
if [[ -z "$string" ]]; then
	echo "String is empty"
elif [[ -n "$string" ]]; then
	echo "String is not empty"
fi


echo "I'm in ${PWD}"
echo "I'm in `pwd`"

echo ${food:-Cake}

str="/path/to/foo.cpp"
echo ${str%.cpp}
echo ${str%.cpp}.o
echo ${str%/*}
echo ${str##*.}
echo ${str##*/}
echo ${str#*/}
echo ${str##*/}
echo ${str/foo/bar}


name="long"
echo ${name}
echo ${name:0:2}
echo ${name::2}
echo ${name::-1}
echo ${name:(-1)}
echo ${name:(-2)}
echo ${name:(-2):2}
echo ${name:(-2):1}
length=2
echo ${name:0:length}

SRC="/path/to/foo.cpp"
bashpath=${SRC##*/}
echo $bashpath
dirpath=${SRC%$bashpath}
echo $dirpath

src="HELLO WORLD!"
echo ${src}
echo ${src,,}
src="hello world!"
echo ${src^}
echo ${src^^}

arr=(hello World)
echo "${arr[@],}"
echo "${arr[@]^}"

fruits=('Apple' 'Banana' 'Orange')
echo ${fruits}


array1=(foo{1..5})
array2=({A..F})
echo ${array1[*]}
echo ${array2[@]}
array3=(${array1[@]} ${array2[@]})
echo ${array3[*]}
echo ${!arry1[@]}

for e in ${array1[*]}; do
	echo ${e}
done

for i in ${!array1[@]}; do
	printf "%s\t%s\n","${i}","${array1[$i]}"
done










