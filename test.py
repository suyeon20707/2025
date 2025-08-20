import streamlit as st
import random

# ----------------------
# 🌌 배경 + CSS 스타일
# ----------------------
page_bg = """
<style>
.stApp {
    background-image: url("https://cdn.pixabay.com/photo/2016/11/19/14/00/dna-1838696_1280.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* 오버레이(배경 위 반투명 그라데이션) */
.stApp::before {
    content: "";
    position: fixed;
    top:0; left:0;
    width:100%; height:100%;
    background: linear-gradient(120deg, rgba(0,150,136,0.5), rgba(156,39,176,0.5));
    z-index: -1;
}

/* 메인 컨텐츠 카드 스타일 */
.block-container {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    animation: fadeIn 1s ease-in-out;
}

/* 사이드바 초록빛 그라데이션 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #43a047, #66bb6a, #a5d6a7);
    color: white;
    font-weight: bold;
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* 제목 꾸미기 */
h1, h2, h3 {
    text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
}

/* 버튼 스타일 */
.stButton>button {
    background: linear-gradient(90deg, #00c853, #64dd17);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #64dd17, #00c853);
    transform: scale(1.05);
}

/* 등장 애니메이션 */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

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
3. **중기**: 염색체가 세포의 중앙에 나열되고, 방추사가 염색체에 부착되는 시기이다.  
4. **후기**: 방추사에 의해 염색 분체가 양극으로 끌려가는 시기이다.  
5. **말기**: 새로운 핵막과 인이 생겨 두 개의 핵이 뚜렷하게 관찰되고, 방추사가 없어지는
