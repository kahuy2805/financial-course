# Lesson 6.2: RSI - Relative Strength Index

[← Back to Chapter 6](README.md) | [Next Lesson: MACD - Moving Average Convergence Divergence →](lesson_6.3_macd.md)

---

## Overview

The Relative Strength Index (RSI) is one of the most popular oscillators used by traders worldwide. Unlike moving averages that show direction, RSI measures momentum and overbought/oversold conditions. Master this indicator and you'll have a powerful tool to identify when prices are about to reverse.

**Time to complete:** 25-30 minutes

---

## Prerequisites

- Completion of Lesson 6.1: Moving Average Strategies
- Understanding of uptrends and downtrends
- Familiarity with basic price momentum concepts

---

## Core Content

### What is RSI?

**RSI (Relative Strength Index)** is a momentum oscillator that measures the speed and change of price movements on a scale of 0 to 100.

**Key Concept:** RSI tells you if a stock is:
- **Overbought** (RSI > 70) - Price has risen too much, too fast → Potential sell signal
- **Oversold** (RSI < 30) - Price has fallen too much, too fast → Potential buy signal
- **Neutral** (RSI 30-70) - Normal momentum levels

**Real-World Analogy:**
RSI is like a speedometer on your car:
- 0-30 = Reversing fast (oversold, buyers may step in)
- 30-70 = Normal speed (neutral zone)
- 70-100 = Going too fast (overbought, collision risk!)

### How RSI Works

**The Basic Calculation:**

RSI is based on comparing "up moves" to "down moves" over a specific period (usually 14 days).

**Simplified Formula:**
```
RSI = 100 - (100 / (1 + RS))

Where RS = Average of UP days ÷ Average of DOWN days
```

**Real Example: Apple Stock - Last 14 Days**

Let's say over 14 days, Apple had:
- **9 days UP** with average gains of $2.50
- **5 days DOWN** with average losses of $1.80

**Calculation:**
- Average Gain = (9 × $2.50) ÷ 14 = $1.607
- Average Loss = (5 × $1.80) ÷ 14 = $0.643
- RS = $1.607 ÷ $0.643 = 2.50
- RSI = 100 - (100 ÷ 3.50) = 71.4

**Interpretation:** RSI of 71.4 = Overbought territory (above 70)

### The RSI Scale Explained

**0-100 Scale:**

| RSI Level | Meaning | Action |
|---|---|---|
| 70-100 | **Overbought** | Potential sell, expect pullback |
| 50-70 | **Strong uptrend** | Momentum still bullish |
| 50 | **Neutral** | No clear direction |
| 30-50 | **Weak uptrend** | Losing momentum |
| 0-30 | **Oversold** | Potential buy, expect bounce |

### The Three Core Strategies

#### Strategy 1: Overbought/Oversold Trading

The most straightforward RSI strategy: Buy oversold, sell overbought.

**Overbought Setup (RSI > 70 - Sell Signal)**

When RSI exceeds 70, the stock has risen very quickly. This often means:
- Buyers are exhausted
- A pullback or reversal is likely
- Traders who bought low want to take profits

**Real Example: Tesla (TSLA) - August 2024**

Scenario: TSLA rallies hard on earnings news
- Price: $290 (up 8% in 2 days)
- RSI: 78 (deeply overbought)
- Signal: SELL or take profits
- Expected outcome: 2-3% pullback in next few days

**What Happened:**
- Price did pull back to $282
- Traders who sold at RSI 78 avoided $8 loss
- Timing: Sold near the local top

**Oversold Setup (RSI < 30 - Buy Signal)**

When RSI falls below 30, the stock has fallen very quickly. This often means:
- Sellers are exhausted
- A bounce or reversal is likely
- Smart money is buying the dip

**Real Example: Microsoft (MSFT) - Intraday Trading**

Scenario: Market-wide sell-off hits MSFT hard
- Price: $420 (down 5% in one day)
- RSI: 22 (oversold)
- Signal: BUY or position for bounce
- Expected outcome: 2-4% bounce in next few days

**What Happened:**
- Price bounced to $440
- Traders who bought at RSI 22 gained 4.8%
- Timing: Bought near the local bottom

**Rules for Overbought/Oversold Trading:**

✓ Wait for RSI to cross 70 (overbought) - don't trade at RSI 75, too much deviation
✓ Look for a reversal candlestick (bearish candle above resistance)
✓ Exit when RSI drops below 70 OR price breaks support
✓ For oversold (RSI < 30), mirror the logic for buys

#### Strategy 2: RSI Divergence

A **divergence** is when RSI and price move in opposite directions. This is a powerful reversal signal.

**Bearish Divergence (Price makes higher high, RSI makes lower high)**

This suggests the uptrend is losing momentum and about to reverse.

**Visual Example:**

```
Price Chart:           RSI Chart:
$190 ←— New High       70% ← Previous high
     ╲                  60% ← NEW lower high (divergence!)
$185 ←— Previous High
     ╲
$180
```

**What This Means:**
- Price reached new high ($190)
- RSI didn't reach a new high (stuck at 60%)
- Fewer buyers are willing to keep pushing
- Reversal likely

**Real Example: Netflix (NFLX) - September 2024**

**Day 1:** Price = $650, RSI = 75 (strong uptrend)
**Day 2:** Price = $655 (new high), RSI = 72 (lower high!)
**Day 3:** Price = $660 (even higher), RSI = 68 (even lower!)

**What Happened:**
- Bearish divergence was clear
- Price reversed hard, dropped to $620 (3% loss)
- Smart traders exited before the reversal

**Bullish Divergence (Price makes lower low, RSI makes higher low)**

This suggests the downtrend is losing momentum and about to reverse.

**Visual Example:**

```
Price Chart:           RSI Chart:
$180                    30% ← NEW higher low (divergence!)
     ╲
$175 ←— New Low         25% ← Previous low
     ╲
$170 ←— Previous Low
```

**What This Means:**
- Price reached new low ($170)
- RSI didn't reach a new low (bounced to 30%)
- Fewer sellers are willing to keep pushing
- Reversal likely

**Real Example: Amazon (AMZN) - February 2024**

**Day 1:** Price = $180, RSI = 18 (strong downtrend)
**Day 2:** Price = $175 (new low), RSI = 22 (higher low!)
**Day 3:** Price = $170 (even lower), RSI = 26 (even higher!)

**What Happened:**
- Bullish divergence was clear
- Price reversed hard, climbed to $195 (5% gain)
- Smart traders entered long before the bounce

#### Strategy 3: RSI Support and Resistance

RSI itself has support and resistance levels that can signal reversals.

**RSI = 50 as Dynamic Support**

When RSI bounces off the 50 level during an uptrend, it signals strength.

**Real Example: Apple in Uptrend**

- Uptrend established (price above all moving averages)
- Price pulls back: RSI falls to 48
- RSI bounces off 50 (doesn't go to 30)
- Signal: Uptrend is healthy, bounce likely
- Action: BUY on the bounce

**Why This Works:**
- RSI 50 = The midpoint between overbought and oversold
- Respecting this level shows trend is strong but not overextended
- Bouncing off 50 = Buyers are stepping in, not letting price fall

**Key Levels to Watch:**

| RSI Level | Significance |
|---|---|
| 70 | Overbought threshold |
| 60 | Strong uptrend midpoint |
| 50 | Major pivot point |
| 40 | Weak downtrend midpoint |
| 30 | Oversold threshold |

### Combining RSI with Moving Averages

The most powerful setup combines RSI with moving averages for confirmation.

**The Complete Setup:**

```
1. Confirm trend with Moving Averages
   → Price above 20, 50, 200 = Uptrend confirmed

2. Check RSI for confirmation
   → RSI > 50 = Confirms uptrend momentum
   → RSI < 30 = Dip is good entry point

3. Enter on bounce
   → Price pulls back to moving average
   → RSI bounces off support (50 or 30)
   → Both indicators confirm buy signal
```

**Real Trading Example: Nvidia (NVDA)**

Setup:
- **Trend:** Uptrend confirmed (price > 20, 50, 200 EMA)
- **Price action:** Pulls back toward 20-day EMA
- **RSI:** Falls to 35 (oversold but not panic)
- **Setup:** PERFECT BUY

Why perfect?
- Moving averages = Trend is UP
- RSI 35 = Oversold enough to bounce but uptrend is intact
- Risk/reward = Clear stop loss below 20-day EMA

### Common RSI Settings

**14-period RSI** (Most popular)
- Best for: Swing trading (3-5 day trades)
- Sensitivity: Standard
- Used by: 80% of traders

**7-period RSI** (Faster)
- Best for: Day trading, intraday
- Sensitivity: Very responsive, more false signals
- Benefit: Earlier entries

**21-period RSI** (Slower)
- Best for: Position trading, longer holds
- Sensitivity: Less noise, fewer signals
- Benefit: Fewer false signals

**Rule of Thumb:** Match RSI period to your timeframe
- Day trading (hourly charts) = 7-period RSI
- Swing trading (daily charts) = 14-period RSI
- Position trading (weekly charts) = 21-period RSI

---

## Common Mistakes to Avoid

### Mistake #1: Trading Overbought/Oversold Without Confirmation

**Problem:** RSI > 70, so you sell. Price continues to 80.

**Solution:** Wait for RSI to TURN DOWN from overbought, not just be overbought.

### Mistake #2: Ignoring the Trend

**Problem:** Shorting oversold RSI in a strong uptrend.

**Solution:** Overbought/oversold works best within established trends.

### Mistake #3: Over-trading Divergences

**Problem:** Every small divergence is a reversal signal? Actually, it's not.

**Solution:** Confirm divergence with price action (candlestick reversal) before trading.

### Mistake #4: Using Too Many RSI Settings

**Problem:** 7, 14, and 21 period RSI all giving conflicting signals.

**Solution:** Stick to ONE RSI period that matches your timeframe.

### Mistake #5: Forgetting That Strong Trends Override RSI

**Problem:** Stock in strong uptrend, RSI 75, so you sell. Stock rallies 20% more.

**Solution:** In strong trends, respect the trend first. RSI overbought in uptrends is normal.

---

## Real-World Application

### RSI in Different Trading Styles

**Day Trader (Multiple trades per day):**
- Uses 7-period RSI on 1-hour chart
- Buys when RSI bounces off 30
- Sells when RSI touches 70
- Closes all positions by end of day

**Swing Trader (3-5 day trades):**
- Uses 14-period RSI on daily chart
- Enters when price pulls back + RSI 30-40
- Exits when RSI divergence confirms
- Holds 3-5 days per trade

**Position Trader (Weeks/months):**
- Uses 21-period RSI on daily/weekly chart
- Uses RSI to time better entry points
- Ignores short-term overbought/oversold
- Focuses on major divergences

### RSI Success Stories

**Case Study: Quarterly Earnings Bounces**

Many stocks drop hard on earnings disappointment, creating oversold RSI. Smart traders:
1. Wait for RSI < 20 (panic selling)
2. Confirm with moving average support
3. Buy the bottom
4. Exit on 50% bounce

**Result:** 4-8% gains in 3-5 days

---

## Practice Exercise

### Exercise 1: Interpret RSI Values

For each RSI reading, identify what it means and what action to consider:

**Your Analysis:**

1. RSI = 72 on a stock in uptrend
   - **Condition:** _____________
   - **Signal:** _____________
   - **Action:** _____________

2. RSI = 28 on a stock in downtrend
   - **Condition:** _____________
   - **Signal:** _____________
   - **Action:** _____________

3. RSI = 52 on a stock in uptrend
   - **Condition:** _____________
   - **Signal:** _____________
   - **Action:** _____________

**Answer Key:**
1. Overbought, Sell signal, Take profits or go short
2. Oversold, Buy signal, Buy the dip or cover shorts
3. Neutral/Strong, Continue trend, Stay in position

### Exercise 2: Identify Divergences

Analyze this price and RSI data:

```
Day 1:  Price = $100, RSI = 50
Day 2:  Price = $105, RSI = 65
Day 3:  Price = $108, RSI = 72
Day 4:  Price = $110, RSI = 68 (lower high than Day 3!)
Day 5:  Price = $112, RSI = 64 (even lower high!)
```

**Questions:**
1. What type of divergence occurred?
2. What does this mean?
3. What action would you take?

**Answer Key:**
1. Bearish divergence (price makes higher highs, RSI makes lower highs)
2. Uptrend is losing momentum, reversal likely
3. Sell, take profits, or get ready to exit

### Exercise 3: Real Chart Analysis

1. Open a charting platform (TradingView, Finviz, etc.)
2. Pick any stock currently in strong uptrend
3. Add 14-period RSI to the chart
4. Answer these questions:
   - Is RSI above or below 50?
   - When was the last overbought reading (RSI > 70)?
   - How did price react after that overbought reading?
   - Is there any divergence visible?

**Report:** Write 3-4 sentences about what RSI tells you about the current momentum.

---

## Key Takeaways

✓ **RSI 0-100** = Momentum scale
✓ **RSI > 70** = Overbought (potential sell)
✓ **RSI < 30** = Oversold (potential buy)
✓ **Divergence** = Price and RSI disagree, reversal coming
✓ **14-period** = Standard setting for swing trading
✓ **Confirm with trends** = Don't fight the trend using RSI alone

---

## Next Steps

**Before moving to Lesson 6.3:**
- [ ] Understand what overbought and oversold mean
- [ ] Recognize the difference between RSI and price trends
- [ ] Spot at least one divergence on a real chart
- [ ] Add RSI to your broker's charting platform
- [ ] Practice identifying potential reversal setups

---

[← Back to Chapter 6](README.md) | [↑ Back to Course Index](../../MASTER_INDEX.md) | [Next Lesson →](lesson_6.3_macd.md)

---

*Lesson 6.2 Complete | Next: Lesson 6.3 - MACD - Moving Average Convergence Divergence*
