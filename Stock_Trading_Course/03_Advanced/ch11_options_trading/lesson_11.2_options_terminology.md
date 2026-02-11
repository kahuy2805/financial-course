# Lesson 11.2: Options Terminology

## Introduction

Options trading has its own language. Understanding these terms is essential before trading any options strategies. This lesson covers the fundamental terminology you'll encounter in every options trade, broker platform, and market discussion.

---

## Strike Price

The **strike price** (also called **exercise price**) is the predetermined price at which the option holder can buy (for calls) or sell (for puts) the underlying asset.

**Key Points:**
- Determined when the option is created (written)
- Remains fixed for the life of the option
- Used to calculate intrinsic value and payoff

**Example:**
```
AAPL trading at $180
Available strike prices: $170, $175, $180, $185, $190, $195, $200

Buying the $175 Call means: You have the right to buy AAPL at $175
Buying the $185 Put means: You have the right to sell AAPL at $185
```

### Strike Selection Impact

Different strikes represent different risk/reward profiles:

```
Lower Strikes (Out-of-the-money Calls)
- Lower premium
- Higher probability of expiring worthless
- Larger potential profit percentage
- Requires bigger stock move

At-the-Money Strikes
- Medium premium
- 50/50 chance of profit
- Balanced risk/reward
- Good for uncertainty situations

Higher Strikes (In-the-money Calls)
- Higher premium
- Higher probability of profit
- Smaller potential profit percentage
- Requires smaller stock move
```

---

## Premium

The **premium** is the price of the option contract—what you pay to buy it, or receive to sell it.

**Important:**
- Paid/received upfront
- Quoted per share but represents $100 per contract (multiply by 100)
- Subject to change until the contract is closed

**Example:**
```
If a call option is quoted at $3.50:
- You pay $350 to buy one contract (1 contract = 100 shares)
- If you sell it, you receive $350

Option chain display:
Call Option for AAPL (expires 3/15/2024)
Strike | Bid  | Ask
-------|------|-----
$175   | $6.20| $6.50
$180   | $3.10| $3.20  ← Premium spread
$185   | $1.20| $1.30
```

### Premium Components (Recap from Lesson 11.1)

```
Premium = Intrinsic Value + Time Value

Example: AAPL at $180
- $175 Call at $7.25
  - Intrinsic: $180 - $175 = $5.00
  - Time Value: $7.25 - $5.00 = $2.25

- $185 Call at $1.50
  - Intrinsic: $0 (out-of-the-money)
  - Time Value: $1.50
```

---

## Expiration Date

The **expiration date** is the last day the option can be exercised. This is a critical date in options trading.

**Standard Expirations:**
- **Weekly**: Expire every Friday (for liquid stocks)
- **Monthly**: Third Friday of each month
- **Quarterly**: Last Friday of quarter months (March, June, September, December)
- **LEAPS**: Long-dated options expiring 6+ months away (up to 3 years)

**Example Timeline:**
```
Today: February 9, 2024
Current Options Available:
- Weekly: Feb 16, Feb 23, Mar 1
- Monthly: Feb 16, Mar 15, Apr 19
- Quarterly: Mar 15, Jun 21, Sep 20
- LEAPS: Feb 2025, Feb 2026

Days to Expiration (DTE):
- Feb 16 expires in 7 days
- Mar 15 expires in 34 days
- Jun 21 expires in 132 days
```

**What Happens at Expiration?**

For **in-the-money** options:
- Automatically exercised (assigned)
- Call buyer receives stock; put buyer delivers stock
- Occurs at market close on expiration day

For **out-of-the-money** options:
- Expire worthless
- Contract is closed; no assignment occurs

**Example:**
```
You own 1 AAPL $175 Call, AAPL trading at $182 on expiration day
- Option is in-the-money by $7
- You're automatically assigned (forced to exercise)
- You buy 100 shares at $175 strike
- Immediately stock is in your account
- Net effect: Same as paying $175/share + premium paid

You own 1 TSLA $250 Call, TSLA trading at $240 on expiration day
- Option is out-of-the-money by $10
- Option expires worthless
- Contract is closed; no action needed
- You keep your premium loss
```

---

## In-the-Money (ITM), At-the-Money (ATM), and Out-of-the-Money (OTM)

These terms describe an option's relationship to the current stock price.

### For Calls

| Term | Definition | Example (Stock at $100) | Profitable? |
|------|-----------|------------------------|------------|
| **ITM** (In-the-Money) | Strike < Stock Price | $90 Strike Call | Yes (has intrinsic value) |
| **ATM** (At-the-Money) | Strike ≈ Stock Price | $100 Strike Call | Borderline |
| **OTM** (Out-of-the-Money) | Strike > Stock Price | $110 Strike Call | No (pure time value) |

### For Puts

| Term | Definition | Example (Stock at $100) | Profitable? |
|------|-----------|------------------------|------------|
| **ITM** (In-the-Money) | Strike > Stock Price | $110 Strike Put | Yes (has intrinsic value) |
| **ATM** (At-the-Money) | Strike ≈ Stock Price | $100 Strike Put | Borderline |
| **OTM** (Out-of-the-Money) | Strike < Stock Price | $90 Strike Put | No (pure time value) |

**Real Example:**
```
AAPL trading at $180

Calls:
- $175 Call: IN-THE-MONEY (profitable, $5 intrinsic)
- $180 Call: AT-THE-MONEY (balanced risk/reward)
- $185 Call: OUT-OF-THE-MONEY (needs 2.8% rise to be ITM)
- $190 Call: OUT-OF-THE-MONEY (needs 5.6% rise to be ITM)

Puts:
- $175 Put: OUT-OF-THE-MONEY (needs 2.8% fall to be ITM)
- $180 Put: AT-THE-MONEY (balanced risk/reward)
- $185 Put: IN-THE-MONEY (profitable, $5 intrinsic)
- $190 Put: IN-THE-MONEY (profitable, $10 intrinsic)
```

**Why This Matters:**

- **ITM options** have higher premiums but are more likely to be assigned
- **OTM options** have lower premiums but higher probability of expiring worthless
- **ATM options** have the highest time value and are best for directional uncertainty

---

## Implied Volatility (IV)

**Implied Volatility** is the market's expectation of how much a stock will fluctuate in the future. It's expressed as a percentage (e.g., 25%, 75%).

### IV Basics

```
High IV (Volatility Expansion)
- Option premiums are expensive
- Market expects large price swings
- Good for sellers, bad for buyers
- Occurs before earnings, FDA decisions, etc.

Low IV (Volatility Contraction)
- Option premiums are cheap
- Market expects small price swings
- Good for buyers, bad for sellers
- Occurs during calm/stable periods
```

**Real Example:**
```
NVIDIA options, one month to expiration:

Before Earnings (High IV = 45%):
$500 Call trading at $15 (high premium)

After Earnings (Low IV = 25%):
$500 Call trading at $8 (lower premium)
Same strike, same time remaining, but IV collapsed
Option sellers profited; option buyers lost money

This is called "vega risk" (sensitivity to IV changes)
```

### Volatility Rank

Traders compare current IV to historical ranges:
```
IV Percentile (low = 5%, high = 95%):
- At 5th percentile: IV is historically low (good for buyers)
- At 50th percentile: IV is average (neutral)
- At 95th percentile: IV is historically high (good for sellers)
```

---

## American vs. European Options

### American Options

Can be exercised **any time before or on the expiration date**.

**Characteristics:**
- More flexible (can close early to avoid assignment)
- Generally more expensive than European equivalents
- Used in USA equity/index options
- Allow early exercise to capture dividends

**Example:**
```
You own an American call with 10 days to expiration
The stock jumps 20% higher
You can exercise today, or close the position, or hold
You have choices
```

### European Options

Can be exercised **only on the expiration date**.

**Characteristics:**
- Less flexible but sometimes cheaper
- Used in most index options (SPX)
- Predictable outcome (only at expiration matters)
- Lower premium than American equivalent

**Example:**
```
You own a European put with 10 days to expiration
The stock crashes 15% lower
You CANNOT exercise early
You must hold until expiration or close the position
No early assignment possible
```

---

## Moneyness Examples

### Complete AAPL Option Chain (Stock at $180)

```
CALL OPTIONS (Expiration: March 15, 2024)

Strike | Bid   | Ask   | IV   | Delta | Moneyness
-------|-------|-------|------|-------|----------
$170   | $11.80| $12.10| 22%  | 0.92  | ITM
$175   | $6.20 | $6.50 | 24%  | 0.71  | ITM
$180   | $3.10 | $3.20 | 27%  | 0.55  | ATM
$185   | $1.20 | $1.30 | 28%  | 0.32  | OTM
$190   | $0.40 | $0.50 | 30%  | 0.12  | OTM

PUT OPTIONS (Expiration: March 15, 2024)

Strike | Bid   | Ask   | IV   | Delta | Moneyness
-------|-------|-------|------|-------|----------
$170   | $0.35 | $0.45 | 30%  | -0.08 | OTM
$175   | $1.10 | $1.20 | 28%  | -0.29 | OTM
$180   | $3.00 | $3.10 | 27%  | -0.45 | ATM
$185   | $6.10 | $6.40 | 24%  | -0.71 | ITM
$190   | $11.70| $12.00| 22%  | -0.92 | ITM

Key Observations:
- ITM options have higher bids (more valuable)
- ATM options show the largest bid-ask spreads
- Calls and puts mirror each other (put at $185 = call at $175)
- IV increases at OTM strikes (skew)
```

---

## Additional Important Terms

### Bid-Ask Spread

The difference between the highest buy price (bid) and lowest sell price (ask).

```
Example: $180 Call shows Bid $3.10, Ask $3.20
- You pay $3.20 to buy (ask)
- You receive $3.10 to sell (bid)
- Cost of round trip = $0.10 = 3.2% of premium
```

### Open Interest

The total number of outstanding contracts (not yet closed or exercised).

```
High Open Interest = Liquid, tight spreads
Low Open Interest = Illiquid, wide spreads, hard to exit

Example: AAPL 180 Call
- Open Interest: 50,000 contracts
- Highly liquid, easy to trade
- vs. $185 Call with 500 open interest = less liquid
```

### Volume

Number of contracts traded today.

```
Daily Volume for $180 Call: 15,000 contracts
- Shows if this strike is being actively traded today
- Helps gauge liquidity
```

### Assignment

Forced exercise of an option.

```
You sold 1 AAPL $175 Call for $6.50
At expiration, AAPL is at $182 (ITM)
You are assigned: forced to deliver 100 shares at $175
You must have 100 shares (or buy them) to cover assignment
Assignment occurs after market close on expiration day
```

---

## Key Takeaways

1. **Strike Price**: The fixed price at which you buy/sell the underlying asset
2. **Premium**: The price of the option; includes intrinsic and time value
3. **Expiration Date**: The deadline by which the option must be exercised or closes
4. **Moneyness (ITM/ATM/OTM)**: Describes profitability relative to stock price
5. **Implied Volatility**: Market's expectation of future price movement
6. **American vs. European**: When you can exercise the option
7. **Bid-Ask Spread**: Cost of trading; liquidity indicator
8. **Open Interest & Volume**: Gauge liquidity and ease of exiting trades

---

## In the Next Lessons

- Lesson 11.4 explores the Greeks—mathematical measures of how options respond to market changes
- Lesson 11.3 shows practical strategies using these terms
- Lesson 11.5 combines these concepts into spread strategies

---

## Self-Assessment Questions

1. If a stock is at $100, which put option is ITM: the $95 put or the $105 put?
2. What happens if you're assigned on a short call you sold?
3. Why might high IV be good for option sellers but bad for option buyers?
4. Can you exercise an American put before expiration? What about a European put?
5. If you buy an option and IV increases (but stock price stays the same), does your option gain or lose value?

