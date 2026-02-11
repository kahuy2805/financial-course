# Lesson 13.3: Measuring Portfolio Performance

## Overview
Numbers don't lie. Understanding how to measure portfolio performance objectively removes emotion and helps you track what's actually working. Three metrics matter most: Sharpe Ratio, Alpha, and Beta.

## The Fundamental Metric: Total Return

### Simple Return Calculation
```
Total Return % = (Ending Value - Beginning Value) / Beginning Value × 100

Example:
Portfolio Value Jan 1:      $100,000
Portfolio Value Dec 31:     $110,000
Dividends/Interest Received: $2,000

Total Return = ($110,000 - $100,000 + $2,000) / $100,000
             = $12,000 / $100,000
             = 12%
```

### Time-Weighted Return (TWR)
**When you make deposits/withdrawals, use TWR:**

```
Portfolio:
Jan 1:   $100,000 → Jan 31: $105,000 (5% return)
Feb 1:   Deposit $20,000 → Now worth $125,000
Feb 28:  $125,000 → Mar 1: $130,000 (4% return)

TWR = (1.05 × 1.04) - 1 = 9.2%

(Not just simple 30,000/120,000 = 25%, which includes
the deposit, not just investment performance)
```

### Money-Weighted Return (MWR)
**Account for timing of deposits/withdrawals:**

```
Example:
Jan 1:  Invest $100,000 → Earn 10% → $110,000
Jul 1:  Deposit $50,000 → Now $160,000 → Earn 5% → $168,000

MWR accounts for fact that second deposit
only earned 5% for 6 months, not full year
```

## Sharpe Ratio: Risk-Adjusted Returns

### Definition
```
Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Portfolio Standard Deviation

Measures: How much excess return you get per unit of risk taken
```

### Calculation Example
```
Portfolio Return (annual):           12%
Risk-Free Rate (10-year Treasury):   4%
Portfolio Standard Deviation:        15%

Sharpe Ratio = (12% - 4%) / 15%
             = 8% / 15%
             = 0.53

Interpretation: For each unit of risk, you earn 0.53 units of return
```

### Sharpe Ratio Interpretation
```
Sharpe Ratio    Interpretation                Quality
< 0.5           Poor (negative returns or high volatility)
0.5 - 1.0       Below average
1.0 - 2.0       Good (typical for balanced portfolios)
2.0 - 3.0       Excellent
> 3.0           Outstanding (rare for individual investors)

Comparison Benchmarks:
S&P 500:        ~0.6-0.8
US Bonds:       ~0.3-0.5
Your Target:    > 1.0 (better than just stock market)
```

### Why Sharpe Ratio Matters
```
Scenario A: Stock Portfolio
Return: 20%
Volatility: 25%
Sharpe: 0.64

Scenario B: Balanced Portfolio
Return: 12%
Volatility: 10%
Sharpe: 0.80

Scenario B looks inferior (lower return)
But Scenario B is superior risk-adjusted
(better returns per unit of risk)
```

### Calculating Your Own Sharpe Ratio

**Step 1: Gather Monthly Returns**
```
Month    | Portfolio Value | Monthly Return %
Jan      | $100,000        | --
Feb      | $101,200        | +1.2%
Mar      | $99,500         | -1.7%
Apr      | $102,300        | +2.8%
...      | ...             | ...
Dec      | $112,000        | +0.8%
```

**Step 2: Calculate Average Return**
```
Monthly returns: +1.2%, -1.7%, +2.8%, +0.5%, ...
Average Monthly Return = Sum / 12 months
Example: 0.8% monthly average
Annual Return = (1.008^12 - 1) × 100 = 9.97%
```

**Step 3: Calculate Standard Deviation**
```
Use Excel/Google Sheets: =STDEV(range of monthly returns)
Example: Monthly Std Dev = 2.1%
Annualized = 2.1% × √12 = 7.27%
```

**Step 4: Calculate Sharpe Ratio**
```
Sharpe = (9.97% - 4%) / 7.27%
       = 5.97% / 7.27%
       = 0.82
```

## Beta: Correlation to Market

### Definition
```
Beta = Measures how much a stock/portfolio moves relative to the market

Beta = 1.0:   Moves in perfect sync with market
Beta > 1.0:   More volatile than market
Beta < 1.0:   Less volatile than market
```

### Beta Examples
```
Apple (tech):      Beta = 1.3 (moves 30% more than market)
Procter & Gamble:  Beta = 0.6 (moves 40% less than market)
Market Index:      Beta = 1.0 (by definition)

If market goes up 10%:
Apple expected:    +13% (10% × 1.3)
P&G expected:      +6% (10% × 0.6)
```

### Calculating Your Portfolio Beta

```
Portfolio Beta = Σ (Asset Weight × Asset Beta)

Example:
Position A: 50% allocation, Beta 1.2 → 0.50 × 1.2 = 0.60
Position B: 30% allocation, Beta 0.8 → 0.30 × 0.8 = 0.24
Position C: 20% allocation, Beta 1.5 → 0.20 × 1.5 = 0.30

Portfolio Beta = 0.60 + 0.24 + 0.30 = 1.14
```

### Using Beta to Understand Risk

```
Scenario: Market drops 20%

Your Portfolio Beta 0.5:
Expected portfolio decline = 20% × 0.5 = 10%
(Less risky than market, good for downturns)

Your Portfolio Beta 1.5:
Expected portfolio decline = 20% × 1.5 = 30%
(More risky than market, amplifies gains/losses)
```

### Finding Beta Values
```
Company Beta can be found:
- Yahoo Finance (Finance.yahoo.com)
- ETF fact sheets (specify beta in prospectus)
- Morningstar
- Your brokerage's research tools
- Marketwatch
```

## Alpha: Outperformance vs. Market

### Definition
```
Alpha = Portfolio Return - Expected Return Given Beta

Measures: How much you're beating (or losing to) the market
```

### Calculation Example
```
Your Portfolio Return: 15%
Your Portfolio Beta: 1.2
Risk-Free Rate: 4%
Market Return: 12%

Expected Return = Risk-Free Rate + Beta × (Market Return - Risk-Free Rate)
                = 4% + 1.2 × (12% - 4%)
                = 4% + 1.2 × 8%
                = 4% + 9.6%
                = 13.6%

Alpha = Actual Return - Expected Return
      = 15% - 13.6%
      = +1.4% (you beat market by 1.4%)
```

### Alpha Interpretation
```
Alpha = +2%:     Beating market by 2% (excellent)
Alpha = +0.5%:   Beating market by 0.5% (slight outperformance)
Alpha = 0%:      Matching market return (efficient)
Alpha = -1%:     Underperforming by 1% (worse than index)
Alpha = -3%:     Significantly underperforming
```

### Why Alpha is Hard to Achieve
```
Challenge 1: Consistency
- Getting +1% alpha once is luck
- Getting +1% alpha for 5+ years takes skill

Challenge 2: Costs
- Trading fees reduce alpha
- Taxes reduce alpha
- Need to beat market by cost amount at minimum

Challenge 3: Reversion
- Past alpha often doesn't persist
- Many "beat the market" managers underperform next period
```

## Performance Attribution

### Breaking Down Returns: Why Did You Make/Lose Money?

```
Total Return = 12%

Decomposed into:
Capital Appreciation:     +8% (prices went up)
Dividends/Interest:       +2% (income generated)
Currency impact (intl):   +1% (if foreign holdings)
Fees/Costs:              -1% (trading, management fees)
```

### Risk vs. Return Attribution
```
Sector Contribution:
Tech (40% position):      +5% contribution (high beta)
Utilities (15% position): +1% contribution (low beta)
Healthcare (20%):         +3% contribution (steady)

Conclusion: Tech drove most of gains
Action: Consider if tech weighting is intentional
```

## Portfolio Benchmarking

### Selecting Appropriate Benchmarks

```
Portfolio Type              Benchmark
60/40 Balanced              60% S&P 500 + 40% Bloomberg Agg Bond
100% Dividend Stocks        S&P High Dividend Yield Index
Growth-focused              Russell 1000 Growth
Value-focused               Russell 1000 Value
International-heavy        MSCI EAFE (developed markets)
```

### Comparison Template
```
Your Portfolio Performance vs. Benchmark:

                Your Port    Benchmark    Difference
1-Year Return:  +12.5%      +11.2%       +1.3% (beating!)
3-Year Return:  +9.8%       +10.2%       -0.4% (lagging)
5-Year Return:  +8.2%       +8.5%        -0.3% (slightly behind)

Max Drawdown:   -18%        -20%         (better downside)
Sharpe Ratio:   0.95        0.88         (better risk-adj)
```

## Performance Metrics Worksheet

### Monthly Performance Tracking
```
Year: ______

Month  | Portfolio Value | Monthly Return % | YTD Return % | Notes
Jan    | $_____________  | _____%          | _____%       |
Feb    | $_____________  | _____%          | _____%       |
Mar    | $_____________  | _____%          | _____%       |
...    | ...             | ...             | ...          |
Dec    | $_____________  | _____%          | _____%       |
```

### Annual Metrics Calculation
```
Year: ______

Total Return:           _____%
Monthly Avg Return:     _____%
Monthly Std Dev:        _____%
Annualized Volatility:  _____%
Risk-Free Rate:         _____%
Sharpe Ratio:          _______

Portfolio Beta:         _______
Market Return:          _____%
Expected Return:        _____%
Alpha:                  _____%
```

## Common Performance Pitfalls

### 1. Focusing on Absolute Return Only
**Wrong:** "I made 10%"
**Right:** "I made 10% with only 8% volatility (Sharpe 0.75)"

### 2. Comparing to Wrong Benchmark
**Wrong:** Comparing dividend portfolio to growth index
**Right:** Compare dividend portfolio to dividend benchmark

### 3. Short-Term Focus
**Wrong:** "My portfolio lost money in March"
**Right:** "My portfolio is up 8.2% YTD"

### 4. Ignoring Risk Metrics
**Wrong:** "Another fund returned 20% last year!"
**Right:** "But it had 30% volatility (Sharpe 0.33) vs mine at 0.92"

### 5. Not Accounting for Fees
**Problem:** Reporting gross returns while paying 1% in fees
**Solution:** Always report net returns (after fees/taxes)

## Key Takeaways

1. **Sharpe Ratio:** Best single metric for investor success (risk-adjusted returns)
2. **Beta:** Understand your portfolio's volatility vs. market
3. **Alpha:** Difficult to achieve consistently; don't overweight it
4. **Total Return:** Must include all income and appreciation
5. **Consistency matters:** Judge performance over years, not months
6. **Benchmarking:** Only compare to appropriate benchmarks
7. **Track monthly:** Build a historical performance record

## Next Steps

- [ ] Calculate your portfolio's Sharpe Ratio this month
- [ ] Determine your portfolio's beta
- [ ] Choose appropriate benchmark
- [ ] Set up monthly return tracking spreadsheet
- [ ] Review performance vs. benchmark quarterly
