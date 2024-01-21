FROM node:20.11.0

# ワークディレクトリを指定
WORKDIR /source

# 環境変数を設定
ENV WATCHPACK_POLLING=true

# ソースコードをコンテナにコピー
COPY ./source/frontend /source

# 各パッケージをインストール
RUN npm install

#CMD ["npm", "run", "dev"]