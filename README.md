# About
用于在Linux平台运行微信机器人的Docker配置.
*   运行环境: Docker, Wine, LXDE
*   采用Hook方案, 参考资料: [WeChatFerry](https://github.com/lich0821/WeChatFerry)

# Usage
## 获取资源
在[Releases](https://github.com/lich0821/WeChatFerry/releases)
下载安装包``WeChatSetup``和工具包``v??.?.?.zip``, 放到工程目录``docker/res``

## 构建镜像
```sh
$ cd docker
$ sudo ./docker_build.sh
```

``Dockerfile``中, 默认``root``密码为``123``, 请按需修改.

## 启动镜像
```sh
$ sudo ./docker_run.sh
```

``docker_run.sh``默认端口映射, 请按需调整:
*   xRDP端口: 3389, 映射到主机13389
*   WeChatFerry命令端口: 8001, 映射到主机18001
*   WeChatFerry消息端口: 8002, 映射到主机18002

## 安装应用
*   启动Windows的``远程桌面连接``, 地址填写:``服务器IP:13389``, 点``连接(N)``;
*   xRDP登录窗口, ``username``: root, ``password``: 123, 点``OK``;
*   进入桌面
    1.  双击桌面图标``WeChatSetup``
    2.  在终端安装: 左下角启动终端``LXTerminal``, 执行:
        ```sh
        $ wine res/WeChatSetup-3.9.2.23.exe
        ```
    开始常规安装流程. 完成后关闭.

## 启动应用
*   进入桌面
    1.  双击桌面图标``WeChatFerry``
    2.  在终端启动:
        ```sh
        $ ./launch.sh
        ```

