# Lesson 11.5: Options Spread Strategies

## Introduction

A **spread** is an options strategy involving two or more options of the same type (calls or puts) but with different strikes and/or expirations.

Spreads are used to:
- Reduce the cost of buying options
- Cap risk while limiting profit
- Create defined-risk positions
- Trade specific market conditions with precision

This lesson covers three major spread categories: vertical, calendar, and diagonal spreads.

---

## Why Use Spreads?

### Advantages

1. **Lower Cost**: Selling a call offsets the cost of buying another
2. **Defined Risk**: You know maximum loss upfront
3. **Defined Profit**: You know maximum profit upfront
4. **Better Greeks**: Theta is more balanced, gamma more manageable
5. **Precision**: Trade specific outcomes, not directional bets

### Example of Cost Reduction

```
Bullish on AAPL, wants call option exposure:

Strategy 1: Buy Call (Simple)
- Buy $180 call for $3.50
- Cost: $350 per contract
- Profit: Unlimited
- Loss: Full $350 if expires worthless

Strategy 2: Buy Call, Sell Call (Bull Call Spread)
- Buy $180 call for $3.50
- Sell $185 call for $1.20
- Net cost: $3.50 - $1.20 = $2.30 = $230
- Profit: Limited to $5 × 100 = $500
- Loss: Limited to $230
- Return on investment: 217% if stock moves above $185 (better than 100%+ return)
```

---

## Vertical Spreads

A **vertical spread** involves buying and selling options of the same type with the same expiration but different strikes.

The name comes from looking at an option chain vertically (different strikes).

### Bull Call Spread (Bullish Strategy)

**Setup:**
- Buy lower strike call (ITM or ATM)
- Sell higher strike call (OTM)
- Same expiration date

**How It Works:**
```
AAPL at $180, bullish outlook, 30 days to expiration

Buy $175 call for $6.50
Sell $185 call for $1.20
Net debit: $6.50 - $1.20 = $5.30 per share = $530

Risk Profile:
- Max profit: $185 - $175 - $5.30 = $4.70 per share = $470
- Max loss: Net debit = $530
- Breakeven: $175 + $5.30 = $180.30

Return on Risk: $470/$530 = 89% return if profitable
```

**P&L at Expiration:**
```
Stock Price | Long $175 | Short $185 | Net P&L
------------|----------|-----------|--------
$170        | -$5.30   | $1.20 | -$4.10 (loss)
$175        | $0       | $1.20 | $1.20 (small loss)
$180        | $5.00    | $1.20 | $6.20 - $5.30 cost = $0.90 (small profit)
$185        | $10.00   | -$5.00 | $5.00 - $5.30 cost = -$0.30 (small loss)
$190        | $15.00   | -$10.00 | $5.00 - $5.30 cost = -$0.30 (max loss)

Profit Zone: $180.30 to $185
```

**When to Use:**
- Moderately bullish outlook
- Want to reduce cost of long call
- Stock likely to rise, but not by huge amount
- Want defined risk/reward

**Greeks Profile:**
- Delta: Positive (bullish)
- Gamma: Mixed (positive on long, negative on short)
- Theta: Slightly positive (sold premium helps)
- Vega: Slightly negative (short premium effect)

---

### Bear Call Spread (Bearish Strategy)

**Setup:**
- Sell higher strike call (OTM)
- Buy lower strike call (ITM or ATM)
- Same expiration date

**How It Works:**
```
AAPL at $180, bearish outlook, 30 days to expiration

Sell $185 call for $1.20
Buy $190 call for $0.40
Net credit: $1.20 - $0.40 = $0.80 per share = $80

Risk Profile:
- Max profit: $0.80 = $80 (if stock below $185)
- Max loss: $5.00 - $0.80 = $4.20 per share = $420
- Breakeven: $185 - $0.80 = $184.20

Return on Risk: $80/$420 = 19% return if profitable
```

**P&L at Expiration:**
```
Stock Price | Short $185 | Long $190 | Net P&L
------------|-----------|----------|--------
$170        | $1.20 | -$0.40 | $0.80 (max profit)
$180        | $1.20 | -$0.40 | $0.80 (profit)
$184.20     | $0.80 | -$0.40 | $0.40 (breakeven)
$185        | $0 | -$0.40 | -$0.40 (loss)
$190        | -$5.00 | $0 | -$4.20 (max loss)

Profit Zone: Below $184.20
```

**When to Use:**
- Moderately bearish outlook
- Want to collect premium
- Expect stock to stay flat or fall
- Want defined risk with income

**Greeks Profile:**
- Delta: Negative (bearish)
- Gamma: Mixed (short dominant, overall negative)
- Theta: Positive (seller benefits from decay)
- Vega: Positive (short OTM helps)

---

### Bull Put Spread (Bullish Strategy, Income Focus)

**Setup:**
- Sell lower strike put (ITM or ATM)
- Buy higher strike put (OTM)
- Same expiration date

**How It Works:**
```
AAPL at $180, bullish outlook, wants income, 30 days to expiration

Sell $175 put for $3.50
Buy $170 put for $1.20
Net credit: $3.50 - $1.20 = $2.30 per share = $230

Risk Profile:
- Max profit: $2.30 = $230 (if stock above $175)
- Max loss: $5.00 - $2.30 = $2.70 per share = $270
- Breakeven: $175 - $2.30 = $172.70

Return on Risk: $230/$270 = 85% return if profitable
```

**P&L at Expiration:**
```
Stock Price | Short $175 | Long $170 | Net P&L
------------|-----------|----------|--------
$165        | -$10.00 | $5.00 | -$2.70 (max loss)
$170        | -$5.00 | $0 | -$2.70 (max loss)
$172.70     | -$2.70 | $0 | $0 (breakeven)
$175        | $0 | $0 | $2.30 (max profit)
$180        | $0 | $0 | $2.30 (profit)

Profit Zone: Above $172.70
```

**When to Use:**
- Bullish outlook
- Want to generate income (credit spread)
- Stock likely to stay above support level
- Want defined risk with income potential

**Greeks Profile:**
- Delta: Positive (bullish)
- Gamma: Negative (seller affected)
- Theta: Positive (strong time decay benefit)
- Vega: Slightly positive (short ITM benefits from IV drop)

---

### Bear Put Spread (Bearish Strategy, Income Focus)

**Setup:**
- Sell higher strike put (OTM)
- Buy lower strike put (ITM or ATM)
- Same expiration date

**How It Works:**
```
AAPL at $180, bearish outlook, wants income, 30 days to expiration

Sell $170 put for $1.20
Buy $165 put for $0.40
Net credit: $1.20 - $0.40 = $0.80 per share = $80

Risk Profile:
- Max profit: $0.80 = $80 (if stock above $170)
- Max loss: $5.00 - $0.80 = $4.20 per share = $420
- Breakeven: $170 - $0.80 = $169.20

Return on Risk: $80/$420 = 19% return if profitable
```

**P&L at Expiration:**
```
Stock Price | Short $170 | Long $165 | Net P&L
------------|-----------|----------|--------
$160        | -$10.00 | $5.00 | -$4.20 (max loss)
$165        | -$5.00 | $0 | -$4.20 (max loss)
$169.20     | -$0.80 | $0 | $0 (breakeven)
$170        | $0 | $0 | $0.80 (profit)
$180        | $0 | $0 | $0.80 (max profit)

Profit Zone: Above $169.20
```

**When to Use:**
- Bearish outlook
- Want to generate premium income
- Expect stock to stay above lower support
- Want defined risk with income

**Greeks Profile:**
- Delta: Negative (bearish)
- Gamma: Negative (seller affected)
- Theta: Positive (strong time decay benefit)
- Vega: Negative (OTM benefits from IV drop)

---

## Vertical Spread Comparison

| Spread | View | Buy/Sell | Cost | Max Profit | Max Loss | Best When |
|--------|------|----------|------|-----------|----------|-----------|
| **Bull Call** | Bullish | Buy Low/Sell High | Debit | Capped | Debit | Moderate bullish |
| **Bear Call** | Bearish | Sell High/Buy Low | Credit | Credit | Capped | Moderate bearish |
| **Bull Put** | Bullish | Sell Low/Buy Lower | Credit | Credit | Capped | Bullish on income |
| **Bear Put** | Bearish | Sell High/Buy Lower | Credit | Credit | Capped | Bearish on income |

---

## Calendar Spreads (Time Spreads)

A **calendar spread** involves buying and selling options of the same type and strike but different expirations.

### Strategy: Long Calendar Spread

**Setup:**
- Buy far-term option (e.g., 60 days out)
- Sell near-term option (e.g., 30 days out)
- Same strike, same type

**How It Works:**
```
AAPL at $180, neutral outlook, 60 days to expiration

Buy $180 call (60 days): $4.00
Sell $180 call (30 days): $3.50
Net debit: $4.00 - $3.50 = $0.50 per share = $50

The Goal:
- The 30-day option decays faster (theta decay accelerates)
- Pocket the premium as it decays
- Then have long 30-day option remaining
- Repeat by selling the next 30-day call

Profit Scenario:
Day 30 (near-term expires):
- Stock still at $180 (no movement)
- Far-term now has 30 days left
- Buy it back (should be ~$2.50 instead of $4.00)
- Realize loss on long side: -$1.50

But wait... the 30-day short expired:
- Expired worthless (at-the-money)
- Already pocketed $3.50 credit
- Net: $3.50 - $1.50 = $2.00 profit on minimal move

More realistic example with theta:
Day 30:
- Stock still at $180
- Near-term expires worthless: gain $3.50
- Far-term (now 30 days out): worth $2.00
- Original cost: $4.00
- Unrealized loss: -$2.00
- Net profit: $3.50 - $2.00 = $1.50
- Return: $1.50/$50 net debit = 3000% return!
```

**When to Use:**
- Neutral outlook (stock will stay range-bound)
- Want to profit from time decay
- IV is stable to declining
- Stock near resistance/support (predictable)

**Greeks Profile:**
- Delta: Near zero (neutral)
- Gamma: Slightly negative (long-term dominates short-term)
- Theta: Positive (short-term decay is faster)
- Vega: Slightly positive (long-term IV benefits)

---

## Diagonal Spreads

A **diagonal spread** combines vertical and calendar spread characteristics:
- Different strikes AND different expirations
- Combines directional view with time decay

**Example:**
```
AAPL at $180, bullish outlook, 60 days available

Buy $175 call (60 days): $6.50
Sell $185 call (30 days): $0.80
Net debit: $6.50 - $0.80 = $5.70

Benefits:
- Bullish directional position (long lower strike)
- Funded by short-term premium
- Can roll up after 30 days if bullish

If AAPL at $190 after 30 days:
- Short $185 call assigned or closed at profit
- Long $175 call now worth $15+
- Close long for large profit
```

---

## Risk Management with Spreads

### Position Sizing

```
Bull Call Spread Example:
- Max risk: $530 per spread
- Account size: $50,000
- Risk per trade: 1% = $500
- Can do approximately 1 spread safely
- 2-3 spreads = 2-3% risk (aggressive)

Rule of Thumb:
- Risk no more than 2% per trade
- For $50,000 account: max $1,000 risk per trade
- Plan max loss before entering
```

### Early Exit Rules

```
Spread becomes 50% of max profit:
- Bull call spread with $470 max profit
- When profit reaches $235, exit with profit
- Don't wait for expiration
- Lock in gains, reduce theta risk

Spread hits 50% of max loss:
- Bull call spread with $530 max loss
- When loss hits $265, exit to cut losses
- Prevents maximum loss from happening
- Protects capital
```

### Rolling Spreads

```
Original Bull Call Spread:
- Buy $175 call, sell $185 call
- Stock rises to $190 (short call threatened)

Roll Up:
Day 1:
- Close: Sell $175 call at $16, buy $185 call at $6
- Profit on original spread: $16 - $6 - $5.30 cost = $4.70

Day 2:
- Open new spread: Buy $185 call, sell $195 call
- Different strikes, further out in time
- Extends the position with more profit potential
```

---

## Spread Strategy Comparison Table

| Strategy | Market View | Profit Source | Risk Level | Time Factor |
|----------|-------------|---------------|-----------|------------|
| Bull Call Spread | Bullish | Stock rise | Limited | Theta negative |
| Bear Call Spread | Bearish | Premium decay | Limited | Theta positive |
| Bull Put Spread | Bullish | Premium decay | Limited | Theta positive |
| Bear Put Spread | Bearish | Premium decay | Limited | Theta positive |
| Calendar Spread | Neutral | Time decay | Limited | Theta positive |
| Diagonal Spread | Bullish/Bearish | Direction + time | Limited | Theta neutral |

---

## Key Takeaways

1. **Spreads reduce cost** by selling one option to finance buying another
2. **Vertical spreads** use different strikes to cap risk and profit
3. **Bull spreads** are bullish; **bear spreads** are bearish
4. **Credit spreads** generate income; **debit spreads** need capital
5. **Calendar spreads** profit from time decay with neutral positions
6. **Diagonal spreads** combine vertical and calendar benefits
7. **Always know maximum risk and profit before entering**
8. **Exit at 50% profit** rather than waiting for expiration

---

## In the Next Lessons

- Lesson 11.6 shows how to use spreads and other strategies for income generation
- Lesson 11.7 applies these spreads to risk management
- Lesson 11.8 explores exercises with realistic scenarios

---

## Self-Assessment Questions

1. Why does buying a call and selling a call (bull call spread) reduce your cost?
2. What's the maximum profit on a bull call spread if the stock soars far above your sold strike?
3. How does a calendar spread profit if the stock stays flat?
4. When would you choose a bull put spread instead of a bull call spread?
5. In a bear call spread, why do you need to buy the higher strike call?

