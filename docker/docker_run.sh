#!/bin/sh
# 容器启动命令示例

docker run -itd \
    -p 13389:3389 \
    -p 18001:8001 \
    -p 18002:8002 \
    -v ./package:/root/package \
    -v ./wechat/program:/root/.wine/drive_c/Program\ Files/Tencent/WeChat \
    -v ./wechat/share/icons:/root/.local/share/icons \
    -v ./wechat/user_dat:/root/.wine/drive_c/users/root/AppData/Roaming/Tencent/WeChat \
    --ulimit nofile=8192 \
    --name wechat_ferry \
    wechat_ferry:0.1

