import requests

API_URL = "https://www.nfkeys.store/api/keys/redeem"

HEADERS = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://www.nfkeys.store",
    "referer": "https://www.nfkeys.store/redeem",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}


def redeem_key(key):
    response = requests.post(
        API_URL,
        json={"code": key},
        headers=HEADERS,
        timeout=30,
    )

    if response.status_code != 200:
        raise Exception("เว็บตอบกลับผิดพลาด")

    data = response.json()

    if data.get("result") != "ok":
        raise Exception("คีย์ไม่ถูกต้อง หรือถูกใช้ไปแล้ว")

    profile_data = data.get("assignedProfile") or {}
    tokens = data.get("tokens") or {}

    return {
        "profile_name": profile_data.get("name", "-"),
        "avatar_url": profile_data.get("avatarUrl", ""),
        "plan_tier": data.get("planTier", "-"),
        "redeemed_ts": data.get("redeemedAt"),
        "expires_ts": data.get("expiresAt"),
        "profile_number": data.get("profileNumber", "-"),
        "slot": data.get("slot", "-"),
        "capacity": data.get("capacity", "-"),
        "links": {
            "pc": tokens.get("desktop", ""),
            "mobile": tokens.get("mobile", ""),
            "tv": tokens.get("tv", ""),
        },
    }
