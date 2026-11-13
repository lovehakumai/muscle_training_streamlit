## K01: 次のコードが出力する1行を予想してください。raw と text の違いも1文で説明してください。

```python
# AI担当：知識確認用の別題材コード。課題の解答ではない。
raw = b"rain"
text = "rain"
print(type(raw).__name__, type(text).__name__)
```

rawはbが接頭についたstr型 -> "rain"をバイト表示に変換したもの
textはそのままの文字列"byte"

type(raw)はデータ型を表示するものである。
type(raw) -> Byte
type(text) -> String

__name__プロパティについては知らない。

## K02 : 次のコードが出力する1行を予想してください。空文字 "" と None の違いも1文で説明してください。

```python
# AI担当：知識確認用の別題材コード。課題の解答ではない。
values = ["", "0", None]
print([value is None for value in values])
```

"" -> 文字型, 値がないが文字列として扱われる
None -> None型, 文字列として扱われない、データがない状態の型
として扱われる

## K03:  次のStreamlitアプリを開き、Add を押して処理が終わった後、もう一度 Add を押したとします。2回目の操作が終わった時の表示は何になりますか。理由を1〜2文で説明してください。

```python
# AI担当：実行順を確認する別題材コード。本番の解答ではない。
import streamlit as st

count = 0
if st.button("Add"):
    count += 1
st.write(count)
```

2回目は1になる。なぜならstreamlitは実行ごとにスクリプトを全て再実行するから。count=0で最初に定義しているので何度やり直してもcountは0からのスタートになる。


