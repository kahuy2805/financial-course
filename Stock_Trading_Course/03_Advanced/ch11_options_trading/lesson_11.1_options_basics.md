# Lesson 11.1: Options Basics - What are Options?

## Introduction

Options are **derivative contracts** that give the holder the right (but not the obligation) to buy or sell an underlying asset at a predetermined price before or on a specific date. They're called "derivatives" because their value derives from an underlying security—typically a stock.

This lesson provides a foundation for understanding options trading before moving to more advanced strategies.

---

## What Makes Options Unique?

Unlike stock ownership, which requires capital commitment upfront, options offer:

1. **Leverage**: Control a large amount of stock with a small upfront investment
2. **Flexibility**: Profit in rising, falling, or sideways markets
3. **Risk Control**: Define maximum losses and profits upfront
4. **Income Generation**: Generate returns from assets you already own

---

## The Two Main Option Types

### Call Options

A **call option** gives the holder the right to **BUY** an underlying asset at a specified price (the strike price) before or on the expiration date.

**Who trades calls?**
- Bullish investors expecting the stock to rise
- Income generators using covered calls
- Speculators betting on price increases with leverage

**Real Example:**
```
Stock: Apple (AAPL) trading at $180
Call Option: Buy the right to purchase AAPL at $185 (strike)
Cost: $5 per share (or $500 per contract, since 1 contract = 100 shares)
Expiration: 30 days from now

Scenario 1 - Stock rises to $200
- You exercise: Buy 100 shares at $185, sell at $200 market price
- Profit: ($200 - $185) × 100 - $500 premium paid = $1,500 - $500 = $1,000
- Return on investment: $1,000/$500 = 200%

Scenario 2 - Stock falls to $170
- You don't exercise (option expires worthless)
- Loss: -$500 (premium paid)
- You lost your entire investment but didn't have to buy 18,000 shares of AAPL
```

**Call payoff formula:**
```
Maximum Loss = Premium Paid
Breakeven = Strike Price + Premium Paid
Maximum Profit = Unlimited (in theory)
```

---

### Put Options

A **put option** gives the holder the right to **SELL** an underlying asset at a specified price (the strike price) before or on the expiration date.

**Who trades puts?**
- Bearish investors expecting the stock to fall
- Portfolio protectors hedging existing stock positions
- Sellers generating income from puts

**Real Example:**
```
Stock: Tesla (TSLA) trading at $250
Put Option: Buy the right to sell TSLA at $240 (strike)
Cost: $4 per share (or $400 per contract)
Expiration: 30 days from now

Scenario 1 - Stock falls to $200
- You exercise: Buy 100 shares at $200 market price, sell at $240 strike
- Profit: ($240 - $200) × 100 - $400 premium paid = $4,000 - $400 = $3,600
- Return: $3,600/$400 = 900%

Scenario 2 - Stock rises to $270
- You don't exercise (right to sell at $240 is worthless)
- Loss: -$400 (premium paid)
- You lost your entire investment but were protected from $250 to $240
```

**Put payoff formula:**
```
Maximum Loss = Premium Paid
Breakeven = Strike Price - Premium Paid
Maximum Profit = Strike Price × 100 - Premium Paid
```

---

## Call vs. Put Comparison

| Aspect | Call | Put |
|--------|------|-----|
| **Right to** | BUY at strike | SELL at strike |
| **Profitable when** | Stock rises | Stock falls |
| **Buyer sentiment** | Bullish | Bearish |
| **Buyer's max loss** | Premium paid | Premium paid |
| **Buyer's max profit** | Unlimited | Strike price minus premium |
| **Seller sentiment** | Bearish | Bullish |
| **Seller's max loss** | Unlimited (calls) | Strike minus premium |
| **Seller's max profit** | Premium received | Premium received |

---

## Options Pricing Basics

### Why Do Options Cost What They Do?

An option's price (called the **premium**) depends on two components:

**1. Intrinsic Value**
The profit you could make if you exercised today.

```
For Calls: MAX(Stock Price - Strike, 0)
For Puts: MAX(Strike - Stock Price, 0)

Example:
- Stock at $180, Call strike $175: Intrinsic = $180 - $175 = $5
- Stock at $180, Call strike $185: Intrinsic = $0 (not profitable)
- Stock at $180, Put strike $185: Intrinsic = $185 - $180 = $5
```

**2. Time Value**
The additional cost for the *potential* for the option to become more profitable before expiration.

```
Premium = Intrinsic Value + Time Value

Example: AAPL $180
- $175 Call trading at $7
  - Intrinsic: $5
  - Time Value: $7 - $5 = $2
  - The $2 represents the chance it goes even higher by expiration

- $185 Call trading at $2
  - Intrinsic: $0 (out-of-the-money)
  - Time Value: $2 (entire premium is time value)
  - You're betting stock rises $5+ in the remaining time
```

---

## Long vs. Short (Open vs. Sell) Positions

### Buying Options (Going Long)

When you **buy** an option, you:
- Pay the premium upfront
- Have limited risk (lose only what you paid)
- Need the market to move significantly in your favor
- Benefit from time value early in the contract's life

**Buy Call Profit/Loss:**
```
Profit/Loss = (Stock Price at Expiration - Strike) × 100 - Premium Paid

If AAPL was $180, you buy $185 call for $500:
- Stock at $190: ($190-$185) × 100 - $500 = $500 - $500 = $0 (breakeven)
- Stock at $200: ($200-$185) × 100 - $500 = $1,500 - $500 = $1,000 profit
- Stock at $170: ($170-$185) × 100 - $500 = $0 (can't go negative) - $500 loss
```

### Selling Options (Going Short)

When you **sell** an option, you:
- Receive the premium immediately
- Have potentially unlimited risk (on short calls)
- Need the market to stay relatively stable
- Benefit from time decay

**Sell Call Profit/Loss:**
```
Profit/Loss = Premium Received - (Stock Price at Expiration - Strike) × 100

If AAPL was $180, you sell $185 call for $500:
- Stock at $190: $500 - ($190-$185) × 100 = $500 - $500 = $0 (breakeven)
- Stock at $200: $500 - ($200-$185) × 100 = $500 - $1,500 = -$1,000 loss
- Stock at $170: $500 - ($170-$185) × 100 = $500 - $0 = $500 profit
```

---

## Key Takeaways

1. **Calls** are bullish bets; **Puts** are bearish bets
2. **Call buyers** profit from rising prices; **call sellers** profit from stable/falling prices
3. **Put buyers** profit from falling prices; **put sellers** profit from stable/rising prices
4. Options provide **leverage** but have **time decay** working against long positions
5. **Premium** consists of intrinsic value + time value
6. Options are **zero-sum games**: profit for one side = loss for the other
7. Limited risk for option buyers, potentially unlimited risk for sellers (except puts)

---

## In the Next Lessons

- Lesson 11.2 dives deeper into options terminology
- Lesson 11.4 explains the Greeks—the mathematical factors that drive option prices
- Later lessons show how professionals use options strategies to manage risk and generate income

---

## Self-Assessment Questions

1. What's the difference between intrinsic and time value?
2. Why would someone buy a put option instead of shorting a stock?
3. If you buy a call option for $300 and the stock falls, what's your maximum loss?
4. Explain why call sellers profit when the stock price stays flat.
5. Can a call option with a strike price below the current stock price expire worthless?

