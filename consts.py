import re

import config

def InvertedDict(input_dict):
    return {value : key for key, value in input_dict.items()}

# =================================== Misc ===================================

kTableOfContentsIdentifier = '[WELCOME] TABLE OF CONTENTS'
kDlfAddedRulesSectionGroupId = '9900'
kDlfAddedRulesSectionGroupName = 'Dynamic Loot Filter Added Rules'

kSectionGroupHeaderTemplate = \
'''#===============================================================================================================
# [[{}]] {}
#==============================================================================================================='''

# Note: added a few extra dashes from NeverSink's template here
kSectionHeaderTemplate = \
'''#------------------------------------------------
#   [{}] {}
#------------------------------------------------'''

kSectionRePattern = re.compile(r'\[\d+\]+ .*')

# ================================= Map Tier =================================

# No idea if the ShapedMap matters, but NeverSink used it in his filters
kHideMapsBelowTierRuleTemplate = \
'''Hide $type->hide_maps_below_tier $tier->hide_maps_below_tier
Class Maps
ShapedMap False
MapTier < {}'''


# ================================= Currency =================================

kCurrencyTierNames = {1 : 't1exalted',
                      2 : 't2divine',
                      3 : 't3annul',
                      4 : 't4chaos',
                      5 : 't5alchemy',
                      6 : 't6chrom',
                      7 : 't7chance',
                      8 : 't8trans',
                      9 : 't9armour'}

kCurrencyTierNameToNumberMap = InvertedDict(kCurrencyTierNames)

# =============================== Chaos Recipe ===============================

kChaosRecipeRuleTemplate = \
'''Show $type->chaos_recipe_rares $tier->{}
SetBorderColor {}
SetFontSize 40
ItemLevel >= 60
Rarity Rare
Class {}
MinimapIcon {} {}'''

kChaosRecipeItemSlots = ['Weapons',
                         'Body Armours',
                         'Helmets',
                         'Gloves',
                         'Boots',
                         'Amulets',
                         'Rings',
                         'Belts']

# Need no spaces in tier tags
kChaosRecipeTierTags = {'Weapons' : 'weapons',
                        'Body Armours' : 'body_armours',
                        'Helmets' : 'helmets',
                        'Gloves' : 'gloves',
                        'Boots' : 'boots',
                        'Amulets': 'amulets',
                        'Rings' : 'rings',
                        'Belts' : 'belts'}
                        
kChaosRecipeTierToItemSlotMap = InvertedDict(kChaosRecipeTierTags)

kChaosRecipeBorderColors = {'Weapons' : '200 0 0 255',
                            'Body Armours' : '255 0 255 255',
                            'Helmets' : '255 114 0 255',
                            'Gloves' : '255 228 0 255',
                            'Boots' : '0 255 0 255',
                            'Amulets': '0 255 255 255',
                            'Rings' : '65 0 189 255',
                            'Belts' : '0 0 200 255'}

kChaosRecipeWeaponClassesString = '"' + '" "'.join(config.kChaosRecipeWeaponClasses) + '"'

kChaosRecipeClasses = {'Weapons' : kChaosRecipeWeaponClassesString,
                       'Body Armours' : '"Body Armours"',
                       'Helmets' : '"Helmets"',
                       'Gloves' : '"Gloves"',
                       'Boots' : '"Boots"',
                       'Amulets': '"Amulets"',
                       'Rings' : '"Rings"',
                       'Belts' : '"Belts"'}

kChaosRecipeMinimapIconSizeColorParams = {'Weapons' : '2 Red',
                                          'Body Armours' : '2 Pink',
                                          'Helmets' : '2 Orange',
                                          'Gloves' : '2 Yellow',
                                          'Boots' : '2 Green',
                                          'Amulets': '3 Cyan',
                                          'Rings' : '3 Purple',
                                          'Belts' : '2 Blue'}

kChaosRecipeMinimapIconType = 'Moon'

kChaosRecipeRuleStrings = [kChaosRecipeRuleTemplate.format(
                                   kChaosRecipeTierTags[item_slot],
                                   kChaosRecipeBorderColors[item_slot],
                                   kChaosRecipeClasses[item_slot],
                                   kChaosRecipeMinimapIconSizeColorParams[item_slot],
                                   kChaosRecipeMinimapIconType)
                               for item_slot in kChaosRecipeItemSlots]

