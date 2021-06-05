"""
ustcwlt
v1.0
url.py
生成不同请求的url
"""

__all__ = ["generate_url"]


def generate_url(urltype, data=None):
    """
    urltype: "base"       data:  None
          "showc"             None
          "setc"              (port, time) int(1-9) int(sec)
          "fastsetc"          None
          "showp"             None
          "setp"              (port, time)
          "logout"            None
    """
    url = "http://wlt.ustc.edu.cn/cgi-bin/ip"
    if urltype == "base":
        return url

    if urltype == "showc":
        url += "?cmd=disp"
        return url

    if urltype == "setc":
        url += "?cmd=set&url=URL&urltype=" + str(data[0] - 1) + \
                      "&exp=" + str(data[1])
        return url

    if urltype == "fastsetc":
        url += "?cmd=set"
        return url

    if urltype == "showp":
        url += "?cmd=pref"
        return url

    if urltype == "setp":
        url += "?cmd=pref&url=URL&urltype=" + str(data[0] - 1) + \
                      "&exp=" + str(data[1])
        return url

    if urltype == "logout":
        url += "?cmd=logout"
        return url
