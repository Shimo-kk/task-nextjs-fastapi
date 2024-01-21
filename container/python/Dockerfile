FROM python:3.9

# ワークディレクトリを指定
WORKDIR /source

# 環境変数を設定
ENV PYTHONPATH /source
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# ソースコードをコンテナにコピー
COPY ./source/backend /source

# コンテナ内でpipをアップグレード
RUN pip install --upgrade pip
# 各パッケージをインストール
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--reload", "--port", "8000", "--host", "0.0.0.0"]