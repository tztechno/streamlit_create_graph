import streamlit as st
import matplotlib.pyplot as plt

st.sidebar.write(f'F(x) = A * x^4 + B * x^3 + C * x^2 + D * x')
a = st.sidebar.slider('A', value=1, min_value=-10, max_value=10, step=1)
b = st.sidebar.slider('B', value=1, min_value=-10, max_value=10, step=1)
c = st.sidebar.slider('C', value=1, min_value=-10, max_value=10, step=1)
d = st.sidebar.slider('D', value=1, min_value=-10, max_value=10, step=1)

def f(x):
    return a*(x**4) + b*(x**3) + c*(x**2) + d*x 

P = []
for i in range(-30, 30):
    x = i / 10
    y = f(x)
    P.append((x, y))
    
x_values = [point[0] for point in P]
y_values = [point[1] for point in P]

# グラフを右側に配置
st.title('Create and Show Graph F(x)')
st.markdown(f'## F(x) = {a} * x^4 + {b} * x^3 + {c} * x^2 + {d} * x')
col1, col2, col3 = st.columns([1,7,2])  

# 右側の列にグラフを表示
with col2:
    fig = plt.figure()
    plt.plot(x_values, y_values)
    st.pyplot(fig)

