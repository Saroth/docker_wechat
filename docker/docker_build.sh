#!/bin/sh
# 容器构建命令示例
PWD=$(cd `dirname $0`; pwd)
cd $PWD/..

docker build \
  -f ./docker/Dockerfile \
  -t wechat_ferry:0.1 \
  .

