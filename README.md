1. swap some eth for weth
2. deposit some eth into aave
3. borrow some asset with the eth collateral
    1. Sell that borrowed asset. (short selling)
4. repay everything back


works with paraswap, uniswap, 1inch

Testing:
    Integration test: Kovan
    Unit test: Mainnet-fork (fork everything on mainnet to local), this can be done
    because we dont using oracles here and aave has all
    