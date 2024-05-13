import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

# Read data from CSV
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
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

# Export as PNG
fig.write_image("test.png")
