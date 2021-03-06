FROM python:3.7-alpine AS builder

COPY requirements.txt /
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
 && pip install cython \
 && apk del .build-deps

RUN apk add --no-cache python3-dev libressl-dev musl-dev libffi-dev libpng-dev freetype-dev build-base jpeg-dev zlib-dev libxml2-dev
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install --user --upgrade pip
RUN pip install --user -r /requirements.txt
ENV TZ="America/Chicago"

FROM python:3.7-alpine
RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev py3-lxml && \
    apk add --no-cache libxslt && \
    pip install --no-cache-dir lxml>=3.5.0 && \
    apk del .build-deps
ENV TZ="America/Chicago"
COPY --from=builder /root/.local /root/.local
COPY / /mailtrail
WORKDIR /mailtrail

RUN export PYTHONPATH=/mailtrail:$PYTHONPATH
RUN python setup.py install

CMD [ "python", "/mailtrail/run.py" ]
