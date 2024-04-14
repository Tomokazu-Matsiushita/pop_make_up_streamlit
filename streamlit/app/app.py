import streamlit as st
import pandas as pd
from utils.variables import *
from datetime import datetime

st.set_page_config(
  layout="wide"
)

# 日付範囲選択ウィジェット
# st.header("日付範囲を選択")
# target_dt = st.date_input("日付", datetime.today())

# 年と月の選択
st.sidebar.header("月を選択")
years = list(range(2020, datetime.now().year + 1))  # 2020年から現在の年まで
selected_year = st.sidebar.selectbox("年", years, index=len(years)-1)  # デフォルトは現在の年

months = list(range(1, 13))  # 1月から12月
selected_month = st.sidebar.selectbox("月", months)

# 選択された日付を fnc1 関数に渡してデータを取得
#this_month_trn, trn_num_ct, trn_user_ct, user_trn_ct, user_trn_ct_sum, mean_ct, rate_3over_week = fnc1(target_dt)

# 選択された年月を datetime オブジェクトに変換
target_month = datetime(year=selected_year, month=selected_month, day=1)

# 選択された月を fnc1 関数に渡してデータを取得
this_month_trn, trn_num_ct, trn_user_ct, user_trn_ct, user_trn_ct_sum, mean_ct, rate_3over_week = fnc1(target_month)

with st.container():#border=True):
  st.header('XXXX株式会社')
   
col1, col2, col3 = st.columns(3)

with col1:
  with st.container():#border=True, height=500):
    st.markdown('<h5>選択された月のデータ</h5></br></br>', unsafe_allow_html=True)
    st.markdown('総利用食数')
    st.markdown(f"<h2 style='text-align:center; font-weight:bold;'>{trn_num_ct}<span style='font-size:0.5em;'>食</span></h2>", unsafe_allow_html=True)
    st.markdown('総利用者数')
    st.markdown(f"<h2 style='text-align:center; font-weight:bold;'>{trn_user_ct}<span style='font-size:0.5em;'>人</span></h2>", unsafe_allow_html=True)

with col2:
    with st.container():#border=True, height=500):
      st.markdown('<h5>一人当たりの週平均利用日数</h5>', unsafe_allow_html=True)
      with st.container():#height=300, border=False):
        st.write('<div style="display: flex; justify-content: center; ">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
      st.markdown(f"<h5 style='text-align:center; font-weight:bold;'>前月比  {plus_minus_mean_ct}{abs(dif_mean_ct).round(1)}回</h5>", unsafe_allow_html=True)
      st.write(f'週3回以上の利用者　{round(rate_3over_week*100,1)}%')
      st.write(f'前月比　{plus_minus_mean_ct}{round(abs(rate_3over_week - rate_3over_week_pre)*100,1)}%')

with col3:
   with st.container():#border=True,height=500):
      st.markdown('<h5>年代別利用率</h5>', unsafe_allow_html=True)
    #  st.plotly_chart(fig2)
      st.write('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
      st.plotly_chart(fig2, use_container_width=True)

with st.container():#border=True):
  st.markdown(f"<h4 style='text-align:center; font-weight:bold;'>部署別利用食数</h4>", unsafe_allow_html=True)
  st.write('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
  st.plotly_chart(fig3, use_container_width=True)













# config適用
# streamlit config show
