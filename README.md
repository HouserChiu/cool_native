# 使用frida破解Native层加密

所需设备和环境：

设备：安卓手机(获取root权限)

抓包：fiddler + xposed + JustTrustMe

反编译：jadx-gui，ida

# 抓包

按照惯例，这里隐去app的名称，开启fiddler抓包后app提示连接不到网络，判断是证书验证，开启xposed框架，再次请求，成功抓到包，连续请求两次来对比参数变化：
