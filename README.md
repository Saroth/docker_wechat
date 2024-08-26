# About
用于运行微信Hook的Docker配置。
*   运行环境：Docker、Wine、LXDE、xRDP
    -   LXDE：轻量的桌面环境，微信只能在图形界面下安装和运行。
    -   xRDP：用于从``Windows``远程连接桌面进行配置。
*   基于[WeChatFerry](https://github.com/lich0821/WeChatFerry)部署，thanks to [lich0821](https://github.com/lich0821/WeChatFerry/commits?author=lich0821)
*   资源使用情况：
    -   磁盘：
        -   构建后镜像大小约4.63G；
        -   Wine第一次启动，自动初始化后占用1.49G；
        -   微信安装后，初始状态占用1.41G；
        -   微信长期使用，磁盘占用会持续增加；
    -   内存：
        -   桌面登录后，总占用165M；
        -   微信启动并登录后，总占用1.86G；

# Usage
## 获取资源
在[Releases](https://github.com/Saroth/docker_wechat/releases)
下载安装包``WeChatSetup``和工具包``v??.?.?.zip``，放到工程目录``/package``。

**WeChatFerry迭代频繁，最新版本[![PyPi](https://img.shields.io/pypi/v/wcferry.svg)](https://pypi.python.org/pypi/wcferry)在[WeChatFerry-Release](https://github.com/lich0821/WeChatFerry/releases)获取**。

## 构建镜像
```sh
$ sudo ./docker/docker_build.sh
```

关于``Dockerfile``:
-   使用``root``作为xRDP默认用户。
-   ``root``默认密码为``123``，请按需修改。

## 启动镜像
```sh
$ sudo ./docker/docker_run.sh
```

脚本有容器访问配置，``宿主机`` => ``容器``关系如下，请按需调整：
*   端口映射：
    -   xRDP端口： ``13389`` => ``3389``
    -   WeChatFerry命令端口： ``18001`` => ``8001``
    -   WeChatFerry消息端口： ``18002`` => ``8002``
*   目录挂载：
    -   安装资料： ``./package`` => ``/root/package`` (仅在第一次安装微信时使用)
    -   程序文件： ``./wechat/program`` => ``/root/.wine/drive_c/Program\ Files/Tencent/WeChat``
    -   图标文件： ``./wechat/share/icons`` => ``/root/.local/share/icons``
    -   用户数据： ``./wechat/user_dat`` => ``/root/.wine/drive_c/users/root/AppData/Roaming/Tencent/WeChat``
    -   **将程序和用户数据目录挂载到宿主机，在容器删除并重启后，避免再次安装程序**。

## 安装应用
*   ``Windows``启动``远程桌面连接``，**地址**：``服务器IP:13389``
*   进入xRDP登录窗口，**username**：``root``，**password**：``123``
*   进入桌面，启动安装程序。有2种启动方式：
    1.  命令行启动：左下角启动终端``LXTerminal``，执行：
        ```sh
        $ wine package/WeChatSetup-3.9.10.27.exe
        ```
    2.  桌面快捷方式启动：双击桌面图标``WeChatSetup``

开始常规安装流程，完成安装后关闭。

## 启动应用
*   进入桌面，启动应用。有2种启动方式：
    1.  命令行启动：
        ```sh
        $ ./launch.sh
        ```
    2.  桌面快捷方式启动：双击桌面图标``WeChatFerry``
*   微信常规配置，左下角Settings：
    -   Notifications：关闭所有
    -   General -> General：不选所有
    -   Manage Files -> Auto-Download：不选
*   启动并登录后，直接关闭远程桌面，不要``Logout``。因为登出后图形界面下运行的所有程序都会退出。

## 测试
在主机运行测试脚本：``./test/test_wcferry.py``，消息默认发送给``文件传输助手``。

# FAQ
## 关于版本

## 关于各种运行异常

