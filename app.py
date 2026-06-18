import streamlit as st
import yfinance as yf

st.set_page_config(page_title="AI Stock Research Assistant")

st.title("AI Stock Research Assistant")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, NVDA, MSFT)")

if ticker:
    stock = yf.Ticker(ticker.upper())
    info = stock.info

    st.header(info.get("longName", ticker.upper()))

    st.write("Current Price:", info.get("currentPrice"))
    st.write("Market Cap:", info.get("marketCap"))
    st.write("P/E Ratio:", info.get("trailingPE"))

    st.subheader("Company Overview")
    st.write(info.get("longBusinessSummary"))

    hist = stock.history(period="1y")

    if not hist.empty:
        st.subheader("1-Year Stock Price")
        st.line_chart(hist["Close"])

