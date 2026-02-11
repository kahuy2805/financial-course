# Lesson 8.4: Momentum Trading Strategies

## Learning Objectives
- Understand momentum indicators and their application
- Identify stocks with strong directional momentum
- Trade momentum with proper risk controls
- Avoid momentum traps and reversals

## What is Momentum Trading?

Momentum trading captures accelerating price moves in a specific direction. It operates on the principle that strong moves tend to continue before reversing.

### Key Characteristics
- **Principle**: "The trend is your friend" - trade direction, not price level
- **Holding Period**: 3-10 days typically
- **Entry Signal**: Acceleration above resistance
- **Exit Signal**: Momentum divergence or target
- **Risk Management**: Tight stops based on recent swing lows
- **Typical Gain**: 3%-8% per trade

## Types of Momentum

### 1. Absolute Momentum
```
Definition: Stock moving up or down in absolute terms
Example: Stock rallies +5% in 3 days = positive momentum

Identification:
- Higher closes each day
- Volume increasing on ups
- Higher lows maintained
- Price above 20-day MA

Fade (Short):
- Stock down 5% in 2 days = negative momentum
- Lower closes
- Volume on downs
- Price below 20-day MA
```

### 2. Relative Momentum
```
Definition: Stock outperforming or underperforming market average

Example:
- S&P 500 up 1% (positive market)
- AAPL up 4% (outperforming) = relative momentum
- AAPL down 2% = underperforming despite market strength

RS (Relative Strength) ratio:
- AAPL price / S&P 500 price
- Rising ratio = outperformance (positive momentum)
- Falling ratio = underperformance (negative momentum)
```

## Momentum Indicators

### 1. RSI (Relative Strength Index)

**Standard Setup: 14-period**

```
Calculation: RSI = 100 - (100 / (1 + RS))
RS = Average gain over 14 periods / Average loss over 14 periods

Levels:
- RSI > 70: Overbought (extended move)
- RSI 50-70: Strong uptrend
- RSI 30-50: Weak uptrend
- RSI < 30: Oversold (extended down move)
- RSI 30: Potential bounce zone

Momentum Trading:
- BUY: RSI 50-70 AND price making new highs = momentum confirmed
- SELL: RSI above 70 AND price makes lower high = divergence
- SHORT: RSI below 30 AND price making new lows = momentum down
- COVER: RSI crosses above 50 from below = bounce signal
```

**Practical Example:**
```
Stock: TSLA daily chart
- RSI: 65 (strong momentum)
- Price: $850 (making higher highs)
- Support: $840 (recent swing low)

Momentum Trade Setup:
- Entry: At breakout of $850 resistance
- Position: 20 shares
- Stop Loss: Below $840 (-$200)
- Target: +$5 move = $855 (+$100)
- Expected hold: 2-5 days

Why it works: RSI 65 shows momentum but not yet extreme (70)
Price making new highs confirms RSI reading
```

### 2. MACD (Moving Average Convergence Divergence)

**Settings: 12-26-9**

```
Components:
- MACD Line: 12-period EMA minus 26-period EMA
- Signal Line: 9-period EMA of MACD
- Histogram: MACD minus Signal line (visual momentum)

Momentum Signals:
- BUY: MACD above signal line AND histogram expanding upward
- SELL: MACD below signal line OR histogram shrinking
- Divergence: Price makes new high but MACD doesn't = momentum failure

Setup Example:
Price: $100 moving up
MACD just crossed above signal line
Histogram expanding (getting taller)
→ MOMENTUM CONFIRMED - good entry

Price: $105 making new high
MACD getting shorter, rolling over
→ MOMENTUM FAILURE - exit signal
```

**3-Day Momentum Trade Example:**
```
Stock: AMD
Day 1 (Tuesday):
- MACD crosses above signal line
- Histogram positive and expanding
- Price: $105.00 | Stop: $102.00 | Entry: 50 shares

Day 2 (Wednesday):
- Price rallies to $107.00
- MACD histogram still expanding
- Action: Hold, momentum strong

Day 3 (Thursday):
- Price: $108.50
- MACD histogram starts shrinking
- Divergence warning: Price high but momentum lower
- Exit at $108.30 for +$163 profit (3.1%)
```

### 3. Rate of Change (ROC) Indicator

```
Definition: Percentage change over a set period
Formula: ROC = ((Close today - Close N periods ago) / Close N periods ago) × 100

Settings: 10-period or 12-period ROC
- Positive ROC: Uptrend
- Negative ROC: Downtrend
- Extreme ROC (±10%): Exhaustion approaching
- ROC crossing zero: Trend change

Momentum Trade Usage:
- ROC +5% to +10%: Strong momentum, buy
- ROC +15%+: Extreme, consider fade/short
- ROC -10%: Strong downtrend, short
- ROC -15% to -20%: Exhaustion, potential bounce
```

## Momentum Trading Strategies

### Strategy 1: Momentum Breakout Trade

**The Setup:**
```
Identification:
1. Stock consolidates for 3-7 days (lower volatility)
2. Volume dries up during consolidation
3. Strong directional bar (high volume) breaks consolidation
4. Momentum indicators confirm (RSI 60+, MACD strong)

Entry Conditions:
- Price closes above consolidation resistance
- Volume 50%+ above average
- RSI above 60 (not yet extreme)
- MACD showing momentum

Position Management:
- Entry: Market order at breakout close
- Stop Loss: Below consolidation low
- Target: 1:1 risk-reward initially
- Scale out at 1:2 if momentum continues
```

**Real Example with $15,000 Portfolio:**

```
Stock: NVIDIA (NVDA)
Consolidation: 5 days between $875-$885 (range $10)
Volume: Declining to 60% of average
Day 5: Gap breakout above $887 on volume 200% average

Entry Setup:
- Price: $887.50 (at breakout)
- Position: 16 shares (consolidation range $10)
- Total invested: $14,200 (94% of account)
- Stop Loss: $884.00 (-$3.50 per share = -$56)
- Target 1: $890.50 (+$3 = +$48)
- Target 2: $897.50 (+$10 = +$160)

Risk: $56 (0.37%)
Reward: $48-$160 (0.32%-1.07%)
```

### Strategy 2: Momentum Continuation Trade

**The Setup:**
```
Identification:
1. Stock has strong 3-5 day uptrend already
2. NOT at all-time high (not extended)
3. Minor pullback (1-2 days)
4. Bounce from pullback, resuming uptrend

Entry:
- Buy on bounce from minor pullback
- RSI in 50-70 range (momentum but not extreme)
- MACD still positive and above signal line
- Price above 20-day MA

Example Setup:
Stock rallied: $100 → $108 (uptrend 4 days)
Pullback: $108 → $104.50 (2-day pullback)
Bounce: Entering at $105.50 pullback recovery

Rationale: Previous momentum continues, minor dip absorbed
```

**Trade Example:**

```
Stock: Tesla (TSLA)
- 4-day uptrend: $840 → $858
- 2-day pullback: $858 → $850
- Bounce entry: $853.00

Position:
- Entry: 20 shares @ $853
- Total: $17,060 (slightly overleveraged on $15K)
- Better: 15 shares @ $853 = $12,795

Stop Loss: $845.00 (-$8 = -$120 for 15 shares)
Target 1: $860.00 (+$7 = +$105)
Target 2: $870.00 (+$17 = +$255)

Hold: 3-7 days expected
Risk: $120 (0.8%)
Reward: $105-$255 (0.7%-1.7%)
```

### Strategy 3: Momentum Reversal/Fade Trade

**The Setup:**
```
Identification:
1. Stock in momentum move (up 10%+ in 2-3 days)
2. Momentum indicators show DIVERGENCE
   - Price making new high
   - RSI rolling over from 70+
   - MACD histogram shrinking
3. Failed breakout above key resistance

Entry (SHORT):
- Sell at pullback from extreme high
- Stop loss above recent high
- Target: Previous support level

Example:
Stock rallied 10%: $100 → $110 in 3 days
RSI hit 75 then rolling over
Price tries $112 but rejected (failed breakout)
→ Short setup triggered
```

**Short Trade Example:**

```
Stock: Rivian (RIVN)
- 3-day momentum rally: $18 → $23
- RSI now 72 (overbought)
- Price attempts $24 but rejected at high

Short Entry:
- Entry: $23.00 (short 200 shares)
- Total short: $4,600
- Stop Loss: $23.50 (+$100 loss if stopped)
- Target 1: $20.00 (-$600 profit)
- Target 2: $18.00 (-$1,000 profit)

Risk: $100 (0.67% on $15K)
Reward: $600-$1,000 (4%-6.7%)
Risk-Reward: 1:6.0 (excellent)

Hold: 3-7 days expected
Exit: RSI bounces back above 50 or price reversal confirmed
```

## Sector Momentum vs. Stock Momentum

### Sector Momentum = Market Tailwind

```
Scenario 1: TAILWIND (favorable)
- Tech sector trending up 8% (NASDAQ up)
- AAPL trending up 5% (stock momentum)
- Combined benefit: Easier to trade, higher success rate

Strategy: Enter AAPL momentum trades
Rationale: Sector strength supports stock move

Scenario 2: HEADWIND (unfavorable)
- Tech sector down 3% (NASDAQ down)
- AAPL up 2% (stock momentum vs market)
- Contradiction: Hard to sustain, reversal risk high

Strategy: Be cautious, smaller positions, tight stops
Rationale: Going against sector strength is risky
```

### Momentum Stock Screener

Track daily for momentum setups:

```
Criteria:
1. Up 5%+ last 3 days
2. RSI > 60 (momentum)
3. Price > 50-day MA (in trend)
4. Volume 50%+ above 20-day average
5. MACD above signal line

Morning Scan Results (example):
- AAPL: ✓✓✓✓✓ (5/5 criteria) = HIGH priority
- MSFT: ✓✓✓✓✗ (4/5 criteria) = MEDIUM priority
- AMD: ✓✓✓✗✗ (3/5 criteria) = LOW priority

Focus entries on HIGH priority stocks
```

## Multi-Day Momentum Trade Example

### Day-by-Day Trade Development

**Entry Day (Monday)**
```
Stock: Broadcom (AVGO)
- Pattern: Opening range breakout
- Price: $615.00 (breaking above $610 resistance)
- Volume: 150% of average
- RSI: 62 (momentum not extreme)
- MACD: Positive, above signal line

Entry Decision:
- 30 shares @ $615.10
- Stop Loss: $610.00 (-$153)
- Target 1: $625.00 (+$300)
- Target 2: $635.00 (+$600)
```

**Day 2 (Tuesday)**
```
Morning: $615.00 again
Lunch: Rally to $620.00
Close: $619.50

Status: +$130 paper profit (+1.4% position)
RSI: 68 (momentum strong but not extreme)
MACD: Histogram expanding

Action: HOLD, momentum is strong
Adjust stop to $612.00 to reduce risk
```

**Day 3 (Wednesday)**
```
Open: Gap up to $623.00
Close: $625.00 (hit Target 1!)

Action: Sell 10 shares (1/3 position) @ $625.20
Profit taken: +$305

Remaining: 20 shares
Move stop to cost: $615.00
Let remaining run to Target 2
```

**Day 4-5 (Thursday-Friday)**
```
Thursday: Consolidation $624-$627
Friday: Rally to $635.50 (Target 2 hit!)

Action: Sell remaining 20 shares @ $635.00
Final profit: +$400

Total Trade Results:
- Partial profit: +$305
- Final profit: +$400
- Total profit: +$705 (+7.6% total position)
- Hold: 4 days
- Win: YES
```

## Momentum Trading Risk Management

### Daily Checklist

```
Before Each Trade:
☐ Verify momentum indicators aligned (RSI + MACD + ROC)
☐ Check sector momentum (NASDAQ, XLK, XLV, etc.)
☐ Volume confirms price move (50%+ above average)
☐ Risk calculated and position sized accordingly
☐ Stop loss placed at logical technical level

During Trade:
☐ Monitor divergences (price vs. indicators)
☐ Watch volume (declining = momentum ending)
☐ Check RSI for extremes (>70 or <30)
☐ Track profit/loss vs. target
☐ Scale out at predefined profit targets

Exit Conditions:
☐ Stop loss hit (discipline)
☐ Target hit (take profits)
☐ Divergence confirmed (momentum failure)
☐ Hold time exceeded (move stalled)
☐ Daily loss limit hit (reduce position size)
```

## Common Momentum Trading Mistakes

1. **Chasing climactic moves**: Entering at extremes (RSI 80+)
2. **Ignoring divergences**: Price high but momentum rolling over
3. **Trading against sector**: Stock up but sector down = risky
4. **Over-position**: Risking too much on momentum trade
5. **Holding through reversals**: Not exiting on divergence
6. **Low-liquidity stocks**: Momentum evaporates with gap downs
7. **Revenge trading**: Adding after stop hit
8. **No profit-taking plan**: All or nothing mentality

## Momentum Trading Journal

Track momentum trades for improvement:

```
Trade #53 - Momentum Continuation
Entry Date: 2024-02-12
Stock: AAPL
Entry Price: $182.50
Entry Signal: Bounce from pullback in 4-day uptrend
Position Size: 40 shares
Stop Loss: $180.00 (1:1 risk $100)
Target 1: $185.00 (1:1 ratio)
Target 2: $188.00 (2:1 ratio)

Indicators at Entry:
- RSI: 58 (momentum, not extreme)
- MACD: Positive, histogram expanding
- Volume: 120% of average

Exit 1: 2024-02-14 @ $185.10 (10 shares) | +$106
Exit 2: 2024-02-15 @ $188.50 (30 shares) | +$600

Total Profit: +$706 (+9.7% on position)
Hold Time: 3 days
Win/Loss: WIN

Learning: Strong pullback buy in uptrend momentum worked well.
Divergence: MACD histogram shrank before final exit, exit timed well.
```

## Summary

Momentum trading captures short-term directional acceleration:
- Identifies momentum with RSI, MACD, and ROC
- Enters on breakouts or continuation trades
- Holds 3-7 days capturing 3%-8% moves
- Fades extended moves showing divergence
- Scales out on predefined targets

Success requires alignment of technical indicators and discipline.

## Key Takeaways

1. Momentum indicators (RSI 60-70, MACD positive, expanding histogram) confirm entry
2. Breakout trades use consolidation range as stop
3. Continuation trades enter on pullbacks in established trends
4. Divergence (price high, momentum rolling over) = exit signal
5. Sector momentum provides tailwind or headwind to trade
6. Scale out 1/3-1/3-1/3 on targets rather than all-or-nothing
7. Never enter at momentum extremes (RSI >75)
8. Volume confirms momentum - without volume, move is suspect

## Next Steps

- Scan for 5 stocks showing all momentum criteria
- Identify sector momentum for each candidate
- Plan entry on consolidation breakout
- Set targets based on previous resistance
- Track momentum divergences for 1 week
