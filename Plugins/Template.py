# -*- coding:utf-8 -*-
"""
用于 XXX 网站的自动任务
需要提供内容：cookie
任务配置实例：
{
    "TaskName": "Template 自动签到",
    "TaskPlugin": "Template",
    "TaskMark": "Template 自动签到",
    "TaskRunTime": "0/1 * * * * * *",
    "Data": {
      "cookie": "XXX=XXX;"
    }
}
"""

PLUGIN_NAME = "这是模块的名称"
PLUGIN_DESCRIPTION = "这里是模块的介绍"
PLUGIN_VERSION = "v1.0.1"
PLUGIN_AUTHOR = "作者名字"

import Module.console as console


def main(**kwargs):
    """
    启动自动签到， 程序会调用这一部分，此程序将会得到 json 文件中关于任务的信息
    比如：
    kwargs['TaskName'] 任务名
    kwargs['TaskPlugin'] 所使用的的插件
    kwargs['TaskMark'] 任务备注
    kwargs['TaskRuntime'] 任务执行时间 cron 表达式
    kwargs['Data'] 用户传入的数据
    """
    console.success("这是一个调用自定义模块的案例。")

    # 返回信息说明：
    # return 的信息主要用于显示在控制台上，以便指示用户
    # NotNext -- 不在继续执行任务安排函数的接下来的代码，不加默认为 False。若为 True 任务安排函数只会把返回的内容打印在控制台上而不进行主代码中像发送签到数据那样的操作
    # *State -- （必要）状态大概指示  Success=成功(success) Failed=失败(error) Warning=警告(warn) Unknown=未知(log)
    # *Message -- （必要）信息内容概要
    # *Detail -- （必要）信息内容的细节
    # *More -- （必要）附加的内容，将会直接添加在消息末尾。（会自动在前面加一个换行符）
    return {
        "NotNext": False,
        "State": "Success",
        "Message": "任务成功完成！",
        "Detail": "通过请求接口自动签到了。目前XX数量XX，XX数量XX。",
        "More": "附加的内容，将会填在任务结果的末尾。",
        "Data": "这服务器返回的数据可以填写这里，也可以不填。"
    }
