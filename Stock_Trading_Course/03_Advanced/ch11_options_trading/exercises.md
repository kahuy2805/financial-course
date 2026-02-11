# Chapter 11 Options Trading Exercises

## Exercise Set 1: Options Basics

### Exercise 1.1: Call Option Profit/Loss Calculations

**Scenario A: Simple Long Call**

You purchase 1 TSLA call option with the following details:
- Current stock price: $250
- Strike price: $260
- Premium paid: $4.50
- Expiration: 30 days

Calculate the profit/loss in the following scenarios:

```
1. Stock price at expiration: $270
   - Intrinsic value at expiration: _______
   - Total cost (premium paid): _______
   - Profit/Loss: _______
   - Return on investment: _______%

2. Stock price at expiration: $260 (at strike)
   - Intrinsic value: _______
   - Profit/Loss: _______
   - Return: _______%

3. Stock price at expiration: $250 (no move)
   - Intrinsic value: _______
   - Profit/Loss: _______
   - Return: _______%

4. Stock price at expiration: $240 (down 4%)
   - Intrinsic value: _______
   - Profit/Loss: _______
   - Maximum loss on this trade: _______
```

**Answer Key:**
1. Intrinsic: $10, Cost: $450, Profit: $550 ($1,000 - $450), Return: 122%
2. Intrinsic: $0, Loss: -$450, Return: -100%
3. Intrinsic: $0, Loss: -$450, Return: -100%
4. Intrinsic: $0, Loss: -$450, Return: -100% (max loss is always premium paid)

---

### Exercise 1.2: Put Option Profit/Loss

You purchase 1 SPY put option:
- Current stock price: $450
- Strike price: $440
- Premium paid: $2.50
- Expiration: 30 days

Calculate profit/loss for:

```
1. Stock price at expiration: $430
   - Intrinsic value: _______
   - Premium paid: _______
   - Profit/Loss: _______
   - Return: _______%

2. Stock price at expiration: $440
   - Intrinsic value: _______
   - Profit/Loss: _______

3. Stock price at expiration: $460 (up 2.2%)
   - Intrinsic value: _______
   - Profit/Loss: _______
   - Maximum loss: _______

4. What was the breakeven price for this put?
   - Formula: Strike - Premium = _______
```

**Answer Key:**
1. Intrinsic: $10, Cost: $250, Profit: $750, Return: 300%
2. Intrinsic: $0, Loss: -$250
3. Intrinsic: $0, Loss: -$250, Max Loss: -$250
4. Breakeven: $440 - $2.50 = $437.50

---

### Exercise 1.3: Intrinsic vs. Time Value

AAPL is trading at $180. The following calls are available:

```
Strike | Premium | Intrinsic | Time Value | Notes
-------|---------|-----------|------------|-------
$170   | $11.50  | ________ | ________   | Deep ITM
$175   | $7.25   | ________ | ________   | ITM
$180   | $4.00   | ________ | ________   | ATM
$185   | $2.00   | ________ | ________   | OTM
$190   | $0.75   | ________ | ________   | Deep OTM

Questions:
1. Which option has highest time value? Why?
2. Which option has zero intrinsic value?
3. If AAPL drops to $175 tomorrow, what would you expect for the $180 call?
4. If AAPL rises to $185, which options expire worthless?
```

**Answer Key:**
Strike | Premium | Intrinsic | Time Value
$170   | $11.50  | $10       | $1.50
$175   | $7.25   | $5        | $2.25
$180   | $4.00   | $0        | $4.00 (highest time value)
$185   | $2.00   | $0        | $2.00
$190   | $0.75   | $0        | $0.75

1. $180 call (ATM) - ATM options have maximum time value
2. $185 and $190 calls (OTM)
3. Would drop significantly (gamma decay + lost intrinsic value)
4. Only the $190 call ($185 is ITM so exercised)

---

## Exercise Set 2: The Greeks

### Exercise 2.1: Delta Interpretation

Four options with the following deltas:

```
Option | Delta | Question
-------|-------|----------
A      | 0.75  | If stock up $5, call gains approximately: $_____
       |       | Probability of expiring ITM: ______%
B      | 0.35  | If stock down $2, call loses approximately: $_____
       |       | Probability of expiring ITM: ______%
C      | -0.60 | If stock up $3, put loses approximately: $_____
       |       | Probability of expiring ITM: ______%
D      | -0.10 | If stock down $4, put gains approximately: $_____
       |       | Probability of expiring ITM: ______%
```

**Answer Key:**
A: Gains $3.75, ~75% probability
B: Loses $0.70, ~35% probability
C: Loses $1.80, ~60% probability
D: Gains $0.40, ~10% probability

---

### Exercise 2.2: Gamma and Delta Changes

You own a $180 call on AAPL (currently at $180) with:
- Delta: 0.50
- Gamma: 0.08

```
Scenario 1: Stock rises to $181
- New delta approximately: _______
- Option gains beyond the delta move: _______ (this is gamma benefit)
- Total gain if closed: estimate _______

Scenario 2: Stock falls to $179
- New delta approximately: _______
- Option loses less than delta would suggest: _______ (gamma helps in reverse)
- Total loss if closed: estimate _______

Scenario 3: Stock rallies to $185 (5-point move)
- Starting delta: 0.50
- After $1 move: 0.58
- After $2 moves: 0.66
- After $3 moves: 0.74
- After $4 moves: 0.82
- After $5 moves: 0.90
- Total option profit vs. $2.50 (5 × delta 0.50): estimate _______
```

**Answer Key:**
Scenario 1: 0.58, Gamma benefit ~$0.02-0.03, Total gain ~$0.80
Scenario 2: 0.42, Gamma helps ~$0.02-0.03, Total loss ~$0.70
Scenario 3: $2.70-3.00 profit (more than just delta × 5)

---

### Exercise 2.3: Theta Decay Over Time

You buy a $185 call for $2.00 with 45 days to expiration.
Assume stock stays at $180 (doesn't move).
Theta schedule:

```
Days to Expiration | Daily Theta | Days Remaining | Expected Value
------------------|-------------|-----------------|----------------
45 days            | -$0.01      | 45              | $2.00 - 0.01 × 45 = $_____
30 days            | -$0.02      | 30              | $2.00 - (0.01×15 + 0.02×30) = $_____
14 days            | -$0.04      | 14              | $2.00 - (0.01×15 + 0.02×16 + 0.04×14) = $_____
7 days             | -$0.06      | 7               | $2.00 - all previous - 0.06×7 = $_____
1 day              | -$0.12      | 1               | $2.00 - all previous - 0.12×1 = $_____

Questions:
1. How much value is lost in days 1-15? _______
2. How much in days 16-30? _______
3. How much in days 31-45? _______
4. What percentage lost in final 7 days? _______%
```

**Answer Key:**
Days 45: $1.55
Days 30: $0.99
Days 14: $0.14
Days 7: -$0.24 (worthless)
Days 1: -$0.36 (worthless)

1. Days 1-15: -$0.15
2. Days 16-30: -$0.32
3. Days 31-45: -$0.15
4. Final 7 days: ~80% of remaining time value

---

### Exercise 2.4: Vega and IV Impact

AAPL $180 call trading at $4.00 with:
- IV: 25%
- Vega: 0.20

Scenario: Stock stays exactly at $180, but IV changes.

```
1. IV increases to 30% (+5 points)
   - IV impact: 5 × $0.20 = $_____
   - New estimated call price: $_____
   - Return: _______%

2. IV decreases to 20% (-5 points)
   - IV impact: -5 × $0.20 = $_____
   - New estimated call price: $_____
   - Return: _______%

3. If you bought before earnings (IV 25%), stock flat, after earnings (IV 20%)
   - You bought at: $4.00
   - IV collapse impact: $_____
   - Loss from IV crush alone: _______%
```

**Answer Key:**
1. +$1.00, $5.00, +25%
2. -$1.00, $3.00, -25%
3. Lose $1.00, -25% (even with stock flat, option down due to IV)

---

## Exercise Set 3: Basic Strategies

### Exercise 3.1: Covered Call Analysis

You own 100 shares of JPMorgan (JPM) purchased at $150.
Current price: $158

You sell 1 call with the following parameters:
- Strike: $165
- Premium received: $2.50
- Expiration: 30 days

```
Scenario Analysis:

1. JPM rises to $170 (up 7.6% in 30 days)
   - Stock gain: ($_____per share) × 100 = $_____
   - Call assigned at: $165
   - Premium collected: $_____
   - Total return: $_____ = _______%
   - What you missed: Stock from $165 to $170 = $_____

2. JPM stays at $158 (no move)
   - Stock gain: $_____
   - Call expires worthless, keep premium: $_____
   - Total return: $_____ = _______%

3. JPM falls to $145 (down 8.2%)
   - Stock loss: ($_____ - $_____) × 100 = $_____
   - Premium cushion: $_____
   - Net loss: $_____ = _______%
   - Premium helped by: _______%

4. What's your maximum profit? $_____
   - At what stock price does this occur? $_____
```

**Answer Key:**
1. Gain $7, $700 stock + $250 premium = $950 = 6.3%, Missed $500
2. No gain on stock, gain $250 on premium, $250 = 1.67%
3. Loss $13, Loss $1,300, +$250 premium = -$1,050 = -7.0%, Cushioned by 1.7%
4. Max profit $1,200 (up 8%), Occurs at $165 and above

---

### Exercise 3.2: Protective Put Scenario

You own 100 shares of Tesla (TSLA) at $250.
Current price: $250

You buy 1 put with:
- Strike: $240
- Premium paid: $3.00
- Expiration: 30 days

```
Scenario Analysis:

1. TSLA rises to $280 (12% gain)
   - Stock gain: $_____
   - Put expires worthless, lost premium: $_____
   - Net gain: $_____ = _______%
   - Was insurance worth it? Why/why not?

2. TSLA stays at $250
   - Stock gain: $_____
   - Put expires worthless: $_____
   - Net: $_____ = _______%
   - Insurance cost: _______%

3. TSLA falls to $230 (down 8%)
   - Stock loss without put: $_____
   - Put protection: Sell at $240 instead of $230: $_____
   - Total loss after insurance: $_____ = _______%
   - Insurance saved you: $_____

4. TSLA crashes to $200 (down 20%)
   - Stock loss would be: $_____
   - Put limits your loss to: $240 per share
   - Total loss after insurance: $_____ = _______%
   - Insurance saved you: $_____
   - Breakeven stock price: $_____
```

**Answer Key:**
1. Gain $3,000, Lose $300 premium, Net $2,700 = 10.8%
2. $0, -$300, -$300 = -1.2%, Insurance cost 1.2%
3. -$2,000 stock, +$1,000 put protection = -$1,000 loss - $300 premium = -$1,300 = -5.2%, Saved $700
4. -$5,000 stock loss, Capped at $250 entry - $3 premium = $247, Loss -$300 = -1.2%, Saved $4,700, $247

---

## Exercise Set 4: Vertical Spreads

### Exercise 4.1: Bull Call Spread

NVIDIA (NVDA) at $875. You are bullish but want to reduce the cost of buying a call.

Setup:
- Buy $870 call for $8.50
- Sell $885 call for $2.00
- Net debit: $6.50
- Expiration: 30 days

```
P&L at Different Stock Prices:

Stock Price | Long $870 | Short $885 | Total P&L | Profit/Loss
------------|----------|-----------|-----------|------------
$850        | ______   | ______    | ______    | $______
$860        | ______   | ______    | ______    | $______
$870        | ______   | ______    | ______    | $______
$877.50     | ______   | ______    | ______    | $______
$885        | ______   | ______    | ______    | $______
$900        | ______   | ______    | ______    | $______

Fill in the missing values and answer:
1. Maximum profit: $_____
2. Maximum loss: $_____
3. Breakeven stock price: $_____
4. Profit zone: Between $______ and $______
5. Return on risk: ______%
```

**Answer Key:**
Stock Price | Long $870 | Short $885 | Total P&L | Profit/Loss
$850        | -$8.50   | +$2.00    | -$6.50   | -$650
$860        | -$8.50   | +$2.00    | -$6.50   | -$650
$870        | $0       | +$2.00    | $2.00    | +$200
$877.50     | $7.50    | -$7.50    | $0.00    | $0
$885        | $15.00   | -$15.00   | $0.00    | -$650
$900        | $30.00   | -$30.00   | $0.00    | -$650

1. Max profit: $1,500 (difference of $15 × 100 - $650 cost)
2. Max loss: $650 (net debit paid)
3. Breakeven: $876.50
4. Profit zone: $877.50 to $885
5. Return on risk: ($1,500 / $650) = 231%

---

### Exercise 4.2: Bull Put Spread (Income Strategy)

Ford (F) at $10.00. You are bullish and want to generate income.

Setup:
- Sell $9.50 put for $0.45
- Buy $9.00 put for $0.15
- Net credit: $0.30
- Expiration: 30 days

```
P&L at Expiration:

Stock Price | Short $9.50 | Long $9.00 | P&L       | Profit/Loss
------------|-------------|-----------|-----------|------------
$8.50       | ______      | ______    | ______    | $______
$8.75       | ______      | ______    | ______    | $______
$9.00       | ______      | ______    | ______    | $______
$9.20       | ______      | ______    | ______    | $______
$9.50       | ______      | ______    | ______    | $______
$10.50      | ______      | ______    | ______    | $______

Questions:
1. Maximum profit (in dollars): $_____
2. Maximum loss: $_____
3. Breakeven price: $_____
4. Probability of profit (approximately): ______%
```

**Answer Key:**
Stock Price | Short $9.50 | Long $9.00 | P&L      | Profit/Loss
$8.50       | -$1.00      | +$0.50    | -$0.50   | -$50
$8.75       | -$0.75      | +$0.25    | -$0.50   | -$50
$9.00       | -$0.50      | $0        | -$0.50   | -$50
$9.20       | -$0.30      | $0        | -$0.30   | -$30
$9.50       | $0          | $0        | $0.30    | $30
$10.50      | $0          | $0        | $0.30    | $30

1. Max profit: $30 (credit received)
2. Max loss: $50 ($0.50 spread width - $0.30 credit = $0.20 × 100)
3. Breakeven: $9.20
4. Probability: ~70% (put strike $9.50, 20% OTM in standard distribution)

---

## Exercise Set 5: Calendar Spreads

### Exercise 5.1: Long Calendar Spread (Time Decay)

Microsoft (MSFT) at $380. You expect the stock to stay relatively flat.

Setup:
- Buy 1 MSFT $380 call (60 days): $4.00
- Sell 1 MSFT $380 call (30 days): $3.50
- Net debit: $0.50
- ATM calendar spread

```
Scenario: 30 days pass, stock still at $380

At Day 30:
1. Your short call (30 days out) is now: _______
   - Expires worthless, gain: $_____

2. Your long call (now 30 days remaining) is worth approximately: $_____
   - Original cost: $_____
   - Current loss on this leg: $_____

3. Net P&L: $_____
   - Return on $50 risk: ______%

Alternative Scenario: 30 days pass, stock rises to $390

1. Short call ($380) is ITM, assigned or at: $_____
   - Loss on short leg: $_____

2. Long call ($380) worth approximately: $_____
   - Gain on long leg: $_____

3. Net P&L: $_____

Maximum profit occurs when: _______
```

**Answer Key:**
Day 30 (Stock at $380):
1. Worthless, gain $3.50 = $350
2. Worth approximately $2.00 (30 days left, ATM)
3. Loss -$2.00 = -$200
4. Net: $350 - $200 = $150 = 300% return

Stock rises to $390:
1. -$10 = -$1,000 loss
2. Worth $12+ (30 days left, $10 ITM) = $1,200+ profit
3. Near breakeven or small profit

Max profit: When stock stays near $380 on short expiration

---

## Exercise Set 6: Income Strategy Planning

### Exercise 6.1: Monthly Covered Call Income Plan

You have a $50,000 account and own 250 shares of dividend-paying stock (Blue Chip Corp) at $180 (cost basis).

Plan:
- Own 250 shares = $45,000 position
- Sell 2.5 calls monthly (round to 2 calls since 0.5 not possible)
- Strike: 5% OTM ($189)
- Monthly premium per call: $1.25
- Days to expiration: 30 days

```
Calculate Monthly:

1. Premium collected: 2 calls × $1.25 × 100 = $_____

2. Monthly return on capital: $_____ / $45,000 = _____%

3. Annualized return: _____% × 12 = _____%

4. Scenario A (Stock rises to $195):
   - Assigned at $189: gain per share = $_____
   - Profit on assignment: $_____ × 250 shares = $_____
   - Plus premium collected: $_____
   - Total profit: $_____
   - Annualized return if repeated: _____% annually

5. Scenario B (Stock falls to $170):
   - Call expires worthless
   - Stock loss: $_____ × 250 = $_____
   - Premium cushion: $_____
   - Net loss: $_____ = _____% loss

6. Over 1 year, selling calls monthly (12 times):
   - If never assigned (stock flat): Income = $_____
   - If assigned 3 times per year: Income + assignment gains = approximately $_____
   - Total return for year: _____% (conservative estimate)
```

**Answer Key:**
1. 2 × $1.25 × 100 = $250
2. $250 / $45,000 = 0.556%
3. 0.556% × 12 = 6.67%
4. Gain $9 per share, $2,250 + $250 = $2,500, (2,500/45,000) = 5.56% monthly if repeated = 67% annually
5. Loss $10 × 250 = -$2,500, Cushion $250, Net -$2,250 = -5% loss
6. $250 × 12 = $3,000 if flat, $3,000 + ($2,500 × 3 assignments) = $10,500, About 23% total return

---

### Exercise 6.2: Cash-Secured Put Income Plan

You have $100,000 and want to generate income using put-selling.

Strategy:
- Sell cash-secured puts (20-30 delta, ~25%)
- Strike: $250 (on stock trading at $260)
- Monthly premium: $2.00 per share ($200 per contract)
- Keep $25,000 cash per put secured

```
Plan:

1. Number of puts you can safely sell: $100,000 / $25,000 = _____ puts

2. Monthly premium income: _____ puts × $200 = $_____

3. Monthly return: $_____ / $100,000 = _____%

4. Annualized return (if never assigned): _____% × 12 = _____%

5. Probability of profit (delta 0.25): Approximately _____% chance stock stays above $250

6. Expected outcome over 12 months:
   - Win months (stock above $250): 10 months × $800 = $_____
   - Loss months (assigned): 2 months × (loss calculation) = $_____

   If assigned at $250, with $200 premium collected:
   - Net entry: $250 - $2.00 = $248
   - You own stock at $248 cost basis
   - Can sell covered calls on it to generate more income

7. Total annual income if no assignment: $_____
   - Return: _____% on $100,000

8. Net return including occasional assignment (assume 2 assignments/year):
   - Premium collected: $_____
   - Assignment gains (if stock avg $260 at assignment): $_____
   - Total: $_____
   - Return: _____% annually
```

**Answer Key:**
1. 4 puts
2. 4 × $200 = $800
3. $800 / $100,000 = 0.8%
4. 0.8% × 12 = 9.6%
5. 75% (since 25 delta = ~25% probability ITM = ~75% probability not ITM)
6. 10 × $800 = $8,000, 2 assignments...
   - If assigned and stock at $260: $10 gain × 100 × 2 = $2,000
   - Total: $8,000 + $2,000 = $10,000
7. 4 × $200 × 12 = $9,600 = 9.6%
8. $9,600 + $2,000 = $11,600 = 11.6%

---

## Exercise Set 7: Risk Management

### Exercise 7.1: Position Sizing

You have a $75,000 account. Your trading plan is:
- Risk no more than 2% per trade
- Average win: $300
- Average loss: $300
- Win rate: 60%

```
1. Maximum loss per trade: $75,000 × 2% = $_____

2. If you sell bull call spreads with max loss $300:
   - How many can you do concurrently? _____
   - Total risk with maximum position: $_____

3. If you sell puts with max loss $500:
   - How many can you do? _____
   - Total risk: $_____

4. Diversification rule: "Don't have more than _____ of account at risk in one sector"
   - If Tech sector: AAPL, MSFT, NVDA
   - If each has $300 max loss: Total Tech risk = $_____
   - Maximum per sector: $75,000 × _____ = $_____
```

**Answer Key:**
1. $1,500 per trade
2. 5 spreads max, $1,500 total
3. 3 puts max, $1,500 total
4. 30%, 3 × $300 = $900 in Tech, Max $22,500 (30% of account)

---

### Exercise 7.2: Stop Loss Rules

You own 100 shares of energy stock XLE at $80 cost basis.
You sell 1 covered call:
- Strike: $85
- Premium: $1.50
- Days to expiration: 30

```
Stop Loss Decision:

1. Set a stop loss at: _____ (5% below entry = _____)
   - If XLE hits this, you buy back the call and exit

2. XLE falls to $76 (hits stop):
   - Cost on stock: $80 - $76 = $_____ per share loss
   - Stock loss: $_____ per share × 100 = $_____
   - Call buy-back cost: estimate $_____
   - Total realized loss: approximately $_____
   - Return: _____% (acceptable for a stop loss)

3. Alternative: "If call delta exceeds 0.60, close position"
   - This would occur if stock rises to approximately: $_____
   - At this price, call worth approximately: $_____
   - Loss on buyback: $1.50 - $2.50 = $_____
   - Why take this loss? _______

4. Best stop loss rule for covered calls:
   a) Price-based (stock X% below entry)
   b) Delta-based (when probability ITM exceeds ___%)
   c) Time-based (close if _____ days remain and not profitable)
```

**Answer Key:**
1. $76
2. Loss $4, -$400 stock, maybe +$0.50 on call (partial gain) = net -$350 to -$400, ~5%
3. ~$82, ~$3.00, -$1.50, To prevent assignment / cap losses further
4. Combination of all three

---

### Exercise 7.3: Monitoring Greeks

You manage the following position:

```
Portfolio Overview:
- Position 1: Long 5 AAPL $180 calls (Delta 0.50, Gamma 0.08, Theta -0.02, Vega 0.20)
- Position 2: Short 3 AAPL $190 calls (Delta -0.30, Gamma -0.06, Theta +0.03, Vega -0.15)

Calculate Portfolio Greeks:

Net Delta: (5 × 0.50) + (3 × -0.30) = _____ (positive = bullish)
Interpretation: _______

Net Gamma: (5 × 0.08) + (3 × -0.06) = _____ (positive = long gamma)
Interpretation: _______

Net Theta: (5 × -0.02) + (3 × +0.03) = _____
Interpretation: _______

Net Vega: (5 × 0.20) + (3 × -0.15) = _____
Interpretation: _______

Scenarios:

1. AAPL rises $5:
   - Delta impact: 1.6 × $5 = _______
   - Gamma makes you gain MORE because accelerating delta
   - Expected gain with gamma: estimate _______

2. AAPL falls $5:
   - Delta impact: 1.6 × (-$5) = _______
   - Gamma makes you lose LESS (acceleration works against loss)
   - Expected loss with gamma: estimate _______

3. IV increases from 25% to 30% (+5):
   - Vega impact: 0.85 × 5 = _______
   - Position helps from IV expansion: _______

4. 7 days pass, stock unchanged, IV same:
   - Theta impact: 0.01 × 7 = _______
   - Losing money to time decay: $_______
   - How to fix: (sell more short premium / buy theta decay / time to exit)
```

**Answer Key:**
Net Delta: 2.5 - 0.9 = 1.6 (net long, bullish position)
Net Gamma: 0.40 - 0.18 = 0.22 (positive, benefits from moves)
Net Theta: -0.10 + 0.09 = -0.01 (slight negative, losing to time)
Net Vega: 1.0 - 0.45 = 0.55 (positive, benefits from IV expansion)

1. 1.6 × $5 = $8.00 per share, $400 on 100 shares (or $800 with gamma acceleration)
2. -$8.00 per share = -$400 (or -$200 with gamma helping)
3. 0.85 × 5 = $4.25, Helps you (positive vega)
4. 0.01 × 7 = -$0.07, -$7 daily = -$49 weekly, (sell more short premium)

---

## Exercise Set 8: Integrated Scenarios

### Scenario 8.1: Earnings Approach

You own 200 shares of GOOG (Google) at $140. Earnings are in 2 weeks.

Current situation:
- Stock: $145
- IV: 35% (elevated due to earnings)
- Your unrealized gain: $1,000
- Options available: Various strikes

```
Decision: How to manage position through earnings?

Option A: Do Nothing
- Pros: _______
- Cons: _______
- Expected outcome: _______

Option B: Sell Covered Calls (30-day, $155 strike)
- Premium collected: ~$3.00
- Probability of assignment (delta ~0.35): _______
- Pros: _______
- Cons: _______
- Expected outcome: _______

Option C: Buy Protective Puts ($135 strike, 2-week expiration)
- Premium cost: ~$1.50
- Insurance cost: _______
- Pros: _______
- Cons: _______
- Expected outcome: _______

Option D: Sell Position Before Earnings
- Realized gain: $_____
- Pros: Avoid gap risk, _______
- Cons: Miss continued gains, _______
- Expected outcome: _______

Your Decision: _______
Rationale: _______
```

**Answer Key:**
A: All upside kept, but large gap risk possible, Could lose big
B: $600 income, ~35%, Collect premium, Miss big gains if earnings great, Good if neutral
C: $300 cost, 2%, Protected below $135, Expensive for short time, Fair if expect volatility
D: $1,000 realized gain, Lock profits avoid surprises, Miss continued gains, Safe

---

### Scenario 8.2: Market Crash Simulation

The market has dropped 15% suddenly. You're down $7,500 on a $50,000 account (15% loss).

Current portfolio:
- Multiple covered calls on positions
- One long call position that expired worthless (-$500)
- Two short put positions (now ITM, at risk of assignment)

```
Immediate Actions:

1. Buy-back ITM short puts (lock losses)?
   - Current loss estimate: $_____
   - Stop hemorrhaging or hope for recovery? _______

2. Covered call assignments likely at reset where?
   - Covered calls were sold 20% OTM
   - Market down 15%, so calls now closer to: ITM / ATM / OTM
   - Strategy: Buy back or let assign? _______

3. Cash position:
   - Had 20% cash ($10,000) set aside
   - Use to: (A) Accumulate stocks at lower prices, (B) Cover margin, (C) Buy protective puts)
   - Choice: _______

4. Sizing adjustment:
   - Previous: 2% risk per trade
   - After loss: Reduce to: _____ % for next month
   - Reason: _______

5. Position review:
   - Exit weakest positions? _______
   - Consolidate to highest conviction trades? _______
   - Accept losses and move forward? _______
```

**Answer Key:**
1. Probably lock losses, $800-1500, Prevents further erosion
2. Now closer to ATM (5% OTM became 5% ITM after 15% drop), Let assign but plan for it
3. C - Buy protective puts (protect from further downside)
4. 0.5-1% (reduce risk by half during drawdown)
5. Yes, consolidate, plan recovery

---

## Answer Verification Guide

When checking your answers:

1. **Show all calculations**: Premium × 100, price differences, percentages
2. **Include units**: Dollar amounts ($), percentages (%), shares (×100)
3. **Think about reasonableness**:
   - Long option buyers lose limited to premium
   - Short option sellers risk grows as ITM
   - Spreads have defined risk/reward
4. **Check scenarios**: Verify across multiple price outcomes
5. **Consider Greeks**: Delta for direction, gamma for acceleration, theta for time, vega for IV

---

## Self-Check Rubric

**For each exercise, verify:**

- [ ] All calculations shown
- [ ] Profit/loss makes sense mathematically
- [ ] Greeks impact aligns with position direction
- [ ] Position sizing follows 1-2% rule
- [ ] Stop losses defined before entering
- [ ] Risk vs reward understood
- [ ] Tax implications considered (for real trading)
- [ ] Volatility/IV environment considered

---

## Next Steps After Exercises

1. **Practice paper trading**: Use a platform with virtual options
2. **Track metrics**: Win rate, average profit/loss, returns
3. **Keep a journal**: What worked, what didn't, lessons learned
4. **Gradually increase complexity**: Master basics before spreads
5. **Start small**: One contract at a time initially
6. **Review regularly**: Monthly assessment of performance

