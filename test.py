import streamlit as st
import random

# ----------------------
# 개념 정리 데이터
# ----------------------
concepts = {
    "체세포 분열 (Mitosis)": """
- 목적: 성장, 손상된 세포 회복, 무성생식
- 과정: 간기 → 전기 → 중기 → 후기 → 말기 → 세포질 분열
- 결과: 2개의 딸세포 (2n → 2n)
- 유전적 다양성: 없음
    """,
    "체세포 분열 단계별 정리": """
1. **간기**: 분열기 이전에 유전 물질을 복제하고, 세포질 내의 여러 물질을 합성하는 시기이다.  
2. **전기**: 염색질이 염색사로 되며, 염색사는 점차 굵어져서 염색체로 된다. 핵막과 인이 서서히 사라지며, 세포 양극에서 방추사가 나타나는 시기이다.  
3. **중기**: 염색체가 세포의 중앙에 나열되고, 방추사가 염색체에 부착되는 시기이다. 시간 상으로는 가장 짧지만, 세포가 중앙에 나열되기 때문에 염색체의 수와 모양을 관찰하기에 가장 쉽다.  
4. **후기**: 방추사에 의해 염색 분체가 양극으로 끌려가는 시기이다.  
5. **말기**: 새로운 핵막과 인이 생겨 두 개의 핵이 뚜렷하게 관찰되고, 방추사가 없어지는 시기이다.  
6. **세포질 분열**: 세포질이 둘로 나뉘어 각각의 딸세포가 만들어진다.  
    """,
    "감수 분열 (Meiosis)": """
- 목적: 배우자(난자, 정자) 형성
- 과정: 1차 감수분열 → 2차 감수분열
- 결과: 4개의 딸세포 (2n → n)
- 유전적 다양성: 있음 (교차, 독립적 분리)
    """,
    "체세포 분열 vs 감수 분열 비교": """
| 구분 | 체세포 분열 | 감수 분열 |
|------|-------------|-----------|
| 목적 | 성장/재생 | 생식세포 형성 |
| 분열 횟수 | 1회 | 2회 |
| 딸세포 수 | 2개 | 4개 |
| 염색체 수 | 동일 (2n) | 절반 (n) |
| 유전적 다양성 | 없음 | 있음 |
    """
}

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
# Streamlit UI
# ----------------------
st.set_page_config(page_title="생명과학1 - 유전 학습 앱", layout="wide")
st.title("🧬 생명과학1 - 체세포 분열 & 감수분열 학습 앱")

menu = st.sidebar.radio("메뉴 선택", ["개념 정리", "퀴즈 풀기"])

# ----------------------
# 개념 정리 페이지
# ----------------------
if menu == "개념 정리":
    st.header("📘 체세포 분열과 감수분열 개념 정리")
    for title, desc in concepts.items():
        with st.expander(title):
            st.write(desc)

            # 체세포 분열 전체 과정 그림
            if "체세포 분열 (Mitosis)" in title:
                st.image(
                    "https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC:Major_events_in_mitosis.svg"
                    caption="체세포 분열 과정",
                    use_container_width=True
                )

            # 감수 분열 과정 그림
            elif "감수 분열" in title:
                st.image(
                    "https://upload.wikimedia.org/wikipedia/commons/8/8c/Meiosis_diagram_en.svg",
                    caption="감수 분열 과정",
                    use_container_width=True
                )

# ----------------------
# 퀴즈 페이지
# ----------------------
elif menu == "퀴즈 풀기":
    st.header("📝 퀴즈 도전!")

    selected_quizzes = random.sample(quiz_data, k=3)
    score = 0
    for i, quiz in enumerate(selected_quizzes):
        st.subheader(f"Q{i+1}. {quiz['question']}")
        user_answer = st.radio("정답을 선택하세요:", quiz["options"], key=f"q{i}")

        if st.button(f"정답 확인 {i+1}", key=f"btn{i}"):
            if user_answer == quiz["answer"]:
                st.success("✅ 정답입니다! 🎉")
                score += 1
            else:
                st.error(f"❌ 틀렸습니다. 정답은 👉 {quiz['answer']}")

    st.info("👉 퀴즈는 매번 새로고침하면 다른 문제가 랜덤으로 나옵니다.")
