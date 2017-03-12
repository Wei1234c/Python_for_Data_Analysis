# IPython log file

# %time 一次執行一個statement
get_ipython().magic('time print("hello")')
# %timeit 執行一個statement n 次，求出平均執行時間
get_ipython().magic('timeit -n 10 print("hello")')
get_ipython().magic('timeit [x for x in range(100)]')
get_ipython().magic('run -m cProfile -s cumulative test.py')
# 使用 cProfile 模組
get_ipython().magic('run -m cProfiletest.py')
# 使用 cProfile 模組
get_ipython().magic('run -m cProfile test.py')
get_ipython().magic('run -m cProfile -s cumulative test.py')
get_ipython().magic('run -p -s cumulative test.py')
get_ipython().magic('run -p -s cumulative test.py')
get_ipython().magic('prun -l 7 -s cumulative test.py')
get_ipython().magic('prun -l 7 -s cumulative print("hello")')
def printHello():
    print("Hello")
    
get_ipython().magic('prun -l 7 -s cumulative printHello')
def printHello():
    print("Hello")
    
get_ipython().magic('prun -l 7 -s cumulative printHello')
def printHello():
    print("Hello")
    
get_ipython().magic('prun -l 7 -s cumulative printHello')
# prun 指令，針對一個函式來計算
def printHello():
    print("Hello")
    
get_ipython().magic('prun -l 7 -s cumulative printHello()')
# prun 指令，針對一個函式來計算
def printHello():
    print("Hello")
    
get_ipython().magic('prun -l 7 -s cumulative printHello()')
# 針對一個或多個函式進行效能分析
get_ipython().magic('lprun -f printHello()')
reload(sys)
sys.reload(sys)
import sys 
sys.reload(sys)
import sys
import imp
imp.reload(sys)
# prun 指令，針對一個函式來計算
def printHello():
    print("Hello")
    
get_ipython().magic('prun -l 7 -s cumulative printHello()')
get_ipython().magic('pinfo b')
get_ipython().magic('pinfo b')
b = [1,2,3]
b
get_ipython().magic('pinfo b')
def add_number(a, b):
    """
    Add two numbers together
    
    Returns
    _______
    
    the sum: typeof arguments
    
    """
    return a + b
get_ipython().magic('pinfo add_number')
get_ipython().magic('pinfo2 add_number')
get_ipython().magic('pinfo2 max')
# ?問號還可以用來搜尋IPython namespace
import numpy as np
get_ipython().magic('psearch np.*load*')
get_ipython().magic('run test.py')
# -i 讓 test.py可以訪問IPython交互式環境(命稱: interactive)中定義的變數
get_ipython().magic('run -i test.py')
get_ipython().magic('paste')
get_ipython().magic('cpaste')
# 顯示IPython的快速參考
get_ipython().magic('quickref')
# 用 ? 可以查看 options
get_ipython().magic('pinfo %reset')
# 顯示IPython的快速參考
get_ipython().magic('quickref')
# 用 ? 可以查看 options
get_ipython().magic('pinfo %reset')
# 顯示所有的魔術命令的詳細文件
get_ipython().magic('magic')
# 以最新的異常跟蹤的底部進入交互式interpreter
get_ipython().magic('debug')
# 列出指令歷史紀錄
get_ipython().magic('hist')
# 在異常發生後自動進入調適器
get_ipython().magic('pdb')
# 執行clip board中的代碼
get_ipython().magic('paste')
# 打開特殊提示符號，以便手工黏貼等待執行的clip board中的代碼
get_ipython().magic('cpaste')
# 刪除interactive命名空間中的全部變數
get_ipython().magic('reset')
# 刪除interactive命名空間中的全部變數
get_ipython().magic('reset')
# 刪除interactive命名空間中的全部變數
get_ipython().magic('reset')
# 通過分頁器打印輸出Object
get_ipython().magic('page Object')
# 執行腳本
get_ipython().magic('run test.py')
# 透過cProfile執行statement，並打開分析器的輸出結果
get_ipython().magic('prun print("Hello")')
# 報告statement的執行時間
get_ipython().magic('time print("Hello")')
# 報告statement的平均執行時間，使用 -n 指定執行次數
get_ipython().magic('timeit -n 1 print("Hello")')
# 顯示interactive命名空間中定義的變數
b = [1,2,3]
get_ipython().magic('who')
# 顯示interactive命名空間中定義的變數
get_ipython().magic('whos')
# 刪除變數，並清除其在IPython中的物件上的一切引用
get_ipython().magic('xdel b')
get_ipython().magic('whos')
get_ipython().magic('history')
get_ipython().magic('reset')
get_ipython().magic('reset')
get_ipython().magic('reset')
# 執行 %logstart 可開始記錄日誌
get_ipython().magic('logstart')
# 執行 %logstart 停止記錄日誌
get_ipython().magic('logstop')
