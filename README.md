# USTCWlt
这是一个提供登录南七技校网络通和设置网络功能的Python库

## 食用方法
<br/>step 1: 导入</br>
```Python
import ustcwlt
```
  
  

<br/>step 2: 创建WltAccount对象的实例</br>
```Python
wa = WltAccount(user_name="name", password="123456", user_agent="...")
```
user_agent为用户代理字符串，默认为win10新版Edge，可不指定
  
  
  
<br/>step 3: 调用login()方法</br>
```Python
wa.login()
```
  
  
  
<br/>step 4: 调用set_connection方法设置网络</br>
```Python
wa.set_connection(port=8, time=14)
```
port: 整数1-9，对应9个网络出口
 
time: 开通时间（小时），0为永久
  
  
  
<br/>现在已经连上校园网了，如果想要断开连接:</br>
```Python
wa.logout()
```
