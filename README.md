# Olist E-Commerce Sales Dashboard

## Step 1 — Dataset and Decision-Maker

- **Dataset:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **What it is:** 110,000+ delivered orders from Olist, the largest department store on Brazilian marketplaces, 2016–2018.
- **One row =** one item in a delivered order (we merged orders, items, and product categories).
- **Decision-maker:** **Olist operations manager** — the person who runs the marketplace on a day-to-day basis and needs to know whether sales are healthy and which product categories drive revenue.

## Step 2 — Why a Dashboard

1. **Who looks, how often?** The operations manager reviews the dashboard **every Monday morning** when planning the week's seller outreach and category promotions.
2. **Decision it supports:** *If the manager sees monthly revenue drop more than 10% month-over-month, they will investigate the top categories and call the customer success team for the worst-performing ones.*
3. **What they do today:** Without a dashboard, someone on the team manually exports CSVs and builds a slide deck every week — about 4 hours of work, and by the time it lands the numbers are already stale.
4. **Why a dashboard, not a weekly email:** The manager needs to slice by category on the fly when a drop appears (is it one category or the whole store?), which an email attachment cannot do.

## Step 3 — What We Show (and What We Cut)

**Top of page — three headline KPIs (st.metric):**
1. Total revenue (R$)
2. Number of delivered orders
3. Average order value

**Middle — two charts:**
- Monthly revenue trend line: shows *why* the headline number moved (growth? seasonality? drop?)
- Top 10 product categories by revenue: shows *where* the money comes from

**Filters:** product category multiselect + month range slider — the manager only cares about categories they are actively managing.

**Two things we chose NOT to show:**
1. **Delivery time / freight cost breakdown** — interesting in EDA but the manager's weekly decision does not change based on freight; that belongs to the logistics team's own dashboard.
2. **Customer review ratings** — we did not load the reviews file; ratings matter to the CS team, not to weekly revenue planning.

**Things in the data that could mislead:**
- The first months (2016) and last month (2018-08) are partial — the default month range starts at 2017-01 so the manager does not compare a full month against a half month.
- Revenue is in Brazilian Reais (R$), not USD — labeled on every metric.

## Step 4 — Refresh Frequency

1. **Production refresh:** nightly batch from the order database (orders arrive continuously but revenue decisions are made weekly, so real-time is unnecessary).
2. **How often it is reviewed:** every Monday morning — same cadence as the weekly planning meeting.
3. **Alert threshold:** if monthly revenue drops more than 10% vs the previous month, that should trigger an immediate Slack alert, not wait for Monday.
4. **Stale-data cost:** if the dashboard is a week out of date, the manager might miss a sudden category decline and waste a week of promotions on the wrong product line.

## How to Run

```bash
uv run streamlit run app.py
```

Deployed on Streamlit Cloud with Python 3.14.
