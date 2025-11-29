import requests, time

def glmr_bridge():
    print("Moonbeam — GLMR Whale Bridge Exit (> 500k GLMR → Ethereum)")
    seen = set()
    while True:
        r = requests.get("https://api.moonscan.io/api?module=account&action=txlist&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json().get("result", [])[:25]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Moonbeam → Ethereum bridge contract
            if tx["to"].lower() != "0x4e8501e7b9e6d599b36e84d4c1e5f3d3c9c6d590": continue
            
            value = int(tx["value"]) / 1e18
            if value >= 500_000:
                print(f"WHALE EXIT VIA BRIDGE\n"
                      f"{value:,.0f} GLMR leaving Polkadot ecosystem → Ethereum\n"
                      f"Wallet: {tx['from']}\n"
                      f"Tx: https://moonscan.io/tx/{h}\n"
                      f"→ Real money escaping Moonbeam\n"
                      f"{'-'*60}")
        time.sleep(3.1)

if __name__ == "__main__":
    glmr_bridge()
