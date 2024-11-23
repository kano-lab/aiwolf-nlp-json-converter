# aiwolf-nlp-json-converter

## 対応していないキー
[旧ゲームサーバ](https://github.com/aiwolfdial/AIWolfNLPServer)から与えられる情報の内、本プログラムではいくつか含まれていない情報が存在します。 \
下記に詳細を記載しますので、ご確認の上ご使用ください。

### ゲームの現状態を示す情報 (gameInfo)
- `cursedFox`: 妖狐は5人、13人人狼で使用しない予定の役職なので対応していません。
- `englishTalkList`: 過去にここに割り当てられていた内容が`TalkList`と同一であったため、不要と判断し対応していません。
- `existingRoleList`: `gameSetting`の`roleNumMap`から把握できる内容であるため不要と判断し対応していません。
- `guardedAgent`: 騎士は5人人狼で使用しない予定の役職なので対応していません。
- `latestAttackVoteList`: 5人人狼において使用されない項目の上、`attackVoteList`から確認できる内容であるため不要と判断し対応していません。
- `latestExecutedAgent`: `executedAgent`の値から確認できる内容であるため不要と判断し対応していません。
- `latestVoteList`: `voteList`から確認できる内容であるため不要と判断し対応していません。
- `mediumResult`: 5人人狼において使用されない項目であるため不要と判断し対応していません。
- `remainTalkMap`: 旧サーバにおいて`INITIALIZE`,`DAILY_INITIALIZE`でのみ付与されていた情報である上、`maxTalk`から取得可能な内容であるため不要と判断し対応していません。
- `remainWhisperMap`: 5人人狼において`whisper`は行われないため不要と判断し対応していません。
- `talkList`:  旧サーバにおいて`INITIALIZE`,`DAILY_INITIALIZE`でのみ付与されていた情報である上、`talkHistory`から取得可能な内容であるため不要と判断し対応していません。
- `whisperList`: 5人人狼において使用されない項目であるため不要と判断し対応していません。

### ゲームの設定を示す情報 (gameSetting)
- `enableRoleRequest`: 新サーバにおいて削除された機能であるため対応していません。
- `validateUtterance`: 新サーバにおいて削除された機能であるため対応していません。
- `votableInFirstDay`: 大会において初日は挨拶の日であり、その人に投票は行わないため対応していません。
- `whisperBeforeRevote`: 5人人狼において使用されない項目であるため不要と判断し対応していません。

