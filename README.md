# Quant Finance Toolkit

A comprehensive Python toolkit for quantitative finance, including options pricing, backtesting strategies, portfolio optimization, and more.

## 🚀 Features

- **Options Pricing**: Black-Scholes model and Greeks calculation
- **Backtesting Engine**: Simple moving average crossover strategy with performance metrics (Sharpe ratio, max drawdown, etc.)
- **Portfolio Optimization**: Mean-variance optimization using SciPy
- **Data Integration**: Fetch historical data via yfinance
- **Visualization**: Professional charts with matplotlib

## 📦 Installation

```bash
git clone https://github.com/Hello-007-w/quant-finance-toolkit.git
cd quant-finance-toolkit
pip install -r requirements.txt
```

## 🚀 Quick Start

### 1. Black-Scholes Option Pricing

```python
from black_scholes import black_scholes_call, black_scholes_put

# Example: European Call Option
call_price = black_scholes_call(S=100, K=105, T=1.0, r=0.05, sigma=0.2)
print(f"Call Option Price: ${call_price:.2f}")

put_price = black_scholes_put(S=100, K=105, T=1.0, r=0.05, sigma=0.2)
print(f"Put Option Price: ${put_price:.2f}")
```

### 2. Run Moving Average Crossover Backtest

```bash
python moving_average_strategy.py
```

This will backtest a simple MA strategy on AAPL and print performance metrics.

## 📈 Project Structure

```
quant-finance-toolkit/
├── README.md
├── requirements.txt
├── black_scholes.py          # Options pricing models
├── moving_average_strategy.py # Backtesting example
├── LICENSE
└── .gitignore
```

## 👩‍💻 Contributing

Contributions are welcome! Please open an issue or submit a PR.

## ⚖️ License

MIT License

---

*Built with ❤️ for quantitative finance enthusiasts.*