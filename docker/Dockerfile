# FROM fedora:latest
FROM fedora:39
LABEL describe="Fedora for WeChat hook, base on LXDE, Wine, xRDP, WeChatFerry."

WORKDIR /root
RUN dnf update -y \
        && dnf groupinstall -y "LXDE" \
        && dnf install -y wine \
        && dnf install -y xrdp \
        && dnf clean all

COPY ./res ./res

RUN echo "root:123" | chpasswd \
        && mkdir ~/Desktop \
        && mv res/*.desktop ~/Desktop \
        && mv res/*.sh . \
        && unzip -o res/v*.zip -d res

# Port for xRDP
EXPOSE 3389
# Port for WeChatFerry command
EXPOSE 8001
# Port for WeChatFerry message
EXPOSE 8002

ENTRYPOINT ["./entrypoint.sh"]
CMD ["bash"]

