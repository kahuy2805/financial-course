# Lesson 11.7: Risk Management with Options

## Introduction

Options offer tremendous advantages but also significant risks. A single bad trade or series of losses can devastate a portfolio. Professional traders spend more time on risk management than on finding trades.

This lesson covers the framework for managing options risk systematically and sustainably.

---

## The Risk Hierarchy

### Types of Options Risk (Ordered by Impact)

```
Level 1: Assignment Risk (Biggest)
- Forced to buy/sell stock at strike
- Can create unexpected large positions
- Tax implications
- Cash management issues

Level 2: Directional Risk (Biggest)
- Stock moves against your position
- Loses money in wrong direction
- Can happen quickly and unexpectedly

Level 3: Volatility Risk (Medium)
- IV expansion/contraction impacts position
- Can help or hurt regardless of direction
- Professional traders manage vega actively

Level 4: Time Decay Risk (Varies)
- Theta helps or hurts depending on position
- Long options bleed value
- Can't be prevented, only managed

Level 5: Liquidity Risk (Smaller)
- Can't exit position at reasonable price
- Wide bid-ask spreads
- Need to hold position longer
- Tied-up capital

Level 6: Early Assignment Risk (Rare)
- American options can be assigned early
- Most happens with dividend-paying stocks
- Ex-dividend dates critical
```

---

## Position Sizing: The Foundation

### The Kelly Criterion (Professional Standard)

**Kelly Criterion** suggests the optimal bet size based on your win rate and average payoff.

```
Kelly % = (Win Rate × Avg Winner - Loss Rate × Avg Loss) / Avg Loss

Example:
- Win rate: 65%
- Average winner: $300
- Average loser: -$200
- Loss rate: 35%

Kelly = (0.65 × 300 - 0.35 × 200) / 200
      = (195 - 70) / 200
      = 125 / 200
      = 0.625 = 62.5%

This suggests betting 62.5% of capital on each trade
But this is too aggressive for most traders!

Professional traders use:
- Half Kelly (31.25%) for more conservative sizing
- Quarter Kelly (15.6%) for very conservative sizing
- Smaller positions until track record proven
```

### Practical Position Sizing Rules

**Rule 1: Risk Per Trade**
```
Start with account size and max loss tolerance:

Account: $50,000
Max risk per trade: 1-2% of account
Max loss limit: $500-$1,000 per trade

If selling put with max loss $500:
- Can do 1 put spread per month
- If doing multiple: Total risk ≤ $1,000

If selling call with $300 max profit:
- Can do 3 spreads per month
- 3 × $300 = $900 monthly income
- 1.8% monthly return = 21.6% annually
```

**Rule 2: Capital Deployment**
```
Never deploy more than X% of account to single strategy:

Portfolio of $100,000:
- Covered calls: 30% = $30,000 of stock
- Cash-secured puts: 30% = $30,000 cash
- Long options: 10% = $10,000 capital
- Cash reserve: 30% = $30,000 emergency buffer

Benefits:
- If one strategy fails, others cushion losses
- Can meet margin calls without liquidating winners
- Flexibility to add positions in dips
```

**Rule 3: Max Concurrent Positions**
```
Control total number of open positions:

Beginner: 1-3 total positions
- Learn to manage positions properly
- Don't overwhelm yourself
- Time to check positions daily

Intermediate: 5-10 positions
- Can track Greek exposure
- Rotate strategies
- Monitor daily

Advanced: 10-20+ positions
- Portfolio-level management
- Automated monitoring
- Professional-level discipline

Rule: Never exceed your ability to monitor
A forgotten position is a losing position
```

---

## Stop Loss Rules

### Mental vs. Hard Stops

**Mental Stop (Discouraged):**
```
"I'll sell when it hits a certain level"
- Often doesn't execute when moment comes
- Emotions override decisions
- 90% of traders don't follow mental stops
- Not recommended
```

**Hard Stop (Professional Standard):**
```
"I set a stop loss order immediately upon entry"
- Automatically executes
- No emotion, no judgment
- Removes you from bad trades
- Professional standard
```

### Stop Loss Rules by Strategy

```
COVERED CALLS:
If stock falls 5% below entry:
- Buy back the call
- Accept loss on call premium
- Cut losses on stock position
- Prevents further bleeding

Example:
- Own AAPL at $180
- Sold $185 call for $2.50
- AAPL falls to $171 (5% drop)
- Buy back call and exit
- Realize loss: -$9 + $2.50 = -$6.50 per share = -$650

LONG CALLS/PUTS:
If time value decays below 25% of premium paid:
- Close position
- Cut losses
- Avoids theta cliff

Example:
- Buy $185 call for $1.50
- 7 days later: worth $0.30
- Time value: 80% depleted
- Close position: lose $1.20 per share = -$120

SHORT PUTS:
If assignment risk exceeds threshold:
- Example: Delta exceeds 0.60
- Buy back position at loss
- Prevents forced assignment
- Locks in acceptable loss

SPREADS:
50% of max loss rule:
- Bull call spread: max loss $530
- If loss hits $265, close trade
- Prevents maximum loss from occurring
```

### Stop Loss Order Examples

```
AAPL Covered Call Trade:
- Own 100 AAPL at $180
- Sold $185 call for $2.50
- Set stop: SELL 100 AAPL if price hits $170

Entry: Long 100 AAPL @ $180, Short 1 $185 call @ $2.50
Stop Order: SellStop 100 AAPL @ $170 (auto-buys back call)

If AAPL falls to $170:
- Position auto-closed
- Loss on stock: $10 per share = $1,000
- Gain on call (bought back at $5): +$2.50 - $2.50 = break-even on call
- Net loss: approximately -$1,000

Better approach:
- Don't auto-sell stock
- Instead: "If AAPL < $170, buy back $185 call at market"
- Allows decision-making on stock holding decision
```

---

## The Greeks and Risk Management

### Delta Management for Directional Control

```
Portfolio Greeks Targeting:

Neutral Portfolio:
- Net Delta near 0
- Long calls = -Short calls
- Not betting on direction
- Profit from time decay and volatility

Example:
- Own 10 long calls (Delta 0.50 each) = +5.0 delta
- Sell 20 covered calls (Delta 0.35 each) = -7.0 delta
- Net portfolio delta: -2.0
- Slightly bearish, but close to neutral
- If market up 1%, lose about $200
- If market down 1%, gain about $200
```

### Gamma Risk (Acceleration Risk)

```
High Gamma Risk Situations:
- Hold many ATM options
- Days to expiration 7 or less
- Volatile stock (high gamma values)

Example Problem:
- Own 10 ATM calls on volatile stock
- Each call has Gamma 0.15
- Stock rallies $2
- Delta increases: 0.50 → 0.80
- Position gains accelerate
- But reverse happens on down move

Management:
- Reduce size near expiration
- Avoid ATM options if volatile
- Take profits on winners
- Close positions 3-5 days before expiration
```

### Vega Risk (Volatility Risk)

```
Long Vega Risk (Holding long options):
- Vulnerable to IV crush
- Before earnings: High IV
- After earnings: IV collapses 30-50%
- Long option buyers often lose money even if direction right

Management:
- Close long options BEFORE earnings
- Don't hold through event
- Take 50% profit and exit
- Or hedge with short options (calendar spread)

Short Vega Risk (Holding short options):
- Vulnerable to IV expansion
- Before earnings: IV doubles
- Short calls become more expensive to buy back
- Short puts lose money as IV expands

Management:
- Reduce size going into events
- Close short options if IV spikes
- Use stops based on Greeks, not just price
```

### Theta Management (Time Decay)

```
Long Theta Decay (Holding short options):
- Benefit daily from decay
- Theta accelerates last 7 days
- Plan to exit before expiration

Example:
- Sell 10 puts with theta +$1.50/day average
- For 20 days before expiration
- Month 1: theta = +$0.50/day × 20 days = $1,000 profit
- Month 2: theta = +$1.50/day × 10 days = $1,500 profit
- Don't hold into final week (slippage risk)

Short Theta (Holding long options):
- Bleed value daily
- Biggest hit last week
- Plan exit before expiration

Example:
- Buy 5 calls with theta -$0.30/day
- After 20 days: lost $3,000 in theta alone
- If stock unchanged, up from time value loss
- This is why selling is preferred for steady income
```

---

## Drawdown Management

### Expected vs. Unexpected Drawdowns

```
Expected Drawdown (Normal trading losses):
- 10-15% of account on bad month
- 5-10% on average month
- All traders experience these
- Plan for them

Unexpected Drawdown (Disaster management):
- 20%+ in single month
- From concentrated bets, bad timing
- From event risk (earnings, Fed decision, etc.)
- Requires immediate action

Management Rule:
- If drawdown exceeds 15% in single month
- Or 25% from peak in any period
- REDUCE position size by 50%
- Assess what went wrong
- Return to full size when recovered
```

### Emotional Management During Drawdowns

```
Common Emotional Errors:
1. Panic selling (lock in large losses)
2. Revenge trading (larger bets to recover quickly)
3. Changing systems (abandon working strategy)
4. Over-leverage (compound the problem)
5. Ignoring stops (hope for recovery)

Professional Response to Drawdown:
1. Accept the loss without emotion
2. Review trades that went wrong
3. Improve decision-making
4. Reduce size, NOT increase it
5. Follow your stops
6. Trust your edge to recover

Recovery Math:
- Lose 20% on $10,000 = $8,000 left
- Need 25% gain to break even: $8,000 × 1.25 = $10,000
- Lose 50% on $10,000 = $5,000 left
- Need 100% gain to break even: $5,000 × 2.0 = $10,000
- Larger losses require larger gains to recover
- Avoiding losses is easier than recovering from them
```

---

## Hedging Strategies

### Portfolio-Level Hedging

```
Long Stock Portfolio ($100,000):
- Own: Various stocks
- Risk: Market crash
- Hedge: Buy put options on indices (SPY, QQQ)

Hedge Mechanics:
- Own $100,000 of individual stocks
- Buy $10,000 of puts on SPY (10% hedged)
- If market crashes 10%: $10,000 gain from puts offsets losses
- Cost: 2-3% per month in put premiums
- Protects downside while keeping upside

When to Hedge:
- Before Fed decisions
- Before earnings season
- During geopolitical uncertainty
- When personal need for capital looming
```

### Individual Position Hedging

```
Protective Put (Review from Lesson 11.3):
- Own 100 shares at $100
- Buy $95 put for $2
- Insured against falls below $95
- Cost: $200 for peace of mind
- Works well for appreciated positions
```

---

## Managing Different Market Conditions

### Bull Market Conditions

```
Environment: Stock market rising steadily

Risks:
- Covered calls capped on upside
- Puts not generating enough credit
- Time decay hurting long options

Strategy Adjustments:
- Use longer-term calls: 60-90 days instead of 30 days
- Sell calls further OTM: Lower probability of cap
- Sell more puts: Rising market favors put sellers
- Use bull call spreads instead of long calls
- Reduce hedges (expensive insurance in bull market)

Risk Management:
- Don't get complacent (crashes come)
- Keep some cash for opportunities
- Take profits on winners early
```

### Bear Market Conditions

```
Environment: Stock market falling or volatile

Risks:
- Long options lose money (theta/vega/direction)
- Forced assignments on puts at bad prices
- Stock correlations increase (diversification fails)

Strategy Adjustments:
- Stop selling puts (lower probability of profit)
- Use protective puts on holdings
- Use bear call spreads for income (safer than puts)
- Sell call spreads, not naked calls
- Increase cash position (5% daily moves possible)

Risk Management:
- Tighten stops (can't tolerate large swings)
- Reduce position size
- Increase quality (blue chips over spec stocks)
- Consider VIX hedge (long volatility position)
- Accept lower returns
```

### Sideways/Choppy Conditions

```
Environment: Market unclear, range-bound, volatile

Risks:
- Whipsaws force stop losses
- Long options lose from theta
- Assignment risk on short options

Strategy Adjustments:
- Use iron condors (sell both calls and puts)
- Use straddle/strangle spreads
- Increase time frames (reduce gamma effects)
- Sell wider spreads (higher probability)
- Use calendar spreads (exploit time decay)

Risk Management:
- Widen stop losses to avoid whipsaws
- Track volatility metrics (VIX)
- Use medium delta (0.40-0.50) for selling
- Concentrate on theta collection
- Accept small, consistent profits
```

---

## Record Keeping and Analysis

### Essential Trade Metrics to Track

```
For Every Trade, Record:

Entry Data:
- Date entered
- Underlying asset
- Strategy type (covered call, put spread, etc.)
- Strike price(s)
- Premium collected/paid
- Expiration date
- Account size at entry

Exit Data:
- Date exited
- Exit price(s)
- Profit/loss in dollars
- Profit/loss as percentage
- Days held
- Reason for exit (assignment, stop, profit target, etc.)

Analysis Data:
- Implied volatility at entry/exit
- Stock price at entry/exit
- Delta at entry (used for probability estimate)
- Was it profitable? (Y/N)
- Did it follow your rules? (Y/N)
- What did you learn?
```

### Monthly Review Process

```
Each month, review:

1. Win Rate
- How many trades were profitable?
- Target: 60%+ for selling strategies
- Target: 40%+ for buying strategies

2. Average Winner vs. Loser
- Was winning trades bigger than losing trades?
- Goal: Average winner ≥ Average loser
- If not: Widen winners, tighten losers

3. Return on Capital
- Monthly return: Profits / Capital Deployed
- Target: 0.5-1.5% for income strategies
- Track vs. benchmark (S&P 500)

4. Position Management
- Did you follow stops?
- Did you exit winners early (too early)?
- Did you hold losers too long?
- Did you respect position sizing rules?

5. Strategy Performance
- Which strategies most profitable?
- Which strategies caused most losses?
- Which you most comfortable with?
- Adjust allocation to best performers

6. Emotional Decisions
- Did emotions override plans?
- Which trades regret?
- How to prevent in future?
```

---

## The Risk Management Checklist

Before entering ANY option trade:

```
[ ] Position Size Check
    - Max loss: ___% of account (target: 1-2%)
    - Max loss amount: $_____
    - Can I afford to lose this amount?

[ ] Stop Loss Defined
    - Where will I exit if wrong?
    - Price target for stop? $_____
    - Time stop (days to exit)? _____ days

[ ] Greeks Understood
    - Delta impact if stock moves $1? $_____
    - Gamma impact on delta? _____
    - Theta daily impact? $_____
    - Vega if IV increases 1%? $_____

[ ] Risk vs. Reward
    - Max profit: $____
    - Max loss: $____
    - Risk/reward ratio: acceptable? (>1.0 to 1)

[ ] Catalysts Checked
    - Earnings date: _____
    - Fed meetings/decisions: _____
    - Corporate events: _____
    - Safe to hold through catalysts?

[ ] Exit Plan Defined
    - Profit target: $____
    - Break-even exit if timing wrong: $____
    - Time stop: ___ days
    - Will take this loss if reached

[ ] Position in Context
    - Total capital deployed to this sector: ____%
    - Total number of open positions: _____
    - Greek correlation to portfolio: _____
    - Acceptable?
```

---

## Key Takeaways

1. **Position sizing is foundational**: Risk 1-2% per trade maximum
2. **Hard stops are essential**: Execute them without emotion
3. **Manage Greeks actively**: Delta (direction), Gamma (acceleration), Theta (time), Vega (volatility)
4. **Plan for assignment**: Before entering, decide if acceptable
5. **Track everything**: Win rate, avg winner/loser, returns
6. **Adjust for conditions**: Bull/bear/sideways markets need different strategies
7. **Reduce size in drawdowns**: Protect capital, don't revenge trade
8. **Hedge when needed**: Insurance is expensive but protects large gains
9. **Follow your rules**: Discipline matters more than being right
10. **Never risk more than you can afford to lose** on any single trade

---

## In the Next Lesson

- Lesson 11.8 provides comprehensive exercises and real-world scenarios
- Practice calculating P&L, managing positions, and making decisions
- Test your knowledge with realistic option chain data

---

## Self-Assessment Questions

1. If your account is $50,000 and max risk per trade is 1%, what's your max loss per trade?
2. You sell a put spread with max loss $400. How many can you do if account is $100,000 and you want 2% total risk?
3. If a covered call position needs a 5% stop loss and you own stock at $100, where do you set the stop? What could you do instead?
4. Explain how a portfolio delta of -0.5 differs from -2.0 in terms of directional risk.
5. A position is down 20% of account value. What should you do: (A) double position to recover faster, (B) reduce size, (C) take mental break, or (D) B and C?

