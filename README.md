# About
这是一个在Linux系统下，使用容器运行微信的方案。
*   容器运行环境：Docker、Wine、LXDE、xRDP
    -   LXDE：轻量的桌面环境，微信只能在图形界面下安装和运行。
    -   xRDP：用于从``Windows``远程连接桌面进行配置。
*   基于[WeChatFerry](https://github.com/lich0821/WeChatFerry)部署，
    thanks to [lich0821](https://github.com/lich0821)
*   资源使用情况：
    -   磁盘：
        -   构建后镜像大小约4.69G；
        -   Wine第一次启动，自动初始化后容器占用1.49G；
        -   微信安装后，初始状态占用1.41G。
            默认配置已将这部分文件放到宿主机的挂载目录；
        -   微信长期使用，磁盘占用会持续增加；
    -   内存：
        -   桌面登录后，总占用194M；
        -   微信启动，总占用约1.7G，微信登录后，总占用约**4.9G**。
            宿主机需要预留充足的内存空间；

# Usage
## 获取资源
在[WeChatFerry发布页](https://github.com/lich0821/WeChatFerry/releases)
下载安装包``WeChatSetup``和工具包``v??.?.?.zip``，放到工程目录``./package``。

WeChatFerry迭代频繁，当前**最新版本是![PyPi](https://img.shields.io/pypi/v/wcferry.svg)**

## 构建镜像
```sh
$ sudo ./docker/docker_build.sh
```

*   默认使用``root``作为xRDP用户，默认密码为``123``，请按需修改。

## 启动镜像
```sh
$ sudo ./docker/docker_run.sh
```

启动脚本的默认容器访问配置，``宿主机`` => ``容器``关系如下，请按需调整：
*   端口映射：
    -   xRDP端口： ``13389`` => ``3389``
    -   WeChatFerry命令端口： ``18001`` => ``8001``
    -   WeChatFerry消息端口： ``18002`` => ``8002``
*   目录挂载：
    -   安装资料： ``./package`` => ``/root/package`` (仅在第一次安装微信时使用)
    -   程序文件： ``./wechat/program`` => ``/root/.wine/drive_c/Program\ Files/Tencent/WeChat``
    -   图标文件： ``./wechat/share/icons`` => ``/root/.local/share/icons``
    -   用户数据： ``./wechat/user_dat`` => ``/root/.wine/drive_c/users/root/AppData/Roaming/Tencent/WeChat``
    -   **将程序和用户数据目录挂载到宿主机，可避免在容器重置后再次安装程序**。

## 登录桌面
*   ``Windows``启动``远程桌面连接``，**地址**：``服务器IP:13389``
*   进入xRDP登录窗口，**username**：``root``，**password**：``123``

## 安装微信
*   如果已配置了挂载目录，且已安装过微信，则不需要再次安装。
*   进入桌面，启动安装程序。有2种启动方式：
    1.  桌面快捷方式启动： 打开桌面图标``WeChatSetup``
    2.  命令行启动：左下角启动终端``LXTerminal``，执行：
        ```sh
        $ wine package/WeChatSetup-*.exe
        ```
*   开始常规安装流程，完成安装后关闭。

## 启动微信
*   进入桌面，启动应用。有2种启动方式：
    1.  桌面快捷方式启动： 打开桌面图标``WeChatFerry``
    2.  命令行启动：左下角启动终端``LXTerminal``，执行：
        ```sh
        $ ./res/launch.sh
        ```
        启动后终端不能关闭或退出。
*   微信常规配置，左下角Settings：
    -   Notifications：关闭所有
    -   General -> General：不选所有
    -   Manage Files -> Auto-Download：不选
*   启动并登录后，直接关闭远程桌面，不要``Logout``。
    因为登出后图形界面下运行的所有程序都会退出。

## 测试
在主机运行测试脚本：``./test/test_wcferry.py``，消息默认发送给``文件传输助手``。

# FAQ
## 版本说明
*   版本号和WeChatFerry保持基本一致，方便对照
*   ``tag: v39.2``：支持WeChatFerry的``tag: v39.2.x``及以上版本

## 运行报错
*   故障现象：
    -   不同环境现象不同，目前遇到以下几种
    -   启动过程中Wine报错并退出
    -   Wine启动立即报错并退出
    -   xRDP连接报错
*   故障分析：
    -   目前启动异常的情况，常见于使用旧发行版系统的服务器，
        如：CentOS 7 (kernel 4.x)。
    -   经验证，使用较新发行版系统的服务器，都可以正常运行。
        如：Fedora 39/40 (kernel 6.x)
    -   具体原因暂不明确，推测与内核版本有关。
*   解决方案：
    -   建议使用较新的Linux发行版。

## 闪退或应用黑屏
*   故障现象：
    -   应用启动立即退出
    -   应用界面是黑的，但可以点击可以拖动，拖动过程又能看到应用界面
*   故障分析：
    -   故障出现之前有正常运行过。
    -   目前仅在调试阶段有遇到。
    -   调试过程中，某些操作可能误杀了系统服务进程
*   解决方案：
    -   关闭并删掉容器，重新启动镜像

