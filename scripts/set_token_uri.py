from brownie import SimpleCollectable2, network
from scripts.helpful_scripts import get_account, get_cycle, OPENSEA_URL

cycle_metadata_dic = {
    "NIGHT": "https://ipfs.io/ipfs/Qmd1fKXM1njXMn33PafoKS6CjAtEF93hQLA4SdRtrCb3Dp?filename=0-NIGHT.json"
}


def main():
    print(f"I am on network: {network.show_active()}")
    simp_collectable = SimpleCollectable2[-1]
    numb_of_collactable = simp_collectable.tokenCounter()
    print(f"Number of Collecatable: {numb_of_collactable} token IDs")
    for token_id in range(numb_of_collactable):
        cycle = get_cycle(simp_collectable.tokenIdToCycle(token_id))
        if not simp_collectable.tokenURI(token_id).startswith("https://"):
            print(f"setting URI for token ID: {token_id}")
            set_tokenURI(token_id, simp_collectable, cycle_metadata_dic[cycle])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    txn = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    txn.wait(1)

    print(
        f"Incredible !!!! you can voiew your nft at: {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wiat up to 20 min")
