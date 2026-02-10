# Lesson 3.5: Risk-Reward Ratio Fundamentals

[← Back to Chapter 3](README.md) | [Previous: Setting Stop Losses](lesson_3.4_stop_losses.md) | [Next Lesson: Diversification →](lesson_3.6_diversification.md)

---

## Overview

In this lesson, you'll learn how to evaluate whether a trade is worth taking before you enter it. The risk-reward ratio is the mathematical tool that professional traders use to accept or reject trades. It's the final filter that determines if a trade meets professional standards. By understanding risk-reward ratios, you'll reject bad trades automatically and only take trades with positive expectancy.

**Time to complete:** 25-30 minutes

---

## Prerequisites

- Completion of Lesson 3.4 (Stop Losses)
- Understanding of position sizing and risk calculations
- Ability to calculate simple ratios
- Understanding of profit targets

---

## Core Content

### What is a Risk-Reward Ratio?

**Definition:**

Risk-Reward Ratio = Amount You're Willing to Lose ÷ Amount You Hope to Gain

Or more formally:

**Risk-Reward Ratio = Stop Loss Distance ÷ Profit Target Distance**

**Example:**

You buy Apple at $150.
- Stop loss: $145 (willing to lose $5)
- Profit target: $160 (hope to make $10)
- Risk-Reward Ratio: $5 ÷ $10 = 1:2 (read as "one to two")

This means for every dollar you risk, you have the opportunity to make 2 dollars.

### Understanding Risk-Reward Notation

Risk-reward ratios are written as **"X:Y"**

**Examples:**

1:1 ratio = For every $1 you risk, you can make $1
- This is break-even (not worth taking)

1:2 ratio = For every $1 you risk, you can make $2
- This is good (professional standard)

1:3 ratio = For every $1 you risk, you can make $3
- This is very good (high-conviction trades only)

2:1 ratio = For every $2 you risk, you can make $1
- This is bad (don't take this)

3:1 ratio = For every $3 you risk, you can make $1
- This is terrible (never take this)

### Why Risk-Reward Matters

Here's the fundamental insight: **You don't need a high win rate if you have good risk-reward ratios.**

#### Case Study: Two Traders with Different Win Rates

**Trader A: High Win Rate, Poor Risk-Reward**

- Win rate: 70% (wins 7 out of 10 trades)
- Risk-Reward: 1:0.5 (risking $100 to make $50)
- 10 trades with this ratio:
  - 7 wins × $50 = $350
  - 3 losses × $100 = -$300
  - **Net: +$50 (barely break-even)**

**Trader B: Low Win Rate, Good Risk-Reward**

- Win rate: 40% (wins 4 out of 10 trades)
- Risk-Reward: 1:2 (risking $100 to make $200)
- 10 trades with this ratio:
  - 4 wins × $200 = $800
  - 6 losses × $100 = -$600
  - **Net: +$200 (200% better than Trader A)**

**This is the power of risk-reward.**

Trader B wins fewer trades but makes more money because each win is significantly bigger than each loss.

### The Minimum Acceptable Risk-Reward Ratio

**Professional Standard: 1:1.5 Minimum**

Most professional traders won't take a trade unless the risk-reward ratio is at least 1:1.5.

**Why?**
- Accounts for transaction costs
- Accounts for slippage
- Provides margin for error

**With 1:1.5 ratio and 50% win rate:**
- 10 trades: 5 wins × 1.5 = 7.5, minus 5 losses × 1 = 5
- Net: +2.5 = +25% (positive expectancy)

**Recommended Minimums by Trader Type:**

| Trader Type | Minimum Ratio | Example | Notes |
|-------------|---------------|---------|-------|
| Beginner | 1:1.5 | Risk $100, Gain $150 | Safety margin needed |
| Intermediate | 1:2.0 | Risk $100, Gain $200 | Professional standard |
| Advanced | 1:2.5 | Risk $100, Gain $250 | Higher conviction |

**Key Principle:** If a trade doesn't meet minimum risk-reward, don't take it.

### Calculating Risk-Reward Ratio

The calculation is simple, but doing it correctly matters.

**Formula:**

```
Risk-Reward Ratio = Stop Loss Distance ÷ Profit Target Distance
```

**Important:** These are PRICES, not percentages.

#### Example 1: Simple Calculation

**Setup:**
- Entry: $100
- Stop Loss: $95
- Profit Target: $110

**Calculation:**
- Risk = $100 - $95 = $5
- Reward = $110 - $100 = $10
- Risk-Reward = $5 ÷ $10 = **1:2**

**Result: This is a good trade** (meets 1:1.5 minimum)

#### Example 2: Unfavorable Ratio

**Setup:**
- Entry: $100
- Stop Loss: $95
- Profit Target: $102

**Calculation:**
- Risk = $100 - $95 = $5
- Reward = $102 - $100 = $2
- Risk-Reward = $5 ÷ $2 = **2.5:1** (or written as 1:0.4)

**Result: This is a bad trade** (doesn't meet minimum)

#### Example 3: Professional Trade

**Setup:**
- Entry: $250
- Stop Loss: $240
- Profit Target: $275

**Calculation:**
- Risk = $250 - $240 = $10
- Reward = $275 - $250 = $25
- Risk-Reward = $10 ÷ $25 = **1:2.5**

**Result: This is a professional-grade trade** (exceeds 1:1.5 minimum)

### Setting Profit Targets

**Profit Target Definition:**

The price level where you plan to take profit (exit the winning trade).

This is equally important as the stop loss.

**Methods for Setting Profit Targets:**

#### Method 1: Technical Resistance Levels

**How It Works:**

Find a price level above your entry where the stock has previously faced resistance.

**Example:**

Stock at $100:
- Previous resistance at $108
- Older resistance at $115
- Entry: $100
- Stop: $95
- Profit target: $108 (next resistance level)
- Risk-Reward: $5 ÷ $8 = 1:1.6 ✓

#### Method 2: Fixed Ratio from Entry

**How It Works:**

Use a percentage or fixed amount above entry.

Common percentages:
- Conservative: +5% to +10% above entry
- Moderate: +10% to +20% above entry
- Aggressive: +20% to +30% above entry

**Example:**

Entry at $100, using +10% profit target:
- Profit target: $110
- Stop: $95 (if using fixed 5% below)
- Risk-Reward: $5 ÷ $10 = 1:2 ✓

#### Method 3: Risk-Reward Reversal

**How It Works:**

You set your stop loss first, then calculate the profit target to achieve a desired risk-reward ratio.

**Example:**

Entry: $100
Stop: $95 (risk = $5)
Desired ratio: 1:2
Profit target: $100 + ($5 × 2) = $110

**This is the most disciplined approach** because you lock in a good ratio before entering.

#### Method 4: Fibonacci Retracement/Extension

**How It Works:**

Use Fibonacci levels as profit targets.

**Example:**

Stock trending up at $100:
- Fibonacci extension at $115 and $130
- Entry: $100
- Stop: $95
- Profit target: $115 (first Fibonacci target)
- Risk-Reward: $5 ÷ $15 = 1:3 ✓

### Risk-Reward Ratio in Different Market Environments

The same trade setup changes risk-reward based on market conditions.

#### Bull Market (Prices Rising)

**Typically:** Easier to find good risk-reward ratios
- Stocks often have resistance far above entry
- Reward targets are reachable

**Example:**
- Entry: $100 in uptrend
- Stop: $95 (support holds)
- Target: $115 (resistance above)
- Ratio: 1:3 (excellent)

#### Bear Market (Prices Falling)

**Typically:** Harder to find good risk-reward ratios
- Resistance is close
- Reward targets are limited

**Example:**
- Entry: $100 attempting a bounce in downtrend
- Stop: $95 (support breaks hard)
- Target: $103 (weak resistance nearby)
- Ratio: 1:0.6 (terrible)

**Lesson:** In bear markets, you take fewer trades but maintain discipline.

#### Consolidating Market (Sideways Price Movement)

**Typically:** Moderate risk-reward ratios possible
- Multiple support/resistance levels nearby
- Can find reasonable targets

**Example:**
- Entry: $100 in consolidation range
- Stop: $97 (just outside range)
- Target: $103 (opposite side of range)
- Ratio: 1:2 (good)

### Expected Value and Risk-Reward

This is where risk-reward connects to long-term profitability.

**Expected Value Formula:**

```
Expected Value = (Win % × Average Win) - (Loss % × Average Loss)
```

**Example with Good Risk-Reward:**

- Win rate: 50% (you win half your trades)
- Average win: $200 (on 1:2 risk-reward with $100 risk)
- Average loss: $100 (your risk per trade)
- Expected value per trade: (0.50 × $200) - (0.50 × $100) = $100 - $50 = **+$50 per trade**

**Over 100 trades:** +$50 × 100 = +$5,000 profit

**Example with Poor Risk-Reward:**

- Win rate: 70% (you win 70% of trades)
- Average win: $50 (on 1:0.5 risk-reward with $100 risk)
- Average loss: $100 (your risk per trade)
- Expected value per trade: (0.70 × $50) - (0.30 × $100) = $35 - $30 = **+$5 per trade**

**Over 100 trades:** +$5 × 100 = +$500 profit

**The Insight:**

With good risk-reward, you don't need a high win rate to be profitable. With poor risk-reward, you need an unrealistically high win rate.

### Common Risk-Reward Scenarios

#### Scenario 1: The "Close Target" Trade

**Setup:**
- Stock at $100
- You see an immediate resistance at $102
- Support at $97
- Risk-Reward: $3 ÷ $2 = 1:0.67 (POOR)

**Should You Take It?**
NO. This trade has terrible risk-reward.

**Better Approach:**
Skip this trade and wait for:
- A pullback to $95 (wider stop, same target)
- Or a breakout beyond $102 (better target)

#### Scenario 2: The "Wide Stop, Good Target" Trade

**Setup:**
- Stock at $100
- Major support at $80 (20 points away)
- Resistance at $130 (30 points away)
- Risk-Reward: $20 ÷ $30 = 1:1.5 (ACCEPTABLE)

**Should You Take It?**
Only if:
- Your account is large enough for 20-point stop
- You're comfortable with position sizing implications

**Position Sizing Reality:**
- Account: $10,000
- Risk: 1% = $100
- Stop distance: $20
- Position size: 5 shares
- Position value: $500

This works, but position is small.

#### Scenario 3: The "Perfect Trade"

**Setup:**
- Stock at $100
- Support at $98 (2 points away - tight stop)
- Resistance at $112 (12 points away - good target)
- Risk-Reward: $2 ÷ $12 = 1:6 (EXCELLENT)

**Should You Take It?**
YES, absolutely.

**Position Sizing Reality:**
- Account: $10,000
- Risk: 1% = $100
- Stop distance: $2
- Position size: 50 shares
- Position value: $5,000

This is an ideal trade - good ratio AND good position size.

### Common Mistakes in Risk-Reward Analysis

#### Mistake 1: Using Unrealistic Profit Targets

**Wrong Approach:**
"Stock is at $100, I'll target $200 (100% gain)."

**Reality:**
Most trades don't move 100%. You're setting a target you won't reach, which ruins your analysis.

**Right Approach:**
Use targets based on:
- Technical resistance levels (realistic)
- Fibonacci extensions (realistic)
- Historical volatility (realistic)
- Not wishful thinking

#### Mistake 2: Ignoring Transaction Costs

**Wrong Approach:**
"Risk $100, target $150. That's 1:1.5"

**Reality:**
After commissions and slippage, actual risk-reward might be 1:1.3 (not good enough).

**Right Approach:**
Subtract commissions from your profit target calculation.

#### Mistake 3: Using Unrealistic Win Rates in Calculations

**Wrong Approach:**
"I'll assume an 80% win rate, so this 1:1 trade is fine."

**Reality:**
Most traders are closer to 50% win rate. Assuming 80% is fantasy.

**Right Approach:**
Plan for 50% win rate as baseline. Anything above that is a bonus.

#### Mistake 4: Not Committing to the Profit Target

**Wrong Approach:**
"My profit target is $110, but if it gets to $105, I might take profit early."

**Reality:**
Inconsistent profit-taking ruins your statistics. You can't measure your actual win rate.

**Right Approach:**
Commit to your planned targets. Take profit at your target price level.

#### Mistake 5: Confusing Risk-Reward with Win Rate

**Wrong Approach:**
"This trade has a 1:2 ratio, so I only need a 50% win rate."

**Reality:**
Risk-reward and win rate are independent. A bad trader can have a 1:2 ratio but a 20% win rate.

**Right Approach:**
Good risk-reward is necessary but not sufficient. You still need decent analysis to pick winners.

---

## Real-World Application

### Your Trade Evaluation Checklist

Before entering ANY trade, evaluate the risk-reward:

**Trade Evaluation Checklist:**

```
Stock: ___________________  Price: $___

ENTRY SETUP:
☐ Entry price: $___
☐ Stop loss price: $___
☐ Stop loss distance: $___

PROFIT TARGET:
☐ Profit target price: $___
☐ Profit target distance: $___

RATIO CALCULATION:
☐ Risk-Reward Ratio: 1:___
☐ Is ratio ≥ 1:1.5? Yes/No
☐ If no, do NOT take this trade

ACCOUNT IMPACT:
☐ Risk amount: $___
☐ Account risk %: ___%
☐ Position size: ___ shares
☐ Position value: $___ (% of account: __%)

FINAL DECISION:
☐ Ratio is acceptable: Yes/No
☐ Position size is acceptable: Yes/No
☐ I'm entering this trade: Yes/No
```

### Example Trade Analysis

**Trade Setup:**

You've identified Microsoft (MSFT) for a potential trade.

Current price: $350
You see technical support at: $340
You see technical resistance at: $370

**Step 1: Determine Entry**

Entry price: $350 (current market)

**Step 2: Determine Stop Loss**

Support is at $340. You'll place stop just below: $339

Stop loss distance: $350 - $339 = $11

**Step 3: Determine Profit Target**

Resistance is at $370. First target is there: $370

Profit target distance: $370 - $350 = $20

**Step 4: Calculate Risk-Reward**

Risk-Reward = $11 ÷ $20 = 1:1.82 ✓

**Evaluation: GOOD** (exceeds 1:1.5 minimum)

**Step 5: Calculate Position Size**

Account: $25,000
Risk: 1% = $250
Position size: $250 ÷ $11 = 22.7 shares (round to 23 shares)
Position value: 23 × $350 = $8,050

Position is 32% of account ✓

**Step 6: Final Decision**

Risk-reward: 1:1.82 (GOOD) ✓
Position size: 32% of account (GOOD) ✓
Entry reason: Clear technicals (GOOD) ✓

**DECISION: ENTER TRADE**

Order to place:
- Buy 23 shares of MSFT at $350 (or limit order at $349.50)
- Place stop loss: Sell 23 at $339
- Place profit target: Sell 23 at $370

### Real Portfolio Example: Multiple Trades

**Your account:** $20,000

**Position 1: Apple**
- Entry: $150, Stop: $145, Target: $165
- Risk: $5, Reward: $15, Ratio: 1:3 ✓
- Risk $100, Position: 20 shares

**Position 2: Microsoft**
- Entry: $300, Stop: $290, Target: $315
- Risk: $10, Reward: $15, Ratio: 1:1.5 ✓
- Risk $100, Position: 10 shares

**Position 3: Google**
- Entry: $140, Stop: $135, Target: $148
- Risk: $5, Reward: $8, Ratio: 1:1.6 ✓
- Risk $100, Position: 20 shares

**Portfolio Analysis:**
- Total risk across 3 trades: $300 (1.5% of account)
- Average ratio: 1:2.03 (professional quality)
- If all three hit profit targets: +$380 gain
- If all three hit stops: -$300 loss
- Acceptable risk profile ✓

---

## Common Mistakes to Avoid

### Mistake #1: Taking Low Risk-Reward Trades

**The Problem:**
"I just want a quick 2% gain on this trade."

**The Reality:**
If you risk $100 to make $20, you need an 83% win rate to be profitable (impossible).

**The Solution:**
No trade with less than 1:1.5 ratio. Period.

### Mistake #2: Using Unrealistic Targets

**The Problem:**
"This stock is at $100, I'll target $200 (a 100% move)."

**The Reality:**
Most trades won't move 100%. You're setting yourself up for lots of losses.

**The Solution:**
Use targets based on technical levels and historical patterns.

### Mistake #3: Not Tracking Your Actual Ratio Outcomes

**The Problem:**
You calculate a 1:2 ratio but you exit early, turning it into a 1:0.5 ratio.

**The Reality:**
You're ruining your trading statistics and can't measure if your approach actually works.

**The Solution:**
Stick to your planned targets. Let winners run. Let losers hit stops.

### Mistake #4: Trying to "Make Back" Poor Ratio Trades with High Win Rate

**The Problem:**
"This trade is 1:0.8, but I have a 70% win rate, so it's fine."

**The Reality:**
You're depending on something unlikely (70% win rate) to justify something unwise (poor ratio).

**The Solution:**
Only take trades with good ratios. Let good win rate be a bonus.

### Mistake #5: Analyzing Risk-Reward After Entry

**The Problem:**
You enter a trade, then look at what your risk-reward ratio was.

**The Reality:**
Analysis after entry doesn't change anything. It's too late.

**The Solution:**
Calculate and analyze risk-reward BEFORE entering. It's part of your entry decision.

---

## Quick Review

**What is Risk-Reward Ratio?**

The relationship between what you're willing to lose and what you hope to make.
- 1:2 = Risk $1, make $2
- 1:3 = Risk $1, make $3

**Minimum Professional Standard:**

1:1.5 ratio (risk $1, make at least $1.50)

**Why It Matters:**

- Good risk-reward requires only 50% win rate for profitability
- Poor risk-reward requires 70%+ win rate to profit (difficult)
- Professional traders prioritize ratio over win rate

**How to Calculate:**

Risk-Reward = Stop Loss Distance ÷ Profit Target Distance

**The Core Principle:**

Reject trades that don't meet your minimum ratio. Don't compromise on this rule.

---

## Practice Exercise

### Exercise 1: Calculate Risk-Reward Ratios

For each trade, calculate the risk-reward ratio:

**Trade 1: Apple**
- Entry: $150
- Stop: $145
- Target: $165
- Risk: $___
- Reward: $___
- Ratio: 1:___
- Accept (≥1:1.5)? Yes/No

**Trade 2: Tesla**
- Entry: $250
- Stop: $240
- Target: $260
- Risk: $___
- Reward: $___
- Ratio: 1:___
- Accept? Yes/No

**Trade 3: Microsoft**
- Entry: $300
- Stop: $290
- Target: $310
- Risk: $___
- Reward: $___
- Ratio: 1:___
- Accept? Yes/No

**Trade 4: Netflix**
- Entry: $400
- Stop: $385
- Target: $420
- Risk: $___
- Reward: $___
- Ratio: 1:___
- Accept? Yes/No

### Exercise 2: Reverse Engineering Profit Targets

Given entry, stop, and desired ratio, calculate the profit target:

**Setup 1:**
- Entry: $100
- Stop: $95 (risk = $5)
- Desired ratio: 1:2
- Profit target: $100 + ($5 × 2) = $_____

**Setup 2:**
- Entry: $200
- Stop: $190 (risk = $10)
- Desired ratio: 1:3
- Profit target: $_____

**Setup 3:**
- Entry: $50
- Stop: $46 (risk = $4)
- Desired ratio: 1:1.5
- Profit target: $_____

### Exercise 3: Expected Value Calculation

Calculate expected value for these scenarios:

**Scenario A: Good Ratio**
- Win rate: 50%
- Average win: $200 (1:2 ratio with $100 risk)
- Average loss: $100
- Expected value: (0.50 × $200) - (0.50 × $100) = $_____
- Per 100 trades: $_____

**Scenario B: Poor Ratio**
- Win rate: 60%
- Average win: $50 (1:0.5 ratio with $100 risk)
- Average loss: $100
- Expected value: (0.60 × $50) - (0.40 × $100) = $_____
- Per 100 trades: $_____

### Exercise 4: Real Trade Evaluation

You have a $15,000 account. You've identified a stock with these characteristics:

- Current price: $120
- Support level: $115
- Resistance level: $135
- You want 1% risk

Calculate and evaluate:
1. Entry: $120
2. Stop loss: $_____ (just below support)
3. Profit target: $_____ (at resistance)
4. Stop distance: $_____
5. Risk amount: $_____ (1% of $15,000)
6. Risk-Reward ratio: 1:_____
7. Position size: _____ shares
8. Would you take this trade? Yes/No (explain)

---

## Next Steps

Congratulations! You now understand risk-reward ratios and how to evaluate trades.

**In the next lesson**, you'll learn:
- Why diversification matters
- How to avoid over-concentration
- Building a balanced portfolio

### Before Moving Forward:
- [ ] Complete all practice exercises
- [ ] Understand that risk-reward is non-negotiable
- [ ] Commit to 1:1.5 minimum ratio
- [ ] Never enter a trade without calculating ratio first
- [ ] Understand expected value mechanics

**Ready to continue?** → [Lesson 3.6: Diversification for Beginners](lesson_3.6_diversification.md)

---

## Additional Resources

**For Deeper Learning** (Optional):

- Research: "Expected Value" in trading books
- Calculate: Expected value for your own past trades (if applicable)
- Study: How professional traders set profit targets
- Practice: Identify resistance levels on real stocks for profit targets
- Reflect: Write down why you sometimes don't hit your profit targets

---

**Remember:** Risk-reward ratio is not negotiable. It's the mathematical foundation of successful trading. Good traders obsess over their ratios because that's where long-term profitability comes from.

---

[← Back to Chapter 3](README.md) | [↑ Back to Course Index](../../MASTER_INDEX.md) | [Next Lesson →](lesson_3.6_diversification.md)

---

*Lesson 3.5 Complete | Next: Lesson 3.6 - Diversification for Beginners*
