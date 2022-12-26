from ImageEffects import EffectsCreator

# Global EC
try:
    EC: EffectsCreator = globals()['EC']
except:
    EC: EffectsCreator = EffectsCreator()
