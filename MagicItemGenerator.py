import numpy as np

#LISTS NEEDED
#MagicItem List (Randomly picks between Weapons, Armors, Trinkets, Consumables, SpellFoci)
#Weapons: Longswords, Battleaxes, etc
#Weapon Qualities:
#Armors: Light/Med/Hvy Bucker/Shield/Tower
#Armor Qualities:
#Trinkets: Cloak, Headband, Ring, Gloves, Boots
#Trinket Qualities:
#Consumables: Potion/Scroll
#Consumable Qualities:
#SpellFoci: Wand/Staff/Instrument/Symbol
#SpellFoci Qualities:

Weapons = ['Club',
           'Dagger',
           'Greatclub',
           'Handaxe',
           'Javelin',
           'LightHammer',
           'Mace',
           'Quarterstaff',
           'Sickle',
           'Spear',
           'Cestus',
           'LightCrossbow',
           'Dart',
           'Shortbow',
           'Sling',
           'Battleaxe',
           'Flail',
           'Glaive',
           'Greataxe',
           'Greatsword',
           'Halberd',
           'Lance',
           'Longsword',
           'Maul',
           'Morningstar',
           'Pike',
           'Rapier',
           'Scimitar',
           'Shortsword',
           'Trident',
           'WarPick',
           'Warhammer',
           'Whip',
           'Blowgun',
           'HandCrossbow',
           'HeavyCrossbow',
           'Longbow',
           'WarSpear',
           'PhalanxPike',
           'HeavyThrowingAxe',
           'Chakram',
           'ElvenLongsword',
           'BastardSword',
           'Urumi',
           'LucerneHammer',
           'DwarvenGreathammer',
           'OrcWaraxe',
           'Greatlance',
           'Estoc',
           'RecurveBow',
           'YeomanBow',
           'RepeatingCrossbow',
           'Arbalest',
           'Greatbow']

WeaponQualities = [('AtkDmgBonus',42),
                   ('Vicious', 5),
                   ('StatUsage', 5),
                   ('StatUsageBonus', 5),
                   ('Imbued', 10),
                   ('Inflict', 10),
                   ('TypeBane', 5),
                   ('AttackRate', 2),
                   ('ClassAugment', 5),
                   ('CritRider', 5),
                   ('Spellcasting', 5),
                   ('Unique', 1)]

WeaponQualities2 = [('AtkDmgBonus',42),
                   ('Vicious', 52),
                   ('StatUsage', 57),
                   ('StatUsageBonus', 62),
                   ('Imbued', 72),
                   ('Inflict', 82),
                   ('TypeBane', 87),
                   ('AttackRate', 89),
                   ('ClassAugment', 94),
                   ('Spellcasting', 99),
                    ('Unique', 100)]

ItemRarity = ['Common',
              'Uncommon',
              'Rare',
              'Very Rare',
              'Legendary']

AtkDmgBonus = [('+1A +0D', 5),
               ('+0A +2D', 10),
               ('+1A -1D', 12),
               ('-1A +2D', 14),
               ('-1A +0D', 15),
               ('+0A -1D', 16),
               ('+1A +1D', 19),
               ('-1A -1D', 20)]

Vicious = [('CritChance -1', 6),
           ('CritChance -2', 8),
           ('CritChance -3', 9),
           ('CritDice +1', 14),
           ('CritDice +2', 16),
           ('CritDice +3', 17),
           ('CritMult +1X', 19),
           ('CritMult +2X', 20)]

StatUsage = [('USAGE:STR - STR', 5),
             ('USAGE:STR - DEX', 6),
             ('USAGE:STR - CON', 7),
             ('USAGE:STR - INT', 8),
             ('USAGE:STR - WIS', 9),
             ('USAGE:STR - CHA', 10),
             ('USAGE:DEX - STR', 11),
             ('USAGE:DEX - DEX', 16),
             ('USAGE:DEX - CON', 17),
             ('USAGE:DEX - INT', 18),
             ('USAGE:DEX - WIS', 19),
             ('USAGE:DEX - CHA', 20),
             ('USAGE:CON - STR', 21),
             ('USAGE:CON - DEX', 22),
             ('USAGE:CON - CON', 27),
             ('USAGE:CON - INT', 28),
             ('USAGE:CON - WIS', 29),
             ('USAGE:CON - CHA', 30),
             ('USAGE:INT - STR', 31),
             ('USAGE:INT - DEX', 32),
             ('USAGE:INT - CON', 33),
             ('USAGE:INT - INT', 38),
             ('USAGE:INT - WIS', 39),
             ('USAGE:INT - CHA', 40),
             ('USAGE:WIS - STR', 41),
             ('USAGE:WIS - DEX', 42),
             ('USAGE:WIS - CON', 43),
             ('USAGE:WIS - INT', 44),
             ('USAGE:WIS - WIS', 49),
             ('USAGE:WIS - CHA', 50),
             ('USAGE:CHA - STR', 51),
             ('USAGE:CHA - DEX', 52),
             ('USAGE:CHA - CON', 53),
             ('USAGE:CHA - INT', 54),
             ('USAGE:CHA - WIS', 55),
             ('USAGE:CHA - CHA', 60)]

StatUsageBonus = [('BONUS:STR - X', 2),
                  ('BONUS:X - STR', 4),
                  ('BONUS:STR - STR', 5),
                  ('BONUS:STR - DEX', 6),
                  ('BONUS:STR - CON', 7),
                  ('BONUS:STR - INT', 8),
                  ('BONUS:STR - WIS', 9),
                  ('BONUS:STR - CHA', 10),
                  ('BONUS:DEX - X', 12),
                  ('BONUS:X - DEX', 14),
                  ('BONUS:DEX - STR', 15),
                  ('BONUS:DEX - DEX', 16),
                  ('BONUS:DEX - CON', 17),
                  ('BONUS:DEX - INT', 18),
                  ('BONUS:DEX - WIS', 19),
                  ('BONUS:DEX - CHA', 20),
                  ('BONUS:CON - X', 22),
                  ('BONUS:X - CON', 24),
                  ('BONUS:CON - STR', 25),
                  ('BONUS:CON - DEX', 26),
                  ('BONUS:CON - CON', 27),
                  ('BONUS:CON - INT', 28),
                  ('BONUS:CON - WIS', 29),
                  ('BONUS:CON - CHA', 30),
                  ('BONUS:INT - X', 32),
                  ('BONUS:X - INT', 34),
                  ('BONUS:INT - STR', 35),
                  ('BONUS:INT - DEX', 36),
                  ('BONUS:INT - CON', 37),
                  ('BONUS:INT - INT', 38),
                  ('BONUS:INT - WIS', 39),
                  ('BONUS:INT - CHA', 40),
                  ('BONUS:WIS - X', 42),
                  ('BONUS:X - WIS', 44),
                  ('BONUS:WIS - STR', 45),
                  ('BONUS:WIS - DEX', 46),
                  ('BONUS:WIS - CON', 47),
                  ('BONUS:WIS - INT', 48),
                  ('BONUS:WIS - WIS', 49),
                  ('BONUS:WIS - CHA', 50),
                  ('BONUS:CHA - X', 52),
                  ('BONUS:X - CHA', 54),
                  ('BONUS:CHA - STR', 55),
                  ('BONUS:CHA - DEX', 56),
                  ('BONUS:CHA - CON', 57),
                  ('BONUS:CHA - INT', 58),
                  ('BONUS:CHA - WIS', 59),
                  ('BONUS:CHA - CHA', 60)]

Imbued = [('1d4 Physical', 5),
          ('1d6 Physical', 8),
          ('1d8 Physical', 9),
          ('1d10 Physical', 10),
          ('1d12 Physical', 11),
          ('1d4 Acid', 16),
          ('1d6 Acid', 19),
          ('1d8 Acid', 20),
          ('1d10 Acid', 21),
          ('1d12 Acid', 22),
          ('1d4 Cold', 27),
          ('1d6 Cold', 30),
          ('1d8 Cold', 31),
          ('1d10 Cold', 32),
          ('1d12 Cold', 33),
          ('1d4 Fire', 38),
          ('1d6 Fire', 41),
          ('1d8 Fire', 42),
          ('1d10 Fire', 43),
          ('1d12 Fire', 44),
          ('1d4 Force', 49),
          ('1d6 Force', 52),
          ('1d8 Force', 53),
          ('1d10 Force', 54),
          ('1d12 Force', 55),
          ('1d4 Lightning', 60),
          ('1d6 Lightning', 63),
          ('1d8 Lightning', 64),
          ('1d10 Lightning', 65),
          ('1d12 Lightning', 66),
          ('1d4 Necrotic', 71),
          ('1d6 Necrotic', 74),
          ('1d8 Necrotic', 75),
          ('1d10 Necrotic', 76),
          ('1d12 Necrotic', 77),
          ('1d4 Poison', 82),
          ('1d6 Poison', 85),
          ('1d8 Poison', 86),
          ('1d10 Poison', 87),
          ('1d12 Poison', 88),
          ('1d4 Psychic', 93),
          ('1d6 Psychic', 96),
          ('1d8 Psychic', 97),
          ('1d10 Psychic', 98),
          ('1d12 Psychic', 99),
          ('1d4 Radiant', 104),
          ('1d6 Radiant', 107),
          ('1d8 Radiant', 108),
          ('1d10 Radiant', 109),
          ('1d12 Radiant', 110),
          ('1d4 Thunder', 115),
          ('1d6 Thunder', 118),
          ('1d8 Thunder', 119),
          ('1d10 Thunder', 120),
          ('1d12 Thunder', 121),
          ('On-Hit Blinded - 1 round', 122),
          ('On-Hit Charmed - 1 round', 123),
          ('On-Hit Deafened - 1 round', 124),
          ('On-Hit Exhaustion - 1 round', 125),
          ('On-Hit Frightened - 1 round', 126),
          ('On-Hit Grappled - 1 round', 127),
          ('On-Hit Incapacitated - 1 round', 128),
          ('On-Hit Paralyzed - 1 round', 129),
          ('On-Hit Petrified - 1 round', 130),
          ('On-Hit Poisoned - 1 minute', 131),
          ('On-Hit Prone', 132),
          ('On-Hit Restrained - 1 round', 133),
          ('On-Hit Stunned - 1 round', 134),
          ('On-Hit Unconscious - 1 round', 135),
          ('On-Hit Negative Level', 136),
          ('On-Hit Reduce Str By 1 - 1 minute', 137),
          ('On-Hit Reduce Dex By 1 - 1 minute', 138),
          ('On-Hit Reduce Con By 1 - 1 minute', 139),
          ('On-Hit Reduce Int By 1 - 1 minute', 140),
          ('On-Hit Reduce Wis By 1 - 1 minute', 141),
          ('On-Hit Reduce Cha By 1 - 1 minute', 142),
          ('On-Hit Reduce AC By 1 - 1 round', 143),
          ('On-Hit Reduce Speed By 5ft - 1 round', 144),
          ('On-Hit Push 5ft Back', 145),
          ('On-Hit Quarter LifeSteal', 146),
          ('On-Hit Half LifeSteal', 147),
          ('On-Hit Full Lifesteal', 148),
          ('On-Hit Double Lifesteal', 149),
          ('On-Hit Hit Point Reduction', 150),
          ('On-Hit Increase Str By 1 - 1 minute', 151),
          ('On-Hit Increase Dex By 1 - 1 minute', 152),
          ('On-Hit Increase Con By 1 - 1 minute', 153),
          ('On-Hit Increase Int By 1 - 1 minute', 154),
          ('On-Hit Increase Wis By 1 - 1 minute', 155),
          ('On-Hit Increase Cha By 1 - 1 minute', 156),
          ('On-Hit Increase AC By 1 - 1 round', 157),
          ('On-Hit Increase Speed By 5ft - 1 round', 158)]

Inflict = [('Inflict 2d8 Physical', 2),
           ('Inflict 2d8 Acid', 4),
           ('Inflict 2d8 Cold', 6),
           ('Inflict 2d8 Fire', 8),
           ('Inflict 2d8 Force', 10),
           ('Inflict 2d8 Lightning', 12),
           ('Inflict 2d8 Necrotic', 14),
           ('Inflict 2d8 Poison', 16),
           ('Inflict 2d8 Psychic', 18),
           ('Inflict 2d8 Radiant', 20),
           ('Inflict 2d8 Thunder', 22),
           ('Inflict 5d8 Physical', 23),
           ('Inflict 5d8 Acid', 24),
           ('Inflict 5d8 Cold', 25),
           ('Inflict 5d8 Fire', 26),
           ('Inflict 5d8 Force', 27),
           ('Inflict 5d8 Lightning', 28),
           ('Inflict 5d8 Necrotic', 29),
           ('Inflict 5d8 Poison', 30),
           ('Inflict 5d8 Psychic', 31),
           ('Inflict 5d8 Radiant', 32),
           ('Inflict 5d8 Thunder', 33),
           ('Inflict Blinded - 1 minute', 35),
          ('Inflict Charmed - 1 minute', 37),
          ('Inflict Deafened - 1 minute', 39),
          ('Inflict Exhaustion - 1 minute', 41),
          ('Inflict Frightened - 1 minute', 43),
          ('Inflict Grappled - 1 minute', 45),
          ('Inflict Incapacitated - 1 minute', 46),
          ('Inflict Paralyzed - 1 minute', 47),
          ('Inflict Petrified - 1 minute', 48),
          ('Inflict Poisoned - 1 minute', 50),
          ('Inflict Prone', 52),
          ('Inflict Restrained - 1 minute', 54),
          ('Inflict Stunned - 1 minute', 55),
          ('Inflict Unconscious - 1 minute', 56),
          ('Inflict Negative Level', 58),
          ('Inflict Reduce Str By 2 - 1 minute', 59),
          ('Inflict Reduce Dex By 2 - 1 minute', 60),
          ('Inflict Reduce Con By 2 - 1 minute', 61),
          ('Inflict Reduce Int By 2 - 1 minute', 62),
          ('Inflict Reduce Wis By 2 - 1 minute', 63),
          ('Inflict Reduce Cha By 2 - 1 minute', 64),
          ('Inflict Reduce AC By 2 - 1 minute', 65),
          ('Inflict Reduce Speed By 10ft - 1 minute', 67),
          ('Inflict Push 15ft Back', 69),
           ('Inflict Death', 70)]

AttackRate = [('Rapid AttackRate', 3),
              ('Slow AttackRate', 4)]

TypeBane = [('SlaughterDemon Bane 2d6 Physical', 5),
            ('SlaughterDemon Bane 2d8 Physical', 8),
            ('SlaughterDemon Bane 2d10 Physical', 9),
            ('SlaughterDemon Bane 2d12 Physical', 10),
            ('PestilenceDemon Bane 2d6 Physical', 15),
            ('PestilenceDemon Bane 2d8 Physical', 18),
            ('PestilenceDemon Bane 2d10 Physical', 19),
            ('PestilenceDemon Bane 2d12 Physical', 20),
            ('DesireDemon Bane 2d6 Physical', 25),
            ('DesireDemon Bane 2d8 Physical', 28),
            ('DesireDemon Bane 2d10 Physical', 29),
            ('DesireDemon Bane 2d12 Physical', 30),
            ('LiesDemon Bane 2d6 Physical', 35),
            ('LiesDemon Bane 2d8 Physical', 38),
            ('LiesDemon Bane 2d10 Physical', 39),
            ('LiesDemon Bane 2d12 Physical', 40),
            ('Devil Bane 2d6 Physical', 45),
            ('Devil Bane 2d8 Physical', 48),
            ('Devil Bane 2d10 Physical', 49),
            ('Devil Bane 2d12 Physical', 50),
            ('Tanari Bane 2d6 Physical', 55),
            ('Tanari Bane 2d8 Physical', 58),
            ('Tanari Bane 2d10 Physical', 59),
            ('Tanari Bane 2d12 Physical', 60),
            ('Yugoloth Bane 2d6 Physical', 65),
            ('Yugoloth Bane 2d8 Physical', 68),
            ('Yugoloth Bane 2d10 Physical', 69),
            ('Yugoloth Bane 2d12 Physical', 70),
            ('Demodand Bane 2d6 Physical', 75),
            ('Demodand Bane 2d8 Physical', 78),
            ('Demodand Bane 2d10 Physical', 79),
            ('Demodand Bane 2d12 Physical', 80),
            ('Qlippoth Bane 2d6 Physical', 85),
            ('Qlippoth Bane 2d8 Physical', 88),
            ('Qlippoth Bane 2d10 Physical', 89),
            ('Qlippoth Bane 2d12 Physical', 90),
            ('Humanoid Bane 2d6 Physical', 95),
            ('Humanoid Bane 2d8 Physical', 98),
            ('Humanoid Bane 2d10 Physical', 99),
            ('Humanoid Bane 2d12 Physical', 100),
            ('SlaughterDemon Bane +1A', 102),
            ('PestilenceDemon Bane +1A', 104),
            ('DesireDemon Bane +1A', 106),
            ('LiesDemon Bane +1A', 108),
            ('Devils Bane +1A', 110),
            ('Tanari Bane +1A', 112),
            ('Yugoloth Bane +1A', 114),
            ('Demodand Bane +1A', 116),
            ('Qlippoth Bane +1A', 118),
            ('Humanoid Bane +1A', 120),
            ('SlaughterDemon Bane +2A', 121),
            ('PestilenceDemon Bane +2A', 122),
            ('DesireDemon Bane +2A', 123),
            ('LiesDemon Bane +2A', 124),
            ('Devils Bane +2A', 125),
            ('Tanari Bane +2A', 126),
            ('Yugoloth Bane +2A', 127),
            ('Demodand Bane +2A', 128),
            ('Qlippoth Bane +2A', 129),
            ('Humanoid Bane +2A', 130),
            ('SlaughterDemon Bane CritChance', 131),
            ('PestilenceDemon Bane CritChance', 132),
            ('DesireDemon Bane CritChance', 133),
            ('LiesDemon Bane CritChance', 134),
            ('Devils Bane CritChance', 135),
            ('Tanari Bane CritChance', 136),
            ('Yugoloth Bane CritChance', 137),
            ('Demodand Bane CritChance', 138),
            ('Qlippoth Bane CritChance', 139),
            ('Humanoid Bane CritChance', 140),
            ('SlaughterDemon Bane CritMult', 141),
            ('PestilenceDemon Bane CritMult', 142),
            ('DesireDemon Bane CritMult', 143),
            ('LiesDemon Bane CritMult', 144),
            ('Devils Bane CritMult', 145),
            ('Tanari Bane CritMult', 146),
            ('Yugoloth Bane CritMult', 147),
            ('Demodand Bane CritMult', 148),
            ('Qlippoth Bane CritMult', 149),
            ('Humanoid Bane CritMult', 150)]

ClassAugment = [('Barbarian - Rage', 1),
                ('Barbarian - Unarmored Defense', 2),
                ('Barbarian - Brutal Critical', 3),
                ('Bard - Bardic Inspiration', 4),
                ('Bard - Expertise', 5),
                ('Bard - Magical Secrets', 6),
                ('Cleric - Channel Divinity', 7),
                ('Cleric - Domain Spell', 8),
                ('Cleric - Divine Strike', 9),
                ('Druid - Wildshape', 10),
                ('Druid - NaturalResistance', 11),
                ('Druid - Circle Spell', 12),
                ('Fighter - Second Wind', 13),
                ('Fighter - Action Surge', 14),
                ('Fighter - Indomitable', 15),
                ('Monk - Martial Arts Die', 16),
                ('Monk - Ki Points', 17),
                ('Monk - Unarmored Defense & Movement', 18),
                ('Paladin - Lay On Hands', 19),
                ('Paladin - Divine Smite', 20),
                ('Paladin - Auras', 21),
                ('Ranger - Favored Enemy/Foe', 22),
                ('Ranger - Primal Awareness Spell', 23),
                ('Ranger - Deft/Natural Explorer', 24),
                ('Rogue - SneakAttack', 25),
                ('Rogue - Expertise', 26),
                ('Rogue - Cunning Action', 27),
                ('Sorcerer - Font of Magic', 28),
                ('Sorcerer - Metamagic', 29),
                ('Sorcerer - Bloodline', 30),
                ('Warlock - Invocation', 31),
                ('Warlock - Pact Boon', 32),
                ('Warlock - Pact Magic', 33),
                ('Wizard - Arcane Recovery', 34),
                ('Wizard - Spellbook', 35),
                ('Wizard - Pact Magic', 36),
                ('Artificer - Infuse Item', 37),
                ('Artificer - Flash of Genius', 38),
                ('Artificer - Magic Item Attunement', 39)]

Spellcasting = [('Bard Spell', 5),
                ('Cleric Spell', 10),
                ('Druid Spell', 15),
                ('Paladin Spell', 20),
                ('Ranger Spell', 25),
                ('Sorcerer Spell', 30),
                ('Warlock Spell', 35),
                ('Wizard Spell', 40),
                ('High Magic Spell', 41),
                ('Fire Spell', 42),
                ('Beasts Spell', 43),
                ('Metal Spell', 44),
                ('Light Spell', 45),
                ('Life Spell', 46),
                ('Heavens Spell', 47),
                ('Shadows Spell', 48),
                ('Death Spell', 49),
                ('Wilds Spell', 50),
                ('Fel Magic Spell', 51),
                ('Change Spell', 52),
                ('Decay Spell', 53),
                ('Excess Spell', 54),
                ('Maw Spell', 55),
                ('Havoc Spell', 56),
                ('Deceit Spell', 57),
                ('Ruin Spell', 58),
                ('Runes Spell', 59),
                ('Vengeance Spell', 60),
                ('Undeath Spell', 61),
                ('Frost Spell', 62),
                ('Physiomancy Spell', 63),
                ('Psychomancy Spell', 64),
                ('Biomancy Spell', 65),
                ('Infernals Spell', 66),
                ('Earth Spell', 67),
                ('Water Spell', 68),
                ('Air Spell', 69),
                ('Fey Spell', 70),
                ('Judgement Spell', 71)]

Armors = ['Padded Armor',
          'Leather Armor',
          'Studded Leather Armor',
          'Hide Armor',
          'Chain Shirt Armor',
          'Scale Mail Armor',
          'Breastplate Armor',
          'Half Plate Armor',
          'Ring Mail Armor',
          'Chain Mail Armor',
          'Splint Armor',
          'Plate Armor',
          'Heavy Plate Armor',
          'Buckler Shield',
          'Medium Shield',
          'Tower shield']

ArmorQualities = [('Defensive', 37),
                  ('DamageBlock', 47),
                  ('DamageResist', 53),
                  ('Vitality', 63),
                  ('Bulky', 69),
                  ('Immunity', 75),
                  ('Aegis', 81),
                  ('TypeResist', 87),
                  ('Regeneration', 93),
                  ('StatArmorUse', 99),
                  ('Unique', 100)]

Defensive = [('+0 AC', 1),
             ('+1 AC', 7),
             ('-1 AC', 8),
             ('+1 AC vs Melee', 11),
             ('-1 AC vs Melee', 12),
             ('+1 AC vs Ranged', 15),
             ('-1 AC vs Ranged', 16),
             ('+1 AC vs Melee, -1 AC vs Ranged', 18),
             ('-1 AC vs Melee, +1 AC vs Ranged', 20)]

DamageBlock = [('PhysDmgBlock 5', 8),
               ('PhysDmgBlock 10', 13),
               ('PhysDmgBlock 15', 15),
               ('AcidDmgBlock 5', 18),
               ('AcidDmgBlock 10', 20),
               ('AcidDmgBlock 15', 21),
               ('ColdDmgBlock 5', 24),
               ('ColdDmgBlock 10', 26),
               ('ColdDmgBlock 15', 27),
               ('FireDmgBlock 5', 30),
               ('FireDmgBlock 10', 32),
               ('FireDmgBlock 15', 33),
               ('ForceDmgBlock 5', 36),
               ('ForceDmgBlock 10', 38),
               ('ForceDmgBlock 15', 39),
               ('LightningDmgBlock 5', 42),
               ('LightningDmgBlock 10', 44),
               ('LightningDmgBlock 15', 45),
               ('NecroticDmgBlock 5', 48),
               ('NecroticDmgBlock 10', 50),
               ('NecroticDmgBlock 15', 51),
               ('PoisonDmgBlock 5', 54),
               ('PoisonDmgBlock 10', 56),
               ('PoisonDmgBlock 15', 57),
               ('PsychicDmgBlock 5', 60),
               ('PsychicDmgBlock 10', 62),
               ('PsychicDmgBlock 15', 63),
               ('RadiantDmgBlock 5', 66),
               ('RadiantDmgBlock 10', 68),
               ('RadiantDmgBlock 15', 69),
               ('ThunderDmgBlock 5', 72),
               ('ThunderDmgBlock 10', 74),
               ('ThunderDmgBlock 15', 75)]

DamageResist = [('Phys Vulnerability', 1),
                ('Acid Vulnerability', 3),
                ('Cold Vulnerability', 5),
                ('Fire Vulnerability', 7),
                ('Force Vulnerability', 9),
                ('Lightning Vulnerability', 11),
                ('Necrotic Vulnerability', 13),
                ('Poison Vulnerability', 15),
                ('Psychic Vulnerability', 17),
                ('Radiant Vulnerability', 19),
                ('Thunder Vulnerability', 21),
                ('Phys Resistance', 23),
                ('Acid Resistance', 28),
                ('Cold Resistance', 33),
                ('Fire Resistance', 38),
                ('Force Resistance', 43),
                ('Lightning Resistance', 48),
                ('Necrotic Resistance', 53),
                ('Poison Resistance', 58),
                ('Psychic Resistance', 63),
                ('Radiant Resistance', 68),
                ('Thunder Resistance', 73),
                ('Phys Immunity', 74),
                ('Acid Immunity', 76),
                ('Cold Immunity', 78),
                ('Fire Immunity', 80),
                ('Force Immunity', 82),
                ('Lightning Immunity', 84),
                ('Necrotic Immunity', 86),
                ('Poison Immunity', 88),
                ('Psychic Immunity', 90),
                ('Radiant Immunity', 92),
                ('Thunder Immunity', 94)]

Vitality = [('-30 HP', 1),
            ('-20 HP', 3),
            ('-10 HP', 6),
            ('+10 HP', 16),
            ('+20 HP', 22),
            ('+30 HP', 26),
            ('+40 HP', 29),
            ('+50 HP', 31),
            ('+75 HP', 32),
            ('+100 HP', 33)]

Bulky = [('-10ft Speed', 1),
         ('-5ft Speed', 4),
         ('+5ft Speed', 14),
         ('+10ft Speed', 19),
         ('+15ft Speed', 22),
         ('+20ft Speed', 24),
         ('+30ft Speed', 25),
         ('10ft Flying Speed', 28),
         ('20ft Flying Speed', 29),
         ('30ft Flying Speed', 30),
         ('10ft Swimming Speed', 33),
         ('20ft Swimming Speed', 34),
         ('30ft Swimming Speed', 35)]

Immunity = [('Blinded Susceptibility', 1),
            ('Charmed Susceptibility', 2),
            ('Deafened Susceptibility', 3),
            ('Exhaustion Susceptibility', 4),
            ('Frightened Susceptibility', 5),
            ('Grappled Susceptibility', 6),
            ('Incapacitated Susceptibility', 7),
            ('Paralyzed Susceptibility', 8),
            ('Petrified Susceptibility', 9),
            ('Poisoned Susceptibility', 10),
            ('Prone Susceptibility', 11),
            ('Restrained Susceptibility', 12),
            ('Stunned Susceptibility', 13),
            ('Unconscious Susceptibility', 14),
            ('Dazed Susceptibility', 15),
            ('NegativeLevel Susceptibility', 16),
            ('Blinded Disadv', 19),
            ('Charmed Disadv', 22),
            ('Deafened Disadv', 25),
            ('Exhaustion Disadv', 28),
            ('Frightened Disadv', 31),
            ('Grappled Disadv', 34),
            ('Incapacitated Disadv', 37),
            ('Paralyzed Disadv', 40),
            ('Petrified Disadv', 43),
            ('Poisoned Disadv', 46),
            ('Prone Disadv', 49),
            ('Restrained Disadv', 52),
            ('Stunned Disadv', 55),
            ('Unconscious Disadv', 58),
            ('Dazed Disadv', 61),
            ('NegativeLevel Disadv', 64),
            ('Blinded Advantage', 74),
            ('Charmed Advantage', 84),
            ('Deafened Advantage', 94),
            ('Exhaustion Advantage', 104),
            ('Frightened Advantage', 114),
            ('Grappled Advantage', 124),
            ('Incapacitated Advantage', 134),
            ('Paralyzed Advantage', 144),
            ('Petrified Advantage', 154),
            ('Poisoned Advantage', 164),
            ('Prone Advantage', 174),
            ('Restrained Advantage', 184),
            ('Stunned Advantage', 194),
            ('Unconscious Advantage', 204),
            ('Dazed Advantage', 214),
            ('NegativeLevel Advantage', 224),
            ('Blinded Immunity', 227),
            ('Charmed Immunity', 230),
            ('Deafened Immunity', 233),
            ('Exhaustion Immunity', 236),
            ('Frightened Immunity', 239),
            ('Grappled Immunity', 242),
            ('Incapacitated Immunity', 245),
            ('Paralyzed Immunity', 248),
            ('Petrified Immunity', 251),
            ('Poisoned Immunity', 254),
            ('Prone Immunity', 257),
            ('Restrained Immunity', 260),
            ('Stunned Immunity', 263),
            ('Unconscious Immunity', 266),
            ('Dazed Immunity', 269),
            ('NegativeLevel Immunity', 272)]

Aegis = [('-2 to Saves', 1),
         ('-2 to StrSaves', 3),
         ('-2 to DexSaves', 5),
         ('-2 to ConSaves', 7),
         ('-2 to IntSaves', 9),
         ('-2 to WisSaves', 11),
         ('-2 to ChaSaves', 13),
         ('-2 to StrDexConSaves', 14),
         ('-2 to IntWisChaSaves', 15),
         ('-1 to Saves', 16),
         ('-1 to StrSaves', 19),
         ('-1 to DexSaves', 22),
         ('-1 to ConSaves', 25),
         ('-1 to IntSaves', 28),
         ('-1 to WisSaves', 31),
         ('-1 to ChaSaves', 34),
         ('-1 to StrDexConSaves', 36),
         ('-1 to IntWisChaSaves', 38),
         ('+1 to Saves', 42),
         ('+1 to StrSaves', 52),
         ('+1 to DexSaves', 62),
         ('+1 to ConSaves', 72),
         ('+1 to IntSaves', 82),
         ('+1 to WisSaves', 92),
         ('+1 to ChaSaves', 102),
         ('+1 to StrDexConSaves', 108),
         ('+1 to IntWisChaSaves', 114),
         ('+2 to Saves', 116),
         ('+2 to StrSaves', 124),
         ('+2 to DexSaves', 132),
         ('+2 to ConSaves', 140),
         ('+2 to IntSaves', 148),
         ('+2 to WisSaves', 156),
         ('+2 to ChaSaves', 164),
         ('+2 to StrDexConSaves', 168),
         ('+2 to IntWisChaSaves', 172),
         ('+3 to Saves', 173),
         ('+3 to StrSaves', 179),
         ('+3 to DexSaves', 185),
         ('+3 to ConSaves', 191),
         ('+3 to IntSaves', 197),
         ('+3 to WisSaves', 203),
         ('+3 to ChaSaves', 209),
         ('+3 to StrDexConSaves', 211),
         ('+3 to IntWisChaSaves', 213),
         ('+Str to Saves', 214),
         ('+Dex to Saves', 215),
         ('+Con to Saves', 216),
         ('+Int to Saves', 217),
         ('+Wis to Saves', 218),
         ('+Cha to Saves', 219)]

TypeResist = [('SlaughterDemon Protection', 4),
            ('PestilenceDemon Protection', 8),
            ('DesireDemon Protection', 12),
            ('LiesDemon Protection', 16),
            ('Devils Protection', 20),
            ('Tanari Protection', 24),
            ('Yugoloth Protection', 28),
            ('Demodand Protection', 32),
            ('Qlippoth Protection', 36),
            ('Humanoid Protection', 40),
              ('Fiend Protection', 41),
              ('SlaughterDemon Weakness', 42),
            ('PestilenceDemon Weakness', 43),
            ('DesireDemon Weakness', 44),
            ('LiesDemon Weakness', 45),
            ('Devils Weakness', 46),
            ('Tanari Weakness', 47),
            ('Yugoloth Weakness', 48),
            ('Demodand Weakness', 49),
            ('Qlippoth Weakness', 50),
            ('Humanoid Weakness', 51)]

Regeneration = [('Regeneration 1, Conscious', 10),
                ('Regeneration 3, Conscious', 20),
                ('Regeneration 5, Conscious', 30),
                ('Regeneration 10, Conscious', 38),
                ('Regeneration 15, Conscious', 44),
                ('Regeneration 20, Conscious', 48),
                ('Regeneration 25, Conscious', 50),
                ('Regeneration 30, Conscious', 51),
                ('Regeneration 1, Unconscious', 56),
                ('Regeneration 3, Unconscious', 61),
                ('Regeneration 5, Unconscious', 66),
                ('Regeneration 10, Unconscious', 70),
                ('Regeneration 15, Unconscious', 73),
                ('Regeneration 20, Unconscious', 75),
                ('Regeneration 25, Unconscious', 76),
                ('Regeneration 30, Unconscious', 77)]

StatArmorUse = [('StrArmorUsage', 5),
                ('DexArmorUsage', 10),
                ('ConArmorUsage', 15),
                ('IntArmorUsage', 20),
                ('WisArmorUsage', 25),
                ('ChaArmorUsage', 30),
                ('StrArmorBonus', 32),
                ('DexArmorBonus', 34),
                ('ConArmorBonus', 36),
                ('IntArmorBonus', 38),
                ('WisArmorBonus', 40),
                ('ChaArmorBonus', 42)]

Trinkets = ['Cloak',
            'Headband',
            'Ring',
            'Gloves',
            'Boots',
            'Belt',
            'Amulet',
            'Robe',
            'Talisman',
            'Gauntlet']

TrinketQualities = [('Defensive', 20),
                    ('DamageResist', 30),
                    ('Vitality', 35),
                    ('Bulky', 40),
                    ('Immunity', 45),
                    ('Aegis', 55),
                    ('Spellcasting', 65),
                    ('ClassAugment', 70),
                    ('StatBonus', 99),
                    ('Unique', 100)]

StatBonus = [('+2 Str Bonus', 6),
             ('+2 Dex Bonus', 12),
             ('+2 Con Bonus', 18),
             ('+2 Int Bonus', 24),
             ('+2 Wis Bonus', 30),
             ('+2 Cha Bonus', 36),
             ('+4 Str Bonus', 40),
             ('+4 Dex Bonus', 44),
             ('+4 Con Bonus', 48),
             ('+4 Int Bonus', 52),
             ('+4 Wis Bonus', 56),
             ('+4 Cha Bonus', 60),
             ('+6 Str Bonus', 62),
             ('+6 Dex Bonus', 64),
             ('+6 Con Bonus', 66),
             ('+6 Int Bonus', 68),
             ('+6 Wis Bonus', 70),
             ('+6 Cha Bonus', 72),
             ('+8 Str Bonus', 73),
             ('+8 Dex Bonus', 74),
             ('+8 Con Bonus', 75),
             ('+8 Int Bonus', 76),
             ('+8 Wis Bonus', 77),
             ('+8 Cha Bonus', 78),
             ('Set Str 20', 83),
             ('Set Dex 20', 88),
             ('Set Con 20', 93),
             ('Set Int 20', 98),
             ('Set Wis 20', 103),
             ('Set Cha 20', 108),
             ('Set Str 22', 112),
             ('Set Dex 22', 116),
             ('Set Con 22', 120),
             ('Set Int 22', 124),
             ('Set Wis 22', 128),
             ('Set Cha 22', 132),
             ('Set Str 24', 135),
             ('Set Dex 24', 138),
             ('Set Con 24', 141),
             ('Set Int 24', 144),
             ('Set Wis 24', 147),
             ('Set Cha 24', 150),
             ('Set Str 26', 152),
             ('Set Dex 26', 154),
             ('Set Con 26', 156),
             ('Set Int 26', 158),
             ('Set Wis 26', 160),
             ('Set Cha 26', 162),
             ('Set Str 28', 163),
             ('Set Dex 28', 164),
             ('Set Con 28', 165),
             ('Set Int 28', 166),
             ('Set Wis 28', 167),
             ('Set Cha 28', 168),
             ('+1 Proficiency Bonus', 169),
             ('+2 Proficiency Bonus', 170)]

Consumables = ['Potion',
               'Scroll']

ConsumableQualities = [('Spellcasting', 49),
                       ('Healing', 99),
                       ('Unique', 100)]

Healing = [('Heal for 2d4+2 hit points', 20),
           ('Heal for 4d4+4 hit points', 30),
           ('Heal for 8d4+8 hit points', 35),
           ('Heal for 16d4+16 hit points', 37),
           ('Heal for 32d4+32 hit points', 38)]

SpellFocus = ['Bard SpellFocus',
             'Cleric/Paladin SpellFocus',
             'Druid/Ranger SpellFocus',
             'Sorcerer/Warlock/Wizard SpellFocus',
             'Artificer SpellFocus']

SpellFocusQualities = [('Spellcasting', 34),
                       ('Spellsave Bonus', 49),
                       ('SpellSlot Bonus', 64),
                       ('Loremaster', 74),
                       ('School Specialization', 79),
                       ('SpellPower', 89),
                       ('SpellAdept', 99),
                       ('Unique', 100)]

SpellsaveBonus = [('+1A +0DC', 5),
                  ('+0A +1DC', 10),
                  ('+0A +0DC', 12),
                  ('+1A +1DC', 14),
                  ('+1A -1DC', 17),
                  ('-1A +1DC', 20)]

SpellSlotBonus = [('+1 1st SpellSlot', 20),
                  ('+1 2nd SpellSlot', 35),
                  ('+1 3rd SpellSlot', 45),
                  ('+1 4th SpellSlot', 50),
                  ('+1 5th SpellSlot', 53),
                  ('+1 6th SpellSlot', 55),
                  ('+1 7th SpellSlot', 56),
                  ('+1 8th SpellSlot', 57),
                  ('+1 9th SpellSlot', 58),
                  ('Regain 1st SpellSlot', 66),
                  ('Regain 2nd SpellSlot', 70),
                  ('Regain 3rd SpellSlot', 72),
                  ('Regain 4th SpellSlot', 73),
                  ('Regain 5th SpellSlot', 74)]

Loremaster = [('Loremaster of High Magic', 1),
              ('Loremaster of Fire', 2),
              ('Loremaster of Beasts', 3),
              ('Loremaster of Metal', 4),
              ('Loremaster of Light', 5),
              ('Loremaster of Life', 6),
              ('Loremaster of Heavens', 7),
              ('Loremaster of Shadows', 8),
              ('Loremaster of Death', 9),
              ('Loremaster of Wilds', 10),
              ('Loremaster of Fel Magic', 11),
              ('Loremaster of Change', 12),
              ('Loremaster of Decay', 13),
              ('Loremaster of Excess', 14),
              ('Loremaster of Maw', 15),
              ('Loremaster of Havoc', 16),
              ('Loremaster of Deceit', 17),
              ('Loremaster of Ruin', 18),
              ('Loremaster of Runes', 19),
              ('Loremaster of Vengeance', 20),
              ('Loremaster of Undeath', 21),
              ('Loremaster of Frost', 22),
              ('Loremaster of Physiomancy', 23),
              ('Loremaster of Psychomancy', 24),
              ('Loremaster of Biomancy', 25),
              ('Loremaster of Infernals', 26),
              ('Loremaster of Earth', 27),
              ('Loremaster of Water', 28),
              ('Loremaster of Air', 29),
              ('Loremaster of Fey', 30),
              ('Loremaster of Judgement', 31)]

SchoolSpecialization = [('Abjuration +1A&DC', 5),
                       ('Conjuration +1A&DC', 10),
                       ('Divination +1A&DC', 15),
                       ('Enchantment +1A&DC', 20),
                       ('Illusion +1A&DC', 25),
                       ('Necromancy +1A&DC', 30),
                       ('Evocation +1A&DC', 35),
                       ('Transmutation +1A&DC', 40),
                       ('Abjuration +2A&DC', 43),
                       ('Conjuration +2A&DC', 46),
                       ('Divination +2A&DC', 49),
                       ('Enchantment +2A&DC', 52),
                       ('Illusion +2A&DC', 55),
                       ('Necromancy +2A&DC', 58),
                       ('Evocation +2A&DC', 61),
                       ('Transmutation +2A&DC', 64),
                       ('Abjuration +1 Upcast', 66),
                       ('Conjuration +1 Upcast', 68),
                       ('Divination +1 Upcast', 70),
                       ('Enchantment +1 Upcast', 72),
                       ('Illusion +1 Upcast', 74),
                       ('Necromancy +1 Upcast', 76),
                       ('Evocation +1 Upcast', 78),
                       ('Transmutation +1 Upcast', 80),
                       ('Abjuration +2 Upcast', 81),
                       ('Conjuration +2 Upcast', 82),
                       ('Divination +2 Upcast', 83),
                       ('Enchantment +2 Upcast', 84),
                       ('Illusion +2 Upcast', 85),
                       ('Necromancy +2 Upcast', 86),
                       ('Evocation +2 Upcast', 87),
                       ('Transmutation +2 Upcast', 88)]

SpellPower = [('+1d6 Physical SpellDmg', 1),
              ('+1d6 Acid SpellDmg', 2),
              ('+1d6 Cold SpellDmg', 3),
              ('+1d6 Fire SpellDmg', 4),
              ('+1d6 Force SpellDmg', 5),
              ('+1d6 Lightning SpellDmg', 6),
              ('+1d6 Necrotic SpellDmg', 7),
              ('+1d6 Poison SpellDmg', 8),
              ('+1d6 Psychic SpellDmg', 9),
              ('+1d6 Radiant SpellDmg', 10),
              ('+1d6 Thunder SpellDmg', 11),
              ('+2d6 Physical SpellDmg', 12),
              ('+2d6 Acid SpellDmg', 13),
              ('+2d6 Cold SpellDmg', 14),
              ('+2d6 Fire SpellDmg', 15),
              ('+2d6 Force SpellDmg', 16),
              ('+2d6 Lightning SpellDmg', 17),
              ('+2d6 Necrotic SpellDmg', 18),
              ('+2d6 Poison SpellDmg', 19),
              ('+2d6 Psychic SpellDmg', 20),
              ('+2d6 Radiant SpellDmg', 21),
              ('+2d6 Thunder SpellDmg', 22),
              ('+3d6 Physical SpellDmg', 23),
              ('+3d6 Acid SpellDmg', 24),
              ('+3d6 Cold SpellDmg', 25),
              ('+3d6 Fire SpellDmg', 26),
              ('+3d6 Force SpellDmg', 27),
              ('+3d6 Lightning SpellDmg', 28),
              ('+3d6 Necrotic SpellDmg', 29),
              ('+3d6 Poison SpellDmg', 30),
              ('+3d6 Psychic SpellDmg', 31),
              ('+3d6 Radiant SpellDmg', 32),
              ('+3d6 Thunder SpellDmg', 33)]

SpellAdept = [('Bypass Acid Resist', 5),
              ('Bypass Cold Resist', 10),
              ('Bypass Fire Resist', 15),
              ('Bypass Force Resist', 20),
              ('Bypass Lightning Resist', 25),
              ('Bypass Necrotic Resist', 30),
              ('Bypass Poison Resist', 35),
              ('Bypass Psychic Resist', 40),
              ('Bypass Radiant Resist', 45),
              ('Bypass Thunder Resist', 50),
              ('Bypass Acid Immune', 53),
              ('Bypass Cold Immune', 56),
              ('Bypass Fire Immune', 59),
              ('Bypass Force Immune', 62),
              ('Bypass Lightning Immune', 65),
              ('Bypass Necrotic Immune', 68),
              ('Bypass Poison Immune', 71),
              ('Bypass Psychic Immune', 74),
              ('Bypass Radiant Immune', 77),
              ('Bypass Thunder Immune', 80)]

#AtkDmgBonus can be (+1 +0, +0 +1, +1 -1, -1 +1, -1 +0, +0 -1, +1 +1, -1 -1) - Weight so Negative Options highly unlikely
#Vicious just reduces crit range or increases multiplier
#Stat Usage (Str-Dex-Con-Int-Wis-Cha) for either Attack or Damage or Both, ALWAYS does both, but may not be same stat for both
#Stat Usage Bonus (Str-Dex-Con-Int-Wis-Cha) ADDS that Stat to Attack or Damage or BOTH, not necessarily both, can lead to double-stacking
#Imbued on hit target takes Damage and/or Effect, no save on it
#Inflict on hit target makes a saving throw, on failure takes Damage and/or Effect
#AttackRate can reduce or increase Attack Rate, if you have Slow with only 1 attack, need both Action and BA to take Attack Action
#TypeBane picks a specific creature/enemy type and rolls again on AtkDmgBonus, Vicious, Imbued, and Inflict
#for TypeBane make a general for normal DnD i.e. Humanoids, Giants, Oozes, and one for HoD; Qlippoth, Khornate, Devils, etc
#ClassAugment well improve the feature for a random class
#Spellcasting gives innate spellcasting to cast a spell 1/day

#print(type(WeaponQualities[0]))
#print(WeaponQualities[0][0], WeaponQualities[0][1])

#ctr = 0
#for i in SpellFocusQualities:
#    ctr += i[1]
#print(ctr)

#print(len(Weapons))

#rng = np.random.default_rng()
#random = rng.integers(low=1, high=len(Weapons))

#rng = np.random.default_rng()
#random = rng.integers(low=1, high=100)
#temp = ''
#for i in WeaponQualities2:
#    temp = i[0]
#    if random > i[1]:
#        continue
#    else:
#        break

def list_replace(OldList, RefList, ListName):
    ctr=0
    Size = RefList[len(RefList)-1][1]
    for i in OldList:
        if i == ListName:
            rng = np.random.default_rng()
            random = rng.integers(low=1, high=Size)
            temp=''
            for j in RefList:
                temp = j[0]
                if random > j[1]:
                    continue
                else:
                    break
            i = temp
        OldList[ctr] = i
        ctr+=1

def create_weapon():
    num_rare = int(input("Enter the numerical rarity between 1-5: "))
    if num_rare not in range(1,6):
        create_weapon()
    else:
        rarity = ItemRarity[num_rare-1]
    rng = np.random.default_rng()
    random = rng.integers(low=1, high=len(Weapons))
    print(rarity, Weapons[random-1])                 
    ctr=0
    temp=''
    temp_list=[]
    num_qual = num_rare*2 - 1
    while ctr < num_qual:
        rng = np.random.default_rng()
        random = rng.integers(low=1, high=100)
        for i in WeaponQualities2:
            temp = i[0]
            if random > i[1]:
                continue
            else:
                break
        temp_list.append(temp)
        ctr+=1
    list_replace(temp_list, AtkDmgBonus, 'AtkDmgBonus')
    list_replace(temp_list, Vicious, 'Vicious')
    list_replace(temp_list, StatUsage, 'StatUsage')
    list_replace(temp_list, StatUsageBonus, 'StatUsageBonus')
    list_replace(temp_list, Imbued, 'Imbued')
    list_replace(temp_list, Inflict, 'Inflict')
    list_replace(temp_list, TypeBane, 'TypeBane')
    list_replace(temp_list, ClassAugment, 'ClassAugment')
    list_replace(temp_list, Spellcasting, 'Spellcasting')
    for i in temp_list:
        print(i)

def create_armor():
    num_rare = int(input("Enter the numerical rarity between 1-5: "))
    if num_rare not in range(1,6):
        create_armor()
    else:
        rarity = ItemRarity[num_rare-1]
    rng = np.random.default_rng()
    random = rng.integers(low=1, high=len(Armors))
    print(rarity, Armors[random-1])                 
    ctr=0
    temp=''
    temp_list=[]
    num_qual = num_rare*2 - 1
    while ctr < num_qual:
        rng = np.random.default_rng()
        random = rng.integers(low=1, high=100)
        for i in ArmorQualities:
            temp = i[0]
            if random > i[1]:
                continue
            else:
                break
        temp_list.append(temp)
        ctr+=1
    list_replace(temp_list, Defensive, 'Defensive')
    list_replace(temp_list, DamageBlock, 'DamageBlock')
    list_replace(temp_list, DamageResist, 'DamageResist')
    list_replace(temp_list, Vitality, 'Vitality')
    list_replace(temp_list, Bulky, 'Bulky')
    list_replace(temp_list, Immunity, 'Immunity')
    list_replace(temp_list, Aegis, 'Aegis')
    list_replace(temp_list, TypeResist, 'TypeResist')
    list_replace(temp_list, Regeneration, 'Regeneration')
    list_replace(temp_list, StatArmorUse, 'StatArmorUse')
    for i in temp_list:
        print(i)

def create_trinket():
    num_rare = int(input("Enter the numerical rarity between 1-5: "))
    if num_rare not in range(1,6):
        create_trinket()
    else:
        rarity = ItemRarity[num_rare-1]
    rng = np.random.default_rng()
    random = rng.integers(low=1, high=len(Trinkets))
    print(rarity, Trinkets[random-1])                 
    ctr=0
    temp=''
    temp_list=[]
    num_qual = num_rare*2 - 1
    while ctr < num_qual:
        rng = np.random.default_rng()
        random = rng.integers(low=1, high=100)
        for i in TrinketQualities:
            temp = i[0]
            if random > i[1]:
                continue
            else:
                break
        temp_list.append(temp)
        ctr+=1
    list_replace(temp_list, Defensive, 'Defensive')
    list_replace(temp_list, Vitality, 'Vitality')
    list_replace(temp_list, Bulky, 'Bulky')
    list_replace(temp_list, Immunity, 'Immunity')
    list_replace(temp_list, Aegis, 'Aegis')
    list_replace(temp_list, Spellcasting, 'Spellcasting')
    list_replace(temp_list, ClassAugment, 'ClassAugment')
    list_replace(temp_list, StatBonus, 'StatBonus')
    list_replace(temp_list, DamageResist, 'DamageResist')
    for i in temp_list:
        print(i)

def create_consumable():
    num_rare = int(input("Enter the numerical rarity between 1-5: "))
    if num_rare not in range(1,6):
        create_consumable()
    else:
        rarity = ItemRarity[num_rare-1]
    rng = np.random.default_rng()
    random = rng.integers(low=1, high=len(Consumables))
    print(rarity, Consumables[random-1])                
    ctr=0
    temp=''
    temp_list=[]
    num_qual = 1
    while ctr < num_qual:
        rng = np.random.default_rng()
        random = rng.integers(low=1, high=100)
        for i in ConsumableQualities:
            temp = i[0]
            if random > i[1]:
                continue
            else:
                break
        temp_list.append(temp)
        ctr+=1
    list_replace(temp_list, Healing, 'Healing')
    list_replace(temp_list, Spellcasting, 'Spellcasting')
    for i in temp_list:
        print(i)

def create_spellfocus():
    num_rare = int(input("Enter the numerical rarity between 1-5: "))
    if num_rare not in range(1,6):
        create_spellfocus()
    else:
        rarity = ItemRarity[num_rare-1]
    rng = np.random.default_rng()
    random = rng.integers(low=1, high=len(SpellFocus))
    print(rarity, SpellFocus[random-1])                 
    ctr=0
    temp=''
    temp_list=[]
    num_qual = num_rare*2 - 1
    while ctr < num_qual:
        rng = np.random.default_rng()
        random = rng.integers(low=1, high=100)
        for i in SpellFocusQualities:
            temp = i[0]
            if random > i[1]:
                continue
            else:
                break
        temp_list.append(temp)
        ctr+=1
    list_replace(temp_list, Spellcasting, 'Spellcasting')
    list_replace(temp_list, SpellsaveBonus, 'Spellsave Bonus')
    list_replace(temp_list, SpellSlotBonus, 'SpellSlot Bonus')
    list_replace(temp_list, Loremaster, 'Loremaster')
    list_replace(temp_list, SchoolSpecialization, 'School Specialization')
    list_replace(temp_list, SpellPower, 'SpellPower')
    list_replace(temp_list, SpellAdept, 'SpellAdept')
    for i in temp_list:
        print(i)

stop = 0
while stop == 0:
    print('\n Select one of the following: \n 1. Create Weapon \n 2. Create Armor \n 3. Create Trinket \n 4. Create Consumable \n 5. Create Spellfocus \n 6. Exit')
    item_type = int(input("Enter the selection between 1-6: "))
    print('\n')
    if item_type == 1:
        create_weapon()
    elif item_type == 2:
        create_armor()
    elif item_type == 3:
        create_trinket()
    elif item_type == 4:
        create_consumable()
    elif item_type == 5:
        create_spellfocus()
    else:
        stop = 1
        continue

