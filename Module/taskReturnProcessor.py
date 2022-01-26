"""
用于任务的结果信息的处理
"""
import Module.console as console

def main(returnInfo):
    """自动签到任务的返回值会给此函数处理，若用户于在之前将 NotNext 的值设成 True 的任务数据则不会调用此函数"""
    # 输出任务执行数据
    p = {"Success": console.success, "Failed": console.error, "Warning": console.warm, "Unknown": console.log}.get(
        returnInfo['State'], console.plain)
    p("任务信息：", returnInfo['Message'])
    p("任务细节：", returnInfo['Detail'])
    p(returnInfo['More'])