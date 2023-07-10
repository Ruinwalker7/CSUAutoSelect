# CSUAutoselect

中南大学自动选课工具 V2.0

原作者：[@DavidHuang](https://github.com/CrazyDaveHDY)

主要修改内容：

- 可以进行二维码选择
- 可以进行多个课程的抢课

## 安装
### Python3
该项目需要 Python3，可以从 [Python 官网](https://www.python.org/) 下载并安装，可以参考CSDN上[小白安装教程](https://blog.csdn.net/qq_45502336/article/details/109531599)

### Repo
点击右上角的 `Clone or download` 下载该项目至本地

对于 git 命令行：
```console
$ git clone https://github.com/CrazyDaveHDY/CSUAutoSelect.git
```

软件运行需要python包requests

### requests模块

在命令行中运行：
```console
$ pip3 install requests
```

## 运行

首先修改`config.ini`，根据config中内容修改账号密码，以及填写要抢课的ID，config文件中已经详细展示了如何进行修改，**请仔细阅读**。稍后具体会展示如何找到课程的ID


按照提示输入学号，教务系统密码，课程 ID 后，进入项目根目录，命令行中运行
```console
$ python3 autoselect.py
```

会在根目录(autoselect.py所在文件夹)生成`code.jpg`，请**人工识别二维码内容**，并输入

之后会自动检测是否开始选课，如果选课还没有开始，将会是下图的输出：

<img src="assets/image-20230711014740394.png" alt="image-20230711014740394" style="zoom: 67%;" />

## 如何找到6位课程ID


1. 课程 ID 查找方法：在 [中南大学教务系统课表查询页面](http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_find_jg0101.jsp?xnxq01id=2022-2023-2&init=1&isview=0) 中点击「按教师」按钮，输入学年学期、教师名称后点击「查询」，格子中央的 6 位数字编号即为课程 ID，这样可以找到公选和体育的ID、

   ![课程 ID.png](https://i.loli.net/2021/01/13/G7mN9BUzpaHRtkw.png)

2. 在查询页面按照时间查询，里面课表都有开课编号

<img src="assets/image-20230711015054530.png" alt="image-20230711015054530" style="zoom:80%;" />


## 声明

因为每学期选课的情况可能都会发生变化，当前代码仅保证能在上传时学期抢课，仅能提供较高的成功率，但不保证所有课程均能抢课成功；

该程序仅保存账户密码在本地，不会危害到你的账户安全；

**脚本所使用的方法并不会对服务器造成太多的负担**，能够有效避免因为选课页面无法快速打开选课页面而导致的抢课失败。

## 许可协议

CSUAutoSelect [GPL-3.0 License](https://github.com/CrazyDaveHDY/CSUAutoSelect/blob/master/LICENSE)

