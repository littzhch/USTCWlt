# USTCWlt 使用指南
## 功能实现
### `class ustcwlt.WltAccount(user_name, password)`
该类提供了所有的功能
 
    参数user_name：str，网络通账号的用户名
    参数password： str，网络通账号的密码
 
该类包括如下方法：
#### `WltAccount.login(connect=False)`
登录账号
 
    参数connect：bool
      若为False，仅登录账号
      若为True，登录账号并根据常用设置开通网络

#### `WltAccount.get_info()`
获取账号信息
 
access为调用login()方法时获取的；
其它信息都是调用本方法时获取的实时信息
 
    返回：dict
    {
     "ip":              str，当前网络的IP地址
     "currentport":     int，当前账号的网络出口；范围为1-9，下同
     "prefport":        int，常用设置的网络出口
     "preftime":        int，常用设置的连接时间；单位为秒，若为0则代表永久，下同
     "access":          int，若为0, 则当前账号未开通网络通服务；若为1，则已开通
    }
    
    
#### `WltAccount.set_connection(port=None, time=None)`
开通网络

    参数port: int 网络出口
    参数time: int 开通时间
    特别，当port和time都为None时，按照常用设置开通网络

    
#### `WltAccount.set_preference(port, time)`
更改常用设置

    param port: int 网络出口
    param time: int 开通时间

#### `WltAccount.logout()`
退出登录

    注意：退出后网络将断开
    
    
## 异常处理
#### `exception ustcwlt.NetworkError`
网络连接出错
 
在创建WltAccount类的实例及调用各方法时都可能触发

#### `exception ustcwlt.LoginError`
登录出现问题
 
在调用login()方法时，若使用非科大IP地址；输入的用户名不存在；或输入的密码错误，会抛出此异常

#### `exception ustcwlt.AccessError`
无权进行操作
 
在调用get_info(), set_connection(), set_preference()方法时，若还未登录或账户未开用网络通服务，会抛出此异常

#### `exception TypeError & ValueError`
在调用set_connection()和set_preference()方法时，若参数类型不符合
要求，会抛出TypeError；若参数范围不符合要求，会抛出ValueError
