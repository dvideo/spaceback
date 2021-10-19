FROM python:3.9.4

RUN mkdir -p /workspace/backend/

COPY ./backend/Pipfile ./backend/Pipfile.lock /workspace/backend/

RUN pip install pipenv && \
    cd /workspace/backend/ && \
    pipenv install --system --deploy

RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs