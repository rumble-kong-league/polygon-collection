from brownie import RKLCollection, accounts
import json

RKL_COLLECTION_ADDRESS = '0xabb95abfb3d79daf27558e5aff8bf714922ba8db'

KONG_HOLDER_ADDRESSES = [
    "0x5Fb043d0E9f5A337e78759aB7564E8EE2158c828",
    "0x18Ee82eEB399263c633419bC0E8c47002FA3B91f",
    "0x39036cEf5E29B4d5B2f47c341b9D9819e428Ed22",
    "0x6713dB93c0a7580Fe0E81dfb1B6D121030120b33",
    "0x3fE87F5D1490273d7A6B6975ac023220105683B4",
    "0xd66bb2D2935487fCEf48bf4e26b3101FBeb7d744",
    "0xEC7209952282DE267D221cd4fCE53e2e1a22ef20",
    "0x439559801F140116633278873b03d851e0b1A1A2",
    "0x8002BD5a34dEBe75B4F38495F8B07929D4d43007",
    "0xaCDA061973A5c4Eb4F9573c199772A31d9cA2829",
    "0x953b0f8aFC70E0FCa9E2e43B0A4914be002c4e94",
    "0x1f1fBBeDa02aFa3679a217a989AE6Be838CB4b84",
    "0xe75C06cEE0A6B854F8d0ABAF5c90D4405557f353",
    "0x6eD14Bd05fCFEC53593B7b2AfA8B8A962B4f083F",
    "0x209322764B24a96eef09feFA4b764784936cd3B2",
    "0x5bfED1241127FE08bb12595D620f36E1a2D613f9",
    "0xfB3C1034c128F7B6159898e25294ADc39eA877d9",
    "0x82e1EC93Be8B2a6a93Cd14a7Fd5326491FC06C94",
    "0x976517df007125187Dcb2350701A8168636617c8",
    "0x328B54f0989b6CCFD8110763EF1F24f3a96Aa8e8",
    "0x90eFdc272E9Ab4C7236FbC32d40142AD814fE082",
    "0x833F85791Df4D89C0735025CB284170b0C1C47Be",
    "0x6f7B7121CfE7e279635291183bc265DCF927790f",
    "0x3DEbfC90039a87Dca69488A1dCE420b9427F8F57",
    "0x115406837DE7D8194421126De6Fa7dc90bDe1663",
    "0xaaf7F903406e8Bdbd0D3440d494F93aD7b0d4a24",
    "0xF3a81F1eDb38b56cea5Bb3BB3481Fb00cE3146D3",
    "0x1E61b817A95457ce2761eEEa634C818a97B90750",
    "0x6e6003c510A42DE03aF6C79a88ec6826E8F653F2",
    "0x4BAa6AbB27856E8E3720c0e1FC4d74Df7890CD34",
    "0x7c4F055042a6B6EAe1AcE82Ac0e3D37158D4C9c0",
    "0xAEF0b9A81d36425b3a17c9450B2eABc1c99F4e27",
    "0x144FF139671A26bbE99b570fE1bbd55bf3E7B9F2",
    "0x37d5DDe7d2B73EcA3BCAf4A5e7ac1f7C420463C8",
    "0x09647dfcF43505CdBeB37339304a9eb09F6504C4",
    "0x2e7Bf50D11A5d717C2373Be3156790C98DA498D7",
    "0x84a0e7bC25D7df82A0BbD6ed5795A47f26037A9A",
    "0xe94B8D917a4111940eE26c9520d009B9847E56D0",
    "0xf5A3F562A132F40F44ABD401D603373dc36C77c5",
    "0x91EE56eeCa7fE55Ba94192c6E49e17Bf7b140363",
    "0x5C4C77b8018Fa5B7f6574Da019f62e3717Fa2b22",
    "0xC5Fa4F262a140B29B76cd3835b112AC0ac49A6C2",
    "0x1b0fe7356A4b54d454B5F2A98330E88bcE3C229b",
    "0xAc9d7336eC3DF01596bD3bF20Ff53ACc66bb4761",
    "0x234Be664469E81E77F91171A1757E414dec0d49c"
]

def main():
  acc = accounts.load('rkl-1')

  rkl = RKLCollection.at(RKL_COLLECTION_ADDRESS, owner=acc)

  token_id = 3074

  for address in KONG_HOLDER_ADDRESSES:
    print(f'airdropping #{token_id} on {address}')

    rkl.mint(address, token_id, 1, hex(0), {'from': acc})

    token_id += 1

if __name__ == '__main__':
  main()