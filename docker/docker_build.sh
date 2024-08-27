#!/bin/sh
# 容器构建命令示例
PWD=$(cd `dirname $0`; pwd)
cd $PWD/..

# 编译注入器
echo -n "Compile injector for Windows... "
cd ./injector
GOOS=windows go build
if [ $? -ne 0 ]; then
  echo "[Error]"
  exit -1
fi
echo "[OK]"
mv injector.exe ../res
cd ..

docker build \
  -f ./docker/Dockerfile \
  -t wechat_ferry:0.1 \
  .

