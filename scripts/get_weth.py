from scripts.helpful_scripts import get_account
from brownie import accounts, interface, config, network


def main():
    get_weth()  # to interact with aave application


def get_weth():
    """
    Mints weth by depositing eth
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 weth")
    return tx
