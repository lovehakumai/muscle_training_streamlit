# AI担当：メモファイルと状態・例外を調べる教材。本番のCSVプレビューには流用しない。
import streamlit as st

INITIAL_COUNT = 0

st.title("観測メモとカウンター")
uploaded = st.file_uploader("メモファイル", type=["txt"], key="note_file")
if uploaded is None:
    st.info("教材のメモファイルを選んでください")
else:
    payload = uploaded.getvalue()
    st.write("ファイル名", uploaded.name)
    st.write("内容の型", type(payload).__name__)
    st.metric("バイト数", len(payload))

if "stored_count" not in st.session_state:
    st.session_state["stored_count"] = INITIAL_COUNT

normal_count = INITIAL_COUNT
increment_text = st.text_input("増やす数", value="2", key="increment")
if st.button("Apply", key="apply"):
    try:
        increment = int(increment_text)
        normal_count += increment
        st.session_state["stored_count"] += increment
    except ValueError:
        st.error("増やす数を整数で入力してください")

if st.button("Reset", key="reset"):
    st.session_state["stored_count"] = INITIAL_COUNT

st.metric("通常の変数", normal_count)
st.metric("保存した値", st.session_state["stored_count"])
st.caption("処理後の表示")
