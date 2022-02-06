# -*- coding:utf-8 -*-
import sys, importlib, ctypes, os, json
import time

from apscheduler.schedulers.background import BackgroundScheduler
from warnings import filterwarnings
from pytz_deprecation_shim import PytzUsageWarning

import Module.console as console
from Module.taskReturnProcessor import main as taskReturnProcessor

# 开启 Windows 下对于 ESC控制符 的支持
if sys.platform == "win32":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# 忽略时区警告
filterwarnings('ignore', category=PytzUsageWarning)

# 加载插件后的字典
plugins = {}

# 任务表
sched = BackgroundScheduler(timezone="Asia/Shanghai")

def taskManager(**kwargs):
    """将会安排任务的执行，是定时调用的"""
    global plugins
    try:
        Taskname = kwargs['TaskName']
        TaskPlugin = kwargs['TaskPlugin']
        TaskMark = kwargs['TaskMark']
        if 'Data' not in kwargs:
            console.error(f"无法执行自动任务 {Taskname} ，因为没有提供所需的 数据(Data) 键(Key) ！若不需要数据请留空但是不要删除！")
        try:
            console.info(f"输出信息如下：\n---------------------------------\n"
                         f"---->即将执行任务 {Taskname}\n"
                         f"---->所使用的插件 {TaskPlugin}\n"
                         f"---->任务备注 {TaskMark}"
                         f"\n---------------------------------")
            returnInfo = plugins[TaskPlugin].main(**kwargs)  # type:dict
            if not returnInfo.get("NotNext", False):
                taskReturnProcessor(returnInfo)
        except BaseException as error:
            console.error(f"无法执行自动任务 {Taskname} ，可能是因为任务执行时并未提供正确的插件。原因出现在插件 " + str(error) + " 。")

    except:
        console.error("无法执行指定签到任务，因为此任务并未提供正确的任务格式！")




def main():

    # 获取所有签到模块
    console.plain("正在读取签到插件......")
    for plugin in os.listdir("./Plugins"):  # 读取插件目录
        filename = os.path.splitext(plugin)[0]
        try:
            plugins[filename] = importlib.import_module("Plugins." + filename)
            console.success(f"输出信息如下：\n---------------------------------\n"
                            f"---->成功加载插件 {filename} ，\n"
                            f"---->插件名称：{plugins[filename].PLUGIN_NAME}\n"
                            f"---->插件作者：{plugins[filename].PLUGIN_AUTHOR}\n"
                            f"---->插件介绍：{plugins[filename].PLUGIN_DESCRIPTION}\n"
                            f"---->插件版本：{plugins[filename].PLUGIN_VERSION}\n"
                            f"---------------------------------")
        except BaseException as error:
            console.error(f"加载插件 {filename} 失败！原因是 " + str(error) + " 。")
    # 获取 Tasklist 中所有的签到任务
    console.plain("正在读取任务文件......")
    for taskFile in os.listdir("./Tasklist"):  # 读取自动签到列表目录
        try:
            if os.path.splitext(taskFile)[1] != ".json":  # 排除非 json 文件
                continue
            with open("./Tasklist/" + taskFile, encoding="utf-8") as f:  # 读入数据
                taskData = json.load(f)
            if type(taskData) != list:  # 对于非列表的 json 排除
                raise BaseException("任务格式不正确，得到了非列表（数组）。")
            for task in taskData:  # type:dict
                console.log(f"正在设置任务 “{task['TaskName']}” 。")
                # 设置任务环节
                TaskPlugin = task['TaskPlugin']
                if TaskPlugin not in plugins:
                    raise BaseException("并未拥有插件 " + TaskPlugin)
                TaskRunTime = task['TaskRunTime'].split(" ") + ["*"] * 7  # type:list

                for x in range(len(TaskRunTime)):
                    if TaskRunTime[x] == "?":
                        TaskRunTime[x] = "*"

                PyTaskRunTime = {
                    "second": TaskRunTime[0],
                    "minute": TaskRunTime[1],
                    "hour": TaskRunTime[2],
                    "day": TaskRunTime[3],
                    "month": TaskRunTime[4],
                    "week": TaskRunTime[5],
                    "year": TaskRunTime[6]
                }

                sched.add_job(taskManager, "cron", kwargs=task, timezone="Asia/Shanghai", **PyTaskRunTime)
                console.log(f"设置任务 “{task['TaskName']} 完成” 。")
        except BaseException as error:
            console.error(f"未能加载任务文件 {'./Tasklist/' + taskFile} ，原因是 {str(error)} 。")
            continue
    sched.start()
    console.log(f"全部任务设置完成。")
    while True:
        time.sleep(1)

