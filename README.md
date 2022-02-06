# PythonDoSign 自动签到打卡框架的介绍
Python 自动化签到打卡框架，使用 Python 编写的任务签到框架，可以有机容纳不同的签到任务。

# PythonDoSign 自动签到打卡框架的目录结构

```
PythonDoSign
│  main.py                        # 程序入口程序
|  taskLoader.py                  # 主要用于插件加载、任务安排等
│  requirements.txt               # 所需支持库的列表
│
├─Module                          # 存放程序运行的自带或者第三方模块 其中的 console.py 和 taskReturnProcessor.py 是自带的
│      console.py                 # 此模块主要是便于控制台的输出
│      taskReturnProcessor.py     # 在每个任务完成后会将任务结果与信息传入此模块中的 main() 函数
│
├─Plugins                         # 自带签到插件的存放位置 其中的 Template.py 是插件模板
│      Template.py                # 插件模板更多信息查看文档
│
└─Tasklist                        # 用于放置用户的自动签到任务
        Template.json             # 其中一个用户签到任务文件
```

# 使用框架说明
框架处于 v22.0126 版本，处于初测阶段，目前不公开发行。

# 下载与使用
克隆/下载此仓库的所有文件，安装 requirements.txt 中的支持库列表即可。使用 Python 版本不小于 3.X （推荐使用 Python 3.9.X）。

更多请查看我们的所写的文档！

# 文档与开发
请读阅读我们的 wiki : https://github.com/wojiaoyishang/PythonDoSign/wiki 或者 https://gitee.com/wojiaoyishang/PythonDoSign/wikis

# 关于
由 我叫以赏 制作！



