#!/bin/bash

# １.3 shell 变量　：本地变量，全局变量，内置变量
# 普通变量的３种定义方法
name='amour'
age=124_amour
age_second="$ age"
echo $name  #使用变量
echo $age
echo $age_second

# 命令变量２种方法
cmd=`ls`
ccd=$(cd)

echo $cmd
echo $ccd
# 全局变量　２种方式
# 1,分步
a="hello"
export a
# 2,同时
export a="hello"

# 1.3.6内置变量
echo '#$0 查询当前脚本名'
echo $0
echo '$# 获取脚本参数个数'
echo $#
echo '$n 获取脚本获得的第n个参数'
echo $n
echo '#$?查询上次执行的结果'
echo $?
echo '#$$ 查看进程编号'
echo $$
echo '# $2'
echo $2
printf $@  #获得所有的参数

# 字符串操作
str='it is strings please pythonic'

echo ${str:1:4}
var=$1
echo $var
# 查看变量的方式　－－－３
$a
"$a"
"${a}"  #推荐
# 只读变量
readonly a
# 删除变量
unset a

# shell表达式
[ 表达式 ]   #两侧都要有空格
test 表达式
arg_num=$#
echo $arg_num
[ $arg_num -eq 1 ]
echo $?
test '${arg_num} -eq 1'
echo $?


# 1.4.3 shell的文件表达式（文件测试运算符）
# filename=$1

# [ -e "{filename}" ] && echo "文件exist"
# [ -f "{filename}" ] && echo "文件f"
# [ -x "{filename}" ] && echo "文件x"
# [ -d "{filename}" ] && echo "文件d"
# [ -r "{filename}" ] && echo "文件r"
# [ -w "{filename}" ] && echo "文件可w"
# 执行代码　　bash 18_file_sytax.sh a a

# 1.4.4 shell的数字表达式
# 获取参数个数　　
# arg_num=$#　
# [ $arg_num -eq 1 ] && echo "参数个数为１"
# [ $arg_num -gt 1 ] && echo "参数个数大于１"
# [ $arg_num -lt 1 ] && echo "参数个数小于１"
# [ $arg_num -ne 1 ] && echo "参数个数不为１"
# 执行代码　bash 18file_sytax.sh a b cas

# arg=$1
# arg_second=$2
# 在脚本外传来的是字符串
# echo $arg
# echo $arg_second
# [ $arg == $arg_second ] && echo "字符串相等"
# [ $arg == $arg_second ] && echo "字符串不相等"

# =============
# 流程控制语句　if, case
# 执行　--- bash xxx.sh param
# arg_num=$#
#
# if [ $arg_num -eq 1 ]
# then
# echo "params are one"
# fi
# [ $arg_num -eq 1 ] && echo "params are one"
# ==============
# if [ $arg_num -eq 1 ]
# then
# echo "params are one"
# else
# echo "else"
# fi

# ==============
# if [ $arg_num -eq 1 ]
# then
# echo "params are one"
# elif [ $arg_num -eq 2 ]
# then
# echo "参数个数为２"
# else
# echo "else"
# fi

# ===============
# case 语句 --- 服务器部署会用到

# arg=$1
# case $arg in
# "start")
# echo "系统正在启动"
# ;;
# "restart")
# echo "重启操作系统"
# ;;
# *)
# echo "其他"
# ;;
# esac

# 运行　bash xx.sh a/start/.....
# ========================
# 循环语句
# cmd=$(ls)
# cmd=$(ll)   没有用，只能是简单的语句
# echo $cmd

# for c in $cmd
# do
# echo $c
# done

# =======================
# 运算　let
# num=10
# let num+=1
# echo $num
#
# num=$(($num+1))
# printf　$num
# echo $num

# =========================
# 循环  while \ until
# num=0
# while [ $num -lt 8 ]  #条件为真，执行，为Ｆalse退出
# do
#     echo $num
#     let num+=1
# done
# 井号与代码空格不能是中文空格
# until [ $num -eq 8 ]  # 条件false,执行，条件为真，退出
# do
#     echo $num
#     printf $num
# let num+=1
# done
# run --- bash xx.sh
# ======================
# 无参函数
no_param_fun(){
    echo "hello world"
    echo "hello html"
    echo "hello c"
    echo "hello c++"
    echo "hello golang - c"
    echo "hello ruby -human python"
}

no_param_fun

# 有参函数
fun(){
    arg=$1
    echo $arg
    echo $0
}

echo $0 "获取当前文件名"
echo $1 '参数为0,不输出'
echo "********"
# fun hello
fun
