# FROM fedora:latest
FROM fedora:40
LABEL describe="Fedora for WeChat, base on LXDE, Wine, xRDP, WeChatFerry."

WORKDIR /root
RUN dnf groupinstall -y "LXDE" \
        && dnf install -y wine \
        && dnf install -y xrdp \
        && dnf clean all

COPY ./res ./res
COPY ./package/v*.zip ./res

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

