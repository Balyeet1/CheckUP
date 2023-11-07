from joserfc import jwt
from joserfc.jwk import RSAKey
from joserfc.errors import InvalidClaimError, MissingClaimError, BadSignatureError

from joserfc.registry import HeaderParameter

parameters = {"use": "sig", "alg": "RS256"}

# https://jose.authlib.org/en/dev/guide/registry/
# What the website says, It's that the header in the payload has restricted parameters, to add more or
# disable them use registry
additional_header_registry = {
    "custom": HeaderParameter("Custom message", "str", required=True),
}

registry = jwt.JWSRegistry(additional_header_registry)

key_size = 1024
key = RSAKey.generate_key(key_size=key_size, parameters=parameters)

header = {"alg": "RS256", 'typ': 'JWT', "custom": "hello"}
claims = {"iss": "my.website", "username": "", "password": ""}

text = jwt.encode(header=header, claims=claims, key=key, registry=registry)

print(text)

decode_value = ""

try:
    decode_value = jwt.decode(text, key, registry=registry)
except BadSignatureError:
    print(BadSignatureError.error)

print(decode_value.header)
print(decode_value.claims)

# Create the validater of the body(claim)
claims_requests = jwt.JWTClaimsRegistry(
    iss={"essential": True, "values": ["my.website", "my.cousin_website"]},
    username={"essential": True},
    password={"essential": True},
)

try:
    claims_requests.validate(decode_value.claims)
except InvalidClaimError:
    print(InvalidClaimError.error)
except MissingClaimError:
    print(MissingClaimError.error)

print("\nclaim validated")

