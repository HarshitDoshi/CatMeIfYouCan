FROM fedora:latest

RUN dnf update -y
RUN dnf upgrade -y
RUN dnf distro-sync -y

RUN dnf install -y git gcc make procps-ng file libxcrypt-compat
RUN dnf install -y man wget curl tmux htop
RUN dnf install -y \
    zlib-devel \
    bzip2 bzip2-devel \
    readline-devel \
    sqlite sqlite-devel \
    openssl-devel \
    tk-devel \
    libffi-devel \
    xz-devel
RUN dnf group install -y "Development Tools"

RUN cd ~ && mkdir scripts
COPY ./scripts/ /scripts

RUN ls -hal /scripts
RUN chmod +700 /scripts/pyenv_setup.sh
RUN /scripts/pyenv_setup.sh

RUN chmod +700 /scripts/nvm_setup.sh
RUN /scripts/nvm_setup.sh

RUN chmod +700 /scripts/homebrew_setup.sh
RUN /scripts/homebrew_setup.sh
