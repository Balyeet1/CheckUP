from joserfc import jwt
from joserfc.jwk import OctKey, RSAKey

# Example of a creation of a Json Web Token(JWT) using Json Web Signature(JWS)
header = {"alg": "HS256"}
claims = {"iss": "https://authlib.org"}
key = OctKey.import_key("secret")
print(jwt.encode(header, claims, key))

parameters = {"use": "enc", "alg": "RSA-OAEP"}
key_size = 2048
key = RSAKey.generate_key(key_size=key_size, parameters=parameters)

# Example of a creation of a Json Web Token(JWT) using Json Web Encryption(JWE)
protected = {"alg": "RSA-OAEP", "enc": "A128GCM"}
claims = {"iss": "https://authlib.org"}
text = jwt.encode(protected, claims, key)
print(text)

print(jwt.decode(text, key))

