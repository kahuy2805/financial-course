# Chapter 13 Exercises: Portfolio Management

## Exercise Set 1: Asset Allocation Design

### Exercise 1.1: Personal Risk Profile Assessment
Create your investor profile based on your circumstances:

```
YOUR PROFILE:

Personal Details:
- Age: _____
- Years to retirement: _____
- Annual income: $__________
- Current net worth: $__________
- Emergency fund (months): _____

Risk Tolerance Factors:
1. Can you handle a 30% portfolio drop without panic selling?
   ☐ Yes (High tolerance)
   ☐ Somewhat (Medium tolerance)
   ☐ No (Low tolerance)

2. Do you have income stability to weather job loss 6+ months?
   ☐ Yes (High tolerance)
   ☐ Somewhat (Medium tolerance)
   ☐ No (Low tolerance)

3. How many years until you need this money?
   ☐ 10+ years (High tolerance)
   ☐ 5-10 years (Medium tolerance)
   ☐ Under 5 years (Low tolerance)

4. Investment experience level:
   ☐ New investor (Lower initial risk)
   ☐ Experienced (Can handle volatility)
   ☐ Expert (Can use advanced strategies)

Risk Profile Result:
High tolerance = 70-80% stocks
Medium tolerance = 50-60% stocks
Low tolerance = 30-40% stocks
```

### Exercise 1.2: Design Your Allocation Model

```
Step 1: Choose Base Model
☐ Age-based: ___% stocks, ___% bonds
☐ Modern 3-fund: ___% stocks, ___% bonds, ___% alternatives
☐ Custom: Design your own

Step 2: Define Sub-Allocations
Stocks (______%):
- US Large-cap: _____% (via ETF/fund choice: ____________)
- US Small/Mid: _____% (via ETF/fund choice: ____________)
- International Developed: _____% (via: ____________)
- Emerging Markets: _____% (via: ____________)

Bonds (______%):
- US Government: _____% (via: ____________)
- US Corporate: _____% (via: ____________)
- International: _____% (via: ____________)

Alternatives (______%):
- Cash: _____% (via: Money Market)
- REITs: _____% (via: ____________)
- Commodities: _____% (via: ____________)

Step 3: Investment Vehicles
For each allocation, specify:

Position: ________________
- Type: ☐ ETF  ☐ Individual Stock  ☐ Mutual Fund
- Target %: ______%
- Target $: $__________
- Current holdings: ____________
- Action needed: ☐ Buy  ☐ Hold  ☐ Reduce  ☐ Sell

Position: ________________
- Type: ☐ ETF  ☐ Individual Stock  ☐ Mutual Fund
- Target %: ______%
- Target $: $__________
- Current holdings: ____________
- Action needed: ☐ Buy  ☐ Hold  ☐ Reduce  ☐ Sell
```

### Exercise 1.3: Allocation Backtesting

Using historical data or projection tools:

```
Test your allocation in various scenarios:

SCENARIO 1: Bull Market (stocks +20%, bonds +2%)
Starting portfolio: $100,000
- Stocks ($60,000): × 1.20 = $72,000
- Bonds ($40,000): × 1.02 = $40,800
New total: $112,800
Gain: $12,800 (12.8%)

Your allocation:
Starting: $__________
- Stocks portion: $___________ × _____ = $___________
- Bonds portion: $___________ × _____ = $___________
New total: $__________
Your gain: $__________ (____%)

SCENARIO 2: Bear Market (stocks -20%, bonds +5%)
Starting: $100,000
- Stocks ($60,000): × 0.80 = $48,000
- Bonds ($40,000): × 1.05 = $42,000
New total: $90,000
Loss: -$10,000 (-10%)

Your allocation:
Starting: $__________
- Stocks portion: $___________ × _____ = $___________
- Bonds portion: $___________ × _____ = $___________
New total: $__________
Your loss: $__________ (___%)

SCENARIO 3: Stagflation (stocks -10%, bonds -5%)
Starting: $100,000
- Stocks ($60,000): × 0.90 = $54,000
- Bonds ($40,000): × 0.95 = $38,000
New total: $92,000
Loss: -$8,000 (-8%)

Your allocation:
Starting: $__________
- Stocks portion: $___________ × _____ = $___________
- Bonds portion: $___________ × _____ = $___________
New total: $__________
Your loss: $__________ (___%)

Analysis:
Which scenario concerns you most? _____________________
Is your allocation aligned with your comfort level? ✓/✗
Adjustments needed: _________________________________
```

## Exercise Set 2: Rebalancing Strategy

### Exercise 2.1: Calculate Current Drift

```
YOUR PORTFOLIO TODAY:

Position                 Cost Basis    Current Value   % of Portfolio   Target %   Drift
_________________       __________    ____________    _____________    ______    _____
_________________       __________    ____________    _____________    ______    _____
_________________       __________    ____________    _____________    ______    _____
_________________       __________    ____________    _____________    ______    _____
_________________       __________    ____________    _____________    ______    _____

TOTAL:                  __________    ____________    100%             100%

Analysis:
Max drift: ______% (exceeds your ____% threshold? YES/NO)
Action needed: ☐ Rebalance now  ☐ Monitor until next review
```

### Exercise 2.2: Plan Rebalancing Trades

```
IF REBALANCING IS NEEDED:

Overweight positions (Sell):
Position: ________________
Current: ______%, Target: ______%, Excess: ______%
Portfolio value: $__________, Excess $: $__________
Action: Sell $__________ of __________________

Underweight positions (Buy):
Position: ________________
Current: ______%, Target: ______%, Deficit: ______%
Portfolio value: $__________, Needed $: $__________
Action: Buy $__________ of __________________

Tax Considerations:
Selling position: ________________
- Original cost: $__________
- Current value: $__________
- Gain/Loss: $__________
- Tax impact if sold: $__________ ☐ Gain (pay tax)  ☐ Loss (harvest)

Final Rebalance Plan:
TRADE 1: ☐ Sell  ☐ Buy __________________ Qty: _____ Price: $_____ Total: $______
TRADE 2: ☐ Sell  ☐ Buy __________________ Qty: _____ Price: $_____ Total: $______
TRADE 3: ☐ Sell  ☐ Buy __________________ Qty: _____ Price: $_____ Total: $______

Estimated Costs:
Trading commissions: $__________
Bid-ask spread: $__________
Total costs: $__________

Expected outcome: Back to target allocation, tax-loss harvested: ☐ Yes ☐ No
```

## Exercise Set 3: Performance Measurement

### Exercise 3.1: Calculate Sharpe Ratio

```
GATHER 12 MONTHS OF MONTHLY RETURNS:

Month      Portfolio Value    Monthly Return %
Jan        $__________        ______%
Feb        $__________        ______%
Mar        $__________        ______%
Apr        $__________        ______%
May        $__________        ______%
Jun        $__________        ______%
Jul        $__________        ______%
Aug        $__________        ______%
Sep        $__________        ______%
Oct        $__________        ______%
Nov        $__________        ______%
Dec        $__________        ______%

CALCULATIONS:

Average Monthly Return: Sum all / 12 = ______%
Annualized Return: (1 + monthly avg)^12 - 1 = ______%

Standard Deviation (monthly):
- Use Excel formula: =STDEV(range) = ______%
- Annualized volatility: Monthly SD × √12 = ______%

Risk-Free Rate (10-year Treasury yield): ______%

Sharpe Ratio = (Return - Risk-Free Rate) / Volatility
             = (______% - ______%) / ______%
             = ______%  / ______%
             = ________

Interpretation:
Your Sharpe: ______
S&P 500 benchmark Sharpe: ~0.6-0.8
Rating: ☐ Poor (< 0.5)  ☐ Below Average (0.5-1.0)  ☐ Good (1.0-2.0)  ☐ Excellent (> 2.0)
```

### Exercise 3.2: Calculate Portfolio Beta

```
PORTFOLIO HOLDINGS:

Position                Weight %    Individual Beta    Contribution
_________________      _______     _____________      _____________
_________________      _______     _____________      _____________
_________________      _______     _____________      _____________
_________________      _______     _____________      _____________

Portfolio Beta = Sum of contributions = ________

Your Portfolio Beta: ________
Market Beta (reference): 1.0

Interpretation:
Beta of 0.8 = Moves 80% as much as market (less volatile, safer)
Beta of 1.0 = Moves in sync with market (average risk)
Beta of 1.2 = Moves 120% as much as market (more volatile, riskier)

In a 20% market decline:
Expected portfolio decline = 20% × _______ (your beta) = _______%

Is this consistent with your risk tolerance? YES / NO
Adjustments needed: _________________________________
```

### Exercise 3.3: Calculate Alpha

```
YOUR RETURNS:

Portfolio return (annual): ______%
Portfolio beta: ________
Risk-free rate (10-yr Treasury): ______%
Market return (S&P 500 benchmark): ______%

CALCULATION:

Expected Return = Risk-Free Rate + Beta × (Market Return - Risk-Free Rate)
                = ______% + _______ × (______% - ______%)
                = ______% + _______ × ______%
                = ______% + ______%
                = ______%

Alpha = Actual Return - Expected Return
      = ______% - ______%
      = ________%

Interpretation:
Alpha = +2%:    Beating market by 2% (excellent!)
Alpha = 0%:     Matching market (efficient)
Alpha = -1%:    Underperforming market

Your alpha: ______%
Status: ☐ Outperforming  ☐ In-line  ☐ Underperforming

Analysis:
What's driving your performance?
_____________________________________________________________
_____________________________________________________________
```

## Exercise Set 4: Tax Efficiency

### Exercise 4.1: Tax-Loss Harvesting Opportunity Scan

```
PORTFOLIO TAX REVIEW:

Position                Cost Basis      Current Value      Unrealized Gain/Loss
_________________      __________      ____________       ___________________
_________________      __________      ____________       ___________________
_________________      __________      ____________       ___________________
_________________      __________      ____________       ___________________

LOSSES AVAILABLE FOR HARVESTING:

Loss Position: ________________  Unrealized Loss: $__________
Replacement: ________________ (different but similar)
Holding period: _____ days (If < 1 year: short-term  If > 1 year: long-term)
Tax benefit at your rate (_____%): $__________ saved

Loss Position: ________________  Unrealized Loss: $__________
Replacement: ________________
Tax benefit: $__________

Total available losses: $__________
Planned gains this year: $__________
Offset available: $__________ of $__________

Action plan:
- Harvest loss: _____________________ (Sell $__________)
- Replace with: _____________________ (Buy $__________)
- Wait 31 days before buying original back
- Expected tax savings: $__________
```

### Exercise 4.2: Asset Location Optimization

```
YOUR ACCOUNTS:

Account 1: _________________ (Type: ☐ Taxable  ☐ Traditional IRA  ☐ Roth IRA  ☐ 401k)
Current holdings:
- _________________ ______% ($__________)
- _________________ ______% ($__________)
- _________________ ______% ($__________)

Account 2: _________________ (Type: ☐ Taxable  ☐ Traditional IRA  ☐ Roth IRA  ☐ 401k)
Current holdings:
- _________________ ______% ($__________)
- _________________ ______% ($__________)
- _________________ ______% ($__________)

OPTIMIZATION ANALYSIS:

Tax-inefficient holdings in taxable accounts? (High-yield bonds, REITs)
Current: _____________________________________________
Recommended: _________________________________________
Action: ______________________________________________

Tax-efficient holdings needed in taxable accounts? (Growth stocks, low dividends)
Current: ______________________________________________
Recommended: __________________________________________
Action: _______________________________________________

OPTIMIZED ALLOCATION:

Tax-Deferred Account (401k/IRA):
- Bonds: ____% ($__________)
- REITs: ____% ($__________)
- High-dividend: ____% ($__________)

Taxable Account:
- Growth stocks: ____% ($__________)
- Dividend stocks: ____% ($__________)
- Municipal bonds: ____% ($__________)

Expected tax savings from optimization: $__________ annually
Timeline for reallocation: ________________________
```

## Exercise Set 5: Dividend Integration

### Exercise 5.1: Dividend Stock Screening

```
STOCK CANDIDATE ANALYSIS:

Candidate 1: ________________
Current Price: $________
Annual Dividend Per Share: $________
Current Yield: ______% (Calc: Dividend / Price × 100)
5-Year Dividend Growth Rate: ______%
Payout Ratio: ______% (Annual Div / Annual EPS)
Dividend History:
- 5 years ago: $________
- 3 years ago: $________
- Current: $________
- Growth rate: ______%/year

Score:
✓ Yield 2-4%: ☐ YES  ☐ NO
✓ Growth > 5%/year: ☐ YES  ☐ NO
✓ Payout ratio < 70%: ☐ YES  ☐ NO
✓ Consistent history: ☐ YES  ☐ NO

Verdict: ☐ BUY  ☐ WATCH  ☐ AVOID

Candidate 2: ________________
[Repeat analysis]

Candidate 3: ________________
[Repeat analysis]
```

### Exercise 5.2: Dividend Portfolio Build

```
YOUR DIVIDEND PORTFOLIO TARGET:

Target allocation: ______% of total portfolio = $__________
Target yield: ______%
Target annual income: $__________

Position Planning:

Position 1: ________________
- Share price: $__________
- Annual dividend: $__________
- Target allocation: ____% = $__________
- Shares to buy: ________ (= $__________ / $__________)

Position 2: ________________
- Target allocation: ____% = $__________
- Shares to buy: ________

Position 3: ________________
- Target allocation: ____% = $__________
- Shares to buy: ________

Dividend ETF: ________________
- Target allocation: ____% = $__________
- Shares to buy: ________

Total invested: $__________
Target yield: ______% × $__________ = $__________ annual income
Dividend reinvestment: ☐ Enabled  ☐ Disabled
```

## Exercise Set 6: Income Stream Analysis

### Exercise 6.1: Current Income Assessment

```
MULTIPLE INCOME STREAMS:

Stream 1: Primary Employment
- Annual income: $__________
- Job security: ☐ Stable  ☐ Moderate  ☐ Uncertain
- Growth rate: ______%/year
- 3-year projection: $__________
- Retention rate: ______% (If you left, how much would you lose?)

Stream 2: Capital Appreciation
- Current portfolio: $__________
- Target return: ______%/year
- Expected annual gain: $__________
- Contribution rate: $__________/year
- 5-year projection: $__________

Stream 3: Dividend Income
- Dividend portfolio: $__________
- Current yield: ______%
- Annual income: $__________
- Growth rate: ______%/year
- 5-year projection: $__________

Stream 4: Trading/Active Income
- Trading capital: $__________
- Target return: ______%/year
- Expected annual income: $__________
- Hours required: ______/week
- Realistic? ☐ YES  ☐ MAYBE  ☐ NO

Stream 5: Side Income
- Current: $__________/month
- Potential: $__________/month
- Effort required: ______/week
- 3-year goal: $__________

TOTAL INCOME PROJECTION:
Current annual: $__________
Stream 1: $__________ (employment)
Stream 2: $__________ (capital appreciation, reinvested)
Stream 3: $__________ (dividends)
Stream 4: $__________ (trading)
Stream 5: $__________ (side income)

Total: $__________

Realism check: Does total seem achievable? YES / NO / MAYBE
Which streams need development? _______________________
```

## Exercise Set 7: Account Scaling Timeline

### Exercise 7.1: Your 10-Year Scaling Plan

```
CURRENT STATUS:
Account value: $__________
Current stage: ☐ $5k-10k  ☐ $10k-50k  ☐ $50k-200k  ☐ $200k+

10-YEAR PROJECTION:

Year 1 Target:
- Account value: $__________
- Monthly savings: $__________
- Monthly trading profit: $__________
- Reinvestment rate: ______%

Year 3 Target:
- Account value: $__________
- Expected dividend income: $__________

Year 5 Target:
- Account value: $__________
- Multiple income streams active: ______
- Annual passive income: $__________

Year 10 Target:
- Account value: $__________
- Annual passive income: $__________
- Financial independence: ☐ YES  ☐ CLOSE  ☐ NO

MONTHLY REINVESTMENT TRACKER:

Month    Profit    Reinvest %    Reinvested $    Trading Capital
_____    $____     _____%        $____           $________
_____    $____     _____%        $____           $________
_____    $____     _____%        $____           $________
_____    $____     _____%        $____           $________

Trend: Is trading capital growing? ☐ YES  ☐ NO
Rate of growth: ______% per month average
```

### Exercise 7.2: Milestone Achievement Plan

```
MILESTONE TRACKING:

Milestone 1: $10,000 Account
- Current value: $__________
- Gap to milestone: $__________
- Months to achieve: ______
- Actions needed:
  ☐ Increase income
  ☐ Increase savings rate
  ☐ Improve trading returns
  ☐ Ensure profit reinvestment
Target completion: __________ (month/year)

Milestone 2: $50,000 Account
- Expected date: __________ (month/year)
- Estimated years from now: ______
- Required annual contribution: $__________
- Required annual return: ______%
- Feasibility: ☐ Realistic  ☐ Challenging  ☐ Very difficult

Milestone 3: $200,000 Account
- Expected date: __________ (month/year)
- Estimated years from now: ______

Milestone 4: $500,000 Account
- Expected date: __________ (month/year)
- Estimated years from now: ______

Milestone 5: Financial Independence
- Target passive income needed: $__________/month
- Current passive income: $__________/month
- Gap: $__________
- Years to achieve: ______
```

## Final Project: Comprehensive Portfolio Plan

### Create Your Portfolio Playbook

Compile the following into a single document:

```
1. Asset Allocation Plan
   - Your chosen allocation with justification
   - Holdings list with percentages
   - Rebalancing schedule (annual/quarterly/threshold)

2. Tax Strategy
   - Asset location plan (what goes in which account)
   - Tax-loss harvesting opportunities
   - Estimated annual tax liability

3. Income Generation Plan
   - Dividend portfolio target
   - Expected annual dividend income by year
   - Trading strategy income target
   - Side income plans

4. Performance Tracking
   - Monthly tracking spreadsheet template
   - Key metrics to monitor (Sharpe, Alpha, Beta)
   - Benchmark selection and justification

5. Scaling Timeline
   - 5-year projection with milestones
   - Account growth targets
   - Income growth targets
   - Financial independence date estimate

6. Risk Management
   - Position sizing rules
   - Stop-loss strategy
   - Portfolio insurance plan
   - Emergency fund plan

7. Annual Review Checklist
   - Rebalancing review
   - Performance evaluation
   - Tax planning for next year
   - Allocation adjustment if needed
   - Income target review

This playbook becomes your road map for the next 5-10 years.
Review quarterly, update annually.
```

## Summary

These exercises transform concepts into action. The goal is not perfection—it's progress. Complete each section honestly and use your answers to guide investment decisions over the next months and years.

Key principle: **A simple plan executed consistently beats a perfect plan executed randomly.**
