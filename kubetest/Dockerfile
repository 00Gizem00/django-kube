FROM python:3.12.3-slim

COPY . /app

WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip && \ 
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]