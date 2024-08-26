#!/bin/sh
# 退出微信并清理用户数据。仅用于开发调试

path="/root/.wine/drive_c/"
rm -rf ${path}users/root/AppData/Roaming/Tencent/*

pid=`ps aux | grep WeChat | grep -v grep | awk '{print $2}'`
if [ -n "${pid}" ]; then
    kill ${pid}
fi

