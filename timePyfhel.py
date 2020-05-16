# Python file to test the basic functions of Pyfhel FHE library with a Microsoft SEAL backend. 
# This demonstrates the add, subtract, multiply and exponent functions of the wrapped SEAL 
# encryption library. 
# By checking the level of noise in the cipher texts we can see how the operations can  
# very quickly degrade the homomorphic performance. The noise level returned indicates the 
# noise buffer remaining in the ciphertext, i.e. how much space we have available within a  
# ciphertext to handle further operations on it, before the noise renders the result invalid.
# Note that when the noise reaches zero we will not get a valid result from any further 
# operations on the ciphertext.
from Pyfhel import Pyfhel
from Pyfhel import PyCtxt
from Pyfhel import PyPtxt
from timer import Timer

# Time the operations
t = Timer()

# Generate our Pyfhel instance 
pyf1 = Pyfhel()
    
# Create the context usingthe suggested modulus values for word and long 
# Values for the modulus p (size of p):
# - 2 (Binary)
# - 257 (Byte)
# - 65537 (Word)
# - 4294967311 (Long)
# Generate the context with large noise deficit
pyf1.contextGen(65537, m=8192, sec=192, flagBatching=True)
pyf1.keyGen()
pyf1.relinKeyGen(10, 10)

# Encode some data into a plaintext
plain1 = pyf1.encodeInt(10)
plain2 = pyf1.encodeInt(27)

# Encrypt with our current key
cipher1 = pyf1.encrypt(plain1)
cipher2 = pyf1.encrypt(plain2)

# Show our initial levels of the two ciphers
print('\nPlaintext values: \nPlaintext1 = ' + str(pyf1.decrypt(cipher1, True)) + '\nPlaintext2 = ' + str(pyf1.decrypt(cipher2, True)))
print('Noise levels: \nCipher1 = ' + str(pyf1.noiseLevel(cipher1)) + '\nCipher2 = ' + str(pyf1.noiseLevel(cipher2)))

# Addition
t.start()
cipherAdd1 = cipher1 + cipher2
cipherAdd2 = cipherAdd1 + cipher1
t.stop('-------------------------------------------------\nAddition')
# Print the results
print('\nAddition values: \nC1 + C2 = C3  = '+ str(pyf1.decrypt(cipherAdd1, True)) + '\nC3 + C1 = C4  = ' + str(pyf1.decrypt(cipherAdd2, True)))
print('Noise levels after addition: \nC3 = ' + str(pyf1.noiseLevel(cipherAdd1)), '\nC4 = ' + str(pyf1.noiseLevel(cipherAdd2)))

# Subtraction
t.start()
cipherSub1 = cipher1 - cipher2
cipherSub2 = cipherSub1 - cipher1
t.stop('-------------------------------------------------\nSubtraction')
# Print the results
print('\nSubtraction values: \nC1 - C2 = C3  = '+ str(pyf1.decrypt(cipherSub1, True)) + '\nC3 - C1 = C4  = ' + str(pyf1.decrypt(cipherSub2, True)))
print('Noise levels after subtracton: \nC3 = ' + str(pyf1.noiseLevel(cipherSub1)), '\nC4 = ' + str(pyf1.noiseLevel(cipherSub2)))

# Multiply
t.start()
cipherMult1 = cipher2 * cipher1
cipherMult2 =  cipher1 * cipherMult1
t.stop('-------------------------------------------------\nMultipliaction')
# Print the results
print('\nMultiplication values: \nC1 - C2 = C3  = '+ str(pyf1.decrypt(cipherMult1, True)) + '\nC3 - C1 = C4  = ' + str(pyf1.decrypt(cipherMult2, True)))
print('Noise levels after multiplication: \nC3 = ' + str(pyf1.noiseLevel(cipherMult1)), '\nC4 = ' + str(pyf1.noiseLevel(cipherMult2)))

# Divide (by mltipliciation of floating point numbers)
plain3 = pyf1.encodeFrac(10.0)
plain4 = pyf1.encodeFrac(0.2)
plain5 = pyf1.encodeFrac(0.5)
cipher3 = pyf1.encrypt(plain3)
cipher4 = pyf1.encrypt(plain4)
cipher5 = pyf1.encrypt(plain5)

t.start()
cipherDiv1 = pyf1.multiply(cipher3, cipher4, True)
cipherDiv2 = pyf1.multiply(cipher3, cipher5, True)
t.stop('-------------------------------------------------\nDivision')
# Print the results
print('\nDivision values: \nC1 / C2 = C3  = '+ str(pyf1.decryptFrac(cipherDiv1,)) + '\nC2 / C1 = C4  = ' + str(pyf1.decrypt(cipherDiv2, True)))
print('Noise levels after division: \nC3 = ' + str(pyf1.noiseLevel(cipherDiv1)), '\nC4 = ' + str(pyf1.noiseLevel(cipherDiv2)))

# Exponent
t.start()
cipherPow1 = pyf1.power(cipher1, 2, True)
cipherPow2 = pyf1.power(cipherPow1, 3, True)
t.stop('-------------------------------------------------\nExponentiation')
# Print the results
print('\nExponent values: \nC1 ** 2 = C2  = '+ str(pyf1.decrypt(cipherPow1, True)), '\nC2 ** 3 = C4  = ' + str(pyf1.decrypt(cipherPow2, True)))
print('Noise levels after exponentiation: \nC2 = ' + str(pyf1.noiseLevel(cipherPow1)), '\nC4 = ' + str(pyf1.noiseLevel(cipherPow2)))


# Mutliplication of arrays
cArray1 = pyf1.encryptBatch([1,2,3,4,9])
cArray2 = pyf1.encryptBatch([2,2,4,2,3])
t.start()
cArrayMult1 = pyf1.multiply(cArray1, cArray2, True)
cArrayMult2 = pyf1.multiply(cArrayMult1, cArray1, True)
t.stop('-------------------------------------------------\nArray Multiplication')
# Print the results
print('\nArray mulitplication values: \n[C1] * [C2] = [C3]  = '+ str(pyf1.decrypt(cArrayMult1, True)[0:5]), '\n[C3] * [C1] = [C4] = ' + str(pyf1.decrypt(cArrayMult2, True)[0:5]))
print('Noise levels after array mulitipilcation: \n[C3] = ' + str(pyf1.noiseLevel(cArrayMult1)), '\n[C4] = ' + str(pyf1.noiseLevel(cArrayMult2)))

# Perform relinearistion on the first result array
print('-------------------------------------------------\nRelinerization\n[C3] size: ' + str(cArrayMult1.size()))
t.start()
pyf1.relinKeyGen(10,3)
t.stop('RelinKeyGen')
t.start()
t.stop('Relinerise')
pyf1.relinearize(cArrayMult1)
print("[C3] size (relinearized): " + str(cArrayMult1.size()))
