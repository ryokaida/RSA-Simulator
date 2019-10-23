#method to do calculations
def simulateRsa():
    print("");
    #get m, p, q, and e
    print("Enter m:");
    m = int(input());
    print("Enter p:");
    p = int(input());
    print("Enter q:");
    q = int(input());
    print("Enter e:");
    e = int(input());
    
    #print m, p, q, and e
    print("");
    print("m: " + str(m));
    print("p: " + str(p));
    print("q: " + str(q));
    print("e: " + str(e));
    print("");

    #calculate n = pq
    n = p * q;

    #calculate phiN = (p-1)(q-1)
    phi1 = p-1;
    phi2 = q-1;
    phiN = phi1 * phi2;

    #print n and phiN
    print("n: " + str(n));
    print("phiN: " + str(phiN));
    print("");

    #calculate d: de = 1 % phiN and d < phiN
    #find 1 % phiN
    oneModPhiN = 1 % phiN;
    print("1 % phiN: " + str(oneModPhiN));

    #sources about k:
    #https://www.di-mgt.com.au/rsa_alg.html
    #https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
    #https://crypto.stackexchange.com/questions/27113/what-is-k-in-rsa
    #find k, by trying each value until something works
    tempK = 1;
    tempResult = 99;
    while (tempResult != 0):
        tempResult = (tempK * phiN + oneModPhiN) % e; #test to see if there is a clean divide
        #if clean divide, then put tempK value into k
        if (tempResult == 0):
            k = tempK;
        #no clean divide, increment tempK to try next value
        else:
            tempK = tempK + 1;

    #find right half of equation: 1 * phiN + (1 % phiN)
    rightHalf = k * phiN + oneModPhiN;
    print("rightHalf: " + str(rightHalf));
    #find  d = rightHalf / e
    tempD = rightHalf / e;
    if (tempD < phiN):
        d = int(tempD);
        print("d: " + str(d));
    else:
        print("d is not less than phiN");
    print("");

    #make public key
    publicK = e;
    publicU = n;
    print("Public key KU: {" + str(e) + ", " + str(n) + "}");
    #make private key
    privateK = d;
    privateR = n;
    print("Public key KR: {" + str(d) + ", " + str(n) + "}");

    #encrypt: c = m^e % n
    print("");
    print("Encrypt");
    ciphertext = m ** publicK % publicU;
    print("Ciphertext: " + str(ciphertext));

    #decrypt: m = c^d % n 
    print("");
    print("Decrypt");
    plaintext = ciphertext ** privateK % privateR;
    print("Plaintext: " + str(plaintext));
    print("");
    #check to see if plaintext = m
    if (plaintext == m):
        print("Successful Decrypt");
    else:
        print("Decrypt failed");


print("RSA Key Generation, Encryption, and Decryption Simulator");
print("");
print("Simulate? y/n:");
toSimulate = input();
if (toSimulate == "y"):
    toContinue = True;
    while (toContinue == True):
        simulateRsa();
        print("");
        print("Simulate again? y/n:");
        toSimulate = input();
        if (toSimulate == "y"):
            toContinue = True;
        else:
            toContinue = False;
print("");
print("Press q to exit.");
input();