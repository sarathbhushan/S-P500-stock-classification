# S-P500-stock-classification
S&amp;P Global stock classification

The S&P 500 comprises ~ 500 stocks and represents the broad stock market. You have a
hypothesis that families of stocks comprising the index actually belong to a few groups that
move in sync to each other. Intuitively it makes sense that stocks in the same or similar sector
behave similarly but you believe that there might be stocks in not directly related sectors that
behave similarly. You want to explore this hypothesis further.
After getting the time series data for each individual stock’s data.

1. You want to identify which stocks have gone up, gone down or have remained flat.
Devise an automated approach to label individual stock as flat, up or down over a 2
year window. Consider nuances where a stock may be temporarily high/low vs a long
term increase/decline in price, vs a recent period of price shocks etc. Propose and
implement a strategy to label stocks in these three buckets (up/down/flat) considering
these nuances. You could add additional labeling classes but try to keep the total
classes less than 8
2. How would you check the quality of the classification above? Quantify the quality.
