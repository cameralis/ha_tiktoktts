import tts

a = tts.TikTokTTSEntity({}, voice="en_us_001")
v = a.get_tts_audio("hello", "en_us_001")
print(v)