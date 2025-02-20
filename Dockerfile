# 拉取基础镜像
FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .
COPY ./simple_fastapi.py .

RUN pip3 install -r requirements.txt

# 暴漏 8040 端口
EXPOSE 8040

CMD ["python","simple_fastapi.py"]