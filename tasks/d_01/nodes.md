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

出力予想
[False, False, True]

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


## K04
次のコードの出力2行を予想し、行・列の数え方の理由を1文で説明してください。

```python
# AI担当：観測メモを使う知識確認のコード。本番の解答ではない。
import csv
from io import StringIO

rows = list(csv.reader(StringIO('station,note\nA,"cool, windy"\n')))
print(len(rows))
print(len(rows[1]))
```

コード
len(rows) : 2, /nで区切られる。2要素, newline引数で改行のコードの扱いが変わる, 基本は ""とするのがいい、なぜなら、\rと\r\nの場合、\rは改行として認められず、\r\nは\nに変換される。
len(rows[1]) : 16, 「A,"cool, windy"\n」の文字数。

## K05
次のコードの出力1行を予想してください。読み取り後の item が文字列か数値かも答え、その理由を1文で説明してください。

```python
# AI担当：小さな物品記録を使う知識確認のコード。本番の解答ではない。
from io import StringIO
import pandas as pd

frame = pd.read_csv(StringIO("item,quantity\n004,2\n"))
print(frame.loc[0, "item"])
```

frame.loc[0, "item"] : ["004", "2"]
read_csvはcsv.readと異なり ","と改行を読み解き要素に分けることができる。

検証環境のpandasは3.1.1です。読み込み方を変更するコードや本番の設計判断は求めていません。

## K06
次のコードの出力2行を予想し、理由を1文で説明してください。
```python
# AI担当：短い観察メモを使う知識確認のコード。本番の解答ではない。
from io import BytesIO

source = BytesIO(b"sun")
print(source.read())
print(source.read())
```
１行目 : sunの文字列をバイト変換した値が表示される(readはメモリに全ての値を展開する)
2行目 : 同様
