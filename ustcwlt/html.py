"""
ustcwlt
v0.3
"""


__all__ = ["analyse_html"]


import re


def analyse_html(html):
    """
    return：

    "type"         "ip"         "port"          "msg"         "time"

    login          [ip]
    failed                                      [msg]
    info           [ip]      [currentport]
    pref                    [prefport] int 1-9             [preftime] int sec
     
    """
    print(html)
    if re.search("公用计算机", html):
        ip = re.search("([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)
        return {"type": "login", "ip": ip}

    if re.search("请重新登录", html):
        msg = re.search("信息：<br>(.*)<p>", html).group(1)
        return {"type": "failed", "msg": msg}

    if re.search("校内测速", html):
        currentport = int(re.search("出口: ([1-9])", html).group(1))
        ip = \
        re.search("当前IP地址([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)
        return {"type": "info", "port": currentport, "ip": ip}

    if re.search("返回主界面", html):
        prefport = int(re.search("常用出口：([1-9])", html).group(1))
        if re.search("常用时间：永久", html):
            preftime = 0
        else:
            preftime = 3600 * int(re.search("常用时间：([1-9]*)", html).group(1))
        return {"type": "pref", "port": prefport, "time": preftime}