"""
ustcwlt
v1.0
account.py
WltAccount类，提供所有功能
"""


__all__ = ["WltAccount"]

import urllib
import urllib.parse
import urllib.error
import urllib.request
import http.cookiejar
from ustcwlt.error import *
from ustcwlt.html import *
from ustcwlt.url import *


class WltAccount:
    def __init__(self, user_name, password):
        """
        param user_name: str 网络通账号的用户名
        param password:  str 账号密码
        """
        try:
            req = urllib.request.Request(generate_url("base"))
            response = urllib.request.urlopen(req)
            html = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        self.is_login = False
        self.access = True
        self.user_name = user_name
        self.password = password
        self.ip = analyse_html(html)["ip"]

        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        self.opener = urllib.request.build_opener(handler)

    def login(self, connect=False):
        """
        登录账号
        param connect: bool 默认为False
                            若为False，仅登录账号
                            若为True，登录账号并根据常用设置开通网络
        """
        login_data = {
            "cmd":          "login",
            "url":          "URL",
            "ip":           self.ip,
            "name":         self.user_name,
            "password":     self.password,
        }
        if connect:
            login_data["set"] = " "
        else:
            login_data["go"] = " "

        login_data = urllib.parse.urlencode(login_data).encode("GBK")

        try:
            req = urllib.request.Request(generate_url("base"), login_data)
            response = self.opener.open(req)
            html = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        info = analyse_html(html)
        if info["type"] == "failed":
            raise LoginError(info["msg"])

        self.is_login = True

        self.access = info["access"]
        if connect and (not self.access):
            raise PermissionError("您没有使用网络通对外连接的权限")


    def get_info(self):
        """
        获取账号信息
        return: dict
        "ip":           str 当前网络的IP地址
        "currentport":  int 当前账号的网络出口
        "prefport":     int 常用设置的网络出口
        "preftime":     int 常用设置的连接时间（秒）；若为0，则代表永久
        "access":       int 若为0, 则当前账号未开通网络通服务；若为1，则已开通
        """
        if not self.is_login:
            raise PermissionError("未登录无法进行操作")

        try:
            req = urllib.request.Request(generate_url("showc"))
            response = self.opener.open(req)
            htmlc = response.read().decode("GBK")
            req = urllib.request.Request(generate_url("showp"))
            response = self.opener.open(req)
            htmlp = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        infoc = analyse_html(htmlc)
        infop = analyse_html(htmlp)

        return {
            "ip":              infoc["ip"],
            "currentport":     infoc["port"],
            "prefport":        infop["port"],
            "preftime":        infop["time"],
            "access":          self.access
            }

    def set_connection(self, port=None, time=None):
        """
        开通网络
        param port: int 网络出口
        param time: int 开通时间（秒）
        特别，当port和time都为None（默认情况）时，按照常用设置开通网络
        """
        if self.access == 0:
            raise PermissionError("您没有使用网络通对外连接的权限")
        if not self.is_login:
            raise PermissionError("未登录无法进行操作")
        if not ((port == None) and (time == None)):
            if type(port) != int:
                raise TypeError("参数port应为int类型")

            if type(time) != int:
                raise TypeError("参数time应为int类型")

            if port <= 0 or port >= 10:
                raise ValueError("port超出范围")

            if time < 0:
                raise ValueError("time超出范围")

            connection_url = generate_url("setc", (port, time))
        else:
            connection_url = generate_url("fastsetc")

        try:
            req = urllib.request.Request(connection_url, method="GET")
            self.opener.open(req)
        except urllib.error.URLError:
            raise NetworkError


    def set_preference(self, port, time):
        """
        更改常用设置
        param port: int 网络出口
        param time: int 开通时间（秒）
        """
        if not self.is_login:
            raise PermissionError("未登录无法进行操作")

        if type(port) != int:
            raise TypeError("参数port应为int类型")

        if type(time) != int:
            raise TypeError("参数time应为int类型")

        if port <= 0 or port >= 10:
            raise ValueError("port超出范围")

        if time < 0:
            raise ValueError("time超出范围")

        preference_url = generate_url("setp", (port, time))

        try:
            req = urllib.request.Request(preference_url, method="GET")
            self.opener.open(req)
        except urllib.error.URLError:
            raise NetworkError


    def logout(self):
        """
        退出登录
        """
        if not self.is_login:
            raise PermissionError("未登录无法进行操作")

        logout_url = generate_url("logout")
        try:
            req = urllib.request.Request(logout_url, method="GET")
            self.opener.open(req)
        except urllib.error.URLError:
            raise NetworkError
        self.is_login = False