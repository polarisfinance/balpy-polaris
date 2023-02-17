#!/usr/bin/env python
import balpy

def main():
    network = "aurora"
    poolId = "0xaed2a4589f21f3ad20ca8e389701579f15821466000200000000000000000001"
    # On Ethereum and Ethereum testnets, you can pass creationHash=None
    # On Polygon, you must pass the pool creation hash to generate verification params
    creationHash = None;
    creationHash = "0x249bea8a725ac04ec96505d6509c8e31b41605ce0f8a8e67a49f569ef97761ed";
    verbose = True;

    bal = balpy.balpy.balpy(network);
    # isVerified = bal.isContractVerified(poolId, verbose=verbose);
    isVerified = False
    if not isVerified:
        command = bal.balGeneratePoolCreationArguments(poolId, verbose=verbose, creationHash=creationHash);
    else:
        print("Pool is already verified")
        quit();
    
    print()
    print(command)
    print()

    print("If you need more complete instructions on what to do with this command, go to:");
    print("\thttps://dev.balancer.fi/resources/pools/verification\n");
    
if __name__ == '__main__':
    main();
