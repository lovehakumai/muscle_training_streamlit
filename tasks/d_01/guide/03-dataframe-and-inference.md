# DataFrameのセルと型推論

要点：`read_csv` はCSVを表へ読み込みます。`frame.loc[行ラベル, 列名]` で行と列を一つずつ指定すると、そのセルの値を取り出します。読み取り時には値の型が推測されることがあります。

K05の回答から、表全体・1行・1セルと、型推論を整理する必要があると分かりました。ここでは物品のバッチ番号を例にします。

## 目次

- [具体例と実測](#具体例と実測)

- [表・行・セルの区別](#表行セルの区別)

- [型を推測する読み取り](#型を推測する読み取り)

- [任意の確認と未確認](#任意の確認と未確認)

- [用語](#用語)

## 具体例と実測

```python
# AI担当：表の単位と読み取り時の型を説明する別題材の例。
from io import StringIO
import pandas as pd

sample = "batch,quantity\n009,5\n010,6\n"
frame = pd.read_csv(StringIO(sample))
print(frame.loc[0, "batch"])
print(type(frame.loc[0, "batch"]).__name__)
print(frame.loc[0].to_dict())
```

2026-11-14、このプロジェクトのルートで `.venv/bin/python`（Python 3.12.0、pandas 3.1.1）に例を渡し、AIが実行した出力です。

```text
9
int64
{'batch': 9, 'quantity': 5}
```

## 表・行・セルの区別

| 式 | この例で取り出すもの | 単位 |
|---|---|---|
| `frame` | batchとquantityの2列を持つ表 | 表全体 |
| `frame.loc[0]` | 行ラベル0の内容 | 1行 |
| `frame.loc[0, "batch"]` | 行ラベル0・batch列の値 | 1セル |

`loc` はラベルで選びます。この例では読み取り後の行ラベルが0から付くため、ラベル0が先頭行に対応しています。1セルを選んだ結果は、同じ行の全フィールドのリストにはなりません。

```mermaid
flowchart LR
    A["DataFrameという表"] -->|"行ラベル0を選ぶ"| B["1行"]
    B -->|"列batchを選ぶ"| C["一つの値"]
```

参考：[pandas公式DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)。2026-11-14確認。

## 型を推測する読み取り

例ではCSV内の `009` が数値として解釈されました。数値9という値は、元にゼロがいくつ付いていたかという書き方を持ちません。

次はbatch列を文字列として読む例です。上の `sample` を定義した後に実行します。

```python
# AI担当：列の型を明示した別題材の読み取り例。
kept = pd.read_csv(StringIO(sample), dtype={"batch": str})
print(kept.loc[0, "batch"])
print(type(kept.loc[0, "batch"]).__name__)
```

同じ環境でAIが実行した出力です。

```text
009
str
```

値の意味に合った型を選ぶ必要があります。今回の例は、列の型をどう扱うかで結果が変わることを確かめる説明です。本番で全ての列にどう適用するかの設計判断は、まだ本人の代わりに決めていません。

CSVを解析するのはpandasだけではありません。標準の `csv.reader` も引用符や区切りを解析し、通常はフィールドを文字列として返します。`read_csv` はDataFrameを作り、今回のような型の推測も行います。

参考：[pandas公式read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)。2026-11-14確認。

## 任意の確認と未確認

採点対象外・提出不要の確認として、バッチ番号を `015` に変え、指定なしと型指定ありのセルの値を比べられます。実行した場合は本人が `submit/notes.md` に入力・操作・結果を残します。

| 対象 | 状態 |
|---|---|
| AIの実測 | 別題材の型指定なし・ありと1行・1セルの取得を確認 |
| 本人の理解 | この解説を読んだ後の説明・操作は未確認 |
| 欠けた値の解釈 | この例だけでpandasの欠損値処理全般を説明したことにはしない。教材で別途扱う |

## 用語

| 用語 | 平易な説明 |
|---|---|
| DataFrame | 行と列を持つpandasの表 |
| セル | 行と列が交わる一つの値の場所 |
| ラベル | 行や列を選ぶために付いた名前や番号 |
| 型推論 | 値を見て、どの型で扱うかライブラリが推測すること |
