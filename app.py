import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

st.title('Olist E-Commerce Sales Dashboard')
st.caption('For the Olist operations manager — track monthly revenue, order volume, and top product categories.')

df = pd.read_csv('sales_clean.csv', parse_dates=['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

# ---- filters ----
categories = sorted(df['category'].dropna().unique())
selected = st.sidebar.multiselect('Product category', categories, default=categories)

months = sorted(df['month'].unique())
month_range = st.sidebar.select_slider('Month range', options=months, value=(months[2], months[-1]))

df = df[df['category'].isin(selected) & df['month'].between(month_range[0], month_range[1])]

# ---- KPIs ----
total_rev = df['price'].sum()
n_orders = df['order_id'].nunique()
avg_order = total_rev / n_orders

c1, c2, c3 = st.columns(3)
c1.metric('Total Revenue (R$)', f'R${total_rev:,.0f}')
c2.metric('Orders', f'{n_orders:,}')
c3.metric('Avg Order Value', f'R${avg_order:,.2f}')

# ---- chart 1: monthly revenue ----
st.subheader('Monthly Revenue Trend')
monthly = df.groupby('month')['price'].sum()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(monthly.index, monthly.values, marker='o')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue (R$)')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# ---- chart 2: top categories ----
st.subheader('Top 10 Categories by Revenue')
top_cat = df.groupby('category')['price'].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(10, 5))
top_cat.plot.barh(ax=ax2)
ax2.set_xlabel('Revenue (R$)')
ax2.invert_yaxis()
st.pyplot(fig2)

# ---- data period ----
st.caption(f'Data: {months[0]} to {months[-1]}, Olist Brazilian E-Commerce Kaggle snapshot. '
           f'Production refresh: nightly batch from the order system; manager reviews every Monday.')
