"""
ustcwlt
v0.3
"""

__all__ = ["NetworkError", "PermissionError", "LoginError"]


class NetworkError(Exception):
    def __init__(self, err="网络连接出错"):
        Exception.__init__(self, err)

class PermissionError(Exception):
    def __init__(self, err="无权进行操作"):
        Exception.__init__(self, err)

class LoginError(Exception):
    def __init__(self, err="登录出现问题"):
        Exception.__init__(self, err)