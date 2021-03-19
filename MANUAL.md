# USTCWlt 使用指南
## 功能实现
### `class ustcwlt.WltAccount(user_name, password)`
该类提供了所有的功能
 
    参数user_name：str，网络通账号的用户名
    参数password： str，网络通账号的密码
 
该类包括如下方法：
#### `self.login([connect])`
登录账号
 
    参数connect：bool，默认为False
      若为False，仅登录账号
      若为True，登录账号并根据常用设置开通网络

#### `self.get_info()`
获取账号信息
 
    返回：dict
    {
     "ip":              str，当前网络的IP地址
     "currentport":     int，当前账号的网络出口
     "prefport":        int，常用设置的网络出口
     "preftime":        int，常用设置的连接时间（秒）
     "access":          int，若为0, 则当前账号未开通网络通服务；若为1，则已开通
    }
    
