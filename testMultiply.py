# Run a comparison of multiplication with default and large polynomial modulus settings
from Pyfhel import Pyfhel
from Pyfhel import PyPtxt
from Pyfhel import PyCtxt

# First context, default m setting = 2048. Low noise deficit available    
pyf = Pyfhel()
pyf.contextGen(65537)
pyf.keyGen()
    
pTxt = pyf.encodeInt(3)
pTxt2 = pyf.encodeInt(5)
cTxt = pyf.encrypt(pTxt)
cTxt2 = pyf.encrypt(pTxt2)
    
cTxt_res = cTxt * cTxt2

print("result1 : " + str(pyf.decrypt(cTxt_res, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res)))

cTxt_res2 = cTxt_res * cTxt

print("result2 : " + str(pyf.decrypt(cTxt_res2, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res2)))

# Second context, m setting = 8192. High noise deficit available.    
pyf2 = Pyfhel()
pyf2.contextGen(65537, m=8192)
pyf2.keyGen()
    
pTxt = pyf2.encodeInt(3)
pTxt2 = pyf2.encodeInt(5)
cTxt = pyf2.encrypt(pTxt)
cTxt2 = pyf2.encrypt(pTxt2)

cTxt_res = cTxt * cTxt2

print("result3 : " + str(pyf2.decrypt(cTxt_res, True)))
print("noise : " + str(pyf2.noiseLevel(cTxt_res)))

cTxt_res2 = cTxt_res * cTxt

print("result4 : " + str(pyf2.decrypt(cTxt_res2, True)))
print("noise : " + str(pyf2.noiseLevel(cTxt_res2)))
