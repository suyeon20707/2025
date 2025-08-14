import streamlit as st

# 동물 이름과 이모지 매핑 (예시)
animal_emojis = {
    "강아지": "🐶",
    "개": "🐶",
    "고양이": "🐱",
    "사자": "🦁",
    "호랑이": "🐯",
    "곰": "🐻",
    "토끼": "🐰",
    "돼지": "🐷",
    "코끼리": "🐘",
    "원숭이": "🐵",
    "여우": "🦊",
    "늑대": "🐺",
    "펭귄": "🐧",
    "부엉이": "🦉",
    "독수리": "🦅",
    "말": "🐴",
    "소": "🐮",
    "양": "🐑",
    "닭": "🐔",
    "오리": "🦆",
    "개구리": "🐸",
    "고래": "🐋",
    "상어": "🦈",
    "물고기": "🐟",
    "문어": "🐙",
    "거북이": "🐢",
    "뱀": "🐍"
}

# Streamlit 페이지 설정
st.set_page_config(page_title="동물 이모지 추천기", layout="centered")

# 제목
st.title("🐾 동물 이모지 추천기")
st.subheader("동물 이름을 입력하면 이모지를 보여드릴게요!")

# 사용자 입력
user_input = st.text_input("동물 이름을 입력하세요 (예: 고양이, 사자, 펭귄 등)").strip()

# 결과 출력
if user_input:
    emoji = animal_emojis.get(user_input)
    if emoji:
        st.markdown(f"### 당신이 찾은 동물: {emoji}")
    else:
        st.warning("해당 동물의 이모지를 찾을 수 없어요. 다른 동물을 입력해 보세요!")

# 하단 정보
st.markdown("---")
st.caption("© 2025 동물 이모지 추천기")

