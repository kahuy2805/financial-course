# Lesson 9.2: Hedging Techniques (Basic Protection)

## Learning Objectives
- Understand hedging as a risk management tool
- Apply basic hedging strategies to protect positions
- Use inverse positions to manage downside
- Calculate hedge costs vs. protection benefits

## What is Hedging?

Hedging is taking an offsetting position to protect against losses in your primary position.

### Key Concepts

```
Basic principle:
- Long position: Stock purchased, profits if up
- Hedge position: Short or put, profits if down
- Purpose: Limit downside while allowing upside

Simple example:
- Long 100 shares AAPL at $180
- Worry: Market could crash
- Hedge: Buy put option at $175
- If AAPL crashes to $150:
  - Stock loss: -$3,000
  - Put profit: +$500
  - Net loss: -$2,500 (limited!)

Cost of hedge:
- Put option cost: $50 per contract (lost if price rises)
- Net outcome if AAPL rallies to $200:
  - Stock profit: +$2,000
  - Put loss: -$50 (put expires worthless)
  - Net profit: +$1,950 (insurance cost)

Insurance analogy:
- Like car insurance: Pay for it, hope not to use it
- If accident: Insurance covers most damage
- Hedge = Protection against market accident
```

## Common Hedging Scenarios

### Scenario 1: Position Winning, Protection Before Correction

**The Situation:**
```
Your position: 100 shares MSFT at $330 (cost $33,000)
Current price: $365 (+10.6% gain)
Concern: Market due for pullback, don't want to give back gains

Hedging options:
1. Trailing stop loss: Sell if price drops 5% from high
2. Partial profit: Sell 50% position to lock in gains
3. Hedge with short: Sell short 50 shares (pair trade)
4. Hedge with puts: Buy put option (costs money)

Option 1: Trailing Stop Loss (FREE)
- High: $365
- Trailing stop: 5% below high = $346.75
- If MSFT drops to $346, sell all 100 shares
- Locks in +$1,675 profit (5% of position)
- Simple and costs nothing

Option 2: Partial Profit (LOW COST)
- Sell 50 shares at $365
- Lock in $1,750 profit (5.3%)
- Keep 50 shares to run for more gains
- If market crashes: Still holding 50 shares for recovery

Option 3: Pair Trade (FREE to negative)
- Sell short 50 shares MSFT at $365
- Long 100 shares: Profits if up, loses if down
- Short 50 shares: Profits if down, loses if up
- Net position: Long only 50 shares (50% hedged)
- Works if MSFT goes up or sideways
- Loses if MSFT drops more than gains on short 50%

Option 4: Put Hedge (COST: 1-3% of position)
- Buy put option at $355 strike for $1.50/share = $150
- Cost: 0.45% of position ($33,000)
- Protects below $355
- If MSFT drops to $340: Put worth $1,500 (limits loss to -$1,500 instead of -$2,500)
- If MSFT rallies to $375: Profit +$4,500 (insurance cost -$150 = net +$4,350)
```

### Scenario 2: Large Open Losses, Hedging to Reduce Pain

**The Situation:**
```
Your position: 50 shares TSLA at $850 (cost $42,500)
Current price: $785 (-7.6% loss)
Concern: Position could deteriorate further before reversal

Options:
1. Accept loss and exit: Sells 50 shares for -$3,250 loss (clean break)
2. Hold and hope: Risk further losses, no hedge
3. Hedge with short: Sell short against position (reduces pain)
4. Hedge with put: Buy protection

Option 3: Short Hedge (Recommended for large losses)
- Current position: Long 50 shares @ $785 (down -$3,250)
- Short 25 shares at $785 (pair trade hedge)
- Result: Long 25 shares net (50% hedged)

If TSLA continues down to $700:
- Long 50 shares: -$7,500 loss
- Short 25 shares: +$2,125 profit (sold at $785, buys back at $700)
- Net: -$5,375 loss (vs. -$7,500 without hedge)
- Reduces further losses by $2,125

If TSLA recovers to $850:
- Long 50 shares: +$3,250 gain (recovers to entry)
- Short 25 shares: -$1,625 loss (sold at $785, buys at $850)
- Net: +$1,625 gain (net recovery)
- Sacrifice some upside for downside protection

If TSLA rallies to $950:
- Long 50 shares: +$5,000 gain
- Short 25 shares: -$4,125 loss
- Net: +$875 gain (limited by hedge)
```

## Basic Hedging Techniques

### Technique 1: Partial Exit (Risk Reduction)

**Simplest hedging method:**

```
Concept: Sell part of winning position to lock in gains

Trade setup:
- Long 100 shares ABC at $50
- Current price: $60 (+20% gain)
- Unrealized profit: +$1,000

Partial exit:
- Sell 33 shares at $60 = $1,980
- Lock in: +$980 profit (calculated as 33 × $60 - 33 × $50)
- Remaining: 67 shares at $50 (cost basis)
- Cash freed: $1,980

New position structure:
- 67 shares still working for more gains
- $1,980 cash available to deploy elsewhere
- Worst case: 67 shares stop out = -$350 loss
- Original profit on 33 shares: +$330 (protected)
- Net worst case: -$20 loss (minimized risk!)

Benefits:
- No additional cost (no put premiums)
- Locks in real profit
- Reduces position size risk
- Provides capital for new opportunity
```

**Multi-Stage Partial Exits:**

```
Position: 100 shares at $100

Day 1 - Stock at $110 (+10%):
- Sell 33 shares at $110
- Lock in: +$330 profit
- Remaining: 67 shares

Day 3 - Stock at $115 (+15%):
- Sell 33 shares at $115
- Lock in: +$495 profit (total: +$825)
- Remaining: 34 shares

Day 7 - Stock at $120 (+20%):
- Sell final 34 shares at $120
- Lock in: +$680 profit (total: +$1,505)
- Remaining: 0 shares

Total trade profit: +$1,505 (15% gain)
Outcome: Walk away with locked-in profits
No regret if stock crashes after you exit
```

### Technique 2: Short Hedge (Pair Trade)

**Using opposite position for downside protection:**

```
Setup:
- Long position: 100 shares $100 (down to $95 = -$500 loss)
- Market risk: Concerned about further decline
- Want to maintain position in case recovery happens

Implementation:
- Buy 50 shares long at $95 (original position)
- Sell short 50 shares at $95 (hedge position)
- Net result: Long only 50 shares (50% hedged)

Payoff scenarios:

1) Market continues down to $80:
   - Long 100 shares: -$2,000 total
   - Short 50 shares: +$750 profit (sold at $95, covers at $80)
   - Net: -$1,250 (reduced by 37.5%)

2) Market recovers to $100 (back to original):
   - Long 100 shares: 0 (back to breakeven)
   - Short 50 shares: -$250 loss
   - Net: -$250 (sacrifice some recovery)

3) Market rallies to $120 (strong recovery):
   - Long 100 shares: +$2,500
   - Short 50 shares: -$1,250 loss (sold at $95, covers at $120)
   - Net: +$1,250 (half of possible $2,500 gain)

Cost of hedge:
- Trading costs: 4 commissions (buy 50 original, sell short 50)
- Opportunity: Sacrifice 50% of upside
- Benefit: Limit 50% of downside risk

When to use:
- Large unrealized losses (>10%)
- Conviction position still intact but timing uncertain
- Want to maintain but reduce risk
```

### Technique 3: Trailing Stop Loss (Mental Hedge)

**Automatic protection without additional cost:**

```
Concept: Stop loss that follows price up, protecting gains

Setup:
- Long 50 shares at $100 (entry cost $5,000)
- Initial stop: $95 (5% loss tolerance)
- Stock rallies to $110 (+10%)

Trailing stop implementation:
- Peak price: $110
- Trailing stop distance: 5% from peak
- Stop loss level: $110 - (5% × $110) = $104.50

Stock continues to $115:
- New peak: $115
- New stop loss: $115 - (5% × $115) = $109.25

Stock drops to $113:
- Still above trailing stop ($109.25)
- Position remains open
- Profit locked in if further drop

Stock drops to $108:
- Now below trailing stop ($109.25)
- Order triggers: Sell 50 shares at market
- Lock in profit: +$400 (from $100 to $108 average exit)

Benefits:
- No cost (free protection)
- Automatic exit if price deteriorates
- Locks in portion of gains
- Reduces psychological pain of large losses

Drawback:
- Can be stopped out on normal pullback
- May exit too early if trailing distance too tight
- Typical trailing stop: 5-7% for swing trades, 10% for position trades
```

## Hedging with Correlated Securities

### Hedging Individual Stock Risk with Sector ETF

**Example:**

```
Position: Long 100 shares NVDA (semiconductor)
Concern: NVDA specific risk (earnings miss, competition)
But bullish on semiconductor sector overall

Hedging idea:
- Keep NVDA long (conviction position)
- Short SPY or sector ETF to hedge market risk
- Benefit: Upside if NVDA outperforms sector
- Limit: Downside if sector crashes

Specific setup:
- Long 100 NVDA at $850 = $85,000
- Short 20 SPY at $500 = $10,000 short
- Ratio: About 1:7 (small hedge position)

Scenarios:

1) NVDA +20%, SPY +5%:
   - NVDA profit: +$17,000
   - SPY loss: -$1,000
   - Net: +$16,000 (gets full NVDA upside)

2) NVDA -10%, SPY -15% (market crash):
   - NVDA loss: -$8,500
   - SPY profit: +$1,500
   - Net: -$7,000 (hedge reduces loss)

3) NVDA -5%, SPY +10% (sector underperformance):
   - NVDA loss: -$4,250
   - SPY loss: -$2,000
   - Net: -$6,250 (full downside, small hedge loss)

Drawback:
- Market hedge doesn't perfectly correlate
- Sometimes both positions lose
- Offset costs (commissions, borrow costs for short)
```

## Hedging Cost Analysis

### When Hedging Makes Financial Sense

```
Example: Long AAPL position $50,000

Hedge option 1: Put option
- Cost: 1.5% = $750 per month
- Annual cost: $9,000 (18% of position!)
- Protection: Limits loss below strike price

Hedge option 2: Trailing stop loss
- Cost: 0% (free)
- Protection: Automatic exit on decline
- Downside: Can be stopped out on normal pullback

Hedge option 3: Pair trade (short 50%)
- Cost: Commissions only ($50-100)
- Protection: Limits downside ~50%
- Downside: Limits upside ~50%

Financial analysis:
For put option to make sense:
- Expected crash probability > cost
- Example: 20% chance crash costs 10% = 2% expected cost
- Put cost 1.5% would be worthwhile
- But uncertain crashes are unpredictable

For traders:
- Trailing stops: Always use (free, psychological benefit)
- Pair trades: Use when uncertain (cost-effective)
- Put options: Skip until experienced with options
```

## Hedging Rules for Intermediate Traders

### What to Hedge

```
Hedge when:
☐ Position is 20%+ of portfolio
☐ Position has 15%+ unrealized gain (protect profit)
☐ Position has 10%+ unrealized loss (reduce pain)
☐ Major economic event coming (Fed, earnings)
☐ Holding through overnight (gap risk)
☐ Technical setup questioned (conviction lowered)
☐ Time to take profits arrived

Don't hedge when:
☐ Position is <10% of portfolio (diversified)
☐ Conviction remains high and thesis intact
☐ Stop loss is tight (already protected)
☐ Trying to "not take loss" (denial)
☐ Hedge cost > expected loss protection
```

### Practical Rules

```
Rule 1: Partial profit is best hedge
- After +10% gain: Sell 1/3 position
- Locks in profit with zero cost
- Recommended over other hedges

Rule 2: Tight stops are automatic hedge
- 1-2% risk per position
- Stop loss naturally limits damage
- Most effective hedge is position sizing

Rule 3: Avoid hedging losses
- Hedging losing position = Throwing good money after bad
- Accept loss with tight stop instead
- One-way bet: Either works or doesn't

Rule 4: Hedge conviction positions
- Only hedge when: Thesis intact but timing uncertain
- Example: Bullish AAPL long-term, worried short-term
- Not hedge: Uncertain whether thesis is right

Rule 5: Simple hedges work best
- Trailing stops: Simple, free, effective
- Partial exits: Simple, effective, provides capital
- Complex hedges (options): Not needed at intermediate level
```

## Hedging Examples

### Example 1: Hedging with Partial Exit

```
Trade: Long 100 MSFT at $340
Time frame: Position trade, 12-16 week hold
Current: Week 4, Price $375 (+10.3% gain)

Situation:
- Position profitable
- Market showing warning signs (VIX rising, tech selling)
- Want to protect profit while holding core

Hedge action:
- Sell 33 shares at $375
- Lock in profit: +$1,155
- Remaining 67 shares for continued hold

New position:
- 67 shares at $340 cost basis
- Stop loss moved to $335 (cost basis - 1%)
- Target remains $420

If market corrects and MSFT drops to $320:
- Remaining 67 shares loss: -$1,340
- Original 33 shares profit locked: +$1,155
- Net: -$185 (nearly breakeven on entire trade!)

If MSFT recovers and reaches $420:
- Remaining 67 shares: +$5,360 profit
- Original 33 shares: Locked +$1,155
- Total: +$6,515 (excellent outcome)

Outcome: Hedge reduced risk while preserving upside
```

### Example 2: Hedging with Pair Trade

```
Trade: Long 80 shares TSLA at $820
Loss: Now at $780 (-$3,200 unrealized loss)
Situation: Conviction intact, but price action weak
Timeline: Holding until $850 target or bounce

Concern: Market deteriorating, could drop to $700

Hedge action:
- Sell short 40 shares TSLA at $780
- Net position: Long 40 shares net (50% hedged)
- Risk from $780: 50 shares would lose $4,000 if drops $50
- Hedged with short 40: Only lose $2,000 if drops $50
- Hedge reduces risk by 50%

Exit scenarios:

If TSLA recovers to $850 (original target):
- Long 80: +$2,400 profit
- Short 40: -$2,800 loss (sold at $780, covers at $850)
- Net: -$400 loss (costs the hedge)

Better outcome: Exit short 40 when breakeven
- At $780: Short 40 is profitable
- Exit short 40 at $780 breakeven: 0 profit/loss
- Remaining long 40: Still owns core position
- Can still target $850 on remaining 40 shares

This demonstrates pair trade hedging for recovery scenarios
```

## Summary

Hedging provides insurance protection against losses:
- Partial exits lock profits (recommended, free)
- Trailing stops provide automatic protection (recommended, free)
- Pair trades reduce downside risk (effective, small cost)
- Put options are expensive (skip for now)
- Hedging costs must be justified by expected protection

Key principle: Simplest hedges (exits and stops) work best.

## Key Takeaways

1. Partial profit taking (33%-50%) is the best hedge
2. Trailing stops (5-7%) provide free automatic protection
3. Pair trades (short 50%) cut downside risk in half
4. Tight initial stops are better hedge than late hedging
5. Never hedge losing positions (accept loss instead)
6. Only hedge conviction positions with thesis intact
7. Hedge cost must not exceed expected protection value
8. Avoid put options until proficient with options
9. Simple hedges work better than complex ones
10. Most effective hedge is proper position sizing

## Next Steps

- Review current positions for hedge candidates
- Practice partial exit discipline
- Set trailing stops on all positions
- Calculate hedge cost vs. benefit
- Implement hedging on next swing trade
