# python-template

VSCode + devcontainer + uv + ruffを使い、できるだけシンプルな構成を目指した

## できること

- uvを使ったパッケージ管理
- devcontainerでの開発
- デプロイ用のDockerfileはなるべく軽量になるように設計

## 各コンポーネントの役割

### devcontainer

- Dockerfile
    - slimのイメージにuvコマンドを追加し、適当にパッケージインストール
- devcontainer.json
    - いつも利用する拡張機能をdevcontainer側にインストール
    - ruffの拡張経由で自動lint+formattingできるようにSetting
    - コンテナ起動時に多少の設定を行う(XXXCreateCommand)

### pyproject.toml

- 多少のdevツールをインストール

### Dockerfile

- マルチステージビルドでを使ってビルドされるimageはなるべく軽量に
- slimのイメージにuvツールをインストールして、.venvにsync
- .venvをslimのみのイメージに移して、pathに追加することで.venvベースで起動

## 試す

1. git cloneする
2. vscodeにDev Containersを入れる
3. vscode右下の「><」マークから 「コンテナーで再度開く」
4. 開いたら開発する
5. sudo docker build . -t hogehogeでメインのコンテナをビルドできる

## 使う

本テンプレートはcopierに対応している

`uv tool install copier`

`copier copy gh:kbf09/python-template /path/to/project`