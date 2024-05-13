import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd

# Read data from CSV
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Create candlestick charts
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'], high=df['AAPL.High'],
                low=df['AAPL.Low'], close=df['AAPL.Close'])
                     ])

fig2 = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'], high=df['AAPL.High'],
                low=df['AAPL.Low'], close=df['AAPL.Close'])
                     ])

# Update layout (optional)
fig.update_layout(
    title="AAPL Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False
)

fig2.update_layout(
    title="AAPLasdf Candlestick Chart",
    xaxis_title="Dateasdf",
    yaxis_title="Priceasdf",
    xaxis_rangeslider_visible=False
)

# Combine the two figures into one subplot
combined_fig = make_subplots(rows=2, cols=1)
combined_fig.add_trace(fig.data[0], row=1, col=1)
combined_fig.add_trace(fig2.data[0], row=2, col=1)

# Update layout of the combined figure (optional)
combined_fig.update_layout(
    title_text="Combined Candlestick Charts",
    height=600, width=800
)

# Export as PNG
pio.write_image(combined_fig, "combined_test.png")
