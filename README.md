![image](https://user-images.githubusercontent.com/49507721/111910368-0cd8d400-8a9c-11eb-9167-57f101761286.png) 
![wlt32](https://user-images.githubusercontent.com/49507721/111910558-d3ed2f00-8a9c-11eb-9b8a-67f994e51358.png)
![wlt48](https://user-images.githubusercontent.com/49507721/111910537-bfa93200-8a9c-11eb-9912-630a55d48400.png)  

# USTCWlt

这是一个提供登录中国数学物理大学（USTC）网络通和设置网络功能的Python库

## 安装
```
pip3 install USTCWlt
```
或者
```
pip install USTCWlt
```

## 使用
```
import ustcwlt
```

具体用法请参考[使用指南](https://github.com/littzhch/USTCWlt/blob/main/MANUAL.md)和[示例程序](https://github.com/littzhch/USTCWlt/blob/main/example.py)

## 已知问题

- 短时间内进行大量操作会出现以下提示，这会导致程序出错
 
    ![err](https://user-images.githubusercontent.com/49507721/115254073-9644fa00-a15f-11eb-9bbc-7820c56d5524.PNG)
- 没有考虑10元/月的网络通账号（因为我周围的人都没有，所以我也不知道是啥样😏）

## 注意
- 网络通网站使用明文存储和传输密码，安全性较低
- 请勿滥用
- 代码只经过简单的测试，如发现bug，欢迎提出
