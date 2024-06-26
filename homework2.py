import streamlit as st
from openai import OpenAI
st.title("30422 배재현🤷‍♂️")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3 = st.tabs(['KING','4343434', '딥러닝'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('배재현이란?')
    st.markdown("일단 이 친구는 2학년떄 마치 초신성처럼 나온 위대한 친구입니다!! "
                " **천재**과 **영재**라고 부르죠 다들 ㅠㅎㅎ ")
    st.image("data:image/jpeg;base64,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")
    st.markdown("2학년때부터 제가 들어온 이후부터 다들 저의 존재를 보고 덜덜 떨더라고요....")

    st.subheader('배재현의 상세한 설명')
    st.markdown(':red[**① 배씨 가문**]: 배씨 가문에서 유일무이하게 나온 천재, 현재 대한민국이 눈여겨 보는 사나이 !!!!!!!!!'
                '배씨가문의 조상인 배현경 장군님을 보겠습니다...')
    st.image('https://i.namu.wiki/i/iQdFrAzFu4gRqvXnn2G8cceMXxmahGDx5-LRACwpnUj8h5U7AIHqKg3Lo61Drt_77qt8Acr9vdd04MLvwBktTA.webp')
    st.markdown(':red[**② 나이,키 등등**]: 2006년생으로 올해의 06년생 중 한명에 뽑힌 분이다. '
                '키는 **177cm** 몸무게는 **60kg**이고 현재 벌크업 중이므로 곧 목표인 74kg을 찍을 것이다. \n미래의 배재현님의 모습을 한번 보도록 하겠습니다 ')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnuddEr8OrdJ4GgUJfyowCTkDtx7cm9tw7K_JluLbvpA&s")
    st.markdown(':red[**③ 딥 블루(Deep Blue)**]: 1977년 인공지능 **딥블루**가 세계 체스 챔피언과의 대결에서 승리를 거두었다.'
                '딥블루는 **가능한 모든 경우를 탐색하는 효율적인 알고리즘**을 이용해 문제를 해결할 뿐 스스로 학습하는 수준에는 이르지 못했다'
                '다만 탐색 알고리즘은 알파고와 같은 인공지능을 구현하는 핵심 개념이 되었다.')
    st.image('https://img2.yna.co.kr/etc/inner/KR/2016/03/11/AKR20160311132000009_02_i_P4.jpg')
    st.caption('1997년 5월 11일 딥 블루와의 대국을 치르면서 고뇌하고 있는 게리 카스파로프,'
               '출처https://img2.yna.co.kr/etc/inner/KR/2016/03/11/AKR20160311132000009_02_i_P4.jpg')

    st.markdown(':red[**④ 알파고(Alphago)**]: 2016년 세계 최고 바둑 기사인 **이세돌과 알파고의 대결**은 인공지능 기술에 대해 대중에게 가증 크게 알린 사건이었다.'
                '알파고는 **인공신경망을 이용해 바둑 경기 16만건을 학습**하면서 스스로 규칙을 찾아냈기 때문에 **인간이 생각하지 못한 전략을 구사**할 수 있었다.')
    st.image('http://image.dongascience.com/Photo/2016/03/14575928244225.jpg')
    st.caption('2016년 3월 10일 알파고와 두 번째 대국을 하고 있는 이세돌 구단,'
           '출처 http://image.dongascience.com/Photo/2016/03/14575928244225.jpg')

    st.markdown(':red[**⑤ ChatGPT(Chat Generative Pre-trained Trasformer)**]: 2022년 11월 30일에 출시되어 현재까지 큰 반향을 일으키고 있는 **생성형 인공지능**이다.'
                '**Large Language Model**로 자연어 처리에 획기적인 발전을 이루었다는 평을 받으며, 출시 5일만에 사용자 1억명을 돌파했다.'
                '다른 LLM모델로 구글의 Bard, 메타의 LLaMA, 네이버 하이퍼클로바X 등이 있다. 챗GPT뿐만 아니라 DALL.E, Midjourney 등의 이미지 생성AI도 각광받고 있다.')
    st.image('https://cdn.eroun.net/news/photo/202304/31633_58340_5223.png')
    st.caption('출처: OpenAI 홈페이지')


with tab2:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('1.인공지능&머신러닝&딥러닝')
    #st.image("images/ai_structure.jpg")
    st.caption("▲인공지능, 머신러닝, 딥러닝의 관계도")

    st.subheader("2. 머신러닝(Machine Learning)")
    st.markdown('머신러닝은 인공지능을 구현하는 대표적인 방법 중의 하나로, **데이터에서 패턴을 찾아내 문제애 대한 답을 예측하는 알고리즘**이다. '
                '머신러닝의 활용 분야로 금융, 이미지프로세싱, 금융분석 및 탐지 분야, 음성인식, 로봇제어 분야 등이 있다.')
    st.write("")
    st.markdown("머신러닝의 학습 방법에는 지도 학습, 비지도 학습, 강화 학습의 3가지로 나뉠 수 있다.")
    st.write("")
    st.markdown("""
    - 지도 학습
    - 비지도 학습
    - 강화 학습
    """)
    st.markdown(":red[**① 지도 학습(Supervised Learning**)] : 지도 학습은 **데이터와 정답**을 함께 제시하여 학습하는 방법이다. "
                "예를 들어, 고양이와 개를 학습시킨다고 했을 때 고양이 데이터와 개 사진 데이터를 입력으로 넣어주면서 정답(고양이, 개) 레이블을 함께 주면서 학습시킨다."
                "지도 학습에는 크게 분류와 회귀 모델로 나뉠 수 있다.")
    st.video("https://youtu.be/hnc1DGz9UCU")
    st.markdown(":red[**② 비지도 학습(Unsupervised Learning)**] : 비지도 학습은 정답이 없는 **데이터만** 주고 학습하게 방법이다. 정답이 없기 때문에 입력 데이터의 패턴이나 특성을 통해 학습하게 된다."
                "마찬가지로 고양이과 개를 학습시킬 때 고양이과 개 사진 데이터만 입력으로 주고 주어진 데이터를 바탕으로 고양이와 개의 특성을 찾아내는 방식이다."
                " 비지도 학습의 대표적인 모델로 군집화가 있다.")
    st.video("https://youtu.be/xwe1cbZaFEg")
    st.markdown(":red[**③ 강화 학습(Reinforcement Learning)**] : 강화 학습은 입력 데이터를 학습하여 **경험과 보상**을 통해 목표값을 찾도록 학습하는 방법이다. 즉 입-출려간의 상관관계를 찾는 것이 아니라, 시행착오에 대한 보상 체계를 바탕으로"
                "지속적인 경험에 통해 최선책을 찾도록 하는 방법이다. 주로 자율주행자동차나 게임, 주식 등에 활용된다.")
    st.video("https://youtu.be/BPCAP7DHLYw")

with tab3:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('딥러닝(Deep Learning)')
    st.markdown("딥 러닝은 인간의 **신경망을 모방**하여 학습하게 하는 기계학습 방법이다. 인간의 뇌는 약 860억 개의 뉴런이 연결되어 신경망을 구성한다."
                " 이러한 신경망을 통해 다양한 감정을 느끼고 생각하게 되는 것이다. 이런 인간의 뇌 신경망을 모방한 것이 **인공 신경망**이다. "
                " 인공 신경망은 **퍼셉트론**(인간의 뉴런에 해당)을 기본 단위로 사용하며, 이 퍼셉트론이 여러 개 연결되어 **심층 인공 신경망(DNN)**을 구성한다."
                )
    st.video("https://youtu.be/kvAa-76IWHc")
st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    #if not openai_api_key:
    #    st.info("Please add your OpenAI API key to continue.")
    #    st.stop()

    client = OpenAI(api_key='sk-proj-OUdVkViMxKBaQnp2GnIWT3BlbkFJzY9CHGiBlP9w6pniUQde')
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)


