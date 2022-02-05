#!/usr/bin/env python
from typing import List, Dict
import json

snapshot_file = './snapshot-4-feb-22.json'
kong_holder_addresses_file = 'kong-holder-addresses-4-feb-22.json'

def get_kong_holder_addresses_from_snapshot():
  # snapshot is a dict. Key is address, value is list of tokenIds.
  # maps owner to their tokenIds
  snapshot: Dict[str, List[int]] = json.loads(open(snapshot_file, 'r').read())

  # each wallet holding a kong receives one curry poster
  kong_holder_addresses = list(snapshot.keys())

  with open(kong_holder_addresses_file, 'w') as f:
    f.write(json.dumps(kong_holder_addresses, indent=4))

def produce_curry_poster_meta():

  def curry_meta_for_token_id(i: int) -> Dict[str, str]:
    return {
      "image": "ipfs://QmdCFbqT9tQ2pWRKbYmva7dxzPTsaFMgDAq3hyJdNmx9vr",
      "description": "RKL Polygon Collection to commemorate important events of the Kong Life.",
      "name": f"RKL SLAM Feb/Mar 2022 Poster #{i}"
    }

  kong_holder_addresses = json.loads(open(kong_holder_addresses_file).read())

  for i in range(len(kong_holder_addresses)):
    meta = curry_meta_for_token_id(i + 1)
    f = open(f'./meta/{i + 1}', 'w')
    f.write(json.dumps(meta, indent=4))


if __name__ == '__main__':
  # get_kong_holder_addresses_from_snapshot()
  produce_curry_poster_meta()
