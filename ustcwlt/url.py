"""
ustcwlt
v0.3
"""

__all__ = ["generate_url"]


def generate_url(type, data=None):
    """
    type: "base"       data:  None
          "showc"             None
          "setc"              (port, time) int(1-9) int(sec)
          "showp"             None
          "setp"              (port, time)
          "logout"            None
    """
    url = "http://wlt.ustc.edu.cn/cgi-bin/ip"
    if type == "base":
        return url

    if type == "showc":
        url += "?cmd=disp"
        return url

    if type == "setc":
        url += "?cmd=set&url=URL&type=" + str(data[0] - 1) + \
                      "&exp=" + str(data[1])
        return url

    if type == "showp":
        url += "?cmd=pref"
        return url

    if type == "setp":
        url += "?cmd=pref&url=URL&type=" + str(data[0] - 1) + \
                      "&exp=" + str(data[1])
        return url

    if type == "logout":
        url += "?cmd=logout"
        return url