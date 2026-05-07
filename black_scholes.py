import numpy as np
from scipy.stats import norm

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate European Call Option price using Black-Scholes model.
    
    Parameters:
    S : float - Current stock price
    K : float - Strike price
    T : float - Time to maturity (in years)
    r : float - Risk-free interest rate
    sigma : float - Volatility of underlying asset
    
    Returns:
    float - Call option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate European Put Option price using Black-Scholes model.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

if __name__ == "__main__":
    # Example usage
    S, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.20
    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)
    print(f"Stock Price: ${S}")
    print(f"Strike Price: ${K}")
    print(f"Time to Maturity: {T} year(s)")
    print(f"Risk-Free Rate: {r*100}%")
    print(f"Volatility: {sigma*100}%")
    print(f"Call Option Price: ${call:.2f}")
    print(f"Put Option Price: ${put:.2f}")