# Lesson 9.3: Managing Multiple Positions

## Learning Objectives
- Track and monitor multiple open positions simultaneously
- Understand position correlation and portfolio risk
- Manage entries, exits, and stops across portfolio
- Balance opportunity with risk across positions

## Challenges of Multiple Positions

### Why Multiple Positions Are Hard

```
Single position (simple):
- One entry to monitor
- One stop loss to track
- One target to manage
- Focus: 100%

Multiple positions (complex):
- Monitor 4 entries simultaneously
- Track 4 stop losses (any could trigger)
- Manage 4 different targets
- Mental energy divided by position count
- Decision fatigue increases errors

Psychological pressures with multiple positions:
1. Attention deficit: Can't watch all equally
2. Decision fatigue: More decisions = worse decisions
3. Revenge trading: Loss in one position creates emotional trade in another
4. Portfolio view vs. position view: Hard to balance all positions together
5. Capital allocation: Which position gets more focus if both need attention?

Managing the complexity:
- Automate: Use alerts and pre-set stop losses
- Systematic: Checklist for monitoring
- Reduce: Start with fewer positions, build up
- Focus: Dedicate time to review (not constant watching)
```

## Portfolio Monitoring System

### Daily Monitoring Checklist

**Morning (5 minutes):**
```
☐ Check overnight news (any gaps needed?)
☐ Scan each position:
  - Is stop loss still in place?
  - Any price movement overnight?
  - Any technical changes requiring action?
☐ Identify which positions need active monitoring today
☐ Plan exits or additions for today
```

**During market hours (30-60 minutes total):**
```
☐ 10:00 AM: Opening action review
  - Opening momentum clear?
  - Any entry signals triggered?
  - Any stops needing adjustment?

☐ 1:00 PM: Mid-day check
  - Positions holding support levels?
  - Any profit targets hit?
  - Any concerning divergences?

☐ 3:30 PM: Closing hour watch
  - Positions holding or failing?
  - Any closing hour reversals?
  - Update stops if necessary?
```

**Evening (10 minutes):**
```
☐ Review all positions closed today
☐ Update trading journal (wins/losses)
☐ Check next day's economic calendar
☐ Identify next day's key setups
☐ Prepare new entry or exit targets
```

### Position Tracking Spreadsheet

Create a simple tracker:

```
| Ticker | Entry | Current | Stop | Target | Risk | Shares | P&L | % P&L |
|--------|-------|---------|------|--------|------|--------|-----|-------|
| AAPL   | 180   | 185     | 175  | 195    | $250 | 50     | $250 | 1.4%  |
| MSFT   | 350   | 348     | 340  | 370    | $500 | 20     | -40  | -0.2% |
| NVDA   | 850   | 870     | 830  | 920    | $800 | 24     | $480 | 2.3%  |
| AMD    | 105   | 103     | 100  | 120    | $150 | 30     | -60  | -0.3% |

Portfolio Summary:
Total deployed: $26,350
Total risk: $1,700
Total P&L: +$630
Portfolio %: +2.4%
Positions in profit: 2/4 (50% win rate)
Largest winner: NVDA (+2.3%)
Largest loser: MSFT (-0.2%)
```

## Position Correlation

### Understanding Position Correlation

```
Correlation definition:
- Measure of how two positions move together
- Range: -1 to +1
  - +1 = Perfectly correlated (move same direction together)
  - 0 = No correlation (move independently)
  - -1 = Perfectly inverse (move opposite)

Example - Highly correlated (+0.8):
- NVDA and AMD (both semiconductors)
- When NVDA up 5%, AMD usually up 4-5%
- When NVDA down 3%, AMD usually down 3-4%
- Risk: If sector crashes, both crash together

Example - Uncorrelated (0.2):
- AAPL and JPM (tech vs. finance)
- AAPL up 5%, JPM might be flat or down
- Different sectors, different drivers
- Benefit: Portfolio diversification

Example - Inverse correlated (-0.3):
- Tech stocks and Treasury bonds
- Tech up, bonds often down (interest rate risk)
- Tech down, bonds often up (flight to safety)
- Good for hedging
```

### Calculating Portfolio Correlation

```
For 2 positions:
- Position 1 (MSFT): Up 5% this week
- Position 2 (AAPL): Up 4% this week
- Correlation: HIGH (+0.8 to +0.9)

For 2 positions:
- Position 1 (AAPL): Up 5% this week
- Position 2 (JPM): Up 1% this week
- Correlation: LOW to MEDIUM (+0.3 to +0.5)

For 2 positions:
- Position 1 (AAPL): Up 5% this week
- Position 2 (TLT bonds): Down 2% this week
- Correlation: INVERSE (-0.3 to -0.5)

Portfolio screening:
If all positions move together (correlation +0.9):
- Portfolio acts like single position
- Diversification not working
- Problem: All 4 positions in tech = concentrated risk

If positions spread across correlations:
- Some +0.5 correlation (sector related)
- Some 0.0 correlation (independent)
- Some -0.3 correlation (inverse hedge)
- Benefits: True diversification
```

## Position Management Across Portfolio

### Entry Management with Multiple Positions

**Scenario:**
```
You have 3 open positions. You identify a 4th high-quality entry.

Decision: Add 4th position?

Analysis:
Current portfolio:
- AAPL: Long, $5,000, 1.5% risk
- MSFT: Long, $6,000, 2% risk
- AMD: Long, $4,000, 1.5% risk
- Total deployed: $15,000 of $20,000 account
- Total risk: $175 (5%)
- Cash available: $5,000

New entry opportunity:
- NVDA: 2% risk = $400
- Capital needed: $6,000 (30% of account)
- Would exceed total capital!

Options:
1. Reduce existing position size
2. Exit weaker position to make room
3. Wait for better opportunity later
4. Pass on 4th position (focus on 3 best ideas)

Recommendation:
- Exit AMD (weakest setup)
- Add NVDA (stronger momentum)
- Keeps portfolio at 3 positions
- Better capital allocation
```

### Exit Management with Multiple Positions

**Scenario:**
```
All 4 positions hitting targets simultaneously.

Position 1 (AAPL): Hit Target 1 (1:1 risk-reward)
- Decision: Sell 1/3 position
- Lock in: $83 profit
- Keep 2/3 running for Target 2

Position 2 (MSFT): Hit Target 1 (1:1 risk-reward)
- Decision: Sell 1/3 position
- Lock in: $166 profit
- Keep 2/3 running for Target 2

Position 3 (AMD): Down approaching stop loss
- Decision: Exit position before stop
- Lock in: -$75 loss (protect remaining capital)
- Free up capital for new opportunity

Position 4 (NVDA): Extended move, no momentum confirmation
- Decision: Hold, but tighten stop to cost basis
- Reduce risk but preserve upside
- Exit if support breaks

Portfolio outcome:
- Took partial profits: +$249
- Exited loss: -$75
- Net portfolio: +$174
- Capital freed: $4,500
- Remaining positions: 3 full + 2 partial
```

### Stop Loss Management

**Coordinating stops across portfolio:**

```
Position 1 - AAPL:
- Stop: $175 (5% from entry $180)
- Status: FIRM (maintains discipline)

Position 2 - MSFT:
- Stop: $340 (3% from entry $350)
- Note: Wider stop due to volatility
- Status: FIRM

Position 3 - AMD:
- Stop: $100 (5% from entry $105)
- Status: FIRM

Position 4 - NVDA:
- Stop: $830 (2% from entry $850, very tight)
- Reason: Highest volatility stock
- Status: Monitor carefully

Portfolio risk summary:
- If all stops hit: Maximum loss $1,175
- Risk as % of account: 5.9% (at tolerance)
- Any single position hitting stop acceptable
- Multiple stops hitting = RED FLAG

Action if 2 stops hit same day:
- Reassess portfolio
- Reduce position sizes
- Increase cash reserve
- Consider market condition (crash?)
```

## Managing Profitable Positions

### Scaling Out of Winners

**Systematic profit-taking approach:**

```
Position: 100 shares MSFT at $350 (cost $35,000)
Stock rallies to $370 (+5.7%)
Profit: +$2,000

Scale-out strategy:
Target 1 ($360): Sell 1/3 (33 shares)
- Partial profit: $330
- Remaining: 67 shares

Target 2 ($375): Sell 1/3 (33 shares)
- Partial profit: +$825
- Total profit so far: +$1,155
- Remaining: 34 shares

Target 3 (+15% from entry = $402.50): Sell final 1/3
- Final profit: +$1,530
- Total profit: +$2,685 (7.7% gain on capital)

Benefits of scaling:
- Lock in gains incrementally
- Reduce emotional attachment to position
- Free capital for new opportunities
- Sleep better knowing some profit captured
- Participate in remaining upside

Alternative: "Give it back" approach
- Sell 1/3 at Target 1: +$330
- Move stop to cost basis: $350
- Remaining 2/3 can move for free (no additional risk)
- Becomes a "free ride" on remainder
```

### Knowing When to Hold Winners

```
Hold criteria:
☐ Trend still intact (price > 50-day MA)
☐ Momentum continuing (RSI 50-70, not exhausted at 80+)
☐ Technical support holding (higher lows maintained)
☐ Sector momentum supporting (not fighting sector decline)
☐ Time hasn't reached target hold (too early to exit)
☐ MACD histogram not rolling over (momentum failing)

Exit criteria:
☐ Target price reached (locked in profit)
☐ Technical support broken (reversal signal)
☐ Momentum divergence (price high, MACD low)
☐ Trend broken (price below 50-day MA)
☐ Time reached maximum hold (take profits before reversal)
☐ Better opportunity elsewhere (reallocate capital)

Example:
Position: Long AAPL swing trade +8% in 5 days
Approaching previous resistance
RSI at 72 (approaching overbought)
Target was 10% gain

Decision:
- RSI says overbought
- But trend still strong
- Partially exit (1/3) at current levels
- Let 2/3 run toward $200 target
- Sets trailing stop at $185

Outcome: Captures $260 profit (partial), keeps upside
```

## Managing Losing Positions

### Exit Discipline

```
Losing position example:
- Entry: NVDA at $850
- Stop loss: $830 (set at entry)
- Current price: $832 (approaching stop)

Psychological pressure:
- "If I close now, it's a real loss"
- "Maybe it will bounce back"
- "I'll give it one more day"

INCORRECT thinking!
- Closed loss = Controlled loss ($18 loss = $432)
- Stop hit = Same loss anyway ($18 loss = $432)
- Bounce false hope = Often results in larger loss

Correct action:
- Place market order to exit at $830
- Accept $432 loss (2.16% of $20K account)
- Move on to next opportunity
- Preserve remaining capital

Exit discipline rules:
1. Exit on stop loss hit (no exceptions)
2. Exit on target reached (lock in profit)
3. Exit on technical break (reversal signal)
4. No "hope trades" (waiting for recovery)
5. No averaging down (adding to losses)
```

### Knowing When to Cut Losses Early

```
Exit early signals:
- Thesis broken (reason for trade no longer valid)
- Entry was clearly wrong in hindsight
- Position building larger losing trend
- Psychological stress unbearable
- Capital needed for better opportunity
- Market condition changed dramatically

Example 1: Cut early to preserve capital
- Entry: TSLA at $850 (momentum setup)
- Stop loss: $830 (-$20)
- Price: $835, approaching stop
- News: Elon tweet creates doubt
- Better decision: Exit at $835 (-$15)
- Saves $5 per share vs. riding to stop

Example 2: Exit weaker position when better one emerges
- Current: AMD down -3%, stop at $100
- Opportunity: AAPL breakout, high conviction setup
- Capital available: Limited
- Decision: Exit AMD at current price (-$150)
- Free capital: $4,500
- Deploy to AAPL: Better risk-reward setup
```

## Portfolio Management During Market Stress

### Extreme Market Conditions (Market crash, -5% or more)

```
Scenario: S&P 500 crashes -5% overnight
All your positions likely down 3-8%

Immediate actions (same day):
1. DON'T PANIC SELL (let emotion settle)
2. Check each position:
   - Any stop losses hit? Yes/No
   - Thesis still intact? Yes/No
   - Technical support still holding? Yes/No
3. Assess portfolio losses:
   - If down 3%: Within normal volatility, hold
   - If down 8%: At risk limit, prepare to reduce
   - If down 12%+: Above tolerance, reduce positions
4. Reduce weakest positions only
   - Best positions: Hold (strong thesis)
   - Weakest positions: Exit (reduce capital at risk)
   - Medium positions: Trim (raise cash)

Portfolio management decision:
Before crash: 4 positions, 6% risk
After -8% crash: Account down $1,600
Remaining portfolio risk: 6% of $18,400 = $1,104
Action: Exit weakest position (-$400 loss realized)
New portfolio: 3 positions, 4% account risk
New cash buffer: $3,500 (19% = safer cushion)
Outcome: Reduced further crash risk

Next day decision:
- Market bounced +2%: Relief, reassess
- Market down more: Reduce further if needed
- Market stabilized: Hold and rebuild
```

## Portfolio Rebalancing During Trades

### Simultaneous Profit Taking and Entry

```
Scenario:
- AAPL position up +12%, approaching max hold time
- MSFT momentum setup triggered, high conviction

Decision:
- Realize some AAPL profit
- Deploy to MSFT setup
- Maintain overall capital usage

Execution:
1. Sell 50% of AAPL position
   - Lock in: +$2,000 profit
   - Capital freed: $5,500
   - Remaining: 50 shares AAPL for further potential

2. Enter MSFT with freed capital
   - Position size: $5,000 (match freed capital)
   - Risk: 1.5% ($300)
   - Shares: 14 shares at $350
   - Stop: $340

Portfolio transition:
- Before: 100 AAPL, 0 MSFT
- After: 50 AAPL + locked +$2,000 profit, 14 MSFT started
- Capital: Same ~$10,500 deployed
- Risk: Slightly higher but still acceptable

Benefit:
- Locked in AAPL profit (real money)
- Captured MSFT setup (new opportunity)
- Rebalanced to best opportunities
```

## Portfolio Monitoring Tools

### Simple Spreadsheet Columns

```
Portfolio tracker template:
- Ticker: Stock symbol
- Strategy: Day/Swing/Position trade
- Entry date: When opened
- Entry price: What we paid
- Current price: Real-time price
- Current date: Today's date
- Days held: Entry date to today
- Shares: Number of shares
- Capital: Shares × Current price
- Stop loss: Dollar amount
- Risk: Capital at risk
- Target: Profit target price
- % gain/loss: (Current - Entry) / Entry
- $ gain/loss: Shares × (Current - Entry)
- Days to target: Days remaining for hold

Summary rows:
- Total deployed: Sum of capital
- Total cash: Account - deployed
- Total risk: Sum of all risks
- Portfolio %: (Total P&L) / (Total deployed)
- Win rate: Winners / Total positions
```

## Summary

Managing multiple positions requires:
- Systematic monitoring (checklist approach)
- Understanding correlation (diversification)
- Disciplined entries and exits (no emotion)
- Scaling profit positions (lock gains, run winners)
- Tight stop discipline (accept losses)
- Portfolio view (balance across all positions)
- Simple tools (spreadsheet tracking)

Key principle: Automation (stops, alerts) reduces mental burden.

## Key Takeaways

1. Monitor 3-4 positions maximum (more = overwhelm)
2. Use alerts for stops and targets (automate)
3. Positions should have different correlations (diversify)
4. Scale out winners in thirds (lock profits)
5. Scale out losses when thesis breaks (not emotion)
6. Exit stops without exception (discipline)
7. Never average down (protect capital)
8. Correlate entries/exits with cash management
9. During stress: Reduce weakest positions first
10. Track all positions in simple spreadsheet

## Next Steps

- Create portfolio tracking spreadsheet
- Set up price alerts for entry and stop levels
- Practice managing 2-3 positions simultaneously
- Develop decision rules for multiple target hits
- Create stress-test scenarios (market crash response)
