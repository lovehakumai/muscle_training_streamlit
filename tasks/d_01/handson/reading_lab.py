# AI担当：観測記録をCLIで調べる教材。本番のアップロード・表示処理には流用しない。
import csv
from io import BytesIO, StringIO

import pandas as pd

FIRST_SITE = "015"
READ_SIZE = 3

sample = (
    "station,note,temperature\n"
    f'{FIRST_SITE},"clear, calm",\n'
    "016,NA,0\n"
    "017,,8\n"
)
raw = sample.encode("utf-8")
print("[1] 文字とバイト")
print("text type:", type(sample).__name__)
print("raw type:", type(raw).__name__)
print("text length:", len(sample))
print("raw length:", len(raw))

source = BytesIO(raw)
print("\n[2] 読み取り位置")
print("before:", source.tell())
print("first:", repr(source.read(READ_SIZE)), "position:", source.tell())
print("rest:", repr(source.read()), "position:", source.tell())
print("again:", repr(source.read()), "position:", source.tell())
source.seek(0)
restored = source.read().decode("utf-8")
print("restored equals sample:", restored == sample)

rows = list(csv.reader(StringIO(restored, newline="")))
print("\n[3] CSVの構造")
print("header:", rows[0])
print("record count:", len(rows) - 1)
print("first record:", rows[1])
print("first record fields:", len(rows[1]))

inferred = pd.read_csv(StringIO(restored))
preserved = pd.read_csv(StringIO(restored), dtype=str, keep_default_na=False)
print("\n[4] 表の値と型")
print("inferred station:", repr(inferred.loc[0, "station"]))
print("inferred station type:", type(inferred.loc[0, "station"]).__name__)
print("preserved station:", repr(preserved.loc[0, "station"]))
print("preserved station type:", type(preserved.loc[0, "station"]).__name__)
print("inferred note missing:", inferred["note"].isna().tolist())
print("preserved note:", preserved["note"].tolist())
print("inferred temperature missing:", inferred["temperature"].isna().tolist())
print("preserved temperature:", preserved["temperature"].tolist())
