"""
ustcwlt
v1.0
一个提供南七技校校园网（网络通）登录、查询、设置功能的Python库
"""

import ustcwlt.account
import ustcwlt.error

WltAccount = ustcwlt.account.WltAccount
NetworkError = ustcwlt.error.NetworkError
AccessError = ustcwlt.error.AccessError
LoginError = ustcwlt.error.LoginError
