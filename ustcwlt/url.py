"""
ustcwlt
v0.3
"""

__all__ = ["get_connection_url"]
_wlt_url = "http://wlt.ustc.edu.cn/cgi-bin/ip"

def get_connection_url(port, time):
    url = _wlt_url + "?cmd=set&url=URL&type=" + str(port - 1) + \
                      "&exp=" + str(time * 3600)
    return url