# task-nextjs-fastapi

### 環境構築手順

1. 秘密鍵、証明書署名要求、サーバー証明書の配置

   container/nginx/ssl ディレクトリ直下に任意の秘密鍵、証明書署名要求、サーバー証明書を作成して配置する

2. 環境変数ファイルの作成(バックエンド用)

   source/backend/app ディレクトリ直下に以下の内容で「.env」ファイルを作成する

   ```
   ALLOW_ORIGINS=["{許可するオリジン}"]
   ALLOW_HEADERS=["{許可するヘッダー}"]

   DATABASE_URL={データベースのURL}
   TEST_DATABASE_URL={テスト用データベースのURL}

   CSRF_KEY={CSRFトークンのキー}
   JWT_KEY={JWTトークンのキー}

   DEBUG=True
   ```

3. Docker コンテナの起動

   `docker compose up -d`

   バックエンド　 https://localhost

   フロントエンド　 http://localhost:3000
