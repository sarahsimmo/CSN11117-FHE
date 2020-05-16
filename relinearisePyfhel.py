# CSN11117: Coursework  Relinearisation Example
from Pyfhel import Pyfhel
from Pyfhel import PyPtxt
from Pyfhel import PyCtxt
    
# We have to use batching (SIMD) to operate over arrays  
pyf = Pyfhel()
pyf.contextGen(65537, m=8192, flagBatching=True)
pyf.keyGen()

cArray1 = pyf.encryptBatch([1,2,3,4])
cArray2 = pyf.encryptBatch([2,2,2,2])

# Multiply our arrays together
cArray_res = pyf.multiply(cArray1, cArray2, True)
print("Array 1 * 2 = Res1 \nsize: " + str(cArray_res.size()))

# Multiply the result with itself
cArray_res2 = pyf.multiply(cArray_res, cArray_res, True)
print("\nRes1 * Res1 \nRes2 size: " + str(cArray_res2.size()))
print("Res2 noise: " + str(pyf.noiseLevel(cArray_res2)))

# Perform relinearistion on the first result array
print("\nRes1 size: " + str(cArray_res.size()))
pyf.relinKeyGen(10,3)
pyf.relinearize(cArray_res)
print("Res1 size (relinearized): " + str(cArray_res.size()))

# Multiply the resultant array with itself again
cArray_res3 = pyf.multiply(cArray_res, cArray_res, True)
print("\nRes1 * Res1 \nRes3 size: " + str(cArray_res3.size()))
print("Res3 noise: " + str(pyf.noiseLevel(cArray_res3)))