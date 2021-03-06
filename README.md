# Macro
## 项目简介

​	本项目是一个中文脚本编写软件，利用自研编译器，让用户可以用接近中文口语化的方式编写各种强大的脚本。只要在电脑前用双手可以完成的动作，Macro都可以替代完成。解放双手，高效工作！

​	我们吸收了“按键精灵”——一款著名的脚本编写软件的一些优秀的功能和语法，比如录屏操作，实时鼠标捕捉功能，鼠标和键盘的语法等等。

​	不过相比于“按键精灵”，该软件支持用户使用中文来进行脚本书写，且语法接近日常生活的表达，让中国用户的学习成本无限降到0！

​	AI高速发展，各种模式识别产生技术突破。许多模式识别在市场中摸爬滚打中，已经技术成熟。所以在语法中，我们加入了文字识别和图像识别，使脚本功能更加强大，更贴合用户的多样化需求。

## 界面展示

#### 1. 编辑界面

![编辑界面](https://github.com/Mister-TT/Macro/blob/main/picture/editor.png)

#### 2. 设置界面

![设置界面](https://github.com/Mister-TT/Macro/blob/main/picture/setting.png)

#### 3. 文件界面（黑夜模式）

![文件界面](https://github.com/Mister-TT/Macro/blob/main/picture/file.png)

#### 4. 帮助界面

![帮助界面](https://github.com/Mister-TT/Macro/blob/main/picture/help.png)



## 功能点

1. 文字识别
2. 图像识别
3. 语音识别（不支持）
4. 录屏功能
5. 基本文件操作：增删改查
6. 格式化代码
7. 检测代码
8. 运行代码
9. 地图功能
10. 录屏功能
11. 输出报错信息
12. 八大语法

## 安装项目基础依赖

```shell
sh install.sh
```

## 项目启动方式

~~~shell
sh start.sh
~~~

## 目录结构
```
├── docs                      # 放置项目文档的目录，如架构图，演示视频等
├── whl                       # 需要用到外部库的的部分轮子
├── macro                     # 项目主体代码目录，该目录下的子目录仅供参考，根据实际情况调整
│  ├── __init__.py            # 初始化文件
│  ├── config.py              # 配置文件，需要和其他模块沟通的变量放这里
│  ├── main                   # 内部含有主体代码的入口和软件icon
│  ├── log                    # 日志对象
│  ├── modules                # 各种模块
│  ├── ....                   
├── .gitignore                # git忽略追踪文件
├── LICENSE                   # 开源许可证明
├── requirements.txt          # 依赖文件
├── README.md                 # read me 文件
```
## python版本要求
建议使用Python 3.7

## 联系方式

如果遇到任何问题，欢迎提issue