# python解方程组小程序
用python解方程组问题，输入可解方程组，自动算出结果
# 依赖
利用了python第三方库sympy，使用前需要安装：
```python
pip install sympy
```
# 使用
python2和python3均可，只要安装了sympy就行。
然后直接运行使用，用户友好型自我感觉还是不错的：
```python
python 解方程组小程序.py
```
# 版本更新
v1.0和v2.0版本都可以使用，只不过v1.0在输入方程组前需要先输入用到的所有变量名，较为麻烦。

v2.0可以直接在输入方程组的同时识别出变量名，但是相应的，变量设定必须要符合规范：

变量第一个字符必须是英文字母，之后可以是数字或是字母，而且不能出现任何特殊符号如：`_+-?`等等。

规范的变量命名如`s1 num3 I1 Ur`。

而相应的，v1.0的变量名更加随意，但是也不能出现特殊符号。
# 感谢
感谢使用，欢迎star和fork
github：https://github.com/thunder-sword/python-Equations
