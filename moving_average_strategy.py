import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fetch_data(ticker: str, period: str = "2y") -> pd.DataFrame:
    """Fetch historical stock data using yfinance."""
    data = yf.download(ticker, period=period, progress=False)
    return data

def calculate_ma_strategy(data: pd.DataFrame, short_window: int = 20, long_window: int = 50) -> pd.DataFrame:
    """Calculate moving averages and generate signals."""
    df = data.copy()
    df['SMA_short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_long'] = df['Close'].rolling(window=long_window).mean()
    df['Signal'] = 0
    df.loc[df['SMA_short'] > df['SMA_long'], 'Signal'] = 1
    df.loc[df['SMA_short'] < df['SMA_long'], 'Signal'] = -1
    df['Position'] = df['Signal'].shift(1)  # Avoid look-ahead bias
    return df

def backtest_strategy(df: pd.DataFrame) -> dict:
    """Run backtest and calculate performance metrics."""
    df['Returns'] = df['Close'].pct_change()
    df['Strategy_Returns'] = df['Position'] * df['Returns']
    
    cumulative_returns = (1 + df['Strategy_Returns']).cumprod()
    total_return = cumulative_returns.iloc[-1] - 1
    
    # Sharpe Ratio (assuming 252 trading days)
    sharpe_ratio = (df['Strategy_Returns'].mean() / df['Strategy_Returns'].std()) * np.sqrt(252)
    
    # Max Drawdown
    running_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - running_max) / running_max
    max_drawdown = drawdown.min()
    
    return {
        'Total Return': f"{total_return:.2%}",
        'Sharpe Ratio': f"{sharpe_ratio:.2f}",
        'Max Drawdown': f"{max_drawdown:.2%}",
        'Final Portfolio Value': f"${cumulative_returns.iloc[-1]:.2f}"
    }

def plot_strategy(df: pd.DataFrame, ticker: str):
    """Plot price, MAs, and signals."""
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close Price', alpha=0.7)
    plt.plot(df.index, df['SMA_short'], label='Short MA (20)', alpha=0.8)
    plt.plot(df.index, df['SMA_long'], label='Long MA (50)', alpha=0.8)
    
    # Plot buy/sell signals
    buy_signals = df[df['Position'] == 1].index
    sell_signals = df[df['Position'] == -1].index
    plt.scatter(buy_signals, df.loc[buy_signals, 'Close'], marker='^', color='g', label='Buy Signal', s=100)
    plt.scatter(sell_signals, df.loc[sell_signals, 'Close'], marker='v', color='r', label='Sell Signal', s=100)
    
    plt.title(f'{ticker} Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    ticker = "AAPL"
    print(f"Fetching data for {ticker}...")
    data = fetch_data(ticker)
    
    print("Calculating strategy...")
    strategy_df = calculate_ma_strategy(data)
    
    print("Running backtest...")
    metrics = backtest_strategy(strategy_df)
    
    print("\n=== Backtest Results ===")
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    print("\nGenerating plot... (close the plot window to exit)")
    plot_strategy(strategy_df, ticker)