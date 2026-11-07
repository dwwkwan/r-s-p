import random
import streamlit as st

# 페이지 설정 및 공포스러운 분위기의 CSS 스타일
st.markdown(
    """
    <style>
    /* 전체 앱 배경 - 어두운 숲속/음산한 초록색 */
    .stApp {
        background-color: #0d1a11;
        color: #ffcccc;
    }

    /* 메인 타이틀 공포스럽게 꾸미기 */
    .horror-title {
        text-align: center;
        color: #ff0000;
        font-family: 'Courier New', Courier, monospace;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 0 0 15px #ff0000;
        letter-spacing: 3px;
        margin-top: 20px;
    }

    .horror-subtitle {
        text-align: center;
        color: #88aa88;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* 가위바위보 선택 버튼 스타일 (오싹한 붉은빛 테두리) */
    div.stButton > button {
        background: radial-gradient(circle, #5a0000 0%, #1a0000 100%) !important;
        color: #ffcccc !important;
        border: 2px solid #ff0000 !important;
        border-radius: 10px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        font-family: 'Courier New', Courier, monospace !important;
        height: 60px !important;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4) !important;
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        background: radial-gradient(circle, #ff0000 0%, #3a0000 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 0 25px #ff0000 !important;
        transform: scale(1.05);
    }

    /* 결과 화면 텍스트 스타일 */
    .result-box {
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        margin-top: 30px;
        padding: 20px;
        border: 1px dashed #ff0000;
        background-color: rgba(20, 0, 0, 0.6);
        border-radius: 10px;
    }

    .result-title {
        font-size: 28px;
        font-weight: bold;
        color: #ff3333;
        margin-bottom: 15px;
        text-shadow: 0 0 10px #ff0000;
    }

    .result-detail {
        font-size: 20px;
        color: #dddddd;
        margin-bottom: 10px;
    }

    /* 다시하기 버튼 오른쪽 아래 배치용 컨테이너 */
    .reset-container {
        display: flex;
        justify-content: flex-end;
        margin-top: 40px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "com_choice" not in st.session_state:
    st.session_state.com_choice = None
if "result" not in st.session_state:
    st.session_state.result = None

# 타이틀
st.markdown('<div class="horror-title">죽음의 가위바위보</div>', unsafe_allow_html=True)
st.markdown('<div class="horror-subtitle">살고 싶다면, 선택하라...</div>', unsafe_allow_html=True)

choices = ["가위", "바위", "보"]

# 게임을 아직 진행하지 않은 경우 (선택 화면)
if st.session_state.user_choice is None:
    st.markdown("<p style='text-align: center; font-family: Courier New;'>운명을 결정할 무기를 고르시오</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✂️ 가위", use_container_width=True):
            st.session_state.user_choice = "가위"
            st.session_state.com_choice = random.choice(choices)
            st.rerun()
            
    with col2:
        if st.button("🪨 바위", use_container_width=True):
            st.session_state.user_choice = "바위"
            st.session_state.com_choice = random.choice(choices)
            st.rerun()
            
    with col3:
        if st.button("📄 보", use_container_width=True):
            st.session_state.user_choice = "보"
            st.session_state.com_choice = random.choice(choices)
            st.rerun()

# 게임을 진행한 경우 (결과 화면)
else:
    user = st.session_state.user_choice
    com = st.session_state.com_choice

    # 승패 판정
    if user == com:
        game_result = "무승부... 목숨을 부지했구나."
    elif (
        (user == "가위" and com == "보") or
        (user == "바위" and com == "가위") or
        (user == "보" and com == "바위")
    ):
        game_result = "승리! 간신히 살아남았다..."
    else:
        game_result = "패배... 어둠이 너를 집어삼킨다."

    # 결과 출력
    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-title">{game_result}</div>
            <div class="result-detail">당신의 선택: <b>{user}</b></div>
            <div class="result-detail">상대의 선택: <b>{com}</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 패배했을 때 공포스러운 콩그리 점프스케어 밈 영상 출력 (선택사항)
    if "패배" in game_result:
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-top: 20px;">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/jpjl0PGjMF8?start=96&end=105&autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 오른쪽 아래에 배치되는 '다시하기' 버튼
    col_empty, col_btn = st.columns([3, 1])
    with col_btn:
        if st.button("다시하기", use_container_width=True):
            st.session_state.user_choice = None
            st.session_state.com_choice = None
            st.session_state.result = None
            st.rerun()
