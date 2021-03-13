"""
ustcwlt
v0.3
"""


__all__ = ["WltAccount"]

import urllib.parse
import urllib.request
import http.cookiejar
from ustcwlt.error import *
from ustcwlt.html import *
from ustcwlt.url import *

_wlt_url = "http://wlt.ustc.edu.cn/cgi-bin/ip"

class WltAccount:
    def __init__(self, user_name, password):
        try:
            req = urllib.request.Request(_wlt_url)
            response = urllib.request.urlopen(req)
            html = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        dict = analyse_html(html)
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

        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        self.opener = urllib.request.build_opener(handler)

    def login(self):
        try:
            req = urllib.request.Request(_wlt_url, self.login_data)
            response = self.opener.open(req)
            html = response.read().decode("GBK")
        except urllib.error.URLError:
            raise NetworkError

        dict =  analyse_html(html)
        if dict["type"] == "loginfailed":
            raise LoginError(dict["msg"])

    def set_connection(self, port, time):
        port = int(port)
        time = int(time)
        if port <= 0 or port >= 10:
            raise ValueError("port超出范围")
        if time < 0:
            raise ValueError("time超出范围")
        connection_url = get_connection_url(port, time)
        try:
            req = urllib.request.Request(connection_url, method="GET")
            self.opener.open(req)
        except urllib.error.URLError:
            raise NetworkError

    def logout(self):
        logout_url = _wlt_url + "?cmd=logout"
        try:
            req = urllib.request.Request(logout_url, method="GET")
            self.opener.open(req)
        except urllib.error.URLError:
            raise NetworkError