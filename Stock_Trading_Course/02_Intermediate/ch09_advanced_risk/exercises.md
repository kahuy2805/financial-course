# Chapter 9 Exercises: Advanced Risk Management

## Exercise 9.1: Portfolio Allocation for Risk Tolerance

### Objective
Design a portfolio allocation matching your risk profile.

### Scenario
You have $20,000 to invest with a 15% maximum acceptable drawdown.

### Tasks

1. **Determine maximum positions:**
   - Acceptable drawdown: 15%
   - Risk per position: 1.5%
   - Maximum positions: 15% / 1.5% = _____ positions

2. **Allocate across strategies:**
   - Position trade (2-3% risk): 1 position = $_____ capital
   - Swing trades (1.5% risk): 2-3 positions = $_____ each
   - Day trades (0.75% risk): 1-2 positions = $_____ each
   - Cash reserve: 10-15% = $_____

3. **Build allocation table:**

| Strategy | # Positions | Capital Each | Risk per Position | Total Risk |
|----------|------------|------------------|-------------------|------------|
| Position | 1          | $6,000            | 2% ($120)         | $120      |
| Swing    | 2          | $4,500            | 1.5% ($67.50)     | $135      |
| Swing    | 1          | $3,000            | 1.5% ($45)        | $45       |
| Day      | 1          | $2,500            | 0.75% ($18.75)    | $18.75    |
| Cash     | -          | $4,000            | 0%                | $0        |

4. **Verify:**
   - Total capital: $6,000 + $4,500 + $3,000 + $2,500 + $4,000 = $20,000 ✓
   - Total risk: $120 + $135 + $45 + $18.75 = $318.75 (1.59%)
   - Maximum drawdown if all stop: $318.75 (1.59% < 15% target) ✓

5. **Adjust for your situation:**
   - More conservative (10% drawdown max): Reduce positions or risk
   - More aggressive (25% drawdown): Increase positions or risk

---

## Exercise 9.2: Hedge Cost Analysis

### Objective
Calculate whether hedging is worth the cost.

### Scenario
You own a $10,000 MSFT position (50 shares at $200).
MSFT is rallying and you're up +$500 (+5% profit).
Major economic event (Fed decision) in 2 days.

### Tasks

1. **Assess risk without hedge:**
   - Current profit: +$500
   - Potential loss if Fed negative: -8% = -$800 (gives back all profit + $300)
   - Worst case: Fed panic causes -15% = -$1,500 loss

2. **Option 1: Exit before Fed (lock profit)**
   - Action: Sell 50 shares at $200.05
   - Profit: +$502.50 (2.5% on $20K account)
   - Cost: Zero (no hedge cost)
   - Benefit: Certain $502.50 locked in

3. **Option 2: Reduce size (partial exit)**
   - Sell 25 shares at $200
   - Lock profit: +$250
   - Keep 25 shares for continued upside
   - Risk remaining: 25 × -8% = -$200
   - Worst case: +$250 - $200 = +$50 (minimum profit guaranteed)

4. **Option 3: Buy protective put**
   - Buy $190 put option (expiration after Fed)
   - Premium cost: $1.50/share = $75 total (0.75% of position)
   - Protection: Limits loss below $190
   - If Fed negative, rallies to $185:
     - Stock loss: -$750
     - Put profit: +$250
     - Net: -$500 (loss of original +$500 profit)
   - If Fed positive, rallies to $215:
     - Stock profit: +$750
     - Put expires worthless: -$75
     - Net: +$675 profit

5. **Hedge cost-benefit analysis:**

| Strategy | Cost | Worst Case | Best Case | Probability | Expected Value |
|----------|------|-----------|-----------|-------------|-----------------|
| No hedge | $0   | -$1,500   | +$1,500   | 50/50       | $0              |
| Exit all | $0   | +$500     | +$500     | 100%        | +$500           |
| Reduce   | $0   | +$50      | +$1,200   | 50/50       | +$625           |
| Put      | $75  | -$500     | +$675     | 50/50       | +$87.50         |

**Question:** Which strategy would you choose? Why?

---

## Exercise 9.3: Managing Multiple Positions

### Objective
Track and manage a portfolio of 4 simultaneous positions.

### Scenario

| Position | Entry | Current | Stop | Target | Days Held |
|----------|-------|---------|------|--------|-----------|
| AAPL     | 180   | 185     | 175  | 195    | 3         |
| MSFT     | 350   | 348     | 340  | 370    | 2         |
| NVDA     | 850   | 870     | 830  | 920    | 5         |
| AMD      | 105   | 104     | 100  | 120    | 2         |

### Tasks

1. **Calculate portfolio metrics:**
   - Position 1 (AAPL): 50 shares
     - Capital deployed: $9,250
     - Unrealized P&L: +$250
     - Risk: $500

   - Position 2 (MSFT): 20 shares
     - Capital deployed: $_____
     - Unrealized P&L: $_____
     - Risk: $_____

   - Position 3 (NVDA): 15 shares
     - Capital deployed: $_____
     - Unrealized P&L: $_____
     - Risk: $_____

   - Position 4 (AMD): 60 shares
     - Capital deployed: $_____
     - Unrealized P&L: $_____
     - Risk: $_____

2. **Portfolio summary:**
   - Total deployed: $_____
   - Total unrealized P&L: $_____
   - Total risk: $_____
   - Portfolio %: ____% (P&L / deployed)

3. **Identify opportunities:**
   - Which position is closest to stop loss?
   - Which position is closest to target?
   - Which position has the best risk-reward ratio?

4. **Make decisions:**
   - Position 1 (AAPL, +2.8%): Hold for target or exit?
   - Position 2 (MSFT, -0.6%): Exit loss or hold for target?
   - Position 3 (NVDA, +2.4%): Sell partial or hold?
   - Position 4 (AMD, -0.9%): Exit or hold?

5. **Create management plan:**
   - Today: Take actions on which positions?
   - This week: Monitor for target hits
   - Stop loss triggers: Immediate exit
   - Profit targets: Scale out 1/3-1/3-1/3

---

## Exercise 9.4: Trailing Stop Implementation

### Objective
Choose optimal trailing stop distances for your positions.

### Scenario
You have 4 different positions with different characteristics.

| Position | Type | Volatility | Conviction | Trailing Stop | Justification |
|----------|------|------------|------------|---------------|----|
| AAPL     | Swing| Normal     | Medium     | 5%            | Normal swing setup |
| TSLA     | Swing| High       | High       | ?             | Your choice |
| JNJ      | Swing| Low        | Low        | ?             | Your choice |
| NVDA     | Pos  | High       | High       | ?             | Your choice |

### Tasks

1. **Choose trailing stop for TSLA:**
   - Volatility: High (stock swings 3-5% daily)
   - Strategy: Swing trade (hold 5-10 days)
   - Conviction: High (strong setup)
   - Options: 3%, 5%, 8%, 12%?
   - Best choice: ____% (explain reasoning)

2. **Choose trailing stop for JNJ:**
   - Volatility: Low (stock swings 1-2% daily)
   - Strategy: Swing trade (hold 5-10 days)
   - Conviction: Low (marginal setup)
   - Options: 2%, 4%, 6%, 10%?
   - Best choice: ____% (explain reasoning)

3. **Choose trailing stop for NVDA (position trade):**
   - Volatility: High (stock swings 3-5% daily)
   - Strategy: Position trade (hold 4-12 weeks)
   - Conviction: High (strong breakout)
   - Options: 5%, 8%, 12%, 15%?
   - Best choice: ____% (explain reasoning)

4. **Test your choices:**
   - TSLA: Current price $850, your trailing stop ____
   - If TSLA rallies to $870: New trailing stop = ____
   - If TSLA drops to $855: Trailing stop at ____
   - If TSLA drops to $____, position exits

5. **Adjust based on market condition:**
   - VIX = 12 (calm market): Would you tighten or widen stops?
   - VIX = 22 (volatile market): Would you tighten or widen stops?

---

## Exercise 9.5: Earnings Risk Management

### Objective
Create earnings risk management plan for positions.

### Scenario
You hold 3 positions. All have earnings within next 5 days.

| Position | Entry | Current | P&L | Days to Earnings | Decision |
|----------|-------|---------|-----|------------------|----------|
| AAPL     | 180   | 188     | +8  | 2 days           | ? |
| MSFT     | 350   | 348     | -2  | 3 days           | ? |
| NVDA     | 850   | 875     | +25 | 5 days           | ? |

### Tasks

1. **For AAPL (2 days to earnings, +$400 profit):**
   - Current: +4.4% profit (good!)
   - Days to target: Still 3+ days needed
   - Options:
     a) Exit now, lock profit
     b) Exit half, keep half running
     c) Buy protective put
     d) Hold full position
   - Your choice: _____ (explain)

2. **For MSFT (3 days to earnings, -$100 loss):**
   - Current: -0.3% loss (small)
   - Days to target: Thesis still intact
   - Options:
     a) Exit loss, move to better trade
     b) Hold through earnings (high risk)
     c) Reduce size to 50%
     d) Add to position (average)
   - Your choice: _____ (explain)

3. **For NVDA (5 days to earnings, +$1,250 profit):**
   - Current: +2.9% profit (good!)
   - Days to earnings: 5 days (full trade possible)
   - Options:
     a) Exit all, lock profit
     b) Partial exit, keep running
     c) Hedge with protective put
     d) Hold full position
   - Your choice: _____ (explain)

4. **Calculate hedge cost:**
   - NVDA position: 15 shares @ $875 = $13,125
   - Protective put at $850: Cost $2/share = $30
   - Cost as %: $30 / $13,125 = 0.23%
   - Benefit: Limits loss below $850
   - Worth it? (Y/N) and why?

5. **Plan gap management:**
   - If earnings negative: NVDA gaps down 10% to $787.50
   - Current stop loss: $830
   - Your stop will NOT protect (gap below it)
   - What's your plan?
     - (a) Accept loss at $787.50
     - (b) Limit order at $800 before open
     - (c) Don't hold through earnings
   - Best choice: _____ (explain)

---

## Exercise 9.6: Position Scaling (Pyramiding)

### Objective
Build a 3-stage pyramid entry position.

### Scenario
You've identified MSFT as high-conviction swing trade.
Entry point: Consolidation breakout
Strategy: Build 3-entry pyramid over 3-5 days

### Tasks

1. **Design pyramid structure:**
   - Account: $20,000
   - Position conviction: HIGH
   - Risk per add: $300 (1.5% of account)
   - Stop loss distance: $10 per share

   Pyramid 1 (Initial):
   - Capital: $5,000
   - Price at entry: $350
   - Shares: $5,000 / $350 = 14.3 shares (14 shares)
   - Cost basis: 14 × $350 = $4,900
   - Risk: 14 × $10 = $140

   Pyramid 2 (Add at dip):
   - Capital: $3,500 (decline from first)
   - Price at entry: $345 (pullback)
   - Shares: $3,500 / $345 = _____ shares
   - Cost basis: _____ × $345 = $_____
   - Total shares so far: _____ shares
   - Average cost: $_____

   Pyramid 3 (Final add):
   - Capital: $2,000 (smaller again)
   - Price at entry: $355 (bounce/breakout)
   - Shares: $2,000 / $355 = _____ shares
   - Total shares: _____ shares
   - Average cost: $_____

2. **Calculate total position:**
   - Pyramid 1 + 2 + 3 = _____ total shares
   - Total capital deployed: $_____
   - Average cost: $_____
   - Stop loss (below all entries): $____
   - Total risk: _____

3. **Compare to single entry:**
   - Single entry: 44 shares at $355 (breakout only)
   - Cost: 44 × $355 = $15,620
   - vs. Pyramid average cost: $_____
   - Savings: $_____ (better cost basis)

4. **Exit plan:**
   - Target: $375
   - Exit all 44 shares at $375
   - Profit at exit: 44 × ($375 - average cost) = $_____

5. **Pyramid vs. single entry comparison:**
   - Single entry profit: 44 × ($375 - $355) = $_____
   - Pyramid profit: 44 × ($375 - _____ ) = $_____
   - Additional profit from pyramiding: $_____

---

## Exercise 9.7: Avoiding Averaging Down

### Objective
Recognize and avoid the averaging down trap.

### Scenario
You entered TSLA at $100 with high conviction.
Position: 100 shares = $10,000
Stop loss: $80 (20% loss tolerance)
The trade is not working...

### Tasks

1. **Track the downtrend:**
   - Day 1: TSLA at $95 (-5%)
     - Your thought: "Maybe add more at support?"
     - Action: HOLD, don't add yet

   - Day 2: TSLA at $90 (-10%)
     - Loss so far: -$1,000
     - Your thought: "If I buy 100 more at $90, my average is $95"
     - Temptation: ADD more to lower average
     - Decision: YES or NO? _____

   - Day 3: TSLA at $85 (-15%)
     - Loss so far: -$1,500
     - Scenario if you added at $90:
       - Total position: 200 shares
       - Average cost: ($10,000 + $9,000) / 200 = $95
       - Paper loss: 200 × ($85 - $95) = -$2,000
     - Additional loss from averaging: $1,000 more
     - Decision: Good idea? YES or NO? _____

   - Day 4: TSLA at $75 (-25%)
     - Original position loss: 100 × ($75 - $100) = -$2,500
     - If averaged at $90: 200 × ($75 - $95) = -$4,000
     - Additional loss: $1,500 (60% worse!)

2. **Compare scenarios:**

| Action | Entry | Shares | Capital | Stop | Loss at Stop | Loss if $50 |
|--------|-------|--------|---------|------|--------------|-------------|
| Hold only | $100 | 100 | $10,000 | $80 | -$2,000 | -$5,000 |
| Add at $90 | Avg $95 | 200 | $19,000 | $80 | -$3,000 | -$9,000 |
| Add at $85 | Avg $92 | 300 | $27,600 | $80 | -$3,600 | -$12,600 |

3. **The psychological trap:**
   - Why does averaging down feel good?
   - Why is it actually terrible?
   - When should you add to a position?
   - When should you ALWAYS exit?

4. **The rule:**
   - If position is LOSING: ___________ (NEVER add)
   - If position is WINNING: ___________ (OK to pyramid)
   - Exit signal: Stop loss hit or ________________

5. **Apply to your trading:**
   - Commitment: I will NEVER average down because:
   - I will instead: (What will you do instead?)
   - In worst case: (Describe your exit plan)

---

## Exercise 9.8: Integrated Risk Management

### Objective
Combine multiple risk management techniques.

### Scenario
You're managing a $20,000 portfolio with 4 positions.

**Current Portfolio:**
- AAPL: 50 shares at $180, current $185 (+$250 profit)
- MSFT: 20 shares at $350, current $348 (-$40 loss)
- NVDA: 15 shares at $850, current $870 (+$300 profit)
- AMD: 60 shares at $105, current $104 (-$60 loss)

**Today's Situation:**
- AAPL earnings: Tomorrow after close
- Major Fed announcement: Friday
- MSFT thesis deteriorating
- NVDA at highs, approaching resistance

### Tasks

1. **For AAPL (earnings tomorrow):**
   - Current: +$250 profit (+1.25% on $20K)
   - Earnings risk: -10% to +10% possible
   - Your decision:
     a) Exit all, lock profit ($250)
     b) Exit half, keep half ($125 locked)
     c) Buy protective put ($30 cost)
     d) Hold full position (risky)
   - Best choice: _____ | Profit/loss if earnings negative: $_____

2. **For MSFT (thesis weakening):**
   - Current: -$40 loss (-0.2%)
   - Time held: 2 days
   - Thesis: Breaking down
   - Your decision:
     a) Hold, averaging down mentality (NO!)
     b) Exit loss, cut it cleanly ($40)
     c) Reduce size 50%
     d) Add stop loss, hold
   - Best choice: _____ | Action: _____

3. **For NVDA (at resistance):**
   - Current: +$300 profit (+1.5%)
   - Position: At highs, near resistance
   - Trailing stop: 8% from entry ($850)
   - Current trailing stop: 8% from high $870 = $_____
   - Your decision:
     a) Tighten trailing stop to 5%
     b) Hold current 8% trailing stop
     c) Take full profit now
     d) Scale out 1/3 at resistance
   - Best choice: _____ | Reason: _____

4. **For AMD (weak position):**
   - Current: -$60 loss (-0.3%)
   - Time held: 2 days
   - Thesis: Still intact but weak execution
   - Your decision:
     a) Hold for better entry (it will come)
     b) Cut loss, redeploy capital
     c) Average down (NEVER!)
     d) Hedge with short (over-complicated)
   - Best choice: _____ | Reasoning: _____

5. **Portfolio management decision:**
   - Total portfolio currently: $20,450 (up $450)
   - Fed announcement Friday: Major risk event
   - Your plan:
     a) Take all profits now (lock gains)
     b) Reduce to 2 largest positions only
     c) Exit weakest 2 positions (MSFT, AMD)
     d) Hold all, monitor daily
   - Best strategy: _____ | Expected outcome: _____

6. **Document your plan:**
   - AAPL: Exit _____ shares before earnings for $_____
   - MSFT: Exit loss $_____ , redeploy to _____
   - NVDA: Trailing stop at _____ or take _____ profit
   - AMD: Exit or _____ ?
   - New cash position: $_____
   - New total risk: ____% of account

---

## Exercise 9.9: Portfolio Rebalancing

### Objective
Rebalance portfolio quarterly to targets.

### Scenario
Quarterly review of portfolio:

**Target allocation:**
- 35% Tech, 25% Finance, 20% Healthcare, 20% Other

**Current allocation (end of quarter):**
- Tech: 55% (up from 35%)
- Finance: 18% (down from 25%)
- Healthcare: 15% (down from 20%)
- Other: 12% (down from 20%)

### Tasks

1. **Identify concentration risk:**
   - Tech overweight: 55% - 35% = _____ (too much!)
   - Finance underweight: 18% - 25% = _____
   - Healthcare underweight: 15% - 20% = _____
   - Other underweight: 12% - 20% = _____

2. **Rebalancing actions:**
   - Tech winners: Trim and take profits
   - Finance laggards: Exit weak positions
   - Healthcare: Add to build back up
   - Other: Add for diversification

3. **Execution plan:**
   - Sell: Tech position up +30%, trim 1/3 (locks profits)
   - Sell: Tech position up +15%, trim 1/2 (reduces concentration)
   - Buy: Healthcare position on dip
   - Buy: Finance position on strength
   - Result: Rebalanced to target allocation

---

## Answer Key Summary

### Exercise 9.1
- Maximum positions: 10 (15% / 1.5%)
- Reasonable allocation: 3-4 positions to stay disciplined
- Capital per position: 20-30% for core positions

### Exercise 9.2
- Exit all: Guaranteed +$500 (safe)
- Reduce 50%: Likely best risk-reward (+$625 expected)
- Hedge put: Expensive relative to expected move

### Exercise 9.3
- Portfolio metrics: Calculate from position details
- Total risk: Should be under 10% of account
- Management: Exit losers, scale winners

### Exercise 9.4
- TSLA (high vol): 8-10% trailing stop
- JNJ (low vol): 3-4% trailing stop
- NVDA (position): 10-12% trailing stop

### Exercise 9.5
- AAPL: Exit (reduce risk before earnings)
- MSFT: Exit loss (thesis uncertain)
- NVDA: Hold or hedge (high conviction, time available)

### Exercise 9.6
- Pyramid shares: Calculate from capital/price
- Average cost: Lower than single entry
- Profit benefit: 15-25% higher than single entry

### Exercise 9.7
- Averaging down: NEVER do this
- Rule: Only add to WINNERS, not losers
- Prevents catastrophic losses

### Exercise 9.8
- AAPL: Exit or reduce (earnings risk)
- MSFT: Exit loss (thesis broken)
- NVDA: Scale out or tighten stop
- AMD: Exit (weak position)

### Exercise 9.9
- Trim overweight positions (take profits)
- Build underweight positions (buy dips)
- Return to target allocation

---

## Advanced Reflection Questions

1. **What is your natural risk tolerance?**
   - Can you handle 15% drawdown without emotion?
   - How about 25% drawdown?
   - How about 50% drawdown?
   - Design allocation based on realistic tolerance

2. **What is your biggest risk weakness?**
   - Averaging down?
   - Holding losers too long?
   - Taking profits too early?
   - Not using stops?
   - Plan specific rule to address it

3. **How will you handle major market stress?**
   - Market crashes -15%?
   - Your portfolio down -10%?
   - Multiple stops hit same day?
   - Have a plan BEFORE it happens

4. **What is your profit-taking discipline?**
   - Do you let winners run or take early?
   - Do you scale out or hold for max?
   - Do you move stops to cost basis?
   - Design system that works for you

5. **How will you know if your risk management is working?**
   - Track win rate (target 40%+)
   - Track average winner size
   - Track average loser size
   - Calculate profit factor (avg winner / avg loser)
   - If losing too much: Reduce risk, improve entries
