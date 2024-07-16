import streamlit as st
tab1, tab2= st.tabs(["등록", "결과"])

with tab1:
   st.header("학번을 등록해주세요")
   name = st.text_input("학년, 반, 번호 입력")
   st.write(name)
   st.button("확인")
if st.button("확인"):
    st.session_state.key="available"
with tab2:
   st.header("결과를 확인해보세요")