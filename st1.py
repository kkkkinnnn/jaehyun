import streamlit as st
import pandas as pd


st.title("안녕")
st.header("헤더")
st.subheader("✨서브헤더💖")
st.write("안녕하세요~~ 스트림릿에 오신 것을 환영합니다.🤣")

st.markdown("""
            **안녕하세요**
            \n반갑습니다
            \n선생님 졸업하고
            찾아올게요
            <font color = "red"><b>이지원이랑 같이올게요""", unsafe_allow_html = True)
if st.button("클릭 버튼") :
    st.write("데이터 로딩중...")

if st.button("도움이 필요하신가요?") :
    st.write("저리가 안도와줘 ㅋㅋ")

rd = st.radio("다음 중 화원고의 밝은 미래를 고르시오.", ("A 배재현", "B 김동하", "C 이지원"))

if rd == "A 배재현":
    st.write("성공😜")
if rd == "B 김동하":
    st.write("당신은 실패했습니다. 사형....🤢")   
if rd == "C 이지원":
    st.write("당신은 실패했습니다. 사형....🤢")    

tx = st.text_input("입력하세요.")
st.write(tx)

df = pd.DataFrame({
    '학번' : [1,2,3,4],
    '이름' : ['kim', 'hong', 'bae', 'lee']
    })
st.write(df)
st.image("https://i.namu.wiki/i/csS3_ePfz-m2w7jIWJGyXki8TqlKqY-MzxHbT_Pu-imrUDYG-hl3ljigViHA-idtRfxhX-H1W0DFFtC8tf9twQ.webp")
  