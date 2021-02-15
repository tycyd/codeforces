import base64

MESSAGE = '''
D14QRFpbUUJBFRNOWURWS11VRRUeE1MaDF1VXVVWR1cUVENDFlxLQFRXX1YQXk8RHl1SV11ARwde
QwsZH11fUUBWEBABXVwfGBEVU1AcEAZHXFVRX0YVE05ZRERXVFtSWVdXU1VDFktZVlNbRkBTWVkR
HktVV1cVH1ReBV5WHxQLEhVEHRdCFkQ=
'''

KEY = 'tyc19841223'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
