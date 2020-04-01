from enum import Enum
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.absolute()


class Stimuli(Enum):
    stimulus01 = CURRENT_DIR / "sentence_3.jpeg"
    stimulus02 = CURRENT_DIR / "building_1.jpg"
    stimulus03 = CURRENT_DIR / "Climb1.mp4"
    stimulus04 = CURRENT_DIR / "mu_1.mp4"
    stimulus05 = CURRENT_DIR / "sentence_2.jpeg"
    stimulus06 = CURRENT_DIR / "building_2.jpg"
    stimulus07 = CURRENT_DIR / "MAZ_146.jpg"
    stimulus08 = CURRENT_DIR / "mu_6.mp4"
    stimulus09 = CURRENT_DIR / "sentence_6.jpeg"
    stimulus10 = CURRENT_DIR / "RandomVoices1.mp4"
    stimulus11 = CURRENT_DIR / "sentence_1.jpeg"
    stimulus12 = CURRENT_DIR / "mu_4.mp4"
    stimulus13 = CURRENT_DIR / "33M_FE_O.jpg"
    stimulus14 = CURRENT_DIR / "faces_1.jpg"
    stimulus15 = CURRENT_DIR / "MLK3.mp4"
    stimulus16 = CURRENT_DIR / "sentence_5.jpeg"
    stimulus17 = CURRENT_DIR / "YR5.mp4"
    stimulus18 = CURRENT_DIR / "mu_2.mp4"
    stimulus19 = CURRENT_DIR / "sentence_4.jpeg"
    stimulus20 = CURRENT_DIR / "Mat3.mp4"
    stimulus21 = CURRENT_DIR / "sentence_8.jpeg"
    stimulus22 = CURRENT_DIR / "BB2.mp4"
    stimulus23 = CURRENT_DIR / "FFX_139.jpg"
    stimulus24 = CURRENT_DIR / "Kaleid1.mp4"
    stimulus25 = CURRENT_DIR / "sentence_7.jpeg"
    stimulus26 = CURRENT_DIR / "HarryPotter5.mp4"
    stimulus27 = CURRENT_DIR / "mu_3.mp4"
    stimulus28 = CURRENT_DIR / "Dis1.mp4"
    stimulus29 = CURRENT_DIR / "Climb3.mp4"
    stimulus30 = CURRENT_DIR / "CC3.mp4"
    stimulus31 = CURRENT_DIR / "faces_2.jpg"
    stimulus32 = CURRENT_DIR / "09F_AN_O.jpg"


class responses(Enum):
    Happy = 1
    Sad = 2
    Angry = 3
    Inspirational = 4
    Scary = 5
    none = 6
    Yes = "1"
    No = "0"
