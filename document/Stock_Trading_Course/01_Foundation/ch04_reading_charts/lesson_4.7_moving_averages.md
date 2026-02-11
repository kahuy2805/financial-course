# Lesson 4.7: Introduction to Moving Averages - The Smoothing Tool of Technical Analysis

[← Back to Chapter 4](README.md) | [Previous: Chart Patterns](lesson_4.6_chart_patterns.md) | [Next: Chapter Exercises →](exercises.md)

---

## Overview

Moving averages are lines drawn on charts that show the average price over a specific number of days. They filter out daily noise and reveal the true trend. In this lesson, you'll learn how moving averages work, the most popular types, and how to use them to confirm trends and find support.

**Time to complete:** 20-25 minutes

---

## Prerequisites

- Completed Lessons 4.1-4.6 (Charts through Patterns)
- Comfortable reading candlestick charts
- Understand trends and support/resistance
- Access to a charting platform (TradingView, your broker)

---

## Core Content

### What is a Moving Average?

A **moving average** is a line that shows the average price over a certain number of days.

**Simple Definition:**

```
5-day moving average = Average of the last 5 closing prices

Day 1: $100
Day 2: $102
Day 3: $101
Day 4: $103
Day 5: $104

Average = (100+102+101+103+104) ÷ 5 = $102

The line on Day 5 is at $102 (the average)

Next day:
Day 6: $105
New average = (102+101+103+104+105) ÷ 5 = $103

The line moves to $103 (hence "moving" average)
```

### Why Moving Averages Matter

**Main Purpose:** Filter out noise and show the true trend.

**Visual Example:**

```
WITHOUT Moving Average (Noisy):
Price
 110  ▓░░░▓░░░▓░░░▓░░░
 105  ░░░▓░░░▓░░░▓░░░▓  ← Looks random, can't see trend
 100
       Day 1-20

WITH Moving Average (Clean):
Price
 110  ▓▓▓▓░░░░░░░░░░░░
 105  ░░░░▓▓▓▓▓▓▓▓▓░░░  ← Clear uptrend!
 100  ════════════════ ← 20-day MA smooths the noise
       Day 1-20
```

The moving average removes daily noise and shows the true trend.

---

## How Moving Averages Work

### Step-by-Step Example: 10-Day Moving Average

**Daily Prices:**
```
Day 1: $100
Day 2: $101
Day 3: $99
Day 4: $102
Day 5: $103
Day 6: $101
Day 7: $104
Day 8: $105
Day 9: $103
Day 10: $106

MA = (100+101+99+102+103+101+104+105+103+106) ÷ 10 = $102.40

Day 11: $107
(Need to drop Day 1, add Day 11)

New MA = (101+99+102+103+101+104+105+103+106+107) ÷ 10 = $103.10

The MA "moves" to $103.10 (slightly higher)
```

### Visual: How Moving Averages Follow Price

```
Price   Price      Moving
Per Day  Line       Average Line

$110                    ╱──── MA moves up as price stays high
$108    ╱╲╱╱╲          ╱
$106    ╱  ╲          ╱ ← Smoother, clearer trend
$104    ╱  ╲        ╱
$102    ╱ ╱╲ ╲      ╱
$100  ═════════════╱

MA lags behind price slightly,
but shows clearer trend
```

---

## Popular Moving Average Lengths

### Short-Term Moving Averages

#### 5-Day MA (Very Short-Term)

**Use Case:** Intraday traders, scalpers
**What it shows:** Last week's trend
**Lag:** Very little lag
**Noise:** Still quite noisy
**Best for:** Active traders during the day

```
Price
 110  ╱╲
 105  ╱  ╲╱╲  ← 5-day MA (very responsive, wiggly)
 100
```

#### 10-Day MA (Short-Term)

**Use Case:** Day traders, short-term traders
**What it shows:** Last 2 weeks' trend
**Lag:** Small lag
**Noise:** Some noise filtered
**Best for:** Active traders

#### 20-Day MA (Short-Term)

**Use Case:** Traders, swing traders
**What it shows:** Last month's trend (1 month ≈ 20 trading days)
**Lag:** Moderate lag
**Noise:** Good noise filtering
**Best for:** Most swing traders use this

```
Price
 110      ╱────╲
 105      ╱      ╲   ← 20-day MA (cleaner than 5-day)
 100  ────────────
```

### Medium-Term Moving Averages

#### 50-Day MA (Medium-Term)

**Use Case:** Swing traders, position traders
**What it shows:** Last ~2.5 months trend
**Lag:** Moderate to higher lag
**Noise:** Most noise filtered
**Best for:** Position traders, medium-term analysis

#### 100-Day MA (Medium-Term)

**Use Case:** Position traders, investors
**What it shows:** Last ~5 months trend
**Lag:** Higher lag
**Noise:** Very clean
**Best for:** Longer-term trend confirmation

### Long-Term Moving Averages

#### 200-Day MA (Long-Term)

**Use Case:** Investors, position traders
**What it shows:** Year-long trend (200 trading days ≈ 1 year)
**Lag:** Significant lag
**Noise:** Completely filtered
**Best for:** Determining the "main" trend

```
Price   Stock over 1 year:
$200   ╱
$190   ╱    ╲  ← Price moves up and down
$180  ╱╱╱╱╱╱╲╲╱╱╱╱╱╱  (chaotic looking)
$170            ╲
$160  ═════════════════ ← 200-day MA (clearly shows year's trend)
```

---

## Types of Moving Averages

### Simple Moving Average (SMA)

**Calculation:**
Average of last N closing prices, with all prices weighted equally.

**Formula:**
SMA = (Price1 + Price2 + Price3 + ... + PriceN) ÷ N

**Characteristics:**
- Most common type
- Easy to understand
- Fair weighting to all prices
- Slower to react to recent changes

**Best for:** Most traders, beginners

### Exponential Moving Average (EMA)

**Calculation:**
Gives MORE weight to recent prices, LESS weight to older prices.

**Characteristics:**
- Faster to react to price changes
- More responsive than SMA
- Better for fast-moving markets
- Can give more false signals

**Best for:** Active traders wanting faster signals

**Note:** Most platforms default to SMA. For this course, we'll use SMA.

---

## Using Moving Averages to Identify Trends

### Uptrend: Price Above Moving Average

```
Price
 120  ╱───────── Price is above MA
 110  │╱╲╱╲╱╲╱  (uptrend confirmed)
 100  │
  90  ════════════ 20-day MA
       (MA is rising)

Interpretation: Stock is in UPTREND
Trading decision: Look for BUYING opportunities
```

### Downtrend: Price Below Moving Average

```
Price
 120  ════════════ 20-day MA
 110  │           (MA is falling)
 100  │╲╱╲╱╲╱╲╱──
  90  └───────────
       Price is below MA (downtrend confirmed)

Interpretation: Stock is in DOWNTREND
Trading decision: Look for SELLING opportunities or stay out
```

### Sideways/Choppy: Price Crossing Moving Average

```
Price
 110  ────────────
 105  ╱╲╱╲╱╲╱╲╱╲  Price crossing MA repeatedly
 100  ════════════ MA (flat)

Interpretation: Stock is CHOPPY, no clear trend
Trading decision: AVOID (high false signals)
```

---

## Moving Averages as Support and Resistance

### Moving Average as Dynamic Support

In an uptrend, the moving average acts as support (like a rising support line).

```
Price
 120  ╱────── Resistance
 115  ╱╲
 110  ╱  ╱╲
 105  ╱  ╱  ╲ ← Price bounces OFF the MA
 100  ════════════ 20-day MA (acts as support)

When price touches MA, it often bounces up
This acts just like a support level
```

### Moving Average as Dynamic Resistance

In a downtrend, the moving average acts as resistance (like a falling resistance line).

```
Price
 120  ════════════ 20-day MA (acts as resistance)
 115  ╱╲╱╲╱╲╱╲╱╲
 110         ╲
 105          ╲
 100           ╲────── Support

When price bounces up to MA, it gets rejected
This acts just like a resistance level
```

---

## Multiple Moving Averages

Professional traders often use MULTIPLE moving averages to get a complete picture.

### The 20/50/200 System

**Common setup used by professionals:**

```
200-day MA (yellow) = "Main trend"
50-day MA (red) = "Medium trend"
20-day MA (blue) = "Short-term trend"

When all three line up:
- All sloping up = STRONG UPTREND
- All sloping down = STRONG DOWNTREND
- Spread apart = Clear trend
- Tangled together = Choppy, avoid trading
```

### Example: 20/50/200 Alignment

**Strong Uptrend:**
```
Price
$150  ╱        200-day MA (highest)
$145  ╱
$140  ╱ ╱      50-day MA (middle)
$135  ╱ ╱
$130  ╱ ╱ ╱    20-day MA (lowest/most responsive)
$125  ╱ ╱ ╱
       ╱ ╱ ╱

All three MAs sloping UP, all spread apart
= STRONG UPTREND, solid buying opportunity
```

**Choppy/Uncertain:**
```
Price
$110  ╱╲╱╲╱╲╱╲╱╲╱╲
$105  ─────────────  All three MAs tangled together
      (Can't see which is which)

= CHOPPY, avoid trading, wait for clarity
```

---

## Moving Average Crossovers (Advanced)

### Golden Cross (Bullish Signal)

When a SHORT-term MA crosses ABOVE a LONG-term MA.

**Example:**
20-day MA crosses above 200-day MA

```
Price
$150           ╱╱╱ ← 20-day MA
$140         ╱╱ (rises above)
$130  200-day MA ← 200-day MA
       (slower, declining)

This is called a "Golden Cross"
= STRONG BUYING SIGNAL

This often signals: Downtrend ending, uptrend beginning
```

### Death Cross (Bearish Signal)

When a SHORT-term MA crosses BELOW a LONG-term MA.

**Example:**
20-day MA crosses below 200-day MA

```
Price
$150  200-day MA ← 200-day MA
$140         ╲╲  (declining)
$130           ╲╲ ← 20-day MA
               ╲╲ (falls below)

This is called a "Death Cross"
= STRONG SELLING SIGNAL

This often signals: Uptrend ending, downtrend beginning
```

---

## Real-World Application

### Scenario 1: Confirming an Uptrend

**What You See:**
Apple (AAPL) daily chart:
- Price at $150
- 20-day MA at $145 (below price)
- 50-day MA at $140 (below price)
- 200-day MA at $130 (well below price)

**Your Analysis:**
All three MAs below price and properly stacked.

**Your Conclusion:**
STRONG UPTREND. This is a good buying opportunity.

**Your Setup:**
- Buy on dips to the 20-day MA ($145)
- Stop loss: Below 50-day MA ($140)
- Target: Previous resistance $155

### Scenario 2: Detecting Trend Change

**What You Observe:**
Stock had been rising (price above all MAs).

Now you notice:
- Price dips and doesn't bounce from 20-day MA
- Price closes below 20-day MA
- 20-day MA starts to flatten

**Your Interpretation:**
Uptrend might be ending. Caution is needed.

**Your Response:**
- Reduce position size
- Move stop loss up to protect profits
- Watch for 20-day MA to flatten or turn down
- If price breaks below 50-day MA, EXIT the position

### Scenario 3: Using MA as Entry Point

**Your Trading Plan:**
Buy Apple at the 20-day MA during an uptrend.

**Setup:**
- 20-day MA is at $145
- Price is rising, pulling back toward $145
- You set a BUY alert at $145.50

**When Alert Triggers:**
- Price touched 20-day MA
- Expected bounce up from support
- Volume confirms buyers appearing

**Your Action:**
BUY at $145.50
Stop: Below 20-day MA at $144
Target: Previous high at $155

### Scenario 4: Golden Cross Setup

**What Happens:**
Tesla (TSLA) 20-day MA crosses above 200-day MA.

**Your Recognition:**
Golden Cross = bullish signal

**Criteria Check:**
- Was it on higher volume? YES
- Did price close above both MAs? YES
- Were both MAs flat/rising before cross? YES

**Your Action:**
BUY on the golden cross (entry).

**Target:**
Look for previous resistance, usually 2-3 weeks ahead.

**Why This Works:**
Professional traders program in golden cross signals. When cross happens, automatic buying from many programs creates upward move.

---

## Common Mistakes to Avoid

### Mistake #1: Using Too Many Moving Averages

**What Traders Do Wrong:**
"I'll use 5, 10, 15, 20, 50, 100, and 200-day MAs."

**Why It's Wrong:**
Too many lines = visual confusion = hard to trade

**The Right Way:**
Start with 2-3 MAs max (20, 50, 200 are standard)

### Mistake #2: Ignoring the MA Slope

**Reality:** A flat MA shows choppy markets. A steep MA shows strong trend.

Don't just look at price/MA relationship. Look at how steep the MA is sloping.

### Mistake #3: Trading Choppy Markets Based on MA

**What Traders Do Wrong:**
"Price bounced off the 20-day MA three times today, so it's a great signal."

**Why It's Wrong:**
In choppy markets, MAs give many false signals. Skip trading when MAs are tangled.

**The Right Way:**
Only trade MA bounces when all MAs are clearly aligned and the trend is obvious.

### Mistake #4: Over-Relying on Moving Averages Alone

**Reality:** MAs are just one tool. Use them with:
- Support/resistance levels
- Chart patterns
- Volume confirmation
- Trend lines

MAs alone = incomplete picture.

### Mistake #5: Not Adjusting MA for Timeframe

**Reality:** On a 1-minute chart, use 10-20 period MA. On daily, use 20/50/200.

Don't blindly use 200-period MA on a 5-minute chart.

---

## Quick Review

**Moving Averages Fundamentals:**

**What They Are:**
- Line showing average closing price over N days
- Filters out noise, reveals true trend

**Popular Types:**
- SMA (Simple, most common)
- EMA (Exponential, more responsive)

**Popular Lengths:**
- 20-day: Short-term trend (month)
- 50-day: Medium-term trend (2.5 months)
- 200-day: Long-term trend (year)

**Reading MAs:**
- Price above MA = Uptrend (buy signals)
- Price below MA = Downtrend (sell signals)
- MAs tangled = Choppy (avoid trading)

**MA as Support:**
- In uptrends: MA acts as support (bounces)
- In downtrends: MA acts as resistance (bounces down)

**Multiple MAs:**
- All aligned and spread = Clear trend
- All tangled together = Choppy/uncertain

**Golden/Death Crosses:**
- Golden Cross (short MA ↑ above long MA) = Buy signal
- Death Cross (short MA ↓ below long MA) = Sell signal

**Key Principle:**
Moving averages show "the big picture." They filter out daily noise and reveal whether stock is truly in uptrend or downtrend.

---

## Practice Exercise

### Exercise 1: Adding Moving Averages to Your Chart

1. Go to TradingView or your charting platform
2. Add a 20-day SMA to a daily chart
3. Add a 50-day SMA
4. Add a 200-day SMA
5. Observe how they line up on your favorite stock

### Exercise 2: Identifying Trend with MAs

Look at 5 different stocks. For each:

1. Is price above or below the 20-day MA?
2. Is price above or below the 200-day MA?
3. Are the MAs aligned or tangled?
4. What is the trend: Up, down, or choppy?

### Exercise 3: Finding MA Support/Resistance Bounces

Look at a daily chart where price bounces from the 20-day MA.

1. How many times did price bounce from this MA?
2. Was each bounce on higher volume?
3. Is this a reliable support level?
4. Would you buy at this MA? (Explain)

### Exercise 4: Golden/Death Cross Research

Research a stock that had a golden or death cross in the past.

1. When did the cross happen?
2. What happened to price after?
3. Did it work or fail?
4. What was the % move?

### Exercise 5: MA in Different Timeframes

Pick one stock. Look at:

1. 1-hour chart: Where are the MAs?
2. 4-hour chart: Where are the MAs?
3. Daily chart: Where are the MAs?
4. Do all timeframes show the same trend direction?

---

## Next Steps

Congratulations! You've completed all 7 lessons on reading stock charts and technical analysis basics.

**In the final section**, you'll practice:
- Chart reading exercises
- Pattern recognition challenges
- Multi-tool analysis combining everything learned

### Before Moving Forward:
- [ ] Understand what moving averages are
- [ ] Know the 3 most common MA lengths (20/50/200)
- [ ] Understand MA as support/resistance
- [ ] Know what golden cross and death cross mean
- [ ] Can read MAs on real charts

**Ready for the exercises?** → [Chapter 4 Exercises: Chart Reading Practice](exercises.md)

---

## Additional Resources

**For Deeper Learning** (Optional):
- TradingView - Add and experiment with different MA periods
- Practice: Find 10 examples of MA support bounces
- Golden Cross: Research historical golden crosses on major indices
- Trading: Many strategies are built on MA crossovers

---

**Remember:** Moving averages are like glasses for stock charts. Without them, the chart looks chaotic and noisy. With them, the true trend becomes crystal clear. They're one of the most important tools in technical analysis.

---

[← Back to Chapter 4](README.md) | [↑ Back to Course Index](../../MASTER_INDEX.md) | [Next Section →](exercises.md)

---

*Lesson 4.7 Complete | Next: Chapter 4 Exercises*
