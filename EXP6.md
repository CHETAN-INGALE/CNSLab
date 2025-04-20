Certainly! Here's a comprehensive overview of the "From DES to 3-DES" experiment available on the Virtual Labs platform by IIIT Hyderabad. This includes the theoretical background and a step-by-step procedure to help you prepare for your practical exams.


## 🧪 Experiment: From DES to 3-DES

### 🎯 Aim

To understand and implement the Triple DES (3-DES) encryption scheme using the standard DES algorithm.

### 📚 Theory

**Data Encryption Standard (DES)** is a symmetric-key algorithm for the encryption of digital data. Due to its relatively short key length (56 bits), DES is susceptible to brute-force attacks. To enhance security, **Triple DES (3-DES)** was developed, which applies the DES algorithm three times to each data block.

**Triple DES Process:**

1. **First Encryption:** Encrypt the plaintext using Key A.
2. **Second Encryption (Decryption Step):** Decrypt the result from the first step using Key B.
3. **Third Encryption:** Encrypt the result from the second step using Key A again.

This sequence is known as **Encrypt-Decrypt-Encrypt (EDE)**. The use of two keys (Key A and Key B) effectively increases the key length, making the encryption more secure than standard DES.

### 🧪 Procedure

To perform the experiment on the Virtual Labs platform:

1. **Generate Inputs:**
   - Click on the respective buttons in **Part I** of the simulation page to generate:
     - Plaintext `m`
     - Key A (`keyA`)
     - Key B (`keyB`)

2. **First Encryption:**
   - In **Part II**, enter the generated plaintext `m` into the "Your text to be encrypted/decrypted" field.
   - Enter `keyA` into the "Key to be used" field.
   - Click on the **DES Encrypt** button to obtain the first ciphertext `c1`.

3. **Second Encryption (Decryption Step):**
   - Enter `c1` into the "Your text to be encrypted/decrypted" field.
   - Enter `keyB` into the "Key to be used" field.
   - Click on the **DES Decrypt** button to obtain the second ciphertext `c2`.

4. **Third Encryption:**
   - Enter `c2` into the "Your text to be encrypted/decrypted" field.
   - Enter `keyA` into the "Key to be used" field.
   - Click on the **DES Encrypt** button to obtain the final ciphertext `c3`.

5. **Verification:**
   - In **Part III**, enter `c3` into the "Enter your answer here" field to verify your Triple DES implementation.

For a detailed walkthrough and to perform the simulation, visit the [experiment page](https://cse29-iiith.vlabs.ac.in/exp/des/procedure.html).
 
