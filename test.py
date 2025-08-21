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
.block-container {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #a5d6a7, #81c784, #4caf50);
    color: white;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
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
    {"type": "mcq", "question": "🧬 체세포 분열의 결과, 하나의 모세포(2n)에서 몇 개의 딸세포가 만들어질까?",
     "options": ["1개", "2개", "4개", "8개"], "answer": "2개", "concept": "체세포 분열의 기본 결과"},
    {"type": "mcq", "question": "🌱 감수분열에서 유전적 다양성이 나타나는 이유는?",
     "options": ["DNA 복제", "세포질 분열", "교차와 독립적 분리", "염색체 수 유지"], "answer": "교차와 독립적 분리", "concept": "감수분열의 특징"},
    {"type": "mcq", "question": "🔬 체세포 분열과 감수분열 모두에서 공통적으로 일어나는 현상은?",
     "options": ["DNA 교차", "중기판에 염색체 배열", "염색체 수 감소", "배우자 형성"], "answer": "중기판에 염색체 배열", "concept": "분열 과정의 공통점"},
    {"type": "mcq", "question": "🦠 감수분열에서 상동염색체가 서로 DNA 일부를 교환하는 현상은?",
     "options": ["분리", "교차", "복제", "독립 분리"], "answer": "교차", "concept": "교차의 의미"},
    {"type": "mcq", "question": "💡 체세포 분열의 최종 결과, 모세포와 딸세포의 염색체 수 관계는?",
     "options": ["동일하다", "절반이다", "배로 늘어난다", "불규칙하다"], "answer": "동일하다", "concept": "체세포 분열의 염색체 유지"},
    {"type": "order", "question": "📖 다음은 감수분열 과정에서 일어나는 일이다. 빈칸에 블록을 순서대로 넣으세요.",
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
     ],
     "concept": "감수분열 단계의 순서"}
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
if "wrong_concepts" not in st.session_state:
    st.session_state.wrong_concepts = []
if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []
if "user_order" not in st.session_state:
    st.session_state.user_order = []

# ----------------------
# 앱 UI
# ----------------------
st.title("🧬 생명과학1 - 유전 퀴즈 대모험 🌱")

# 퀴즈 시작 전
if not st.session_state.quiz_list:
    num_q = st.slider("📝 풀 문제 개수를 선택하세요:", 1, 30, 5)
    if st.button("🚀 퀴즈 시작!"):
        st.session_state.quiz_list = random.sample(quiz_data, k=min(num_q, len(quiz_data)))
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.stage = 0
        st.session_state.wrong_concepts = []
        st.session_state.wrong_questions = []
        st.session_state.user_order = []
        st.rerun()

# 퀴즈 진행 중
else:
    total = len(st.session_state.quiz_list)
    q_idx = st.session_state.current_q
    quiz = st.session_state.quiz_list[q_idx]

    st.progress((q_idx) / total)
    st.markdown(f"### 🏆 문제 {q_idx+1} / {total}")
    st.write(quiz["question"])

    # stage = 0 → 문제 풀이 화면
    if st.session_state.stage == 0:
        if quiz["type"] == "mcq":
            user_answer = st.radio("👉 정답을 고르세요:", quiz["options"], key=f"q{q_idx}")
            if st.button("✅ 제출"):
                if user_answer == quiz["answer"]:
                    st.session_state.score += 1
                    st.session_state.feedback = "🎉 정답입니다! 🧬 훌륭해요!"
                else:
                    st.session_state.wrong_concepts.append(quiz["concept"])
                    st.session_state.wrong_questions.append(quiz)
                    st.session_state.feedback = f"❌ 틀렸습니다... 정답은 👉 {quiz['answer']}"
                st.session_state.stage = 1
                st.rerun()

        elif quiz["type"] == "order":
            if not st.session_state.user_order:
                st.session_state.user_order = [""] * len(quiz["options"])

            blocks = quiz["options"].copy()
            for i in range(len(st.session_state.user_order)):
                st.session_state.user_order[i] = st.selectbox(
                    f"⬜ 순서 {i+1}번", [""] + blocks, key=f"{q_idx}_blank_{i}"
                )

            if st.button("✅ 제출"):
                if st.session_state.user_order == quiz["answer"]:
                    st.session_state.score += 1
                    st.session_state.feedback = "🎉 정답입니다! 🌟 잘했어요!"
                else:
                    st.session_state.wrong_concepts.append(quiz["concept"])
                    st.session_state.wrong_questions.append(quiz)
                    st.session_state.feedback = f"❌ 틀렸습니다... 정답은 👉 {' → '.join(quiz['answer'])}"
                st.session_state.stage = 1
                st.rerun()

    # stage = 1 → 정오답 피드백 화면
    elif st.session_state.stage == 1:
        st.subheader("📢 결과")
        st.info(st.session_state.feedback)

        if q_idx + 1 < total:
            if st.button("👉 다음 문제로"):
                st.session_state.current_q += 1
                st.session_state.stage = 0
                st.session_state.user_order = []
                st.rerun()
        else:
            st.success(f"🎉 퀴즈 완료! 점수: {st.session_state.score} / {total}")
            if st.session_state.wrong_concepts:
                st.warning("📚 부족한 개념 복습 필요!")
                for c in set(st.session_state.wrong_concepts):
                    st.write(f"👉 {c}")
            else:
                st.balloons()
                st.success("🌟 완벽합니다! 모든 개념을 잘 이해했군요!")

            # ❌ 틀린 문제 다시 풀기 버튼
            if st.session_state.wrong_questions:
                if st.button("🔄 틀린 문제 다시 풀기"):
                    st.session_state.quiz_list = st.session_state.wrong_questions.copy()
                    st.session_state.current_q = 0
                    st.session_state.score = 0
                    st.session_state.stage = 0
                    st.session_state.user_order = []
                    st.session_state.wrong_concepts = []
                    st.session_state.wrong_questions = []
                    st.rerun()

            if st.button("🏠 처음으로 돌아가기"):
                st.session_state.quiz_list = []
                st.session_state.current_q = 0
                st.session_state.score = 0
                st.session_state.stage = 0
                st.session_state.wrong_concepts = []
                st.session_state.wrong_questions = []
                st.session_state.user_order = []
                st.rerun()
