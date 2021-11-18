# Base/production image
FROM python:3.9.7-slim-bullseye AS build
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    build-essential \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install --no-cache-dir --upgrade pip==21.3.1

# Install dependencies
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

FROM python:3.9.7-slim-bullseye AS production

LABEL org.opencontainers.image.source="https://github.com/alekspog/stepik-telegram-bot"

# Copy venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY --from=build /opt/venv /opt/venv

# Copy code
WORKDIR /app
COPY . /app

CMD ["python", "send_reviews.py"]
