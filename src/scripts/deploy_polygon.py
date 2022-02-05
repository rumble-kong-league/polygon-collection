from brownie import RKLCollection, accounts

def main():
  acc = accounts.load('<your account name>')

  rkl = RKLCollection.deploy({'from': acc})

  RKLCollection.publish_source(rkl)

if __name__ == '__main__':
  main()
