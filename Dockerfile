FROM python:3.10-slim AS backend-builder

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -rm -d /connectors -g ${APP_USER} ${APP_USER}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Install runtime dependencies and clean it
RUN set -ex \
    && RUN_DEPS=" \
    cron \
    git \
    libcurl4-openssl-dev \
    libssl-dev \
    postgresql-client \
    vim \
    curl \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Copy django requirements file
ADD apps/requirements.txt /requirements.txt

# Install build dependencies and clean it
RUN --mount=type=ssh set -ex \
    && BUILD_DEPS=" \
    build-essential \
    gcc \
    libpcre3-dev \
    libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*


FROM backend-builder AS webapp

WORKDIR /connectors

COPY . .
COPY crontabs/tasks.prod /etc/cron.d/${APP_USER}

# Setup right permissions for APP_USER
RUN chmod +x ./django.sh \
    && chown -R ${APP_USER}:${APP_USER} /connectors \
    && chmod 755 /connectors \
    && chmod gu+s /usr/sbin/cron \
    && chmod 0644 /etc/cron.d/${APP_USER} \
    && crontab -u ${APP_USER} /etc/cron.d/${APP_USER}

USER ${APP_USER}:${APP_USER}

EXPOSE 8000

ENTRYPOINT ["./django.sh"]
