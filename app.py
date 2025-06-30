import streamlit as st
import random as rd

st.title("じゃんけんゲーム✊✌️✋")
st.subheader("じゃんけんゲームをしましょう")
st.subheader("あなたの出す手はどれですか?")
if "winpoint" not in st.session_state:
    st.session_state.winpoint=0
if "losepoint" not in st.session_state:
    st.session_state.losepoint=0
b0=st.button("グー",key="g")
b1=st.button("チョキ",key="c")
b2=st.button("パー",key="p")
enemy=rd.randint(0,2)
if b0:
    st.write("あなたはグーを出しました✊")
    if 0==enemy:
        st.write("相手はパーです✋。あなたの負けです")
        st.session_state.losepoint+=1
    elif 1==enemy:
        st.write("相手はチョキです✌️。あなたの勝ちです")
        st.session_state.winpoint+=1
    elif 2==enemy:
        st.write("相手はグーです✊。あいこです。")
elif b1:
    st.write("あなたはチョキを出しました✌️")
    if 0==enemy:
        st.write("相手はパーです✋。あなたの勝ちです")
        st.session_state.winpoint+=1
    elif 1==enemy:
        st.write("相手はグーです✊。あなたの負けです")
        st.session_state.losepoint+=1
    elif 2==enemy:
        st.write("相手はチョキです✌️。あいこです。")
elif b2:
    st.write("あなたはパーを出しました✋")
    if 0==enemy:
        st.write("相手はパーです✋。あいこです。")
    elif 1==enemy:
        st.write("相手はグーです✊。あなたの勝ちです")
        st.session_state.winpoint+=1
    elif 2==enemy:
        st.write("相手はチョキです✌️。あなたの負けです")
        st.session_state.losepoint+=1
else:
    st.write("あなたの出す手はどれですか?")

st.markdown("あなたの勝利ポイント"+str(st.session_state.winpoint))
st.markdown("あなたの敗北ポイント"+str(st.session_state.losepoint))



