import streamlit as st
import random

# ----------------------
# 🌌 배경 설정
# ----------------------
page_bg = """
<style>
.stApp {
    background-image: url("https://cdn.pixabay.com/photo/2016/11/19/14/00/dna-1838696_1280.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.block-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #a5d6a7, #81c784, #66bb6a);
    color: white;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------------
# 퀴즈 데이터
# ----------------------
quiz_data = [
    {"question": "체세포 분열의 결과, 하나의 모세포(2n)에서 몇 개의 딸세포가 만들어질까?",
     "options": ["1개", "2개", "4개", "8개"], "answer": "2개"},
    {"question": "감수분열에서 유전적 다양성이 나타나는 이유는?",
     "options": ["DNA 복제", "세포질 분열", "교차와 독립적 분리", "염색체 수 유지"], "answer": "교차와 독립적 분리"},
    {"question": "체세포 분열과 감수분열 모두에서 공통적으로 일어나는 현상은?",
     "options": ["DNA 교차", "중기판에 염색체 배열", "염색체 수 감소", "배우자 형성"], "answer": "중기판에 염색체 배열"},
    {"question": "감수분열에서 상동염색체가 서로 DNA 일부를 교환하는 현상은?",
     "options": ["분리", "교차", "복제", "독립 분리"], "answer": "교차"},
    {"question": "체세포 분열의 최종 결과, 모세포와 딸세포의 염색체 수 관계는?",
     "options": ["동일하다", "절반이다", "배로 늘어난다", "불규칙하다"], "answer": "동일하다"}
]

# ----------------------
# 세션 상태 초기화
# ----------------------
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.questions = []
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.stage = 0   # 0: 문제 화면, 1: 피드백 화면
    st.session_state.last_answer = None

st.set_page_config(page_title="생명과학1 - 유전 퀴즈 앱", layout="wide")
st.title("📝 생명과학1 - 유전 퀴즈 앱")

# ----------------------
# 시작 화면 (문제 수 선택)
# ----------------------
if not st.session_state.started:
    st.subheader("🎯 문제 수를 선택하세요")
    num_q = st.slider("문제 개수", 1, len(quiz_data), 3)

    if st.button("퀴즈 시작"):
        st.session_state.questions = random.sample(quiz_data, k=num_q)
        st.session_state.started = True
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.stage = 0
        st.rerun()

# ----------------------
# 퀴즈 진행 화면
# ----------------------
else:
    if st.session_state.current < len(st.session_state.questions):
        quiz = st.session_state.questions[st.session_state.current]

        # 문제 화면
        if st.session_state.stage == 0:
            st.subheader(f"Q{st.session_state.current+1}. {quiz['question']}")
            user_answer = st.radio("정답을 선택하세요:", quiz["options"], key=f"q{st.session_state.current}")
            if st.button("정답 제출"):
                st.session_state.last_answer = user_answer
                if user_answer == quiz["answer"]:
                    st.session_state.score += 1
                st.session_state.stage = 1
                st.rerun()

        # 피드백 화면
        elif st.session_state.stage == 1:
            st.subheader(f"Q{st.session_state.current+1}. {quiz['question']}")
            if st.session_state.last_answer == quiz["answer"]:
                st.success("✅ 정답입니다! 🎉")
            else:
                st.error(f"❌ 틀렸습니다. 정답은 👉 {quiz['answer']}")

            if st.session_state.current < len(st.session_state.questions) - 1:
                if st.button("➡️ 다음 문제로 이동"):
                    st.session_state.current += 1
                    st.session_state.stage = 0
                    st.rerun()
            else:
                st.success(f"🎉 모든 문제를 풀었습니다! 최종 점수: {st.session_state.score} / {len(st.session_state.questions)}")
                if st.button("🔄 다시 시작하기"):
                    for k in list(st.session_state.keys()):
                        del st.session_state[k]
                    st.rerun()
    else:
        st.success(f"🎉 모든 문제를 풀었습니다! 최종 점수: {st.session_state.score} / {len(st.session_state.questions)}")
