# Lesson 9.5: Risk Management During Earnings and News

## Learning Objectives
- Understand earnings-related price risks
- Manage positions through earnings announcements
- Apply news-based risk strategies
- Plan position management for major catalysts

## Why Earnings Create Risk

### Types of Earnings Risk

```
Earnings announcement = Binary event
- Positive earnings: Stock can gap up 5-30%
- Negative earnings: Stock can gap down 5-30%
- Beat estimates: Potential 10-20% move
- Miss estimates: Potential 10-30% move

Gap risk explained:
- Trading stops at 4:00 PM Friday
- Earnings release: After market close 4:30 PM
- Overnight: 17 hours with no ability to trade
- Market open 9:30 AM: First chance to sell/buy
- Gap: Jump from Friday close to next open
- Example: Friday close $100, Friday earnings miss
- Monday open: $85 (-15%) due to gap

Why gaps hurt:
- Your stop loss might be $95
- Gap opens at $85, bypasses your stop
- You exit at $85 instead of $95
- Loss: Additional $500 (10 shares × $10)
- Broker cannot fill your stop at $95 (market closed!)

Implied move calculation:
- At-the-money (ATM) options price the expected move
- High implied volatility = Large expected move
- Options 10% away = Market expects 10% move possible
- If IV on 50 call = 15%, market expects ~15% move
```

## Managing Positions Through Earnings

### Strategy 1: Exit Before Earnings

**Safest approach - eliminate binary risk:**

```
Position: Long AAPL swing trade
Entry: $180 (cost $9,000 for 50 shares)
Current: $185 (+$250 profit)
Earnings date: Thursday after market close

Management plan:
- Monday-Wednesday: Hold position, let it work
- Wednesday close: Position now at $187 (+$350 profit)
- Decision: Exit before earnings risk
- Execute: Sell 50 shares at $187.00
- Profit taken: +$350 (3.9% return)
- Avoid risk: Don't hold through Thursday earnings

Outcome comparison:

Scenario A: Exit Wednesday (+$350):
- Safe: Locked in profit
- Regret risk: If AAPL rallies 10% Friday
  - Would have been +$1,200 profit
  - But took only +$350 (missed upside)

Scenario B: Hold through earnings:
- Upside risk: +10% = +$1,200 profit (GREAT!)
- Downside risk: -15% gap = -$1,350 loss (TERRIBLE!)
- Risk-reward: Not favorable (potential loss > gain)

Decision:
- Exit if profit already captured (lock it in)
- Hold if target not reached (need to run)
- Exit if stop loss too close to earnings (gap risk high)

Rule of thumb:
- Profit reached: EXIT (lock gains before binary event)
- Target not reached: HEDGE or EXIT (don't want to risk profit)
- Loss position: EXIT (reduce risk, no reason to hold)
```

### Strategy 2: Hedge With Protective Put

**Keep position but buy insurance:**

```
Position: Long 100 MSFT at $350 (cost $35,000)
Current: $365 (+$1,500 profit)
Earnings: Monday after close

Hedge setup:
- Buy put option at $355 strike
- Cost: $1.50 per share = $150 total (0.43% of position)
- Protection: Limits loss below $355
- Expiration: Tuesday (after earnings)

Outcome scenarios:

Scenario A: Positive earnings, gap to $380
- Stock at $380 (+$3,000 gain)
- Put expires worthless (-$150 loss)
- Net: +$2,850 profit (7.6% on $35K)

Scenario B: Negative earnings, gap to $330
- Stock at $330 (-$2,000 loss)
- Put worth $2,500 (protection at $355)
- Net: -$1,500 + $2,500 put = +$500 profit!
- Insurance worked perfectly

Scenario C: Neutral earnings, close at $360
- Stock at $360 (+$500 gain)
- Put expires worthless (-$150)
- Net: +$350 profit (0.9% on $35K)

Cost of insurance:
- Put premium: $150 (0.43% cost)
- Worth it if: Potential loss > insurance cost
- If lose 10% = $3,500 loss vs. $150 insurance cost
- Insurance ROI: 23:1 (excellent risk-reward)

When to use puts:
- Position very large (20%+ of portfolio)
- Earnings surprise likely (bad history?)
- Can't stomach 10%+ gap loss
- Want to hold position despite earnings
```

### Strategy 3: Reduce Position Size

**Take partial profits, reduce risk:**

```
Position: Long 100 AAPL at $100 (cost $10,000)
Current: $110 (+10% = +$1,000 profit)
Earnings: Wednesday after market close
Time holding: 2 weeks

Decision: Reduce before earnings risk

Partial exit:
- Sell 50 shares at $110 = $5,500 proceeds
- Lock in: +$500 profit (50 shares × $10)
- Remaining: 50 shares at cost basis $100
- New risk: Only $5,000 at risk

New position structure:
- 50 shares still working for more upside
- Already profitable $500 (captured some gains)
- Reduced risk: Only 50 shares now exposed to gap

Gap scenarios now:

Positive earnings (+10% = $121):
- Remaining 50 shares: +$1,050 profit
- Total profit: +$500 (locked) + $1,050 (remaining) = +$1,550
- Total return: +15.5% on original $10,000

Negative earnings (-15% = $85):
- Remaining 50 shares: -$750 loss
- Total: +$500 (locked) - $750 (remaining) = -$250 loss
- Total return: -2.5% on original $10,000
- Much better than -$1,500 total loss!

Benefits:
- Locked in some profit ($500)
- Still participate in upside (50 shares remaining)
- Reduced downside risk (only 50 shares at risk)
- Psychological comfort (already won something)
```

### Strategy 4: Straddle Position

**Play the move either direction:**

```
Position: Uncertain direction after earnings
Want to profit: Whether stock goes up OR down
Setup: Buy both call and put option

Example: TSLA earnings Thursday
Current stock: $850
IV rank: 85th percentile (high implied volatility)
Expected move: ±8% ($68 either direction)

Buy straddle:
- Buy $850 call = $5.00 cost
- Buy $850 put = $4.50 cost
- Total cost: $9.50 per share × 100 = $950
- Breakeven up: $850 + $9.50 = $859.50
- Breakeven down: $850 - $9.50 = $840.50

Outcome scenarios:

Positive earnings, gap to $920:
- Call profit: $920 - $850 = $70
- Put loss: -$4.50
- Net: +$70 - $4.50 = +$65.50
- Profit: +$6,550 (690% on $950 cost!)

Negative earnings, gap to $780:
- Call loss: -$5.00
- Put profit: $850 - $780 = $70
- Net: $70 - $5.00 = +$65.00
- Profit: +$6,500 (684% on $950 cost!)

Sideways earnings, close at $850:
- Both expire worthless
- Loss: -$950 (100% loss)

Risk-Reward:
- Max loss: $950 (both options expire worthless)
- Max profit: Unlimited if stock moves 10%+ either way
- Cost: 1.1% of stock price ($950 on $85,000 position)

When to use:
- High IV (expensive, rewards movement)
- Large expected move (more than straddle cost)
- Earnings shock likely (up or down)
- Don't care about direction, just want movement

Warning:
- Options trading for beginners is risky
- Save straddles for later experience
- Start with simple strategies (exit/reduce)
```

## Pre-Earnings Risk Checklist

### Before Every Earnings Announcement

```
30 days before earnings:
☐ Note earnings date in calendar
☐ Assess: Is position thesis still valid?
☐ Check: Analyst expectations (beat/miss history?)
☐ Review: Recent company news (positive/negative?)
☐ Calculate: Expected move (implied volatility)

14 days before earnings:
☐ Decide: Hold through earnings? (Y/N)
☐ Plan: Exit timing (Friday before? Thursday?)
☐ Measure: Current profit/loss vs. earnings risk
☐ Set: Profit target before earnings date
☐ Set: Stop loss if holding through earnings

3 days before earnings:
☐ Confirm: Earnings date/time confirmed?
☐ Check: Any news? Any pre-announcements?
☐ Decide: FINAL decision - hold or exit?
☐ If holding: Reduce position size? (Y/N)
☐ If hedging: Options strategy chosen?

1 day before earnings:
☐ Verify: Stop losses set correctly
☐ Alert: Email alert 30 mins before close
☐ Plan: What if gaps down 10%? 15%?
☐ Plan: What if gaps up 15%? 20%?
☐ Mental: Prepare for any outcome
☐ Documentation: Journal entry pre-earnings

Earnings day (before announcement):
☐ Final check: All stops/alerts active?
☐ After hours: Set alerts for stock price
☐ Next morning: Check gap open (pre-market)
```

## Post-Earnings Position Management

### Managing the Gap Open

```
Scenario: AAPL reported earnings, gapped down overnight
- Friday close: $190
- Earnings: Missed expectations (bad news)
- Monday pre-market: $168 (-11.6% gap)

Your position:
- Own 50 shares at $190 entry (cost $9,500)
- Stop loss was $185 (never triggered overnight)
- Gap open: $168 (well below stop)
- Current loss: -$1,100 (-11.6%)

Monday morning actions:

Option 1: Panic sell at open
- Pre-market shows $168, click market sell
- Risk: Further gaps down to $165-$167
- Loss: Potentially -12-13%
- NOT RECOMMENDED (reactive, emotion-based)

Option 2: Wait for stabilization
- Let stock find support in first 30 minutes
- Often gaps down 11%, recovers to 8% down
- Sell when it stabilizes, not at worst point
- Better fill: $170-$172 (better than $168)
- Action: Place limit order to sell at $175 (or better)

Option 3: Accept loss, move forward
- Thesis broken by negative earnings
- No reason to hold further
- Market sell to clear position
- Liquidate within first hour
- Move capital to better opportunity
- Lock in loss (-$1,100)
- Accept and rebuild

Option 4: Wait for recovery attempt
- Stock hits bottom at $165 (15% below entry)
- Recovers some through day to $170
- Wait to see if bounces further
- Sell on strength, not at worst price
- This is gambling, not recommended

Recommended:
- Accept reality of bad earnings
- Sell within first 30-60 minutes
- Don't add to position (averating down)
- Move on and rebuild capital
- Loss is real, but acceptable (-11.6%)
```

## Non-Earnings News Risk

### Types of News Events

```
Major news categories affecting stocks:

Company-specific:
- FDA approval (biotech)
- Product launch (tech)
- CEO change (any company)
- Lawsuit/investigation (financial impact)
- Supply chain issues (operational impact)

Sector-wide:
- Interest rate change (affects all rates-sensitive)
- Regulatory change (affects entire sector)
- Commodity price move (affects materials, energy)
- Currency move (affects exporters)

Market-wide:
- FOMC meeting / Fed announcement
- Jobs report / Economic data
- Trade war news
- Geopolitical tensions

Risk levels:
- Minor news: <2% price move expected
- Medium news: 2-5% price move expected
- Major news: 5-15% price move expected
- Crisis: 15%+ price move expected
```

### Managing News Risk

```
Light news event (FDA decision Monday):
- Your position: BIOPHARMACEUTICAL STOCK
- Timeframe: Swing trade (3-5 days)
- Entry: 2 days ago at $100, now $102

Decision: Hold through news?
- Upside if approved: +5-10%
- Downside if rejected: -10-15%
- Risk asymmetry: More downside than upside
- Decision: EXIT before news (lock in +$100 profit)

Heavy news event (Fed rate decision Wednesday):
- Your position: Bank stock (interest rate sensitive)
- Timeframe: Longer swing trade (5-14 days)
- Entry: 3 days ago, position +2%

Decision: Hold through Fed?
- Market uncertainty: High (VIX likely to spike)
- Expected move: 2-4% either direction
- Time to target: Still 1-2 weeks needed
- Decision: REDUCE SIZE (hedge), don't exit
  - Sell 50% position (lock 1% gain)
  - Hold 50% for potential 5%+ move
  - Risk: No longer exposed if Fed negative

Crisis event (Geopolitical shock):
- Your position: General market positions
- Timeframe: Various
- Market impact: 5-15% likely

Decision: Immediate action needed
- Markets may close, reopen lower
- Exit all positions immediately (priority 1)
- Don't hold through uncertainty
- After calm: Reassess and rebuild
- Better to give back 2% than lose 10%+ on gap
```

## Managing Position Through Earnings: Case Study

### Real Example: Netflix Earnings Swing Trade

```
Setup:
- Netflix NFLX trading $400 (cost: 50 shares = $20,000)
- Swing trade setup identified (pullback in uptrend)
- Entry: Friday Jan 15 at $400
- Target: $420 (+5%)
- Stop loss: $380 (-5%)
- Earnings announced: Wednesday Jan 20 after market close

Week 1 (Jan 15-19):
- Mon: $402 (hold, moving up)
- Tue: $408 (hold, approaching target range)
- Wed morning: $412 (decision time!)
- Decision: Exit before earnings risk

Exit decision logic:
- Profit so far: +$600 (3%)
- Target: $420 (+5% = +$1,000)
- Days to earnings: Same day
- Risk: Gap 10% down = -$2,000
- Risk asymmetry: 2:1 against us
- Best decision: LOCK PROFIT

Execution:
- Sell 50 shares NFLX at $412
- Profit taken: +$600 (3% on $20,000)
- Risk eliminated: Zero overnight risk
- Outcome: Mission accomplished

What happened after:
- Wed after-hours earnings: Missed expectations
- Thu pre-market: $365 (down -8.75%)
- Avoided gap down disaster!
- Would have been: -$1,750 loss if still holding

Journal entry:
- Trade profit: +$600
- Hold time: 4 days
- Opportunity cost: Missed upside if rallied after earnings
- Decision quality: EXCELLENT (got paid and eliminated risk)
- Learning: Exit before binary events, don't gamble
```

## Summary

Managing earnings and news risk requires:
- Identifying earnings dates and planning ahead
- Exiting profitable positions before earnings (simplest)
- Hedging with protective puts if keeping position
- Reducing position size as risk management
- Preparing for gap opens (emotionally and tactically)
- Understanding expected moves (implied volatility)
- Avoiding over-leveraged positions through earnings

Key principle: Profit protection beats profit maximization.

## Key Takeaways

1. Earnings = Binary events with 5-30% gap potential
2. Stop losses don't protect gaps (market closed overnight)
3. Exit before earnings is safest strategy
4. Protect profit before binary events
5. Hedge with puts if large position and bullish
6. Reduce size before earnings to cut risk
7. Plan gap responses before they happen
8. Accept losses from bad earnings immediately
9. Don't try to bottom-fish after gaps
10. Rebuild capital, don't revenge trade

## Next Steps

- Build earnings calendar into trading plan
- Make decision rules: Hold or exit?
- Practice gap management mentally
- Review past earnings trades in journal
- Set up alerts for earnings dates 30 days ahead
