FROM nginx:alpine

# 環境変数を設定
ENV TZ="Asia/Tokyo"

# 設定ファイルをコンテナ内にコピー
COPY ./container/nginx/conf.d/default.conf /etc/nginx/default.conf
COPY ./container/nginx/ssl/server.crt /etc/nginx/ssl/server.crt
COPY ./container/nginx/ssl/server.csr /etc/nginx/ssl/server.csr
COPY ./container/nginx/ssl/server.key /etc/nginx/ssl/server.key