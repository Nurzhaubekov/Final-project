import streamlit as st
import pandas as pd
import seaborn as sns

st.title('''**Приложение для анализа данных**
''')
st.write("""
[Вы можете получить данные здесь]
(https://raw.githubusercontent.com/Nurzhaubekov/Final-project/main/googleplaystore_cleaned.csv)
""")


@st.cache
def get_df(link_to_df):
    data = pd.read_csv(link_to_df)

    return data


df = get_df("https://raw.githubusercontent.com/Nurzhaubekov/Final-project/main/googleplaystore_cleaned.csv")

st.sidebar.header('Контроль данных')
num_rows1 = st.sidebar.number_input("Количество строк данных:", value=0)
num_rows2 = st.sidebar.number_input("", value=10840)
df = df[num_rows1:num_rows2]
st.write(df)

# 2
st.subheader("**Некоторые математические операции:**")
des_col = df.describe().columns
all_col = df.columns
sel_col = st.selectbox("Выберите функцию:", des_col)
left_side, right_side = st.columns(2)

left_side.subheader("**Максимальное значение:**")
left_side.write(df[sel_col].max())
left_side.subheader("**Среднее значение:**")
left_side.write(df[sel_col].median())
left_side.subheader("**Значение режима:**")
if len(df[sel_col].mode()) == 1:
    left_side.write(float(df[sel_col].mode()))
else:
    left_side.write((df[sel_col].mode()))

right_side.subheader("**Минимальное значение:**")
right_side.write(df[sel_col].min())
right_side.subheader("**Среднее арифметическое значение равно:**")
right_side.write(df[sel_col].mean())
right_side.subheader("**Суммарное значение:**")
right_side.write(df[sel_col].sum())

# 3
st.subheader("**Визуализация данных:**")
sel_feat1 = st.selectbox("Выберите характеристики данных:", des_col)
sel_feat2 = st.selectbox("", all_col)


def bar_plot():
    con_bar = st.sidebar.slider("Управление строкой для гистограммы:", 1, len(df), value=10)
    bar_data = df[:con_bar]
    sns.barplot(x=bar_data[sel_feat1], y=bar_data[sel_feat2], ci=None, data=bar_data)

    st.pyplot()


def pie_plot():
    con_pie = st.sidebar.slider("Управление строками для круговой диаграммы:", 1, len(df), value=10)
    pie_data = df[:con_pie]
    a = pie_data[sel_feat2].value_counts()
    pie = a.plot.pie(autopct='%1.1f%%')

    st.pyplot()


bar_plot()
pie_plot()