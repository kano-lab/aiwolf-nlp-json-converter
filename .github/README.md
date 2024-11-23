# aiwolf-nlp-converter

## 対応していないキー
[旧ゲームサーバ](https://github.com/aiwolfdial/AIWolfNLPServer)から与えられる情報の内、本プログラムではいくつか含まれていない情報が存在します。 \
下記に詳細を記載しますので、ご確認の上ご使用ください。

### ゲームの現状態を示す情報 (gameInfo)
- `cursedFox`: 妖狐は5人、13人人狼で使用しない予定の役職なので対応していません。
- `englishTalkList`: 過去にここに割り当てられていた内容が`TalkList`と同一であったため、不要と判断し対応していません。
- `existingRoleList`: `gameSetting`の`roleNumMap`から把握できる内容であるため不要と判断し対応していません。
- `guardedAgent`: 騎士は5人人狼で使用しない予定の役職なので対応していません。