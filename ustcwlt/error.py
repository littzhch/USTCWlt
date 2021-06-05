"""
ustcwlt
v1.0
error.py
自定义异常类
"""

__all__ = ["NetworkError", "AccessError", "LoginError"]


class NetworkError(Exception):
    """
    网络连接出错
    在创建WltAccount类的实例及调用各方法时都可能触发
    """
    def __init__(self, err="网络连接出错"):
        Exception.__init__(self, err)


class AccessError(Exception):
    """
    无权进行操作
    在调用get_info(), set_connection(), set_preference()方法时，
    若还未登录或账户未开用网络通服务，会抛出此异常
    """
    def __init__(self, err="无权进行操作"):
        Exception.__init__(self, err)


class LoginError(Exception):
    """
    登录出现问题
    在调用login()方法时，若使用非科大IP地址，输入的用户名不存在，
    或输入的密码错误，会抛出此异常
    """
    def __init__(self, err="登录出现问题"):
        Exception.__init__(self, err)