#!/bin/sh

docker run -itd \
    -p 13389:3389 \
    -p 18001:8001 \
    -p 18002:8002 \
    wechat_hook:0.1

