"""Constants for the TikTok text-to-speech integration."""
from dataclasses import dataclass

CONF_LANG = "lang"
DEFAULT_LANG = "en_us_006"
DOMAIN = "tiktoktts"

SUPPORT_LANGUAGES = [
    # # DISNEY VOICES
    # "en_us_ghostface",  # Ghost Face
    # "en_us_chewbacca",  # Chewbacca
    # "en_us_c3po",  # C3PO
    # "en_us_stitch",  # Stitch
    # "en_us_stormtrooper",  # Stormtrooper
    # "en_us_rocket",  # Rocket
    # # ENGLISH VOICES
    # "en_au_001",  # English AU - Female
    # "en_au_002",  # English AU - Male
    # "en_uk_001",  # English UK - Male 1
    # "en_uk_003",  # English UK - Male 2
    # "en_us_001",  # English US - Female (Int. 1)
    # "en_us_002",  # English US - Female (Int. 2)
    # "en_us_006",  # English US - Male 1
    # "en_us_007",  # English US - Male 2
    # "en_us_009",  # English US - Male 3
    # "en_us_010",  # English US - Male 4
    # # EUROPE VOICES
    # "fr_001",  # French - Male 1
    # "fr_002",  # French - Male 2
    # "de_001",  # German - Female
    # "de_002",  # German - Male
    # "es_002",  # Spanish - Male
    # # AMERICA VOICES
    # "es_mx_002",  # Spanish MX - Male
    # "br_001",  # Portuguese BR - Female 1
    # "br_003",  # Portuguese BR - Female 2
    # "br_004",  # Portuguese BR - Female 3
    # "br_005",  # Portuguese BR - Male
    # # ASIA VOICES
    # "id_001",  # Indonesian - Female
    # "jp_001",  # Japanese - Female 1
    # "jp_003",  # Japanese - Female 2
    # "jp_005",  # Japanese - Female 3
    # "jp_006",  # Japanese - Male
    # "kr_002",  # Korean - Male 1
    # "kr_003",  # Korean - Female
    # "kr_004",  # Korean - Male 2
    # # SINGING VOICES
    # "en_female_f08_salut_damour",  # Alto
    # "en_male_m03_lobby",  # Tenor
    # "en_female_f08_warmy_breeze",  # Warmy Breeze
    # "en_male_m03_sunshine_soon",  # Sunshine Soon
    # # OTHER
    # "en_male_narration",  # narrator
    # "en_male_funny",  # wacky
    # "en_female_emotional",  # peaceful
    "en_male_jomboy", # English	Game On
    "en_us_002", # Jessie
    "es_mx_002", # Warm
    "en_male_funny", # Wacky
    "en_us_ghostface", # Scream
    "en_female_samc", # Empathetic
    "en_male_cody", # Serious
    "en_female_makeup", # Beauty Guru
    "en_female_richgirl", # Bestie
    "en_male_grinch", # Trickster
    "en_us_006", # Joey
    "en_male_narration", # Story Teller
    "en_male_deadpool", # Mr. GoodGuy
    "en_uk_001", # Narrator
    "en_uk_003", # Male English UK
    "en_au_001", # Metro
    "en_male_jarvis", # Alfred
    "en_male_ashmagic", # ashmagic
    "en_male_olantekkers", # olantekkers
    "en_male_ukneighbor", # Lord Cringe
    "en_male_ukbutler", # Mr. Meticulous
    "en_female_shenna", # Debutante
    "en_female_pansino", # Varsity
    "en_male_trevor", # Marty
    "en_female_f08_twinkle", # Pop Lullaby
    "en_male_m03_classical", # Classic Electric
    "en_female_betty", # Bae
    "en_male_cupid", # Cupid
    "en_female_grandma", # Granny
    "en_male_m2_xhxs_m03_christmas", # Cozy
    "en_male_santa_narration", # Author
    "en_male_sing_deep_jingle", # Caroler
    "en_male_santa_effect", # Santa
    "en_female_ht_f08_newyear", # NYE 2023
    "en_male_wizard", # Magician
    "en_female_ht_f08_halloween", # Opera
    "en_female_ht_f08_glorious", # Euphoric
    "en_male_sing_funny_it_goes_up", # Hypetrain
    "en_female_ht_f08_wonderful_world", # Melodrama
    "en_male_m2_xhxs_m03_silly", # Quirky Time
    "en_female_emotional", # Peaceful
    "en_male_m03_sunshine_soon", # Toon Beat
    "en_female_f08_warmy_breeze", # Open Mic
    "en_male_m03_lobby", # Jingle
    "en_male_sing_funny_thanksgiving", # Thanksgiving
    "en_female_f08_salut_damour", # Cottagecore
    "en_us_007", # Professor
    "en_us_009", # Scientist
    "en_us_010", # Confidence
    "en_au_002", # Smooth
    "en_us_ghostface", # Disney	Ghost Face
    "en_us_chewbacca", # Chewbacca
    "en_us_c3po", # C3PO
    "en_us_stitch", # Stitch
    "en_us_stormtrooper", # Stormtrooper
    "en_us_rocket", # Rocket
    "en_female_madam_leota", # Madame Leota
    "en_male_ghosthost", # Ghost Host
    "en_male_pirate", # Pirate
    "fr_001", # French	French - Male 1
    "fr_002", # French - Male 2
    "es_002", # Spanish	Spanish (Spain) - Male
    "es_mx_002", # Spanish MX - Male
    "br_001", # Portuguese	Portuguese BR - Female 1
    "br_003", # Portuguese BR - Female 2
    "br_004", # Portuguese BR - Female 3
    "br_005", # Portuguese BR - Male
    "bp_female_ludmilla", # Ludmilla
    "pt_female_lhays", # Lhays Macedo
    "pt_female_laizza", # Laizza
    "de_001", # German	German - Female
    "de_002", # German - Male
    "id_001", # Indonesian	Indonesian - Female
    "jp_001", # Japanese	Japanese - Female 1
    "jp_003", # Japanese - Female 2
    "jp_005", # Japanese - Female 3
    "jp_006", # Japanese - Male
    "jp_female_fujicochan", # りーさ
    "jp_female_hasegawariona", # 世羅鈴
    "jp_male_keiichinakano", # Morio’s Kitchen
    "jp_female_oomaeaika", # 夏絵ココ
    "jp_male_yujinchigusa", # 低音ボイス
    "jp_female_shirou", # 四郎
    "jp_male_tamawakazuki", # 玉川寿紀
    "jp_female_kaorishoji", # 庄司果織
    "jp_female_yagishaki", # 八木沙季
    "jp_male_hikakin", # ヒカキン
    "jp_female_rei", # 丸山礼
    "jp_male_shuichiro", # 修一朗
    "jp_male_matsudake", # マツダ家の日常
    "jp_female_machikoriiita", # まちこりーた
    "jp_male_matsuo", # モジャオ
    "jp_male_osada", # モリスケ
    "kr_002", # Korean	Korean - Male 1
    "kr_003", # Korean - Female
    "kr_004", # Korean - Male 2
    "BV074_streaming", # Vietnamese	Female
    "BV075_streaming", # Male
    "en_female_f08_salut_damour", # Other	Alto
    "en_male_m03_lobby", # Tenor
    "en_male_m03_sunshine_soon", # Sunshine Soon
    "en_female_f08_warmy_breeze", # Warmy Breeze
    "en_female_ht_f08_glorious", # Glorious
    "en_male_sing_funny_it_goes_up", # It Goes Up
    "en_male_m2_xhxs_m03_silly", # Chipmunk
    "en_female_ht_f08_wonderful_world", # Dramatic
]


@dataclass
class Dialect:
    """Voice for a dialect supported by TikTok TTS."""

    lang: str
