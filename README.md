# About
用于运行微信Hook的Docker配置。
*   运行环境：Docker、Wine、LXDE、xRDP
    -   LXDE：轻量的桌面环境，微信只能在图形界面下安装和运行。
    -   xRDP：用于从``Windows``远程连接桌面进行配置。
*   基于[WeChatFerry](https://github.com/lich0821/WeChatFerry)部署，thanks to [lich0821](https://github.com/lich0821/WeChatFerry/commits?author=lich0821)
*   资源使用情况：
    -   内存：微信和相关服务使用约2.3G；
    -   磁盘：镜像大小6.95G。前期容器小于1G，长期使用将持续扩大；

# Usage
## 获取资源
在[Releases](https://github.com/Saroth/docker_wechat/releases)
下载安装包``WeChatSetup``和工具包``v??.?.?.zip``，放到工程目录``docker/res``。

## 构建镜像
```sh
$ cd docker
$ sudo ./docker_build.sh
```

``Dockerfile``中，默认``root``密码为``123``，请按需修改。

## 启动镜像
```sh
$ sudo ./docker_run.sh
```

``docker_run.sh``默认端口映射，请按需调整：
*   xRDP端口：3389，映射到主机13389
*   WeChatFerry命令端口：8001，映射到主机18001
*   WeChatFerry消息端口：8002，映射到主机18002

## 安装应用
*   ``Windows``启动``远程桌面连接``，**地址**：``服务器IP:13389``
*   进入xRDP登录窗口，**username**：``root``，**password**：``123``
*   进入桌面，启动安装程序。提供2种方式：
    1.  命令行启动：左下角启动终端``LXTerminal``，执行：
        ```sh
        $ wine res/WeChatSetup-3.9.2.23.exe
        ```
    2.  新增快捷方式启动：双击桌面图标``WeChatSetup``

开始常规安装流程，完成安装后关闭。

## 启动应用
*   进入桌面，启动应用。提供2种方式：
    1.  命令行启动：
        ```sh
        $ ./launch.sh
        ```
    2.  新增快捷方式启动：双击桌面图标``WeChatFerry``
*   微信常规配置，左下角Settings：
    -   Notifications：关闭所有
    -   General -> General：不选所有
    -   Manage Files -> Auto-Download：不选
*   启动并登录后，直接关闭远程桌面，不要``Logout``。因为登出后图形界面下运行的所有程序都会退出。

