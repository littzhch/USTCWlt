"""
ustcwlt
v0.3
"""

__all__ = ["NetworkError", "IpError", "LoginError"]



class NetworkError(Exception):
    def __init__(self, err="网络连接出错"):
        Exception.__init__(self, err)

class IpError(Exception):
    def __init__(self, err="非科大IP地址"):
        Exception.__init__(self, err)

class LoginError(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)