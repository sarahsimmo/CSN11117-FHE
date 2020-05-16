# Most basic implmentation of Pyfhel - CSN11117: Coursework  Example 1
from Pyfhel import Pyfhel
from Pyfhel import PyPtxt
from Pyfhel import PyCtxt
    
pyf = Pyfhel()
pyf.contextGen(65537)
pyf.keyGen()
    
pTxt = pyf.encodeInt(3)
pTxt2 = pyf.encodeInt(5)
cTxt = pyf.encrypt(pTxt)
cTxt2 = pyf.encrypt(pTxt2)
    
cTxt_res = cTxt + cTxt2

print("result1 : " + str(pyf.decrypt(cTxt_res, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res)))

cTxt_res2 = cTxt_res + cTxt

print("result2 : " + str(pyf.decrypt(cTxt_res2, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res2)))

cTxt_res3 = cTxt_res2 + cTxt

print("result3 : " + str(pyf.decrypt(cTxt_res3, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res3)))

cTxt_res4 = cTxt_res2 + cTxt_res + cTxt_res3

print("result4 : " + str(pyf.decrypt(cTxt_res4, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res4)))

cTxt_res5 = cTxt_res2 * cTxt_res 

print("result5 : " + str(pyf.decrypt(cTxt_res5, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res5)))

cTxt_res6 = cTxt_res5 + cTxt_res + cTxt_res4

print("result6 : " + str(pyf.decrypt(cTxt_res6, True)))
print("noise : " + str(pyf.noiseLevel(cTxt_res6)))