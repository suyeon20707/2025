import streamlit as st
import random

# ----------------------
# 🌌 배경 및 스타일 업그레이드
# ----------------------
custom_css = """
<style>
/* 배경에 은은한 움직이는 그라디언트 효과 */
.stApp {
    background: linear-gradient(-45deg, #a8edea, #fed6e3, #d4fc79, #96e6a1);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* 메인 컨텐츠 카드 */
.block-container {
    background: rgba(255, 255, 255, 0.9);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    backdrop-filter: blur(8px);
    border: 2px solid rgba(255,255,255,0.3);
}

/* 버튼 화려하게 */
.stButton button {
    font-size: 18px;
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
    transition: all 0.3s ease-in-out;
}
.stButton button:hover {
    transform: scale(1.07);
    box-shadow: 0 0 15px rgba(0,255,100,0.6);
}

/* 사이드바 스타일 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #4caf50, #2e7d32);
    color: white;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

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
    st.session_state.stage = 0
if "last_answer" not in st.session_state:
    st.session_state.last_answer = None

# ----------------------
# 제목
# ----------------------
st.title("🧬 생명과학1 - 체세포 분열 & 감수분열 퀴즈")

# ----------------------
# 문제 수 선택 & 퀴즈 시작
# ----------------------
if not st.session_state.quiz_list:
    num_q = st.slider("풀 문제 개수를 선택하세요:", 1, 30, 5)
    if st.button("퀴즈 시작! 🚀"):
        st.session_state.quiz_list = random.sample(quiz_data * 10, num_q)  # 데이터 확장
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.stage = 0
        st.rerun()

# ----------------------
# 퀴즈 진행
# ----------------------
else:
    current = st.session_state.current_q
    quiz = st.session_state.quiz_list[current]

    # 사이드바 진행률
    progress = (current) / len(st.session_state.quiz_list)
    st.sidebar.progress(progress)
    st.sidebar.write(f"📊 진행률: {int(progress*100)}%")
    st.sidebar.write(f"✅ 점수: {st.session_state.score}")

    # 문제 출제
    if st.session_state.stage == 0:
        st.subheader(f"Q{current+1}. {quiz['question']}")

        if quiz["type"] == "mcq":
            user_answer = st.radio("정답을 선택하세요:", quiz["options"], key=f"q{current}")
        else:  # 순서 배열 문제
            user_answer = st.multiselect("순서를 올바르게 배열하세요:", quiz["options"], key=f"q{current}")

        if st.button("정답 제출"):
            st.session_state.last_answer = user_answer
            if quiz["type"] == "mcq":
                if user_answer == quiz["answer"]:
                    st.session_state.score += 1
            else:
                if user_answer == quiz["answer"]:
                    st.session_state.score += 1
            st.session_state.stage = 1
            st.rerun()

    # 피드백 화면
    elif st.session_state.stage == 1:
        st.subheader(f"Q{current+1}. {quiz['question']}")

        if quiz["type"] == "mcq":
            if st.session_state.last_answer == quiz["answer"]:
                st.success("✅ 정답입니다! 🎉")
            else:
                st.error(f"❌ 틀렸습니다. 정답은 👉 {quiz['answer']}")
        else:
            if st.session_state.last_answer == quiz["answer"]:
                st.success("✅ 올바른 순서입니다! 🎉")
            else:
                st.error(f"❌ 틀렸습니다.\n\n정답은 👉 {' → '.join(quiz['answer'])}")

        if current < len(st.session_state.quiz_list) - 1:
            if st.button("➡️ 다음 문제로 이동"):
                st.session_state.current_q += 1
                st.session_state.stage = 0
                st.rerun()
        else:
            st.success(f"🎉 모든 문제를 풀었습니다! 최종 점수: {st.session_state.score}/{len(st.session_state.quiz_list)}")
            if st.button("🔄 다시 시작하기"):
                st.session_state.quiz_list = []
                st.rerun()
