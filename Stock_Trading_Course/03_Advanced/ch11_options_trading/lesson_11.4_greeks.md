# Lesson 11.4: The Options Greeks

## Introduction

The Greeks are mathematical measures that quantify how an option's price responds to changes in underlying market variables. They're called "Greeks" because they're represented by Greek letters (Delta, Gamma, Theta, Vega, Rho).

Professional traders use the Greeks to:
- Understand option price sensitivity
- Hedge positions
- Optimize strategy timing
- Manage portfolio risk

---

## Delta: Sensitivity to Stock Price Changes

### Definition

**Delta** measures how much an option's price changes when the underlying stock price moves $1.

**Range:**
- Calls: 0 to +1.0
- Puts: -1.0 to 0

### Interpretation

```
Delta of +0.60 (call option):
- Stock rises $1 → call rises approximately $0.60
- Stock falls $1 → call falls approximately $0.60
- The option has 60% of the stock's price sensitivity

Delta of -0.60 (put option):
- Stock rises $1 → put falls approximately $0.60
- Stock falls $1 → put rises approximately $0.60
- Negative relationship to stock price

Delta of +1.0 (deep ITM call):
- Behaves like owning stock
- $1 stock move = $1 option move
- Almost certain to be exercised

Delta of 0.50 (ATM option):
- 50/50 chance of expiring ITM
- Most time value remains
- Highest gamma (price sensitivity changes most)

Delta of +0.10 (deep OTM call):
- Very unlikely to expire ITM
- Stock must rise more than strike difference
- Only time value remains
```

### Real Examples: Delta in Action

```
AAPL Trading at $180, 30 days to expiration

Call Options:
Strike | Premium | Delta | Interpretation
-------|---------|-------|----------------
$170   | $10.50  | 0.92  | Deep ITM, almost stock-like (92% price move)
$175   | $6.50   | 0.68  | ITM, significant delta
$180   | $3.50   | 0.50  | ATM, 50% sensitivity
$185   | $1.50   | 0.28  | OTM, low sensitivity
$190   | $0.60   | 0.10  | Deep OTM, minimal sensitivity

Put Options:
Strike | Premium | Delta | Interpretation
-------|---------|-------|----------------
$170   | $0.30   | -0.08 | Deep OTM, minimal sensitivity
$175   | $1.40   | -0.32 | OTM, low sensitivity
$180   | $3.50   | -0.50 | ATM, 50% inverse sensitivity
$185   | $6.50   | -0.68 | ITM, significant sensitivity
$190   | $10.50  | -0.92 | Deep ITM, stock-like behavior
```

### Using Delta for Strategy Selection

```
Covered Call Decision (stock at $180):

Sell $185 call (Delta 0.28):
- Low probability of assignment
- Good if you want income without losing stock
- Better for slightly bullish outlook

Sell $190 call (Delta 0.10):
- Very low probability of assignment
- Maximum premium preservation
- But assignment is nearly impossible
- Not worth selling such cheap option

Sell $175 call (Delta 0.68):
- High probability of assignment (~68%)
- Use if you want to get paid and don't care about losing stock
- Better for neutral to slightly bearish outlook

Protective Put Decision:

Buy $180 put (Delta -0.50):
- Good all-around protection
- 50% chance of being exercised
- Balanced insurance cost

Buy $175 put (Delta -0.32):
- Cheap protection
- Only protects against 5-point drop
- Use if you expect mild downside, not crash

Buy $185 put (Delta -0.68):
- Expensive protection
- More likely to be exercised
- Use if you expect significant downside
```

### Delta as Probability

An option's delta approximately equals its probability of expiring in-the-money.

```
AAPL $185 Call with Delta 0.28:
- Approximately 28% probability of being ITM at expiration
- 72% probability of being OTM
- This is why it's cheap

AAPL $180 Call with Delta 0.50:
- Approximately 50% probability of being ITM
- 50% probability of being OTM
- True coin flip

AAPL $175 Call with Delta 0.68:
- Approximately 68% probability of being ITM
- 32% probability of being OTM
- Better odds of profit

Traders often use Delta as a quick probability estimate
```

---

## Gamma: The Acceleration Factor

### Definition

**Gamma** measures the rate of change in delta. It tells you how much delta changes when the stock moves $1.

**Range:** Always positive (for both calls and puts)

### Interpretation

```
Gamma of 0.03 (option's delta):
- Stock rises $1 → delta increases by 0.03
- Example: delta 0.50 becomes 0.53

Gamma of 0.10:
- Stock rises $1 → delta increases by 0.10
- Much more sensitive to changes
- Delta shifts rapidly as stock moves

High Gamma Characteristics:
- ATM options have highest gamma
- Short time to expiration (time decay increases gamma)
- These options are "fastest changing"

Low Gamma Characteristics:
- ITM and OTM options have low gamma
- Long time to expiration
- These options change predictably
```

### Real Example: Gamma Effects

```
AAPL at $180, owning $180 Call (Delta 0.50, Gamma 0.08)

Scenario 1: Stock rises to $181 (small move)
- New delta ≈ 0.50 + 0.08 = 0.58
- Call theoretically worth about $0.58 more (delta × move)
- Reality is even better due to gamma acceleration
- Theta decay offsets some gains

Scenario 2: Stock rises to $185 (larger move)
- Multiple 1-point moves: 0.50 → 0.58 → 0.66 → 0.74 → 0.82
- Call gains more than 5 × delta ($2.50) due to gamma
- If delta averaged 0.66 × 5 = $3.30 gain
- This is gamma's benefit: accelerated gains in your direction

Scenario 3: Stock falls to $175 (down 5)
- Delta decreases: 0.50 → 0.42 → 0.34 → 0.26 → 0.18
- Call loses less than 5 × delta ($2.50) due to gamma
- If delta averaged 0.34 × 5 = $1.70 loss
- Gamma limits losses in adverse direction

Key Point: Gamma accelerates profitable moves, decelerates losses
```

### Long vs. Short Gamma Exposure

```
LONG GAMMA (bought options):
- Benefit from big moves in either direction
- Profit increases if volatility increases
- Want stock to make quick, decisive moves
- Lose from staying flat (theta decay)
- Best when you expect big move but direction uncertain

SHORT GAMMA (sold options):
- Hurt by big moves in either direction
- Profit increases if volatility decreases
- Want stock to stay near strike (mean reversion)
- Profit from time decay (theta)
- Best when you expect stock to stay range-bound

Covered Call: Short gamma
- You sold a call (short gamma)
- If stock surges, delta changes fast and you get called away
- If stock falls, delta falls and put protection increases

Protective Put: Long gamma
- You bought a put (long gamma)
- If stock crashes, put delta becomes more negative (works harder)
- If stock rallies, delta stays near -0.50 (maintains protection)
```

---

## Theta: The Time Decay Factor

### Definition

**Theta** measures how much an option loses value each day due to time decay. It's the "decay rate."

**Range:**
- Long options: negative theta (you lose money daily)
- Short options: positive theta (you gain money daily)

### Interpretation

```
Theta of -0.05 (long call):
- Option loses $0.05 per day to time decay
- Over 30 days: loses approximately $1.50 of time value
- Regardless of stock price movement (all else equal)

Theta of +0.05 (short call):
- Option gains $0.05 per day from time decay
- Over 30 days: gains approximately $1.50
- Time works in your favor

Theta Acceleration:
- At 30+ days to expiration: theta is small
- At 7 days to expiration: theta accelerates dramatically
- At 1 day to expiration: theta is maximum
- This is why options lose value fastest in final week
```

### Real Example: Theta in Action

```
AAPL at $180, Buy $185 Call for $1.50 (45 days to expiration)
Theta = -0.03 (loses 3 cents per day)

Day 1:
- Stock still at $180
- Option now worth approximately $1.47 ($0.03 decay)
- Loss: -$3 on 100 shares

After 7 days (still at $180):
- Theta decay approximately 7 × $0.03 = $0.21
- Option worth approximately $1.29
- Loss: -$21 (theta worked against you)

After 30 days (still at $180):
- Theta now accelerating (closer to expiration)
- Theta increased to -0.05 (per day)
- Days 1-20: $0.03 per day = $0.60 total
- Days 21-30: $0.05 per day = $0.50 total
- Total decay approximately: $1.10
- Option worth approximately $0.40
- Loss: -$110 (theta decay hurt)

After 44 days (still at $180, 1 day to expiration):
- Theta very high: -0.10 or more
- Option worth approximately $0.05 (just time value)
- Total loss: -$145 (if we held entire 45 days)

Key Point: Time decay accelerates as expiration approaches
```

### Theta Strategies

```
THETA-POSITIVE STRATEGIES (Benefit from time decay):
- Covered calls (you're short the call)
- Short puts (you're short the put)
- Short straddles/strangles
- Calendar spreads (short near-term, long far-term)
- Ideal: Stock stays near strikes, IV decreases

THETA-NEGATIVE STRATEGIES (Hurt by time decay):
- Long calls
- Long puts
- Long straddles/strangles
- Calendar spreads (long near-term, short far-term)
- Ideal: Stock moves quickly, IV increases

Covered Call Example:
- You sold $185 call for $2.50
- Each day, theta gains you approximately $0.05
- Over 30 days: $1.50 theta decay benefit
- This is why covered calls are profitable without stock movement
```

### The Theta Cliff

```
Time Value Decay Schedule (typical ATM option)

Days to Expiration | Daily Theta | Cumulative Impact
------------------|-------------|------------------
45 days out        | -0.01       | Slow decay
30 days out        | -0.02       | Still manageable
14 days out        | -0.04       | Accelerating
7 days out         | -0.06       | Rapid decay
3 days out         | -0.08       | Very fast decay
1 day out          | -0.12       | Extreme decay

The "Theta Cliff" is the final 7-10 days where
time value vanishes rapidly. Long option buyers
typically close positions before this cliff.
```

---

## Vega: Sensitivity to Volatility

### Definition

**Vega** measures how much an option's price changes when implied volatility (IV) increases by 1 percentage point.

**Range:** Always positive (for both calls and puts)

### Interpretation

```
Vega of 0.15:
- IV increases 1% → option gains $0.15
- IV decreases 1% → option loses $0.15
- IV changes directly impact the option

Vega of 0.30:
- IV increases 1% → option gains $0.30
- Much more sensitive to volatility changes
- Long options benefit from IV expansion

High Vega Options:
- ATM options (maximum vega)
- Long time to expiration (60+ days)
- Longer-dated options benefit more from IV changes

Low Vega Options:
- ITM and OTM options (away from ATM)
- Short time to expiration
- Minimal sensitivity to IV
```

### Real Example: Vega Impact

```
AAPL at $180, Buy $180 Call (30 days, IV = 25%)
- Cost: $3.50
- Delta: 0.50
- Vega: 0.20

Scenario 1: Stock stays at $180, IV increases to 30% (+5%)
- IV impact: 5% × $0.20 vega = $1.00 gain
- Theta impact: -0.02 × 1 day = -$0.02 loss
- Net: Call worth approximately $4.48
- Profit: +$0.98 per share = $98 (28% return)
- Stock didn't move but option gained from IV expansion

Scenario 2: Stock stays at $180, IV decreases to 20% (-5%)
- IV impact: -5% × $0.20 vega = -$1.00 loss
- Theta impact: -$0.02 loss
- Net: Call worth approximately $2.48
- Loss: -$1.02 per share = -$102 (29% loss)
- Stock didn't move but option lost from IV contraction

Scenario 3: Stock rises to $185, IV stays at 25%
- Stock move impact (delta): +0.50 × 5 = $2.50
- Gamma acceleration: approximately +$0.30
- Theta decay: -$0.02
- Net: Call worth approximately $6.28
- Profit: $2.78 per share = $278 (79% return)
- Stock movement dominated the profit

Key Point: Vega can dominate option pricing when stock is stable
```

### IV Crush and Expansion

```
Earnings Announcement Effect (Typical):

Before Earnings (High IV):
- AAPL $180 call trading at $4.00
- IV = 40%, Vega = 0.25
- High option premiums due to earnings uncertainty

Earnings Announced (Stock down 2%):
- Stock falls to $176
- IV collapses to 20% (uncertainty resolved)
- Theoretical call value: $2.00 (intrinsic) - $1.25 IV crash (vega loss) + ($0.50 stock move)
- Actual: approximately $1.25
- Loss: -$275 (68% loss on call buyer)
- Stock only fell 2%, but option fell 69%

This is "IV Crush" - option sellers benefit
```

### Vega Strategies

```
VEGA-POSITIVE (Long IV):
- Long calls
- Long puts
- Long straddles
- Long volatility
- Profit when IV increases (market uncertainty)
- Use when: IV at historical lows, earnings approaching

VEGA-NEGATIVE (Short IV):
- Short calls (covered calls, spreads)
- Short puts
- Short straddles
- Short volatility
- Profit when IV decreases (market settles)
- Use when: IV at historical highs, earnings just passed
```

---

## Rho: Sensitivity to Interest Rates

### Definition

**Rho** measures how much an option's price changes when interest rates increase by 1%.

**Range:** Positive for calls, negative for puts

### Practical Importance

**Rho is the least important Greek for traders because:**
- Interest rates change slowly (not daily volatility)
- Impact is typically under 1% per 1% rate move
- Only matters for very long-dated options (LEAPS)

```
For most traders:
- Rho is negligible
- Focus on Delta, Gamma, Theta, Vega
- Only worry about Rho if trading 2+ year LEAPS
```

---

## The Greeks in Action: Complete Example

### Scenario: AAPL After Earnings

```
Initial Position (45 days before earnings):
- Own 100 AAPL shares at $180
- Stock volatility: 20%
- Implied Volatility (IV): 25%

Option Chain (30 days to expiration):
$180 Call Analysis:
- Price: $3.50
- Delta: 0.50 (50% chance ITM)
- Gamma: 0.08 (delta changes 0.08 per $1 move)
- Theta: -0.02 (loses $0.02 daily)
- Vega: 0.20 (gains $0.20 if IV up 1%)

Scenario 1: "Safe" Q1 Results - Stock up 3% to $185
Day 1 after results:
- Stock at $185: Delta × move = 0.50 × 5 = $2.50 impact
- Gamma acceleration: approximately +$0.20 (prices increased)
- Theta decay: -$0.02 × 1 = -$0.02
- IV drops to 20% (certainty): -0.20 × 5 = -$1.00 vega loss
- Greeks recap: $2.50 + $0.20 - $0.02 - $1.00 = $1.68
- Option worth: $3.50 + $1.68 = $5.18
- Profit: $168 (48% return)
- IV crush offset by positive stock move

Scenario 2: "Weak" Q1 Results - Stock down 4% to $173
Day 1 after results:
- Stock at $173: Delta × move = 0.50 × (-7) = -$3.50 impact
- Gamma loss: approximately -$0.28 (magnified loss)
- Theta decay: -$0.02
- IV spikes to 35% (fear): +0.20 × 10 = +$2.00 vega gain
- Greeks recap: -$3.50 - $0.28 - $0.02 + $2.00 = -$1.80
- Option worth: $3.50 - $1.80 = $1.70
- Loss: -$180 (51% loss)
- Even vega expansion couldn't offset stock drop + gamma loss

Scenario 3: "In-Line" Q1 Results - Stock flat at $180
Day 1 after results:
- Stock at $180: No directional move
- Gamma: no acceleration (stock didn't move)
- Theta decay: -$0.02
- IV drops to 22% (slight relief): -0.20 × 3 = -$0.60
- Greeks recap: $0 - $0.02 - $0.60 = -$0.62
- Option worth: $3.50 - $0.62 = $2.88
- Loss: -$62 (18% loss)
- No direction, so IV drop and theta hurt

This shows how all Greeks work together to determine actual P&L
```

---

## Greeks Summary Table

| Greek | Measures | Long Call | Short Call | Long Put | Short Put |
|-------|----------|-----------|-----------|----------|-----------|
| **Delta** | Price move sensitivity | +0.50 (ATM) | -0.50 (ATM) | -0.50 (ATM) | +0.50 (ATM) |
| **Gamma** | Delta acceleration | Positive (long) | Negative (short) | Positive (long) | Negative (short) |
| **Theta** | Time decay | Negative (-0.02) | Positive (+0.02) | Negative (-0.02) | Positive (+0.02) |
| **Vega** | IV sensitivity | Positive | Negative | Positive | Negative |
| **Rho** | Rate sensitivity | Positive | Negative | Negative | Positive |

---

## Key Takeaways

1. **Delta**: How much the option moves with stock (0-1 for calls, 0 to -1 for puts)
2. **Gamma**: How fast delta changes; accelerates gains, decelerates losses
3. **Theta**: Time decay; long options bleed value, short options gain daily
4. **Vega**: Volatility impact; options worth more when uncertainty increases
5. **Rho**: Interest rate impact; rarely matters for short-term trading
6. **Greeks work together**: Changes in IV can dominate price movement
7. **Trading strategy determines Greek exposure**: Understand your position's Greek profile

---

## In the Next Lessons

- Lesson 11.5 shows how to combine options into spreads using Greeks
- Lesson 11.6 applies Greeks to income generation strategies
- Lesson 11.7 uses Greeks to manage risk

---

## Self-Assessment Questions

1. If an ATM call has delta 0.50 and gamma 0.05, and stock rises $2, what's the new delta?
2. Why do option sellers benefit from high theta?
3. A trader is long an ATM call with vega 0.25. If IV rises 5%, what's the approximate impact?
4. Why is gamma highest for ATM options?
5. If you buy a call and stock moves $5 in your favor, gamma made you profit more than delta alone. Explain why.

