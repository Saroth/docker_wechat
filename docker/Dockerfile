# FROM fedora:latest
FROM fedora:40
LABEL describe="Fedora for WeChat, base on LXDE, Wine, xRDP, WeChatFerry."

WORKDIR /root
# 安装基础运行环境和Go开发环境
RUN dnf groupinstall -y "LXDE" \
        && dnf install -y wine \
        && dnf install -y xrdp \
        && dnf clean all
# 复制资料文件
COPY ./res ./res
COPY ./package/v*.zip ./res
COPY ./injector ./injector
# 安装编译器，编译注入器，完成后清理源码/临时文件/编译器
RUN dnf install -y go \
        && cd ./injector \
        && GOOS=windows go build \
        && cd .. \
        && mv ./injector/injector.exe ./res \
        && rm -rf ./injector \
        && rm -rf .cache/go-build \
        && dnf remove -y gcc \
        && dnf clean all
# 部署运行环境
RUN echo "root:123" | chpasswd \
        && mkdir ~/Desktop \
        && mv res/*.desktop ~/Desktop \
        && unzip -o res/v*.zip -d res \
        && rm res/v*.zip

# Port for xRDP
EXPOSE 3389
# Port for WeChatFerry command
EXPOSE 8001
# Port for WeChatFerry message
EXPOSE 8002

ENTRYPOINT ["./res/entrypoint.sh"]
CMD ["bash"]

