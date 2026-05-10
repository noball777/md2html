# md2html_folio

MarkdownファイルをリッチなHTMLとして表示するローカルビューワーです。  
**viewer.html を Chrome/Edge で開くだけで使えます。インストール不要。**

---

## 使い方

1. [`viewer.html`](viewer.html) をダウンロード
2. Chrome または Edge で開く
3. MDファイルをウィンドウにドロップ（またはボタンから選択）

## 機能

| 機能 | 説明 |
| --- | --- |
| MDレンダリング | GFM（テーブル・チェックリスト・打ち消し線）対応 |
| 目次（TOC） | 見出しから自動生成、スクロール追従 |
| シンタックスハイライト | コードブロックを言語別に色付け |
| Mermaidダイアグラム | \`\`\`mermaid ブロックを図として描画 |
| セクションメモ | 各見出しにメモを追加（元ファイルは変更しない） |
| ライブラリ | 保存フォルダを設定して閲覧履歴を管理 |
| 書き出し | メモ込みのスタンドアロンHTMLとしてエクスポート |
| ダークモード | ライト/ダーク切り替え |
| 印刷/PDF | ブラウザの印刷機能でそのままPDF出力可 |

## AI機能（オプション）

> ⚠️ AI機能は任意です。設定しなくても全機能が使えます。

### 対応プロバイダー

| プロバイダー | 必要なもの | 備考 |
| --- | --- | --- |
| OpenAI (ChatGPT) | APIキー | [取得はこちら](https://platform.openai.com/api-keys) |
| Google Gemini | APIキー | [取得はこちら](https://aistudio.google.com/app/apikey) |
| LM Studio | LM Studio本体 | ローカル動作・無料 |

### AI機能の注意事項

- APIキーはお使いのブラウザにのみ保存されます。外部サーバーへは送信されません。
- AIの出力精度はプロバイダーやモデルにより異なります。
- より精度の高い結果を得るには、MDファイルをAIサービスのWebUIに直接貼り付けることをお勧めします。
- 動作確認済み以外のプロバイダーのご利用は自己責任でお願いします。

### LM Studio のセットアップ

1. [LM Studio](https://lmstudio.ai) をインストール
2. モデルをダウンロードして読み込む
3. 「Local Server」タブ → **Start Server**
4. viewer.html の「AI設定」→ LM Studio を選択 → 接続テスト

## 動作環境

- **Chrome** または **Edge**（最新版推奨）
- ファイルの保存機能には [File System Access API](https://caniuse.com/native-filesystem-api) が必要です

> Firefox では一部機能（ファイル保存）が使えません。

## 配布・利用

MITライセンスで配布しています。社内・個人利用ともに自由に使用できます。

---

*MDを読むための道具、シンプルに。*
