import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

r_code = '''
galaxy <- read_csv("C:/Users/pjjun/OneDrive/바탕 화면/데이터.csv", skip = 12)

galaxy2 <- galaxy %>% mutate(
  "Date (Yr. - 1980)" = `Adopted LMC modulus`,
  "Hubble const." = ...12,
  "Method" = `D (Mpc)`,
  "D (Mpc)" = err,
  "err" = `m-M`,
  "m-M" = `Galaxy ID`,
  "redshift" = `...11`
)

galaxy3 <- galaxy2 %>% 
  filter(`Exclusion Code` != 999999) %>% 
  select("G", "m-M", "err", "D (Mpc)", "Method", "Hubble const.", "Date (Yr. - 1980)", "redshift") %>% 
  mutate("velocity" = 299792 * redshift) %>% 
  filter(Method %in% c("TRGB", "Cepheids", "SNIa SDSS", "Type II Cepheids", "SNIa"))

ggplot(data = galaxy3, mapping = aes(x = `D (Mpc)`, y = velocity)) +
  geom_point(na.rm = TRUE)
'''
url = 'https://www.stat.uchicago.edu/~s343/Lectures/981009/981009.html?'

y = [170, 290, -130, -70, -185, -220, 200, 290, 270, 200, 300, -30, 650, 150, 500, 920, 450, 500, 500, 960, 500, 850, 800, 1090]
x = [0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.450, 0.500, 0.500, 0.630, 0.800, 0.900, 0.900, 0.900, 0.900, 1.000, 1.100, 1.100, 1.400, 1.700, 2.000, 2.000, 2.000, 2.000]

fig, ax = plt.subplots()
ax.scatter(x, y)

class_data = {'월': ['물리', ''], 
        '화': ['통계', '프로그래밍'], 
        '수': ['물리', '프로그래밍'], 
        '목': ['통계', ''], 
        '금': ['컴탐', '']}

class_info = {"물리": {"교수": "문송기", "장소": "26-B101"},
        "통계": {"교수": "문하은", "장소": "18-101"},
        "프로그래밍": {"교수": "서진욱", "장소": "301-118"},
        "컴탐": {"교수": "변해선", "장소": "26-104"}
        }

def selfintro(code, fig, url):
        st.title("자기소개")
        st.header("2024-19651 박정준")
        st.write("")

        st.subheader("취미")
        st.write("프로그래밍에 관심이 있으며, 시간이 날 때 새로운 기술을 공부합니다.")
        st.caption("최근 작성 코드 (R 작성)")
        st.code(code, language = "r")

        st.caption("결과 예시")
        st.pyplot(fig)
        st.markdown(f"[출처]({url})")
        st.write("")

        st.subheader("목표")
        st.write("새로운 개념을 배우고 직접 실험하여 이해를 확장하고 싶습니다.")

def classintro(data, info):
        df = pd.DataFrame(data)
        st.dataframe(df)
        st.json(info)
        st.write("강의 요약")
        col1, col2 = st.columns(2)
        with col1:
                st.metric(label = "수강 과목 수", value = "6")
        with col2:
                st.metric(label = "총 학점", value = "40", delta = "+16")

tab1, tab2 = st.tabs(["자기소개", "강의 소개"])
with tab1:
        selfintro(r_code, fig, url)
with tab2:
        classintro(class_data, class_info)
