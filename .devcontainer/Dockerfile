FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    LANG=JA_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8 \
    TZ=Asia/Tokyo

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    curl \
    wget \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    libgbm1 \
    libdrm2 \
    locales \
    libxslt1.1 \
    libwoff1 \
    libvpx \
    libevent-2.1-7 \
    libopus0 \
    libgstreamer-plugins-base1.0-0 \
    libgstreamer1.0-0 \
    libflite1 \
    libwebpdemux2 \
    libavif15 \
    libharfbuzz-icu0 \
    libwebpmux3 \
    libenchant2 \
    libx264 \
    # libpq-dev \ If you use PostgreSQL
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN sed -i '/ja_JP.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

# poetry (https://python-poetry.org/docs/)
RUN curl -sSL https://install.python-poetry.org | python3.11 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Disable Poetry's virtual environment creation
RUN poetry config virtualenvs.create false
