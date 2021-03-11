"""
ustcwlt
自动登录网络通账号并设置网络
v0.2
"""

__all__ = ["NetworkError", "IpError", "LoginError", "WltAccount"]


import re
import urllib
import urllib.parse
import urllib.request
import http.cookiejar


_wlt_url = "http://wlt.ustc.edu.cn/cgi-bin/ip"
_defaultAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "\
                "AppleWebKit/537.36 (KHTML, like Gecko) "\
                "Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45"



class NetworkError(Exception):
    def __init__(self, err="网络连接出错"):
        Exception.__init__(self, err)

class IpError(Exception):
    def __init__(self, err="非科大IP地址"):
        Exception.__init__(self, err)

class LoginError(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)



def _analyse_html(html):
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
        


def _get_connection_url(port, time):
    url = _wlt_url + "?cmd=set&url=URL&type=" + str(port - 1) + \
                      "&exp=" + str(time * 3600) + \
                      "&go=+%BF%AA%CD%A8%CD%F8%C2%E7+"
    return url



class WltAccount:
    def __init__(self, user_name, password, user_agent=_defaultAgent):
        try:
            req = urllib.request.Request(_wlt_url)
            response = urllib.request.urlopen(req)
            html = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        dict = _analyse_html(html)
        if dict["type"] == "loginwrongip":
            raise IpError


        login_data = {
            "cmd":          "login",
            "url":          "URL",
            "ip":           dict["ip"],
            "name":         user_name,
            "password":     password
        }
        self.login_data = urllib.parse.urlencode(login_data).encode("GBK")

        self.header = {
            "User-Agent": user_agent
        }

        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        self.opener = urllib.request.build_opener(handler)

    def login(self):
        req = urllib.request.Request(_wlt_url, self.login_data, self.header)
        response = self.opener.open(req)
        html = response.read().decode("GBK")
        dict =  _analyse_html(html)
        if dict["type"] == "loginfailed":
            raise LoginError(dict["msg"])

    def set_connection(self, port, time):
        port = int(port)
        time = int(time)
        if port <= 0 or port >= 10:
            raise ValueError("port超出范围")
        if time < 0:
            raise ValueError("time超出范围")
        connection_url = _get_connection_url(port, time)
        req = urllib.request.Request(connection_url, headers=self.header, method="GET")
        self.opener.open(req)

    def logout(self):
        logout_url = _wlt_url + "?cmd=logout"
        req = urllib.request.Request(logout_url, headers=self.header, method="GET")
        self.opener.open(req)
