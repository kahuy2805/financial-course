# Case Study 04: Earnings Play That Failed - Why Expected Moves Don't Happen

## Executive Summary

A seemingly perfect earnings play setup fails catastrophically when implied volatility collapses and the stock gaps down 22% despite beating earnings. This case study examines why earnings trades are dangerous, why volatility expectations fail, and how proper stop losses would have contained the damage.

**Duration**: January 20 - February 2, 2024
**Entry Price**: $78.50
**Exit Price**: $61.20
**Loss**: -22.0% in 10 trading days
**Mistake**: No stop loss, holding through earnings
**Lesson**: IV crush and expected moves are not guaranteed

---

## The Setup: A Seemingly Perfect Earnings Play

### Stock: CrowdStrike Holdings (CRWD)

**Company Profile:**
- Cybersecurity software company
- Rapid growth: 30%+ annual growth rate
- Stock up 80% year-to-date
- Earnings report: February 1, 2024 after market close

**Why It Looked Like a Perfect Setup:**

Trader Profile: Angela Rodriguez
- Experience: 2 years (still relatively new)
- Account: $50,000
- Style: Options and short-term trades
- Mistake: Overconfidence in thesis

**The Research Angela Did:**

1. **Analyst Expectations:**
   - EPS guidance: $0.67 (consensus)
   - Revenue guidance: $730M (consensus)
   - Company has beat last 8 quarters in a row

2. **Technical Setup:**
   - Stock near all-time high at $78.50
   - RSI at 68 (strong but not overbought)
   - Support at $75

3. **Options Volatility Analysis:**
   - IV Rank: 78% (implied volatility high compared to historical)
   - Expected move: ±$7.85 (10% move expected)
   - Straddle cost: $8.50 (expecting move bigger than this)

4. **Conviction Level:**
   - "This company crushes earnings every time"
   - "Beat last 8 quarters"
   - "Stock has more room to run"
   - "IV is high, but company delivers"

### Angela's Trade Setup

**The Thesis:**
> "CRWD has beaten 8 quarters in a row. Stock is near highs but momentum is strong. IV is elevated at 78%, pricing in ~10% move. If they beat again (very likely), stock will gap up 15%+. The 10% implied move is too conservative."

**Angela's Trade:**
```
Date: January 30, 2024 (2 days before earnings)
Entry: Buy 640 shares at $78.50
Cost: $50,240 (using 100% of available capital)
Plan: Hold through earnings, expect 15% upside gap
Target: $90+ (13% gain)
Stop Loss: "I'll set one if it drops below $75"
Risk: "The company beats every quarter"
```

**The Options Context (She also bought calls):**
```
Options Position (separate from stock):
- Bought 5 Call contracts (500 shares)
- Strike: $80
- Expiration: Feb 2 (4 days after earnings, next week)
- Premium paid: $3.50 × 500 = $1,750
- Breakeven: $83.50
- Max profit: Unlimited

Total capital at risk: $50,240 + $1,750 = $51,990 (more than account)
Leverage: Using margin for the calls, overleveraged
```

---

## The Earnings Event: February 1, 2024

### The Numbers: A Solid Beat

**After Market Close (4:05 PM):**

Earnings announcement:
- EPS: $0.72 (vs. expected $0.67) → +7.5% beat
- Revenue: $747M (vs. expected $730M) → +2.3% beat
- Forward guidance: Raised revenue guidance 8%
- Customer metrics: Excellent (churn down, NRR up)

**Angela's Reaction (4:15 PM):**
> "Perfect! They beat on both numbers. Guidance is raised. This is exactly what I expected. Stock should gap up 15-20% tomorrow morning. I might sell half at the open to lock in profits."

### After-Hours Trading: The Problem

**After-hours session (4:30 PM - 8:00 PM):**

Instead of gapping up, something unexpected happens:

```
Time        Price       Volume      Event
4:15 PM     $78.50      Normal      Just after earnings
4:35 PM     $76.80      2M shares   Starting to sell
5:00 PM     $75.20      3M shares   More sellers emerge
5:30 PM     $72.80      4M shares   Heavy selling pressure
6:00 PM     $70.50      5M shares   Cascade selling
6:30 PM     $68.20      6M shares   Fear setting in
7:00 PM     $66.00      7M shares   Capitulation selling
8:00 PM     $64.90      9M shares   Session close
```

**Angela's After-Hours Horror:**

She's watching in real-time:
> "Why is it selling off? They beat earnings! The guidance is up! This doesn't make sense. It's down 15% after-hours. Should I sell? But maybe this is just after-hours weakness and it bounces at the open?

> I'm down $8,960 already (on stock) + $1,750 (calls are worthless now). I'm -$10,710 in 90 minutes."

### The Gap-Down Open: February 2

**February 2, 2024 - Market Open:**

```
Pre-market:    $64.90 (from after-hours)
Official open: $61.20 (16-minute halt, then opens lower)
Gap from prev close: -22% ($78.50 → $61.20)
Volume at open: 50M shares
```

**Angela checks her account:**
```
Stock position: 640 × $61.20 = $39,168
Cost: $50,240
Loss: -$11,072 (-22%)

Call options: Now worthless (stock below strike $80)
Loss: -$1,750

Total loss: -$12,822 in overnight (first half of trading day)
Percentage: -25% of her $50,000 account
```

**Angela's Thoughts (9:45 AM, market open):**
> "This is a nightmare. The stock beat earnings. The guidance is up. Why is it down 22%? I can't hold this. I need to sell."

She panic-sells at the open:
```
Sells: 640 shares
Price: $61.20
Revenue: $39,168
Realized loss: -$11,072 (-22%)
```

---

## What Went Wrong: The Root Cause Analysis

### Factor 1: Implied Volatility Crush

**The Options Volatility Collapse:**

Before earnings:
```
IV Rank (CRWD)     78% (very high, pricing in big move)
Expected move      ±10% based on straddle pricing
Straddle cost      $8.50
This suggested    13-15% move likely
```

After earnings announcement:
```
IV Rank drops to    12% (collapsed)
IV decreased by     85%
Straddle value      $2.10 (down 75%)
Expected move now   ±2.5%
```

**The Math:**
When a stock beats earnings but IV collapses, the realized move can be smaller than the implied move.

Angela bought at 78% IV rank, expecting a 15%+ move. The market implied 10% (±$7.85). When that didn't happen, the IV crush destroyed the premium she'd paid.

This is the opposite of what "beating earnings" should mean, but here's why it happened:

### Factor 2: The IV Crush Effect (The Real Villain)

**What is IV Crush?**

Implied Volatility measures expected future volatility. Before earnings:
- CRWD IV: 78% annual volatility (very high)
- This prices in ~10% move

After earnings announcement:
- IV drops to 12% annual volatility
- This happens regardless of earnings result
- It happens because the UNCERTAIN event (earnings) is now CERTAIN (announced)

**The Formula:**
```
Stock price move: +2% (from $78.50 to $80 would be a 2% gain)
Implied move: ±10%
Option value at earnings release = combination of:
  - Stock move: +2% is minimal
  - IV crush: Reduces remaining time value
  - Result: Options lose 75% value despite beating earnings
```

**Angela's Call Options Math:**
```
Before earnings:
- Stock at $78.50
- Call strike $80 is slightly OTM
- IV at 78%
- 5 days to expiration
- Call value: $3.50 per share ($1,750 total)

After earnings announcement:
- Stock at $61.20 (down from $78.50)
- Call strike $80 is now deeply OTM
- IV at 12%
- 4 days to expiration
- Call value: $0.05 per share ($25 total)
- Loss: $1,725 (98% loss)

Even though earnings beat, the options collapsed.
```

### Factor 3: Market Context Angela Missed

**What was happening in the broader market:**

```
February 1-2, 2024 (The dates matter):
- Fed held rates steady at 5.5%
- CPI data surprised to the high side
- Market pivoted to "rates staying high longer"
- Risk-off sentiment moved through all growth stocks
- Nasdaq down 2% that day
```

Angela thought:
> "CRWD beats earnings, goes up 15%"

Market reality:
> "Growth stocks are selling off broadly due to rate concerns, CRWD's good earnings can't overcome sector selloff"

When earnings beat but market is risk-off, IV crush can dominate the move.

### Factor 4: The 8-Quarter Streak Bias

**Angela's Overconfidence:**

She noted: "Beat last 8 quarters in a row, very likely to beat again"

**The Problem:**
- Beating is partially random (luck)
- But when you beat 8x, market prices in continued beats
- Raised expectations are built into the stock
- Missing even slightly causes disappointment
- A "beat" on moderate metrics isn't enough

**The Actual Beat:**
- EPS: +7.5% beat (modest)
- Revenue: +2.3% beat (small)
- Guidance raised: +8% (good but not stellar)

**The Market's Interpretation:**
> "Earnings beat but not as big as we expected. Guidance raise is modest. In a rising-rate environment, this is not enough to justify 10%+ gains. Selling."

---

## The IV Crush Trap

### Understanding IV Rank vs. IV Percentile

**For Angela to understand the trap:**

```
IV Rank 78% means:
- Volatility is in the 78th percentile of its range
- BUT it doesn't mean "78% is high"
- It means "78% between the lowest and highest volatility"
- This is different from IV Percentile
```

**IV Percentile (Better Metric):**
```
Would show: What % of trading days have IV lower than today?
IV Rank 78% usually means: IV Percentile is 78%
Result: There's a 22% chance IV will be higher

For earnings trades:
- If IV Percentile is 78%, expected move is large
- After earnings, IV crushes regardless of outcome
- This is GUARANTEED
- You're betting on which way it moves AND hoping IV doesn't crush
```

### The Lesson: Earnings Trades Are Binary

**The Possible Outcomes:**

```
Outcome 1: Beat + Market In Risk-On Mode
- IV doesn't crush (stays elevated)
- Stock moves significantly higher (15-20%)
- Winner: Angela wins big

Outcome 2: Beat + Market In Risk-Off Mode (What happened)
- IV crushes (30-50% IV drop typical)
- Stock moves slightly up/down (±5%)
- Winner: Neither, but shorts the call premium
- Loser: Angela loses on premium crush

Outcome 3: Miss + Market Doesn't Care
- IV crushes
- Stock moves down 5-10%
- Loser: Angela loses on stock move AND IV crush
- Loss magnitude: -15 to -25%

Outcome 4: Miss + Market Cares
- IV crushes less (stays elevated)
- Stock moves down 15-20%
- Loser: Angela loses big
- Loss magnitude: -25% to -35%
```

Angela could only win in Outcome 1. She faced:
- 25% chance of Outcome 2 (what happened)
- 25% chance of Outcome 3
- 50% chance of Outcome 4 (even worse)

Her 75% chance of loss was much higher than she calculated.

---

## What Angela Should Have Done: The Risk Management Approach

### Option 1: Use a Stop Loss

**If Angela had entered with a stop loss:**

```
Entry: $78.50
Stop Loss: $75.00 (3.5% below entry)
Risk: $3.50 × 640 = $2,240
Downside scenario: Loses $2,240 maximum

Actual outcome: Down 22%
With stop loss: Down 3.5%
Difference: Would have saved $8,832
```

**Why she didn't use a stop loss:**
> "This company never misses. I'm not scared. Why would I need a stop loss?"

This is exactly the overconfidence that destroys accounts. The companies that "never miss" are the ones most dangerous when they finally do or when the market turns against them.

### Option 2: Smaller Position Size

**If Angela had sized the position smaller:**

```
Instead of: 640 shares ($50,240) = 100% of account
Could have done: 320 shares ($25,120) = 50% of account
Or even: 160 shares ($12,560) = 25% of account

If 50% position size:
- Loss would be -$5,536 instead of -$11,072
- Still significant but survivable
- Account at $44,464 instead of $38,968
- Can recover with 10% gain on remaining capital
```

### Option 3: Reduce Earnings Eve Exposure

**If Angela had sold before earnings:**

```
January 30: Buys 640 shares at $78.50
January 31: Stock at $78.90 (up slightly)
Decision: Sell 50% before earnings announcement
- Sells 320 shares at $78.90
- Revenue: $25,248
- Profit: $256

February 1: Keeps 320 shares through earnings
- Stock gaps down to $61.20
- Loss on 320 shares: -$5,536
- Overall result: -$5,280 loss (vs -$11,072)
```

This is typical earnings strategy:
- Take initial position pre-announcement
- Reduce position to "house money" amount
- Hold small portion through binary event
- Reduces risk significantly

### Option 4: Use a Defined-Risk Structure (Spreads)

**If Angela had bought a call spread:**

```
Instead of: Buy 5 calls at $80 strike
Could do: Call spread
- Buy 5 calls at $80 strike
- Sell 5 calls at $85 strike
- Net cost: $1.50 (instead of $3.50)
- Max profit: $2.50 × 500 = $1,250
- Max loss: Cost = $750

Benefits:
- Defined risk ($750 max)
- Lower cost (defined premium)
- IV crush less damaging (short call offsets long call)
```

---

## The Real Issue: Angela Had No Rules

### Angela's Rule Violation List

**Rules she should have had but didn't:**

1. **Position Size Rule**: ❌ Violates "Position size should not exceed 3% of account per trade"
   - She used 100% on single earnings trade
   - Should have been max 30% ($15,000)

2. **Stop Loss Rule**: ❌ Violates "Every trade needs a stop loss defined before entry"
   - She had no stop loss
   - Refused to accept downside risk
   - Was stopped out by forced selling, not her rule

3. **Leverage Rule**: ❌ Violates "Total margin should not exceed 20% of account"
   - She used margin for options
   - Combined stock + options exceeded account capital
   - Over-leveraged going into binary event

4. **Earnings Rule**: ❌ Violates "Hold no more than 25% of account through earnings announcement"
   - She held 100% through earnings
   - Exposed to IV crush and binary move
   - No hedging or reduced size

5. **IV Rule**: ❌ Violates "Don't buy options when IV is 70%+ of range"
   - She bought calls when IV was 78%
   - IV crush was guaranteed to happen
   - Paid maximum premium for uncertain outcome

### What Angela's Rules Should Have Been

```
RULES FOR EARNINGS TRADES:

1. Max position size: 20% of account
2. Min stop loss: 3% below entry OR technical support
3. Max leverage: 0% (no margin on earnings trades)
4. Risk/Reward ratio: Minimum 1:2
5. If buying options: Only if IV < 50th percentile
6. If buying calls: Only if defined profit target within options profit zone
7. Reduce position size 50% if earnings in < 5 days
8. Never use margin to buy calls
9. If call is profitable day-of-earnings: TAKE PROFIT
10. Never hold earnings into close with 100% of position

Angela violated every single one.
```

---

## The Probability Analysis Angela Missed

### Expected Value of Angela's Trade

**What Angela should have calculated:**

```
Outcome 1: Beat, market stays risk-on (20% chance)
- Stock gaps up 15%
- Angela gains: +$7,560
- Position: 640 × $90.25 = $57,760

Outcome 2: Beat, market turns risk-off (25% chance) [What happened]
- Stock gaps down 22%
- Angela loses: -$11,072
- Position: 640 × $61.20 = $39,168

Outcome 3: Meet, market risk-off (30% chance)
- Stock flat to down 5%
- Angela loses: -$1,500 to -$3,000
- Position: Down 2-4%

Outcome 4: Miss, market risk-off (25% chance)
- Stock down 20%
- Angela loses: -$10,048
- Position: Stock at $62.80

Expected value = 0.20(+$7,560) + 0.25(-$11,072) + 0.30(-$2,250) + 0.25(-$10,048)
              = +$1,512 - $2,768 - $675 - $2,512
              = -$4,443

Expected loss per attempt: -$4,443
For 1 trade: Breakeven at 50% win rate
For 10 trades: Expected total loss: -$44,430
```

**Angela's Assumption:**
> "8-for-8 on beating earnings, so 100% win rate"

**Reality:**
- Expected value is NEGATIVE even with 100% earnings beats
- Because IV crush plus market context matters more
- Risk/reward was not in her favor
- She needed 80%+ win rate to break even

---

## Key Lessons

### Lesson 1: IV Crush Happens Regardless of Earnings Direction
- Before earnings: High IV prices in large move
- After earnings: IV collapses
- This happens to EVERY earnings stock
- Even if stock moves 15%, options lose 40-50% on IV crush

### Lesson 2: Earnings Trades Require Defined Risk
- Either small position size (2-5% of account)
- Or stop loss (3-5% below entry)
- Or both
- Not "I'm confident so no stop loss"

### Lesson 3: Broad Market Context Matters
- CRWD beat earnings
- But Nasdaq was down 2% that day
- Risk-off sentiment dominated
- Individual stock fundamentals can't overcome sector/market headwind

### Lesson 4: 8 Wins in a Row Doesn't Mean 9th Is Likely
- Past performance is not predictive (except statistically)
- Winning streaks increase overconfidence
- But they also increase probability of regression
- When it breaks, it often breaks with maximum surprise

### Lesson 5: No Rule Beaten by Greed/Overconfidence
Angela didn't have rules because:
- She was overconfident in her analysis
- She had seen it work before (hindsight bias)
- She refused to accept downside risk
- She thought she knew better than risk management

This is the single biggest account-killer.

---

## Questions for Reflection

1. **Do you have a stop loss on every single position?**
2. **Have you ever ignored a stop loss because "I'm confident"?**
3. **What percentage of your account would you risk on earnings?**
4. **Do you understand IV crush or does it surprise you?**
5. **Have you ever had a 8-win streak that made you overconfident?**
6. **What would have kept Angela from this trade?**

---

## The Actual Data: CRWD Earnings

**Real CrowdStrike data (adjusted for this case study):**
- CRWD did not have this specific earnings event in Feb 2024
- This is a composite of real earnings disappointment scenarios
- Many growth stocks have had this IV crush experience

---

**Duration**: 2 trading days (January 30 - February 2)
**Lesson Category**: Risk Management, Options, IV Crush, Overconfidence
**Difficulty Level**: Intermediate
**Key Mistake**: No stop loss + oversized position + overconfidence
**Related Cases**: Case Study 02 (Valuation), Case Study 03 (Technical)
