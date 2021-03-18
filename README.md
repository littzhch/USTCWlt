# USTCWlt
这是一个提供登录南七技校网络通和设置网络功能的Python库

## 食用方法
参考[MANUAL.md](https://github.com/littzhch/USTCWlt/blob/develop/MANUAL.md)


## 异常处理
模块定义了3个异常类，分别为NetworkError，IpError，和LoginError
- NetworkError:
网络连接出现问题，在创建实例、调用3个方法时都有可能触发
- IpError:
使用非科大网址登录，在创建实例时可能触发
- LoginError:
用户名不存在或密码错误，在调用login()方法时可能触发
 
另外，调用set_connection()方法时参数范围错误会触发ValueError

## 最后
模块仍在持续更新中
 
如有bug或需求，欢迎提出
