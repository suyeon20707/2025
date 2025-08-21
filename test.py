import streamlit as st
import random

# ----------------------
# 🌌 배경 설정 (DNA 이미지 + 투명 박스 + 초록 사이드바)
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
    background-color: rgba(255, 255, 255, 0.88);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.25);
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
# 퀴즈 데이터 (30문제)
# ----------------------
quiz_data = [
    # ---- 기본 객관식 (20문제) ----
    {"question": "체세포 분열의 결과, 하나의 모세포(2n)에서 몇 개의 딸세포가 만들어질까?",
     "options": ["1개", "2개", "4개", "8개"], "answer": "2개"},
    {"question": "감수분열에서 유전적 다양성이 나타나는 이유는?",
     "options": ["DNA 복제", "세포질 분열", "교차와 독립적 분리", "염색체 수 유지"], "answer": "교차와 독립적 분리"},
    {"question": "체세포 분열과 감수분열 모두에서 공통적으로 일어나는 현상은?",
     "options": ["DNA 교차", "중기판에 염색체 배열", "염색체 수 감소", "배우자 형성"], "answer": "중기판에 염색체 배열"},
    {"question": "감수분열에서 상동염색체가 서로 DNA 일부를 교환하는 현상은?",
     "options": ["분리", "교차", "복제", "독립 분리"], "answer": "교차"},
    {"question": "체세포 분열의 최종 결과, 모세포와 딸세포의 염색체 수 관계는?",
     "options": ["동일하다", "절반이다", "배로 늘어난다", "불규칙하다"], "answer": "동일하다"},
    {"question": "감수분열은 몇 번의 연속적인 분열로 이루어져 있는가?",
     "options": ["1번", "2번", "3번", "4번"], "answer": "2번"},
    {"question": "DNA 복제는 세포 주기의 어느 시기에 일어나는가?",
     "options": ["G1기", "S기", "G2기", "M기"], "answer": "S기"},
    {"question": "세포 주기 중 세포 분열이 실제로 일어나는 시기는?",
     "options": ["G1기", "S기", "G2기", "M기"], "answer": "M기"},
    {"question": "염색체가 가장 응축되어 관찰하기 좋은 시기는?",
     "options": ["전기", "중기", "후기", "말기"], "answer": "중기"},
    {"question": "감수분열에서 염색체 수가 절반으로 줄어드는 시기는?",
     "options": ["감수 1분열", "감수 2분열", "체세포 분열", "간기"], "answer": "감수 1분열"},
    {"question": "인간의 체세포 염색체 수는?",
     "options": ["22개", "23개", "44개", "46개"], "answer": "46개"},
    {"question": "인간의 생식세포 염색체 수는?",
     "options": ["22개", "23개", "44개", "46개"], "answer": "23개"},
    {"question": "감수분열의 결과 몇 개의 딸세포가 만들어지는가?",
     "options": ["1개", "2개", "4개", "8개"], "answer": "4개"},
    {"question": "교차는 감수분열의 어느 시기에 일어나는가?",
     "options": ["전기 I", "중기 I", "후기 I", "말기 I"], "answer": "전기 I"},
    {"question": "감수분열에서 상동염색체가 분리되는 시기는?",
     "options": ["전기 I", "중기 I", "후기 I", "말기 I"], "answer": "후기 I"},
    {"question": "감수분열에서 염색 분체가 분리되는 시기는?",
     "options": ["전기 II", "중기 II", "후기 II", "말기 II"], "answer": "후기 II"},
    {"question": "세포 분열 과정에서 방추사가 형성되는 시기는?",
     "options": ["전기", "중기", "후기", "말기"], "answer": "전기"},
    {"question": "세포 분열에서 핵막이 다시 형성되는 시기는?",
     "options": ["전기", "중기", "후기", "말기"], "answer": "말기"},
    {"question": "체세포 분열은 유전적으로 어떤 세포를 만드는가?",
     "options": ["동일한 세포", "다양한 세포", "염색체 수가 절반인 세포", "무작위 세포"], "answer": "동일한 세포"},
    {"question": "감수분열은 주로 어떤 세포에서 일어나는가?",
     "options": ["체세포", "배우자 형성 세포", "간세포", "신경세포"], "answer": "배우자 형성 세포"},

    # ---- 순서 배열 문제 (10문제) ----
    {"question": "다음은 체세포 분열 과정에서 발생하는 일을 순서와 상관없이 설명한 것이다. 올바른 순서를 고르시오.\n\n"
                 "- A. 핵막이 사라지고 방추사가 형성된다\n- B. 염색체가 중앙에 배열된다\n- C. 염색 분체가 양극으로 이동한다\n- D. 새로운 핵막이 형성되고 세포질이 분리된다",
     "options": ["A → B → C → D", "B → A → C → D", "C → A → B → D", "D → B → A → C"],
     "answer": "A → B → C → D"},
    {"question": "다음은 감수분열 I 과정에서 발생하는 일을 순서와 상관없이 설명한 것이다. 올바른 순서를 고르시오.\n\n"
                 "- A. 핵막이 사라지고 방추사가 형성된다\n- B. 상동염색체가 쌍을 이루어 배열된다\n- C. 상동염색체가 분리되어 양극으로 이동한다\n- D. 세포질이 분리되어 두 개의 세포가 형성된다",
     "options": ["A → B → C → D", "B → A → C → D", "C → B → A → D", "D → C → A → B"],
     "answer": "A → B → C → D"},
    {"question": "다음은 감수분열 II 과정에서 발생하는 일을 순서와 상관없이 설명한 것이다. 올바른 순서를 고르시오.\n\n"
                 "- A. 핵막이 사라지고 방추사가 형성된다\n- B. 염색체가 중앙에 배열된다\n- C. 염색 분체가 분리되어 양극으로 이동한다\n- D. 세포질 분열로 네 개의 딸세포가 형성된다",
     "options": ["A → B → C → D", "B → A → C → D", "C → A → B → D", "D → C → B → A"],
     "answer": "A → B → C → D"},
    {"question": "다음은 체세포 분열의 전기에서 일어나는 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 염색체가 응축된다\n- B. 핵막이 사라진다\n- C. 방추사가 형성된다",
     "options": ["A → B → C", "B → A → C", "C → A → B", "A → C → B"],
     "answer": "A → B → C"},
    {"question": "다음은 감수분열 I 중기의 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 방추사가 형성된다\n- B. 상동염색체가 세포 중앙에 배열된다",
     "options": ["A → B", "B → A"], "answer": "A → B"},
    {"question": "다음은 감수분열 I 후기의 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 방추사가 수축한다\n- B. 상동염색체가 양극으로 이동한다",
     "options": ["A → B", "B → A"], "answer": "A → B"},
    {"question": "다음은 감수분열 II 후기의 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 방추사가 수축한다\n- B. 염색 분체가 양극으로 이동한다",
     "options": ["A → B", "B → A"], "answer": "A → B"},
    {"question": "다음은 체세포 분열 말기의 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 염색체가 풀린다\n- B. 핵막이 다시 형성된다\n- C. 세포질이 분리된다",
     "options": ["A → B → C", "B → A → C", "C → A → B", "A → C → B"],
     "answer": "A → B → C"},
    {"question": "다음은 감수분열 I 말기의 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 세포질 분열이 시작된다\n- B. 두 개의 세포가 형성된다",
     "options": ["A → B", "B → A"], "answer": "A → B"},
    {"question": "다음은 감수분열 II 말기의 과정을 올바른 순서로 배열하시오.\n\n"
                 "- A. 세포질 분열이 일어난다\n- B. 네 개의 딸세포가 형성된다",
     "options": ["A → B", "B → A"], "answer": "A → B"},
]

# ----------------------
# 상태 초기화
# ----------------------
if "quiz_list" not in st.session_state:
    st.session_state.quiz_list = []
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# ----------------------
# 사이드바 설정
# ----------------------
st.sidebar.title("⚙️ 설정")
num_questions = st.sidebar.slider("출제할 문제 수 선택", min_value=1, max_value=30, value=5)

if st.sidebar.button("퀴즈 시작하기"):
    st.session_state.quiz_list = random.sample(quiz_data, k=min(num_questions, len(quiz_data)))
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answered = False

# ----------------------
# 메인 퀴즈 UI
# ----------------------
if st.session_state.quiz_list:
    current_index = st.session_state.current_q
    if current_index < len(st.session_state.quiz_list):
        quiz = st.session_state.quiz_list[current_index]

        st.header(f"문제 {current_index+1} / {len(st.session_state.quiz_list)}")
        st.subheader(quiz["question"])

        user_answer = st.radio("정답을 선택하세요:", quiz["options"], key=f"q{current_index}")

        if not st.session_state.answered:
            if st.button("정답 확인"):
                st.session_state.answered = True
                if user_answer == quiz["answer"]:
                    st.success("✅ 정답입니다! 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ 틀렸습니다. 정답은 👉 {quiz['answer']}")

        if st.session_state.answered:
            if st.button("다음 문제로 넘어가기"):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.rerun()
    else:
        st.success("🎉 모든 문제를 풀었습니다!")
        st.info(f"✅ 최종 점수: {st.session_state.score} / {len(st.session_state.quiz_list)}")
