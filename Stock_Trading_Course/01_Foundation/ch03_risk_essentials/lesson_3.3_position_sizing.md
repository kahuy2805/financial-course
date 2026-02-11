# Lesson 3.3: Position Sizing Basics - The 1-2% Rule in Practice

[← Back to Chapter 3](README.md) | [Previous: The Golden Rule](lesson_3.2_golden_rule.md) | [Next Lesson: Setting Stop Losses →](lesson_3.4_stop_losses.md)

---

## Overview

In this lesson, you'll master the practical application of position sizing. We'll move beyond theory and show you exactly how to determine how many shares to buy using the 1-2% rule. You'll learn advanced techniques for different market conditions and understand how professional traders scale positions. By the end, position sizing will become automatic, and you'll never be confused about "how many shares to buy" again.

**Time to complete:** 25-30 minutes

---

## Prerequisites

- Completion of Lesson 3.2 (The Golden Rule)
- Understanding of the 1-2% risk concept
- Basic arithmetic or calculator access
- Access to stock prices

---

## Core Content

### The Three Components of Position Sizing

Every trade has three variables that determine position size:

1. **Account Size** (how much money you have to trade)
2. **Risk Per Trade** (1-2% of your account)
3. **Stop Loss Distance** (entry price - stop loss price)

Only the third variable changes between trades. The first two are fixed rules.

**Formula:**
```
Position Size = (Account Size × Risk %) ÷ Stop Loss Distance
```

Let's break this down in detail.

### Step 1: Determine Your Account Size

This is the total equity in your trading account.

**Important Distinction:**
- Don't use your entire net worth
- Don't use money you need for bills, emergencies, or other purposes
- Only count capital you can afford to lose entirely without life disruption

**Examples for different traders:**

| Trader | Life Situation | Trading Account |
|--------|----------------|-----------------|
| Sarah | Employed, $50K saved | $10,000 (20% of savings) |
| Marcus | Married with kids | $15,000 (dedicated trading capital) |
| Jasmine | Post-college, no dependents | $25,000 (savings surplus) |
| David | Near retirement | $5,000 (small speculation portion) |

**Your account size for this lesson:**
- Write down your actual trading account balance: $_________

### Step 2: Determine Risk Per Trade

This is either 1% or 2% of your account, calculated in dollars.

**1% Risk (Conservative, Recommended for Beginners):**
```
Risk $ = Account Size × 0.01
```

**2% Risk (Moderate, For Slightly More Aggressive Traders):**
```
Risk $ = Account Size × 0.02
```

#### Examples:

**Account: $10,000**
- 1% risk: $10,000 × 0.01 = **$100 per trade**
- 2% risk: $10,000 × 0.02 = **$200 per trade**

**Account: $15,000**
- 1% risk: $15,000 × 0.01 = **$150 per trade**
- 2% risk: $15,000 × 0.02 = **$300 per trade**

**Account: $25,000**
- 1% risk: $25,000 × 0.01 = **$250 per trade**
- 2% risk: $25,000 × 0.02 = **$500 per trade**

**Your risk amount:**
- If using 1%: $_________
- If using 2%: $_________

### Step 3: Determine Stop Loss Distance

This is where entry price meets stop loss price.

The stop loss distance depends on:
1. **Technical support/resistance levels** (where price naturally bounces)
2. **Volatility** (higher volatility = wider stops)
3. **Time frame** (longer timeframes = wider stops)
4. **Your skill level** (beginners should use wider stops)

#### Stop Loss Distance Examples:

**Tight Stop Loss ($2-3 distance):**
- Used for: Intraday trades, volatile positions, tight support
- Risk per share: $2-3
- Good for: High-frequency traders, tight risk control

**Medium Stop Loss ($5-10 distance):**
- Used for: Day trades, swing trades, normal volatility stocks
- Risk per share: $5-10
- Good for: Most traders, balanced approach

**Wide Stop Loss ($10-20+ distance):**
- Used for: Long-term positions, high-volatility stocks, support far below
- Risk per share: $10-20+
- Good for: Position traders, long-term investors

**How to identify stop loss distance:**
1. Look at technical support (where the stock previously bounced)
2. Look at moving averages (200-day MA is often support)
3. Look at percentage pullback (20% from recent high is common)
4. Add a little buffer (if support is at $95, put stop at $94)

### The Position Sizing Formula in Action

Now let's put all three components together.

**Formula:**
```
Shares to Buy = Risk $ ÷ (Entry Price - Stop Loss Price)
```

#### Real Example 1: Conservative Trader

**Your Setup:**
- Account: $15,000
- Risk: 1% = $150
- Stock: Microsoft (MSFT)
- Entry price: $400
- Stop loss: $390 (technical support)
- Stop distance: $10

**Calculation:**
Shares = $150 ÷ ($400 - $390)
Shares = $150 ÷ $10
Shares = **15 shares**

**Verification:**
- 15 shares × $400 = $6,000 position (40% of account)
- If stops at $390: lose $150 = 1% of account ✓
- Position size is reasonable ✓

#### Real Example 2: Moderate Trader

**Your Setup:**
- Account: $20,000
- Risk: 2% = $400
- Stock: Apple (AAPL)
- Entry price: $180
- Stop loss: $170 (technical support level)
- Stop distance: $10

**Calculation:**
Shares = $400 ÷ ($180 - $170)
Shares = $400 ÷ $10
Shares = **40 shares**

**Verification:**
- 40 shares × $180 = $7,200 position (36% of account)
- If stops at $170: lose $400 = 2% of account ✓
- Position size is reasonable ✓

#### Real Example 3: Tight Stop, Small Position

**Your Setup:**
- Account: $25,000
- Risk: 1% = $250
- Stock: Tesla (TSLA)
- Entry price: $250
- Stop loss: $248 (very tight, within technical range)
- Stop distance: $2

**Calculation:**
Shares = $250 ÷ ($250 - $248)
Shares = $250 ÷ $2
Shares = **125 shares**

**Verification:**
- 125 shares × $250 = $31,250 position (125% of account)
- **This violates position limits!** ✓

**When this happens:** This trade doesn't work at this entry/stop combination. You need either:
1. A wider stop loss, OR
2. A lower entry price, OR
3. Skip the trade

This is a feature of the 1-2% rule: it prevents over-leveraging automatically.

### Advanced Topic: Adjusting for Volatility

The same stock behaves differently in different conditions.

#### High Volatility Example

**Stock: Bitcoin-related ETF (GBTC)**
- Very volatile, moves $5-15 per day
- Historical volatility: 40%+
- Proper stop loss: $20-30+ below entry
- Result: Fewer shares per trade
- Risk management: Very tight since position is smaller

**Position Sizing Impact:**
- Entry: $100
- Stop: $70
- Distance: $30
- $250 risk ÷ $30 = 8.3 shares (small position)

#### Low Volatility Example

**Stock: Utility company (XYZ utility)**
- Stable, moves $1-3 per day
- Historical volatility: 8-10%
- Proper stop loss: $3-5 below entry
- Result: More shares per trade
- Risk management: Can afford larger position

**Position Sizing Impact:**
- Entry: $60
- Stop: $55
- Distance: $5
- $250 risk ÷ $5 = 50 shares (larger position)

**The Key Insight:**
The volatility adjustment happens automatically through your stop loss placement. You don't consciously adjust - you just let the formula work.

### Position Sizing with Different Account Sizes

The same stock with different account sizes creates different position sizes.

**Example: All traders buying Apple at $180, stop at $170**

| Account | Risk % | Risk $ | Shares | Position Value | % of Account |
|---------|--------|--------|--------|----------------|--------------|
| $5,000 | 1% | $50 | 5 | $900 | 18% |
| $10,000 | 1% | $100 | 10 | $1,800 | 18% |
| $20,000 | 1% | $200 | 20 | $3,600 | 18% |
| $50,000 | 1% | $500 | 50 | $9,000 | 18% |

**Notice:** Every trader risks the same percentage of their account (18%) and loses the same amount ($100, $200, $500) in absolute dollars if the trade fails.

The formula automatically scales positions based on account size.

### The Practical Workflow

Here's exactly how professional traders use this in practice:

**Step 1: Scan Stocks**
"Apple looks good. Support at $170, current price $180."

**Step 2: Set Stop Loss**
"I'll use 1% risk. Stop loss will be at $170."

**Step 3: Calculate Position Size**
"Account is $20,000. 1% risk = $200. Stop distance is $10. $200 ÷ $10 = 20 shares."

**Step 4: Check Reasonableness**
"20 shares × $180 = $3,600. That's 18% of my account. Reasonable."

**Step 5: Place Trade**
Order: Buy 20 shares at market or limit price
Stop Loss: Set at $170
Take Profit: Optional (covered in future lessons)

**This entire process takes 30-60 seconds once you know the formula.**

### Position Sizing Across Different Markets

The formula works for any market, but context changes.

#### Stocks (Most Common)

**Example: Microsoft at $400**
- Stop at $395
- 1% risk on $20,000 = $200
- Shares = $200 ÷ $5 = 40 shares
- Position = $16,000 (80% of account)

#### ETFs (Less Volatile)

**Example: S&P 500 ETF (SPY) at $450**
- Stop at $447
- 1% risk on $20,000 = $200
- Shares = $200 ÷ $3 = 66 shares
- Position = $29,700 (149% of account)
- **This doesn't work unless you can use margin**

**Solution:** Accept fewer shares or pass on the trade
- Use 70% of risk: $140 ÷ $3 = 47 shares
- Position = $21,150 (106% - still over)

Sometimes the formula tells you a trade isn't right for your account size.

#### Fractional Shares

Many brokers now allow fractional shares (buying 10.5 shares instead of 10).

**Benefits:**
- Perfect position sizing execution
- No "rounding errors"
- Better capital efficiency

**Example with Fractional Shares:**
- $200 risk ÷ $3 = 66.67 shares
- Position = $30,000.50
- More precise than rounding to 67

---

## Real-World Application

### Your Position Sizing Checklist

Before entering ANY trade, use this checklist:

**Trade Setup Checklist:**

- [ ] Have I identified a clear stop loss level? (Yes/No)
- [ ] Is this based on technical support, not just a random guess?
- [ ] What is my account size right now?
- [ ] Am I using 1% or 2% risk? (Be consistent)
- [ ] What is my exact risk in dollars? $_________
- [ ] What is the distance from entry to stop? $_________
- [ ] Have I calculated position size correctly? Shares = Risk ÷ Distance
- [ ] Result: _________ shares
- [ ] Position value: _________ (shares × entry price)
- [ ] Is this less than 50% of my account? (For safety)
- [ ] Have I set a stop loss order in the system?
- [ ] Am I comfortable with losing this amount? (Emotionally)

**If you can't check every box, don't take the trade.**

### Example Walkthrough: Your First Real Trade

**Scenario:**
You have a $15,000 account. You've identified a good entry in Apple (AAPL).

**Your Observation:**
- Current price: $150
- Technical support: $145
- You want to use 1% risk

**Your Calculation:**
1. Account: $15,000
2. 1% risk: $15,000 × 0.01 = $150
3. Stop distance: $150 - $145 = $5
4. Position size: $150 ÷ $5 = 30 shares
5. Position value: 30 × $150 = $4,500
6. Percentage of account: $4,500 ÷ $15,000 = 30% ✓

**Your Trade Execution:**
- Order: "Buy 30 shares of AAPL at market"
- Stop Loss: "Sell 30 shares AAPL if price hits $145"
- Profit Target: Optional (we'll cover this later)

**Your Risk Management:**
- Max loss if stopped: $150 = 1% of account
- If you lose 10 in a row: $1,500 loss = 10% of account (survivable)
- Account still has $13,500 to continue trading

**The Key Point:**
Every single trade follows this mechanical process. No emotion. No deviation. This is how professionals do it.

### Common Scenario: "The Stock I Want Doesn't Fit"

**Situation:**
You want to buy Tesla (TSLA). Current price $250. The technical stop loss would be at $245 (distance $5).

$250 ÷ $5 = 50 shares × $250 = $12,500 position

But your account is only $15,000. This is 83% of your account in one position.

**Your Options:**

1. **Accept the smaller position (if you can afford it)**
   - Use 0.5% risk instead of 1%: $75 ÷ $5 = 15 shares
   - Position: $3,750 (25% of account)
   - Max loss: $75

2. **Widen your mental stop loss**
   - Stop at $240 instead (distance $10)
   - $150 ÷ $10 = 15 shares
   - Position: $3,750 (25% of account)
   - But this violates your technical analysis

3. **Find a different entry point**
   - Wait for a better technical entry
   - Maybe at $240 with stop at $235
   - Then: $150 ÷ $5 = 30 shares × $240 = $7,200

4. **Skip the trade**
   - Wait for a better opportunity
   - Not every trade is a good trade for your account size

**Professional traders skip trades constantly.** It's not a failure - it's discipline.

### Managing Multiple Positions

As you improve, you'll hold multiple positions. Position sizing helps here too.

**Example Portfolio:**

Your account: $20,000

**Position 1: Apple**
- Buy 40 shares at $150, stop at $145
- Risk: 1% = $200
- Position value: $6,000 (30% of account)

**Position 2: Microsoft**
- Buy 20 shares at $200, stop at $195
- Risk: 1% = $200
- Position value: $4,000 (20% of account)

**Position 3: Google**
- Buy 15 shares at $140, stop at $135
- Risk: 1% = $200
- Position value: $2,100 (10.5% of account)

**Your Portfolio Risk:**
- Total position value: $12,100 (60.5% of account) ✓
- Total risk: $600 (3%)
- Maximum loss if all stop: $600 = 3% of account
- This is healthy diversification

This way, even if all three trades hit their stops, you lose only 3% of your account and can continue.

---

## Common Mistakes to Avoid

### Mistake #1: Using "Maximum Position Size" Instead of Following 1-2% Rule

**What Traders Do Wrong:**
"I can fit 100 shares at $200, so that's $20,000. I'll buy that."

**Why It's Wrong:**
You're not accounting for risk. If your stop is $20 away, that's a 10% position loss.

**The Right Way:**
Calculate backwards from 1-2% risk. Let position size emerge from the formula.

### Mistake #2: Ignoring Volatility When Setting Stop Loss

**What Traders Do Wrong:**
"Apple is at $150. I'll put my stop at $145 because that's -3.3%."

**Why It's Wrong:**
You haven't looked at technical support or volatility. Your stop might be in the middle of normal trading noise.

**The Right Way:**
Base stops on technical levels and volatility, THEN calculate position size from the result.

### Mistake #3: Calculating Position Size Incorrectly

**What Traders Do Wrong:**
"I want to risk $200, stock is at $150, so I'll buy $200 worth = 1.33 shares"

**Why It's Wrong:**
This is backwards. You're dividing risk by price, not risk by stop distance.

**The Right Way:**
Position size = Risk $ ÷ Stop Distance (in dollars per share)

### Mistake #4: Changing Risk Percentage Between Trades

**What Traders Do Wrong:**
"This trade looks risky, so I'll use 0.5%. That trade looks safe, so I'll use 3%."

**Why It's Wrong:**
Inconsistency ruins your statistics. You can't assess your true win rate.

**The Right Way:**
Choose 1% OR 2% and use the same percentage for all trades (at least for your first 50+ trades).

### Mistake #5: Not Accounting for Commissions

**What Traders Do Wrong:**
Calculate position to exactly risk $200, ignoring commissions.

**Why It's Wrong:**
If you pay $5-10 in commissions, your actual risk is $205-210.

**The Right Way:**
Add $5-15 to your mental risk calculation for small account traders.

---

## Quick Review

**The Position Sizing Formula:**
```
Position Size (Shares) = (Account × Risk %) ÷ (Entry - Stop)
```

**Three Essential Components:**
1. Account size (fixed for all trades)
2. Risk % (fixed at 1% or 2%)
3. Stop distance (changes each trade based on technicals)

**The Outcome:**
- Mathematically correct position sizing
- Automatic leverage control
- Risk-based position sizing (not capital-based)
- Consistency across trades
- Sustainable, repeatable results

**In Practice:**
1. Set stop loss based on technicals (not arbitrary)
2. Calculate risk $ (account × 1%)
3. Divide by stop distance to get shares
4. Verify position is reasonable (typically 10-50% of account)
5. Place trade with stop loss

---

## Practice Exercise

### Exercise 1: Position Sizing Calculations

For each scenario, calculate the position size. Your account is $20,000 and you're using 1% risk.

**Trade 1: Apple (AAPL)**
- Entry: $150
- Stop: $145
- Stop distance: $_____
- Risk amount: $_____
- Position size: _____ shares
- Position value: $_____
- % of account: _____%

**Trade 2: Tesla (TSLA)**
- Entry: $250
- Stop: $240
- Stop distance: $_____
- Risk amount: $_____
- Position size: _____ shares
- Position value: $_____
- % of account: _____%

**Trade 3: Microsoft (MSFT)**
- Entry: $300
- Stop: $285
- Stop distance: $_____
- Risk amount: $_____
- Position size: _____ shares
- Position value: $_____
- % of account: _____%

**Trade 4: Netflix (NFLX)**
- Entry: $400
- Stop: $390
- Stop distance: $_____
- Risk amount: $_____
- Position size: _____ shares
- Position value: $_____
- % of account: _____%

### Exercise 2: Different Account Sizes

Same trades as above, but different account. Use 1% risk.

Your account: $10,000

Recalculate position sizes for Trades 1-4 above. How do the shares change?

### Exercise 3: The "Doesn't Fit" Scenario

You want to buy a stock at $500 with a stop at $480 (distance $20).
Your account is $15,000 and you want 1% risk.

1. Calculate your risk amount: $_____
2. Calculate position size: _____ shares
3. Calculate position value: $_____
4. Calculate % of account: _____%
5. Is this reasonable (under 50%)? Yes/No
6. If not, what would you do differently?

### Exercise 4: Building a Multi-Position Portfolio

You have a $25,000 account. You're about to hold 3 positions simultaneously:

**Position A: Stock XYZ**
- Entry: $100, Stop: $95
- Stop distance: $____
- Risk: $250 (1% = $250)
- Shares: _____ (Shares = $250 ÷ $5)

**Position B: Stock ABC**
- Entry: $50, Stop: $48
- Stop distance: $____
- Risk: $250
- Shares: _____

**Position C: Stock DEF**
- Entry: $200, Stop: $190
- Stop distance: $____
- Risk: $250
- Shares: _____

Calculate total position value and total % of account used.

---

## Next Steps

Congratulations! You now understand how to size positions correctly.

**In the next lesson**, you'll learn:
- Where exactly to place stop losses
- How to identify technical support and resistance
- Advanced stop loss strategies

### Before Moving Forward:
- [ ] Complete all practice exercises
- [ ] Understand the position sizing formula
- [ ] Practice calculating position size quickly
- [ ] Commit to letting the formula determine position size
- [ ] Never override the formula based on emotion

**Ready to continue?** → [Lesson 3.4: Setting Stop Losses](lesson_3.4_stop_losses.md)

---

## Additional Resources

**For Deeper Learning** (Optional):

- Research: How professional traders at hedge funds size positions
- Practice: Use a position sizing calculator (many brokers provide these)
- Drill: Calculate position sizes for 10 hypothetical trades daily
- Reflect: Write down why position sizing matters psychologically

---

**Remember:** The position sizing formula removes emotion from your trades. You don't decide how big a position "feels right" - the math decides. This is why it works.

---

[← Back to Chapter 3](README.md) | [↑ Back to Course Index](../../MASTER_INDEX.md) | [Next Lesson →](lesson_3.4_stop_losses.md)

---

*Lesson 3.3 Complete | Next: Lesson 3.4 - Setting Stop Losses*
