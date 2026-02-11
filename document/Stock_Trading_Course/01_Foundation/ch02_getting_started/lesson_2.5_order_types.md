# Lesson 2.5: Market Orders vs Limit Orders vs Stop Orders

[← Back to Chapter 2](README.md) | [Next Lesson: Understanding Bid-Ask Spread →](lesson_2.6_bid_ask_spread.md)

---

## Overview

In the last lesson, you learned to place a "market order." But there are other order types that give you more control over execution price and risk. This lesson explains the three most common order types and when to use each one. You'll learn to match the right order type to your trading situation.

**Time to complete:** 15-20 minutes

---

## Prerequisites

- Completed Lessons 2.1-2.4 (understand brokers, accounts, quotes, and how to trade)
- Understand bid-ask spread (price difference between buyers and sellers)
- Comfortable with basic trading process

---

## Core Content

### Why Order Types Matter

Think of order types like different ways to buy a car:

**Market Order:** "I want this car NOW, whatever price the dealer asks"
- Immediate, but price unknown until deal closes

**Limit Order:** "I want this car BUT only if the price is $20,000 or less"
- You control the price, but might not get the car

**Stop Order:** "I want to sell this car IF the price drops to $15,000"
- Protects against big losses if price crashes

Each has different purposes. Choosing the right one matters.

### 1. Market Order (The Default)

**What It Is:**
An order to buy or sell AT WHATEVER THE CURRENT MARKET PRICE IS, executed immediately.

**How It Works:**

You decide to buy Apple:
1. You place a Market Order: "Buy 10 shares of AAPL"
2. Your broker immediately executes
3. You get shares at the current asking price (whatever it is right now)
4. Order fills within seconds

**Real Example:**
- You see Apple bid-ask: $195.47 - $195.48
- You place Market Order to buy
- Actually fills at $195.50 (price moved slightly while processing)
- You got your shares instantly, but price was slightly higher

**Advantages:**
- **Guaranteed execution** - You WILL get the stock (if liquid)
- **Fast** - Executes within seconds
- **Simple** - No complexity, just buy/sell
- **Good for** - Stocks with high volume (easy to fill)
- **Best for** - Your first few trades while learning

**Disadvantages:**
- **Price uncertainty** - Exact price unknown until execution
- **Slippage** - Actual price might be worse than quoted
- **Bad in volatile markets** - Price can move significantly while order processes
- **Not good for** - Expensive stocks with large spreads, low-volume stocks, or volatile times

**When to Use:**
- Buying quality stocks with good volume (like AAPL, MSFT, GOOGL)
- You want immediate execution (buying ASAP)
- Markets are calm and not volatile
- Stock spread is very tight (small difference between bid-ask)

**When NOT to Use:**
- Stock has low trading volume (illiquid)
- Market is very volatile (prices moving rapidly)
- Exact price matters to you
- Buying small, speculative companies
- During earnings announcements or news events

**Example Trade:**

```
Stock: Apple (AAPL)
Current Price: $195.48 (asking price)
Your Order: Market order, buy 100 shares

What Happens:
- You submit order at 2:47 PM
- Order reaches exchange at 2:47:001 PM
- Price is now $195.52 (moved up slightly)
- Broker buys your 100 shares at $195.52
- You pay $19,552 instead of expected $19,548
- Difference: $4 (slippage)
- Completely normal!
```

### 2. Limit Order (The Controlled Order)

**What It Is:**
An order to buy or sell, BUT ONLY at a specified price or better.

**How It Works:**

You want to buy Apple, but you think $195 is the max you'll pay:
1. Place Limit Order: "Buy 10 shares of AAPL at $195.00 or less"
2. If price drops to $195 or lower, order fills automatically
3. If price never reaches $195, order never fills (you don't buy)

**Real Example:**
- Apple is at $195.48
- You place: "Buy 10 shares, limit price $195.00"
- Price drops to $194.95 during the day
- Your order fills at $194.95
- You paid less than market price!

**Advantages:**
- **Price control** - You choose maximum (buy) or minimum (sell) price
- **Better executions** - Often get better prices than market orders
- **No slippage** - Price won't be worse than your limit
- **Good for** - Expensive stocks, volatile stocks, limit buy/sell prices
- **Best for** - Experienced traders, specific price targets

**Disadvantages:**
- **No guarantee** - Order might never fill if price doesn't reach your limit
- **Missed opportunities** - Stock might go up and you don't buy
- **Partial fills** - Might buy 10 of your 100 share order (stock too illiquid)
- **Complexity** - More to think about than market orders

**When to Use:**
- You have a specific price in mind
- Trying to buy cheaper than current market
- Trying to sell higher than current market
- Stock is volatile (prices change rapidly)
- Stock has low volume (need to control price)
- Large orders that might move the market

**When NOT to Use:**
- You need immediate execution
- Stock is very illiquid (might never fill)
- Trading during fast-moving markets
- First-time traders (adds complexity)
- Stock spreads are very tight (limit adds little value)

**Buy Limit Order Example:**

```
Stock: Apple (AAPL)
Current Market Price: $195.48
Your Limit Order: Buy 10 shares at $194.50 or less

Scenarios:
A) Price drops to $194.45 → Order fills at $194.45 (great!)
B) Price stays at $195+ → Order never fills (you don't buy)
C) Price drops to $194.45 then bounces to $195 → You own 10 @ $194.45
```

**Sell Limit Order Example:**

```
Stock: Apple (AAPL)
Current Market Price: $195.48
Your Limit Order: Sell 10 shares at $200.00 or higher

Scenarios:
A) Price rises to $200.50 → Order fills at $200.50 (great!)
B) Price drops to $190 → Order never fills (you still own stock)
C) Price rises to $200.05 → Order fills at $200.05
```

**Common Limit Strategies:**

**Strategy 1: Buy the Dip**
- Stock usually trades at $100
- Currently down to $95 on news
- Place limit: "Buy at $92"
- If it drops further, you get it cheap
- If it bounces back, order doesn't fill but you weren't forced to overpay

**Strategy 2: Sell at Target**
- You bought stock at $50
- Goal is to sell at $75 (50% profit)
- Place limit: "Sell at $75"
- When stock reaches $75, automatically sells
- You don't have to watch constantly

**Strategy 3: Scaling In**
- Want to buy 100 shares of stock
- Think price might drop gradually
- Place 4 limit orders:
  - Buy 25 @ $95
  - Buy 25 @ $90
  - Buy 25 @ $85
  - Buy 25 @ $80
- As price drops, you accumulate gradually

### 3. Stop Order (The Protective Order)

**What It Is:**
An order that becomes a market order when the stock price reaches a specific price (the "stop price").

**Think of it like:** Setting a trap that springs when price hits a certain level.

**How It Works:**

You own Apple at $195. You're worried it might crash, so you set a safety net:
1. Place Stop Order: "If AAPL drops to $180, sell my shares at market price"
2. Stock stays above $180 → Nothing happens, order sits
3. Stock drops to $180 → Order automatically becomes market order
4. Shares sell immediately (protecting against further drop)

**Real Example:**
- You bought Apple at $195
- Current price: $198 (you're up $3)
- You set a stop at $185 (willing to accept $10 loss)
- Stock soars to $210 → Stop order sits (you're protected)
- Breaking news hits, stock crashes to $182 → Stop order triggers
- Your shares sell at market price (maybe $181.50)
- You limited loss to about $13.50 instead of unlimited loss

**Advantages:**
- **Loss protection** - Prevents catastrophic losses
- **Emotional protection** - Remove temptation to hold falling stock
- **Sleep at night** - Know your maximum loss
- **Automatic** - Works even if you're not watching
- **Good for** - Protecting profits, limiting losses

**Disadvantages:**
- **Stop loss triggers** - Temporary dips can trigger exit (annoying!)
- **Whipsaw effect** - Stop hits, sell, then stock rebounds (regret!)
- **Gap risk** - Stock might gap past your stop (sell at much worse price)
- **Emotional exits** - Limits help, but might exit good long-term holdings
- **Complexity** - More to think about

**When to Use:**
- You own a stock and want downside protection
- Protecting profits (taking profits off table)
- Limiting losses on risky positions
- Can't monitor stock (goes on vacation, busy)
- Trading volatile stocks where big moves are common

**When NOT to Use:**
- Buying stock (place stop after you own it)
- Very volatile stocks (stops might trigger on normal swings)
- Long-term holdings in good companies (don't want to exit on dips)
- Thinly traded stocks (might execute at terrible prices)

**Stop Order Example 1: Protect Profit**

```
Stock: Microsoft (MSFT)
You bought at: $300
Current price: $320 (you're up $20)
Stop order: Sell if drops to $310

Scenarios:
A) Price rises to $330 → Stop sits, you keep gaining
B) Price drops to $310 → Automatic sell at market
   → You lock in at least $10 profit
C) Price drops to $308 → Sell triggers at maybe $307
   → You keep most of your profit
```

**Stop Order Example 2: Limit Loss**

```
Stock: Risky Company (RISKY)
You bought at: $50
Current price: $52 (up $2)
Stop order: Sell if drops to $45

Scenarios:
A) Price rises to $70 → Stop sits, up $20
B) Disaster news, stock crashes to $30
   → Stop at $45 triggers
   → Sell at market price (maybe $44)
   → You limited loss to $6 instead of $20
```

### Stop-Limit Order (Advanced)

**What It Is:**
Combination of stop and limit orders. Becomes a limit order (not market order) when triggered.

**How It Works:**
"If stock drops to $180, sell 10 shares BUT ONLY at $178 or higher"

**Advantage:** Better control of exit price (not forced to sell at market)
**Disadvantage:** Might not fill if stock gaps past limit price

**When to Use:** Protecting positions in volatile stocks where you care about exit price
**When NOT to Use:** If protecting downside, accept worst price (use regular stop)

**Advanced:** We'll skip this for beginners.

### Order Type Comparison Chart

| Feature | Market | Limit | Stop |
|---------|--------|-------|------|
| **Execution Speed** | Immediate | Might wait | Immediate (when triggered) |
| **Price Control** | No | Yes | No |
| **Guarantee Fill** | Almost always | No | Yes (when triggered) |
| **Best For** | Immediate entry/exit | Specific prices | Loss protection |
| **Risk** | Slippage | Missed opportunity | Emotional exits |
| **Complexity** | Simple | Moderate | Moderate |
| **Beginner-friendly** | YES | Okay | Okay |

---

## Real-World Application

### Michael's Trading Decisions

**Scenario 1: Buying a Great Company**
Michael researches Apple and decides to buy.
- Apple is highly liquid
- He wants to enter immediately
- Spreads are tight (bid-ask difference tiny)
- **Decision:** Market order
- **Why:** Volume is high, slippage will be tiny, immediate execution is better

**Scenario 2: Buying a Cheaper Stock**
Michael likes Acme Corp but thinks $30 is too high.
- Current price: $31.50
- He believes it might drop to $28
- Willing to wait for better entry
- **Decision:** Limit order at $28
- **Why:** More patient, wants better price, willing to miss trade if price doesn't drop

**Scenario 3: Protecting a Profit**
Michael bought Tesla at $200, now at $250 (up $50).
- Market is volatile
- Earnings coming up (risky event)
- Wants to protect gains
- **Decision:** Stop order at $220 (willing to give back $30 to protect $30)
- **Why:** Protects profit, limits downside risk, sleeps better

**Scenario 4: Volatile Stock Purchase**
Michael wants to buy a small biotech stock.
- Stock is volatile (price swings wildly)
- Low volume (hard to trade)
- Tight execution is important
- **Decision:** Limit order at exact price he'll pay
- **Why:** Controls slippage in volatile, illiquid environment

### Janet's Learning Journey

**Week 1:**
Janet buys first stock (Apple) with market order.
- Got shares immediately
- Slippage was only $0.05 (negligible)
- Good experience

**Week 2:**
Janet sees discount company priced at $45.
- She researches and thinks it's worth $40
- Places limit order at $40
- Waits 3 days
- Stock drops to $39.50, her order fills
- She's happy she got better price

**Week 3:**
Janet is nervous stock market is getting risky.
- She owns 100 shares at $95
- Places stop order at $80 (willing to give back $15 max)
- Stock drops to $81 next day
- Stop triggers
- She sells at $80.50
- Relieved she protected most of her position

**Learning:** Janet discovered that order types matter. Different situations call for different orders.

---

## Common Mistakes to Avoid

### Mistake #1: Using Limit Orders for Fast-Moving Stocks
**Reality:** If you want to buy a stock that's rising fast, your limit might never fill. Market order is better.

### Mistake #2: Stop Losses Too Tight
**Reality:** Normal stock volatility might trigger your stop, forcing you to sell good stock at bottom. Use 5-10% stop, not 2-3%.

### Mistake #3: Stop Orders on Short-Term Moves
**Reality:** If holding stock long-term, don't use stops on normal daily swings. You'll exit good holdings on temporary dips.

### Mistake #4: Assuming Limit Orders Will Definitely Get Better Prices
**Reality:** Limit orders might not fill if price doesn't reach your limit. Sometimes market order is more efficient overall.

### Mistake #5: Not Canceling Old Limit Orders
**Reality:** Old limit orders sitting in your account might fill unexpectedly. Cancel orders you don't plan to fill.

### Mistake #6: Setting Stop Losses Right Below Support Levels
**Reality:** Smart traders know where others' stops are. Stock might dip below support to trigger stops, then bounce. Use stops just beyond noise.

### Mistake #7: Using Stop Orders Expecting Exact Price
**Reality:** Stop becomes market order when triggered. You might sell at much worse price if stock gaps down. Accept this risk.

---

## Quick Review

**Key Takeaways:**

**Market Order:**
- Buy/sell immediately at current price
- No price control, but guaranteed execution
- Best for: Beginner first trades, liquid stocks, immediate entry/exit needed
- Avoid when: Stock is illiquid, volatile, or has wide spreads

**Limit Order:**
- Buy/sell ONLY at specified price or better
- Price control, but not guaranteed to fill
- Best for: Specific price targets, illiquid stocks, patient traders
- Avoid when: Need immediate execution, stock is very illiquid

**Stop Order:**
- Becomes market order when price hits "stop price"
- Protects against losses or locks in profits
- Best for: Loss protection, protecting profits, risk management
- Avoid when: Already holding long-term without exits planned

**Selection Logic:**
1. **Buying quality stock immediately?** → Market order
2. **Buying, but want better price?** → Limit order
3. **Own stock, want to protect against big drop?** → Stop order
4. **Own stock, want to lock in profit?** → Stop order

---

## Practice Exercise

### Exercise 1: Match Orders to Situations
For each situation, choose the best order type (Market, Limit, or Stop):

1. You want to buy Apple right now
   → _____________

2. You bought Tesla and want to protect against drop
   → _____________

3. You want to buy a cheaper stock but only at a lower price
   → _____________

4. You're selling stock to buy something else immediately
   → _____________

5. You set a profit target of 20% gain
   → _____________

### Exercise 2: Order Type Scenarios
Write down what would happen:

**Scenario 1:**
- Stock trading at $100
- You place market order to buy
- What will happen?
- Why?

**Scenario 2:**
- Stock trading at $100
- You place limit order to buy at $95
- Stock never reaches $95
- What will happen?

**Scenario 3:**
- You own stock at $100
- Stock drops to $95
- You have stop order at $90
- What happens?

### Exercise 3: Plan Your Orders
Plan your next 3 trades. For each:
1. Stock to buy/sell (ticker)
2. Action (buy or sell)
3. Order type (market, limit, or stop)
4. Why you chose this order type
5. Limit price or stop price (if applicable)

### Exercise 4: Risk Management
Create a simple rule for yourself:

"I will use stop orders to protect positions when _______________"

Think about when you'd want loss protection.

### Exercise 5: Paper Trade Different Orders
Using paper trading on your broker:
1. Place a market order (buy 10 shares of any stock)
2. Place a limit order (try to buy at lower price)
3. Place a stop order (create protection level)
4. Watch what happens
5. See which fills, which doesn't
6. Understand execution in real time

---

## Next Steps

Congratulations! You now understand the three main order types and when to use each.

**In the next lesson**, you'll learn:
- Bid-ask spread (what it is and why it matters)
- Liquidity and how it affects your trades
- How to calculate costs in your trading

### Before Moving Forward:
- [ ] Understand market orders
- [ ] Understand limit orders
- [ ] Understand stop orders
- [ ] Know when to use each
- [ ] Know advantages/disadvantages of each
- [ ] Can match order types to situations

**Ready to continue?** → [Lesson 2.6: Understanding Bid-Ask Spread and Liquidity](lesson_2.6_bid_ask_spread.md)

---

## Additional Resources

**For Deeper Learning** (Optional):
- Investopedia - Order Types Guide
- Your broker's help section (detailed for their platform)
- FINRA.org - Order types and execution
- YouTube: "How to use limit orders" "How to use stop orders"
- Paper trade to practice different orders risk-free

---

**Remember:** Different situations need different order types. Market orders are simplest but limit and stop orders give you control. As you gain experience, you'll naturally use all three.

---

[← Back to Chapter 2](README.md) | [↑ Back to Course Index](../../MASTER_INDEX.md) | [Next Lesson →](lesson_2.6_bid_ask_spread.md)

---

*Lesson 2.5 Complete | Next: Lesson 2.6 - Understanding Bid-Ask Spread and Liquidity*
