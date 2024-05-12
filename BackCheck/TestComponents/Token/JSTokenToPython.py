from joserfc import jwt
from joserfc.errors import InvalidClaimError, MissingClaimError, BadSignatureError
from joserfc.jwk import RSAKey
from joserfc.registry import HeaderParameter

text = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..m4OGBiTKNyLB3tkk0xwx6Q.VymtR75ObNBUgVY0yX5XttQ-VlKrJiksVqMuwU35dNup5AsXwSGz7uo-f8Sjt6B2WIL38rtmWf9DLPvkSvbcVQqrA2CE05wIsUXulA3yk9KJZzoWVBVVzvGenoN89d-0.6fTR5zPeX_qOmSo4VDoccaMaAAR_SXVSZrFi22ReyPo"
key = "42a9776651a7d5d414c323055c16903ff49a9df9476c4d9665d08b5df8fb3bba"

decode_value = ""

claims_validations = jwt.JWTClaimsRegistry(
    iss={"essential": True, "value": "teste"},
    aud={"essential": True, "value": "Back Check"},
    exp={"essential": True},
)

try:
    decode_value = jwt.decode(text, key)
except BadSignatureError:
    print(BadSignatureError.error)

try:
    claims_validations.validate(decode_value.claims)
    claims_validations.validate_exp(decode_value.claims.get("exp"))
    print(decode_value.header)
    print(decode_value.claims)

except MissingClaimError:
    print("Missing claim.")
except InvalidClaimError:
    print("Wrong value claim.")

