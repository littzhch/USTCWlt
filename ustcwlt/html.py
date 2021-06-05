"""
ustcwlt
v1.0
html.py
使用正则表达式解析html页面
"""


__all__ = ["analyse_html"]


import re


def analyse_html(html):
    """
    return：

    "urltype"         "ip"         "port"          "msg"         "time"      "access"

    login          [ip]
    failed                                      [msg]
    info           [ip]      [currentport]                                 0 or 1
    pref                    [prefport] int 1-9           [preftime] int sec
     
    """
    if re.search("公用计算机", html):
        ip = re.search("([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)
        return {"urltype": "login", "ip": ip}

    if re.search("请重新登录", html):
        msg = re.search("信息：<br>(.*)<p>", html).group(1)
        return {"urltype": "failed", "msg": msg}

    if re.search("校内测速", html):
        currentport = int(re.search("出口: ([1-9])", html).group(1))
        ip = \
        re.search("当前IP地址([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)

        access = 1
        if re.search("您没有使用网络通对外连接的权限", html):
            access = 0

        return {"urltype": "info", "port": currentport, "ip": ip, "access": access}

    if re.search("返回主界面", html):
        prefport = int(re.search("常用出口：([1-9])", html).group(1))
        if re.search("常用时间：永久", html):
            preftime = 0
        else:
            rst = re.search("常用时间：([1-9]*)([小分秒])", html)
            preftime = int(rst.group(1))
            if rst.group(2) == "小":
                preftime *= 3600
            elif rst.group(2) == "分":
                preftime *= 60
        return {"urltype": "pref", "port": prefport, "time": preftime}