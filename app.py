import streamlit as st
import random

def predict_next(rounds):
    count_banker = 0
    count_player = 0
    last = None
    
    for r in reversed(rounds):
        if r == last:
            if r == '莊':
                count_banker += 1
            elif r == '閒':
                count_player += 1
        else:
            break
        last = r
    
    if count_banker >= 2:
        return '莊'
    elif count_player >= 2:
        return '閒'
    else:
        return random.choice(['莊', '閒'])

st.title("簡易百家樂預測工具")

history = st.text_input("輸入歷史路單 (莊/閒)", "")

if history:
    prediction = predict_next(history)
    st.write(f"下一局預測: {prediction}")

    actual = st.selectbox("請選擇實際結果", ["", "莊", "閒"])

    if actual:
        history += actual
        st.success(f"更新路單: {history}")
