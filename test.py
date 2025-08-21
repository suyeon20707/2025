import streamlit as st
import random

# ----------------------
# 🌌 배경 꾸미기
# ----------------------
page_bg = """
<style>
.stApp {
    background-image: url("https://cdn.pixabay.com/photo/2016/11/19/14/00/dna-1838696_1280.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #1b1b1b;
}

/* 메인 컨테이너 */
.block-container {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

/* 사이드바 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #a5d6a7, #81c784, #4caf50);
    color: white;
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* 버튼 스타일 */
div.stButton > button {
    background: linear-gradient(90deg, #66bb6a, #43a047);
    color: white;
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #43a047, #2e7d32);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------------
# 퀴즈 데이터
# ----------------------
quiz_data = [
    {"type": "mcq", "question": "체세포 분열의 결과, 하나의 모세포(2n)에서 몇 개의 딸세포가 만들어질까?",
     "options": ["1개", "2개", "4개", "8개"], "answer": "2개"},
    {"type": "mcq", "question": "감수분열에서 유전적 다양성이 나타나는 이유는?",
     "options": ["DNA 복제", "세포질 분열", "교차와 독립적 분리", "염색체 수 유지"], "answer": "교차와 독립적 분리"},
    {"type": "mcq", "question": "체세포 분열과 감수분열 모두에서 공통적으로 일어나는 현상은?",
     "options": ["DNA 교차", "중기판에 염색체 배열", "염색체 수 감소", "배우자 형성"], "answer": "중기판에 염색체 배열"},
    {"type": "mcq", "question": "감수분열에서 상동염색체가 서로 DNA 일부를 교환하는 현상은?",
     "options": ["분리", "교차", "복제", "독립 분리"], "answer": "교차"},
    {"type": "mcq", "question": "체세포 분열의 최종 결과, 모세포와 딸세포의 염색체 수 관계는?",
     "options": ["동일하다", "절반이다", "배로 늘어난다", "불규칙하다"], "answer": "동일하다"},
    {"type": "order", "question": "다음은 감수분열 과정에서 일어나는 일이다. 올바른 순서대로 배열하시오.",
     "options": [
         "상동염색체가 짝을 이루어 배열됨",
         "염색분체가 분리되어 양극으로 이동",
         "DNA 복제 완료",
         "세포질 분열로 4개의 세포 형성"
     ],
     "answer": [
         "DNA 복제 완료",
         "상동염색체가 짝을 이루어 배열됨",
         "염색분체가 분리되어 양극으로 이동",
         "세포질 분열로 4개의 세포 형성"
     ]}
]

# ----------------------
# 세션 상태 초기화
# ----------------------
if "quiz_list" not in st.session_state:
    st.session_state.quiz_list = []
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "stage" not in st.session_state:
    st.session_state.stage = 0  # 0: 문제, 1: 정오답 피드백

# ----------------------
# 앱 UI
# ----------------------
st.title("🧬 생명과학1 - 유전 학습 퀴즈 앱")

# 퀴즈 시작 전
if not st.session_state.quiz_list:
    num_q = st.slider("풀 문제 개수를 선택하세요:", 1, 30, 5)
    if st.button("퀴즈 시작! 🚀"):
        st.session_state.quiz_list = random.choices(quiz_data, k=num_q)
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.stage = 0
        st.rerun()

# 퀴즈 진행 중
else:
    total = len(st.session_state.quiz_list)
    q_idx = st.session_state.current_q
    quiz = st.session_state.quiz_list[q_idx]

    st.progress((q_idx) / total)
    st.markdown(f"### 문제 {q_idx+1} / {total}")
    st.write(quiz["question"])

    # ----------------------
    # stage = 0 → 문제 풀이 화면
    # ----------------------
    if st.session_state.stage == 0:
        if quiz["type"] == "mcq":
            user_answer = st.radio("정답을 고르세요:", quiz["options"], key=f"q{q_idx}")
            if st.button("제출"):
                if user_answer == quiz["answer"]:
                    st.session_state.score += 1
                    st.session_state.stage = 1
                    st.session_state.feedback = "✅ 정답입니다! 🎉"
                else:
                    st.session_state.stage = 1
                    st.session_state.feedback = f"❌ 틀렸습니다. 정답은 👉 {quiz['answer']}"
                st.rerun()

        elif quiz["type"] == "order":
            user_order = st.multiselect("순서대로 나열하세요:", quiz["options"], key=f"q{q_idx}")
            if st.button("제출"):
                if user_order == quiz["answer"]:
                    st.session_state.score += 1
                    st.session_state.stage = 1
                    st.session_state.feedback = "✅ 정답입니다! 🎉"
                else:
                    st.session_state.stage = 1
                    st.session_state.feedback = f"❌ 틀렸습니다. 정답은 👉 {' → '.join(quiz['answer'])}"
                st.rerun()

    # ----------------------
    # stage = 1 → 정오답 피드백 화면
    # ----------------------
    elif st.session_state.stage == 1:
        st.subheader("결과")
        st.info(st.session_state.feedback)

        if q_idx + 1 < total:
            if st.button("👉 다음 문제로"):
                st.session_state.current_q += 1
                st.session_state.stage = 0
                st.rerun()
        else:
            st.success(f"🎉 퀴즈 완료! 점수: {st.session_state.score} / {total}")
            if st.button("다시 시작하기"):
                st.session_state.quiz_list = []
                st.session_state.current_q = 0
                st.session_state.score = 0
                st.session_state.stage = 0
                st.rerun()
