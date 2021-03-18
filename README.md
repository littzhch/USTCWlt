# USTCWlt
这是一个提供登录南七技校网络通和设置网络功能的Python库

## 食用方法
参考[MAUNAL.md](https://github.com/littzhch/USTCWlt/develop/MANUAL.md)
- step 1: 导入
```Python
import ustcwlt
```

<br/></br>
- step 2: 创建WltAccount类的实例
```Python
wa = ustcwlt.WltAccount(user_name="name", password="123456", user_agent="...")
```
user_agent为用户代理字符串，默认为win10新版Edge，可不指定

<br/></br>
- step 3: 调用login()方法登录账号
```Python
wa.login()
```

<br/></br>
- step 4: 调用set_connection方法设置网络
```Python
wa.set_connection(port=8, time=14)
```
port: 整数1-9，对应9个网络出口
 
time: 开通时间（小时），0为永久
  
<br/></br>
现在已经连上校园网了，如果想要断开连接，可退出登陆:
```Python
wa.logout()
```

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
