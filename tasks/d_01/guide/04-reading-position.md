# BytesIOと読み取り位置

要点：BytesIOはメモリ上のバイト列をファイルのように扱うものです。`read()` は現在の位置から読み、位置を進めます。末尾にいる時に読み取れる内容は空のbytesです。

K06の回答から、メモリ上のデータと読み取り位置を整理する必要があると分かりました。ここでは短い符号列を使います。

## 目次

- [具体例と実測](#具体例と実測)

- [位置を追う](#位置を追う)

- [読み直しと全体の取得](#読み直しと全体の取得)

- [任意の確認と未確認](#任意の確認と未確認)

- [用語](#用語)

## 具体例と実測

```python
# AI担当：読み取り位置を説明する別題材の例。
from io import BytesIO

source = BytesIO(b"abcde")
print(source.read(2), source.tell())
print(source.read(), source.tell())
print(source.read(), source.tell())
```

2026-11-14、このプロジェクトのルートで `.venv/bin/python`（Python 3.12.0）に例を渡し、AIが実行した出力です。

```text
b'ab' 2
b'cde' 5
b'' 5
```

## 位置を追う

BytesIOを作った時点で、メモリ上に対象のバイト列があります。`read()` はその内容を現在位置から返します。`b"abcde"` は最初からbytesであり、`read()` がstrをbytesへ変換しているわけではありません。

| 操作 | 返す内容 | 操作後の位置 |
|---|---|---|
| 最初に2バイト読む | 先頭の2バイト | 2 |
| 残りを読む | 位置2から末尾まで | 5 |
| もう一度読む | 末尾からは内容がないため空のbytes | 5 |

```mermaid
flowchart LR
    A["位置0"] -->|"2バイト読む"| B["位置2"]
    B -->|"残りを読む"| C["末尾の位置5"]
    C -->|"再び読む"| D["空のbytes、位置は5"]
```

データそのものが消えたわけではなく、読む位置が末尾に進んでいます。`tell()` は現在位置を調べる操作です。

## 読み直しと全体の取得

上の例の続きとして、AIが次を実行しました。

```python
# AI担当：位置を戻す操作と全体を取る操作を比べる別題材の例。
source.seek(0)
print(source.read())
print(source.getvalue(), source.tell())
```

```text
b'abcde'
b'abcde' 5
```

`seek(0)` で読む位置を先頭へ戻せます。`getvalue()` はBytesIOに入っている内容全体を取得し、現在位置は変更しません。同じ入力を読み直す時に、どの操作が位置へ影響するかを区別します。

参考：[Python公式BytesIO](https://docs.python.org/3.12/library/io.html#io.BytesIO)、[IOBase.seek](https://docs.python.org/3.12/library/io.html#io.IOBase.seek)、[IOBase.tell](https://docs.python.org/3.12/library/io.html#io.IOBase.tell)。2026-11-14確認。

## 任意の確認と未確認

採点対象外・提出不要の確認として、最初の `read(2)` を `read(1)` に変え、返る内容と位置を比べられます。実行した場合は本人が `submit/notes.md` に入力・操作・結果を残します。

| 対象 | 状態 |
|---|---|
| AIの実測 | 部分読み・末尾・先頭への移動・全体取得をPython 3.12.0で確認 |
| 本人の理解 | この解説を読んだ後の説明・操作は未確認 |
| 対象の範囲 | 今回はBytesIO。全てのファイルやネットワーク入力が同じ移動操作に対応するとは限らない |

## 用語

| 用語 | 平易な説明 |
|---|---|
| ストリーム | 順にデータを読み書きできるもの |
| BytesIO | メモリ上のbytesをファイルのように読み書きするもの |
| 読み取り位置 | 次の読み取りを始める場所 |
| 末尾 | 現在のデータの最後の位置 |
