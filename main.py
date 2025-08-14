import streamlit as st
🎨 Streamlit 페이지 설정
st.set_page_config(page_title="💼 MBTI 직업 추천기", layout="centered", page_icon="🧠")

# 💡 헤더 꾸미기
st.markdown("<h1 style='text-align: center; color: #4B9CD3;'>💼 MBTI 기반 직업 추천 웹 앱</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>당신의 MBTI 유형에 어울리는 직업을 알아보세요!</h3>", unsafe_allow_html=True)
st.markdown("### ")  # 줄바꿈

# MBTI별 추천 직업 데이터 (예시)
mbti_jobs = {
    "INTJ": ["전략 기획가", "소프트웨어 개발자", "과학자", "엔지니어"],
    "INTP": ["연구원", "데이터 분석가", "이론 물리학자", "기술 컨설턴트"],
    "ENTJ": ["경영 컨설턴트", "프로젝트 매니저", "CEO", "변호사"],
    "ENTP": ["마케팅 전문가", "기술 창업가", "기획자", "정치가"],
    "INFJ": ["상담가", "교사", "심리학자", "작가"],
    "INFP": ["예술가", "작가", "상담사", "사회복지사"],
    "ENFJ": ["HR 전문가", "교육자", "정치인", "코치"],
    "ENFP": ["크리에이티브 디렉터", "공연 예술가", "기획자", "여행 작가"],
    "ISTJ": ["회계사", "관리자", "변호사", "경찰관"],
    "ISFJ": ["간호사", "사회복지사", "초등학교 교사", "비서"],
    "ESTJ": ["경영 관리자", "군인", "법조인", "프로젝트 매니저"],
    "ESFJ": ["간호사", "교사", "사회복지사", "이벤트 플래너"],
    "ISTP": ["기술자", "기계공", "파일럿", "응급 구조사"],
    "ISFP": ["디자이너", "사진작가", "물리치료사", "조각가"],
    "ESTP": ["세일즈 매니저", "기업가", "스턴트 배우", "운동선수"],
    "ESFP": ["연예인", "이벤트 코디네이터", "방송인", "패션 스타일리스트"]
}

# Streamlit 앱 시작
st.set_page_config(page_title="MBTI 직업 추천", layout="centered")

st.title("💼 MBTI 기반 직업 추천 웹 앱")
st.subheader("당신의 MBTI에 어울리는 직업을 알아보세요!")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", options=mbti_list)

# 추천 직업 표시
if selected_mbti:
    st.markdown(f"### 🧠 {selected_mbti} 유형의 추천 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

# 하단 안내
st.markdown("---")
st.caption("© 2025 MBTI Career Recommender")
