"""
ustcwlt
v0.3
"""


__all__ = ["analyse_html"]


import re


def analyse_html(html):
    if re.search("公用计算机", html):
        if re.search("非科大", html):
            return {
                "type": "loginwrongip"
                }
        else:
            ip = re.search("([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)
            return {
                "type": "login",
                "ip": ip
                }
    elif re.search("请重新登录", html):
        msg = re.search("<br>(.*)<p>", html).group(1)
        return {
            "type": "loginfailed",
            "msg": msg
            }
    else:
        currentport = \
        re.search("出口: ([1-9])", html).group(1)
        ip = \
        re.search("当前IP地址([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)
        return {
            "type": "info",
            "port": currentport,
            "ip": ip
            }