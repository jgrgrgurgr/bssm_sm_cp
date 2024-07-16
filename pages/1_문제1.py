import streamlit as st
if 'available' in st.session_state :
    st.write(st.session_state.key)
@st.experimental_dialog("주관식")
def vote(item):
    st.write(f"왜 해당 차종이 더 길다고 생각하시나요?")
    reason = st.text_input("왜냐하면...")
    if st.button("제출하기"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()
if "vote" not in st.session_state:
    st.write("주관식) 어느 차의 전장이 더 길까요?")
    if st.button("EF쏘나타"):
        vote("EF쏘나타")
    if st.button("CN7아반떼"):
        vote("CN7아반떼")
else:
    f"당신은 {st.session_state.vote['item']} 에 투표했습니다. 왜냐하면 {st.session_state.vote['reason']}"