# Lesson 11.3: Basic Options Strategies

## Introduction

Now that you understand calls, puts, and options terminology, let's explore practical strategies professional traders use. This lesson covers two fundamental strategies used by millions of traders: covered calls and protective puts.

These strategies form the foundation for more complex multi-leg strategies you'll learn later.

---

## Strategy 1: Covered Call (Call Covered by Stock)

### Overview

A **covered call** is a strategy where you:
1. **Own** 100 shares of stock
2. **Sell** one call option against those shares
3. Keep the premium income while capping upside

### Who Uses Covered Calls?

- Dividend investors wanting extra income
- Traders with stock that's near a resistance level
- Investors neutral to slightly bullish on a stock
- Anyone wanting to "get paid" on their holdings

### Mechanics

```
Setup:
- Buy 100 shares at $100 (current market price)
- Simultaneously sell 1 call with $105 strike for $2 premium
- Net cost: $100 - $0.02 (per share premium received) = $99.98

The "covered" part:
- If called away (stock assigned), you have the shares to deliver
- This is why it's "covered" - you own the underlying security
- Contrast with "naked" call where you don't own the shares (risky!)
```

### Risk Profile

```
Maximum Profit:
- Stock rises to $105 or higher
- Called away at $105 strike price
- Profit = ($105 - $100) + $2 premium = $7 per share = $700 total
- Return on investment = $700/$10,000 = 7% return

Maximum Loss:
- Stock falls to $0 (and premium doesn't help much)
- You own shares worth $0, but keep $200 premium
- Loss = -$10,000 + $200 = -$9,800
- This is the loss from owning stock, reduced by premium

Breakeven:
- $100 - $0.02 = $99.98 per share
- The premium reduces your loss if stock drops

Scenario Analysis - AAPL at $180, sell $185 call for $2.50:
```

### Real Example: Covered Call Details

```
Position Details:
- Buy 100 AAPL shares at $180
- Sell 1 AAPL $185 call for $2.50 ($250 total)
- Net debit: $18,000 - $250 = $17,750
- Days to expiration: 30

Scenario 1: AAPL at $200 on expiration (stock jumps 11%)
- Called away at $185 strike
- Gain on stock: ($185 - $180) × 100 = $500
- Plus premium: $250
- Total profit: $750 (4.2% return in 30 days)
- Annualized return: ~51%
- However, you miss the additional $1,500 gain from $185 to $200

Scenario 2: AAPL at $185 exactly (at the money)
- Called away at $185 strike
- Gain on stock: ($185 - $180) × 100 = $500
- Plus premium: $250
- Total profit: $750 (4.2% return in 30 days)
- Stock doesn't rise past strike

Scenario 3: AAPL at $175 on expiration (stock drops 2.8%)
- Option expires worthless (not called away)
- Loss on stock: ($175 - $180) × 100 = -$500
- Plus premium: $250 (you keep it)
- Net loss: -$250 (-1.4% loss in 30 days)
- Premium cushions your downside by 1.4%

Scenario 4: AAPL at $170 on expiration (larger drop)
- Option expires worthless
- Loss on stock: ($170 - $180) × 100 = -$1,000
- Plus premium: $250 (cushion)
- Net loss: -$750 (-4.2% loss)
- Premium helped but didn't prevent losses
```

### When to Use Covered Calls

**Good Timing:**
- Stock at resistance level
- You're neutral to slightly bullish
- You've achieved significant gains and want to lock in profit
- You own dividend stocks and want extra income
- IV is high (premium is expensive, good for sellers)

**Avoid When:**
- Stock is breaking out to the upside (don't cap gains)
- IV is very low (not worth the risk)
- You're very bullish and expect big gains
- You need full downside protection

### Common Mistakes

```
Mistake 1: Not being assigned
"I sold the call but stock stayed below strike"
- You keep the premium AND the stock
- This is actually the desired outcome for income

Mistake 2: Margin call on assignment
- When assigned, you deliver 100 shares
- Need to plan for this: have shares ready or buy-to-close the call first
- If margin: holding the short call requires margin until assigned

Mistake 3: Selling calls too close to dividends
- Assignment pulled you through dividend
- You miss the dividend but already in loss
- Check ex-dividend dates before selling calls

Mistake 4: Chasing returns with deep OTM calls
- Selling $200 call when stock at $180 = low premium, low risk
- Selling $170 call when stock at $180 = high premium, high risk (likely assigned)
- Balance premium income with assignment risk
```

---

## Strategy 2: Protective Put (Insurance on Your Stock)

### Overview

A **protective put** is a strategy where you:
1. **Own** 100 shares of stock
2. **Buy** one put option as insurance
3. Limit downside losses while keeping upside potential

This is the insurance strategy—you pay a premium to protect your gains.

### Who Uses Protective Puts?

- Portfolio managers protecting stock positions during uncertainty
- Traders holding through earnings
- Investors after large gains wanting to lock in value
- Anyone wanting "portfolio insurance"

### Mechanics

```
Setup:
- Own 100 shares at $100 (current market price)
- Buy 1 put with $95 strike for $2 premium
- Total cost: $100 per share + $2 premium = $102 per share

Protection:
- If stock falls below $95, you can sell at $95
- You're insured against drops greater than 5%
- This is literally insurance: you paid a premium for protection
```

### Risk Profile

```
Maximum Loss:
- Stock falls to $0
- You exercise put: sell shares at $95 strike
- Loss = $95 - $100 cost - $2 premium paid = -$7 per share
- Loss capped at $700 on 100 shares

Maximum Profit:
- Stock rises indefinitely
- Put expires worthless (not needed)
- Profit = Stock Price - $100 cost - $2 premium paid
- No cap on upside (unlimited profit potential)

Breakeven:
- $100 + $2 premium = $102 per share
- Stock needs to rise $2 to break even

Cost of Insurance:
- You paid $200 premium to protect $10,000 position
- That's 2% cost for 5% protection (not a bad deal)

Scenario Analysis - AAPL at $180, buy $175 put for $2:
```

### Real Example: Protective Put Details

```
Position Details:
- Own 100 AAPL shares at $180
- Buy 1 AAPL $175 put for $2.00 ($200 total)
- Total investment: $18,000 + $200 = $18,200
- Days to expiration: 30 days
- Insurance period: 30 days

Scenario 1: AAPL at $200 on expiration (stock jumps 11%)
- Put expires worthless (not needed)
- Gain on stock: ($200 - $180) × 100 = $2,000
- Minus put premium paid: -$200
- Net profit: $1,800 (9.9% return in 30 days)
- The protection cost you $200 but wasn't needed

Scenario 2: AAPL at $175 on expiration (down to put strike)
- Put expires at-the-money
- Gain on stock: ($175 - $180) × 100 = -$500
- Plus put protection: $5 × 100 = $500 (can exercise)
- Minus put premium: -$200
- Net: -$200 (broke even on stock, lost insurance premium)
- Insurance cost you $200

Scenario 3: AAPL at $160 on expiration (down 11%)
- Put is in-the-money: exercise to sell at $175
- Loss on stock from purchase price: ($160 - $180) × 100 = -$2,000
- Put protection: sell at $175 instead of $160, gaining $1,500
- Net loss on stock movement: -$500
- Minus put premium: -$200
- Total loss: -$700 (-3.8% loss)
- Without put, you'd have lost $2,000 (11%)

Scenario 4: AAPL at $100 on expiration (crash 44%)
- Put protection stops at $175
- Stock crashed to $100
- Put lets you sell at $175: saves you $7,500
- Loss prevented: $100 × 100 = $10,000 losses → $500 loss
- Net after premium: -$700 (-3.8%)
- Without put, you'd have lost $8,000 (-44.4%)
- Put insurance paid for itself many times over
```

### When to Use Protective Puts

**Good Timing:**
- Stock after large gains (wanting to preserve profits)
- Before earnings (protecting from gap risk)
- During market uncertainty (VIX spiking, geopolitical events)
- If stock is at support and could break down
- IV is moderate (not too expensive)

**Avoid When:**
- Stock is in clear downtrend (puts won't help much)
- IV is extremely high (expensive insurance)
- Stock at all-time lows (unlikely to fall further)
- Very short term outlook (time decay hurts buyers)

### Common Mistakes

```
Mistake 1: Buying puts that are too OTM
"I bought the $150 put while stock at $180"
- Very cheap protection ($0.10)
- But only protects against 16.7% drop, not useful
- Buy puts at strikes you actually want to sell at

Mistake 2: Not rolling put protection
"My 30-day put is expiring"
- Insurance expired; buy new put or go uninsured
- Rolling costs money but preserves protection
- Calculate if protection is still needed

Mistake 3: Holding puts through earnings (if very close)
- Puts bought at high IV
- IV crush after earnings can hurt put buyers
- Consider taking profits before earnings if IV high

Mistake 4: Buying puts on positions you doubt
"If I need insurance, why own the stock?"
- Protective puts are for quality stocks you believe in
- Don't use puts to "hedge" a bad stock
- Sell the stock instead if you lack conviction
```

---

## Comparison: Covered Call vs. Protective Put

| Aspect | Covered Call | Protective Put |
|--------|--------------|-----------------|
| **You Own Stock** | Yes | Yes |
| **You Also Buy/Sell** | SELL call | BUY put |
| **Cost** | Receive premium | Pay premium |
| **Upside Capped** | Yes (at strike) | No (unlimited) |
| **Downside Protected** | Partially (by premium) | Yes (fully below strike) |
| **Max Profit** | Premium + (Strike - Cost) | Unlimited |
| **Max Loss** | Stock value - Strike - (Premium) | Strike - Cost - Premium |
| **Sentiment** | Neutral to bullish | Bullish but cautious |
| **Best Used For** | Income generation | Risk management |
| **When Stock Soars** | Lose upside | Keep all gains minus premium |
| **When Stock Crashes** | Lose money (cushioned) | Protected at strike |

---

## Advanced Example: Synthetic Covered Call

A sophisticated trader can create a covered call without owning stock.

```
Synthetic Covered Call = Long 100 shares + Short 1 call
Alternative = Long call + Short 2 calls (ratio)

Example with derivatives only:
- Buy 1 AAPL $175 call for $6
- Sell 2 AAPL $185 calls for $2 each = $4 income
- Net cost: $6 - $4 = $2 debit
- Risk profile similar to owning stock and selling call
- No stock ownership required
- More capital efficient

This is more advanced, but shows how strategies combine
```

---

## Key Takeaways

1. **Covered Call**: Sell income from stock you already own; cap upside to collect premium
2. **Protective Put**: Buy insurance on stock you own; pay premium for downside protection
3. **Covered Call** = income generation (bearish on further upside)
4. **Protective Put** = risk management (cautiously bullish)
5. **Both strategies** involve owning the underlying stock
6. **Neither strategy** is free; tradeoffs exist in every scenario

---

## In the Next Lesson

- Lesson 11.4 introduces the Greeks—the variables that drive option prices
- Understanding Greeks helps you optimize both covered calls and protective puts
- Greeks also form the foundation for more complex strategies

---

## Self-Assessment Questions

1. You own AAPL at $180. You sell the $190 call for $2. If AAPL rises to $200, what's your profit?
2. You own TSLA at $250. You buy the $240 put for $3. If TSLA falls to $200, what's your outcome?
3. Why might an investor prefer a protective put over just selling the stock?
4. When would a covered call strategy cost you upside profits?
5. If you sold a covered call and the stock was called away, what happens next?

