"""
ustcwlt
v0.3
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
        try:
            req = urllib.request.Request(generate_url("base"))
            response = urllib.request.urlopen(req)
            html = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        self.is_login = False
        self.user_name = user_name
        self.password = password
        self.ip = analyse_html(html)["ip"]

        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        self.opener = urllib.request.build_opener(handler)

    def login(self):
        login_data = {
            "cmd":          "login",
            "url":          "URL",
            "ip":           self.ip,
            "name":         self.user_name,
            "password":     self.password,
            "go": " "
        }

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

    def fastconnect(self):
        login_data = {
            "cmd":          "login",
            "url":          "URL",
            "ip":           self.ip,
            "name":         self.user_name,
            "password":     self.password,
            "set": " "
        }

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


    def get_info(self):
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
            "preftime":        infop["time"]
            }

    def set_connection(self, port=None, time=None):
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
        if not self.is_login:
            raise PermissionError("未登录无法进行操作")

        logout_url = generate_url("logout")
        try:
            req = urllib.request.Request(logout_url, method="GET")
            self.opener.open(req)
        except urllib.error.URLError:
            raise NetworkError
        self.is_login = False