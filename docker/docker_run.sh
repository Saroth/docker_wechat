#!/bin/sh

docker run -itd \
    -p 13389:3389 \
    -p 18001:8001 \
    -p 18002:8002 \
    --ulimit nofile=8192 \
    --name wechat_hook \
    wechat_hook:0.1

