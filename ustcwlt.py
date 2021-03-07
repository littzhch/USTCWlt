"""
ustcwlt
自动登录网络通账号并设置网络
"""

import re
import urllib
import urllib.parse
import urllib.request
import http.cookiejar

_wlt_url = "http://wlt.ustc.edu.cn/cgi-bin/ip"
_defaultAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "\
                "AppleWebKit/537.36 (KHTML, like Gecko) "\
                "Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45"


def _get_ip():
    req = urllib.request.Request(_wlt_url)
    response = urllib.request.urlopen(req)
    html = response.read().decode("GBK")
    result = re.search("([1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*)", html).group(1)
    return result


def _get_connection_url(port, time):
    url = _wlt_url + "?cmd=set&url=URL&type=" + str(port - 1) + \
                      "&exp=" + str(time * 3600) + \
                      "&go=+%BF%AA%CD%A8%CD%F8%C2%E7+"
    return url


class WltAccount:
    def __init__(self, user_name, password, user_agent=_defaultAgent):
        login_data = {
            "cmd":          "login",
            "url":          "URL",
            "ip":           _get_ip(),
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
        self.opener.open(req)

    def set_connection(self, port, time):
        connection_url = _get_connection_url(int(port), int(time))
        req = urllib.request.Request(connection_url, headers=self.header, method="GET")
        self.opener.open(req)

    def logout(self):
        logout_url = _wlt_url + "?cmd=logout"
        req = urllib.request.Request(logout_url, headers=self.header, method="GET")
        self.opener.open(req)
