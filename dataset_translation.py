# house_data_translator.py

# MSSubClass translation dictionary
def translate_ms_subclass(value):
    ms_subclass_dict = {
        20: '1-STORY 1946 & NEWER ALL STYLES',
        30: '1-STORY 1945 & OLDER',
        40: '1-STORY W/FINISHED ATTIC ALL AGES',
        45: '1-1/2 STORY - UNFINISHED ALL AGES',
        50: '1-1/2 STORY FINISHED ALL AGES',
        60: '2-STORY 1946 & NEWER',
        70: '2-STORY 1945 & OLDER',
        75: '2-1/2 STORY ALL AGES',
        80: 'SPLIT OR MULTI-LEVEL',
        85: 'SPLIT FOYER',
        90: 'DUPLEX - ALL STYLES AND AGES',
        120: '1-STORY PUD (Planned Unit Development) - 1946 & NEWER',
        150: '1-1/2 STORY PUD - ALL AGES',
        160: '2-STORY PUD - 1946 & NEWER',
        180: 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER',
        190: '2 FAMILY CONVERSION - ALL STYLES AND AGES'
    }
    return ms_subclass_dict.get(value, value)

# MSZoning translation dictionary
def translate_ms_zoning(value):
    ms_zoning_dict = {
        'A': 'Agriculture',
        'C': 'Commercial',
        'FV': 'Floating Village Residential',
        'I': 'Industrial',
        'RH': 'Residential High Density',
        'RL': 'Residential Low Density',
        'RP': 'Residential Low Density Park',
        'RM': 'Residential Medium Density'
    }
    return ms_zoning_dict.get(value, value)

# Street translation dictionary
def translate_street(value):
    street_dict = {
        'Grvl': 'Gravel',
        'Pave': 'Paved'
    }
    return street_dict.get(value, value)

# Alley translation dictionary
def translate_alley(value):
    alley_dict = {
        'Grvl': 'Gravel',
        'Pave': 'Paved',
        'NA': 'No alley access'
    }
    return alley_dict.get(value, value)

# LotShape translation dictionary
def translate_lot_shape(value):
    lot_shape_dict = {
        'Reg': 'Regular',
        'IR1': 'Slightly irregular',
        'IR2': 'Moderately Irregular',
        'IR3': 'Irregular'
    }
    return lot_shape_dict.get(value, value)

# LandContour translation dictionary
def translate_land_contour(value):
    land_contour_dict = {
        'Lvl': 'Near Flat/Level',
        'Bnk': 'Banked - Quick and significant rise from street grade to building',
        'HLS': 'Hillside - Significant slope from side to side',
        'Low': 'Depression'
    }
    return land_contour_dict.get(value, value)

# Utilities translation dictionary
def translate_utilities(value):
    utilities_dict = {
        'AllPub': 'All public Utilities (E,G,W,& S)',
        'NoSewr': 'Electricity, Gas, and Water (Septic Tank)',
        'NoSeWa': 'Electricity and Gas Only',
        'ELO': 'Electricity only'
    }
    return utilities_dict.get(value, value)

# LotConfig translation dictionary
def translate_lot_config(value):
    lot_config_dict = {
        'Inside': 'Inside lot',
        'Corner': 'Corner lot',
        'CulDSac': 'Cul-de-sac',
        'FR2': 'Frontage on 2 sides of property',
        'FR3': 'Frontage on 3 sides of property'
    }
    return lot_config_dict.get(value, value)

# LandSlope translation dictionary
def translate_land_slope(value):
    land_slope_dict = {
        'Gtl': 'Gentle slope',
        'Mod': 'Moderate Slope',
        'Sev': 'Severe Slope'
    }
    return land_slope_dict.get(value, value)

# Neighborhood translation dictionary
def translate_neighborhood(value):
    neighborhood_dict = {
        'Blmngtn': 'Bloomington Heights',
        'Blueste': 'Bluestem',
        'BrDale': 'Briardale',
        'BrkSide': 'Brookside',
        'ClearCr': 'Clear Creek',
        'CollgCr': 'College Creek',
        'Crawfor': 'Crawford',
        'Edwards': 'Edwards',
        'Gilbert': 'Gilbert',
        'IDOTRR': 'Iowa DOT and Rail Road',
        'MeadowV': 'Meadow Village',
        'Mitchel': 'Mitchell',
        'Names': 'North Ames',
        'NoRidge': 'Northridge',
        'NPkVill': 'Northpark Villa',
        'NridgHt': 'Northridge Heights',
        'NWAmes': 'Northwest Ames',
        'OldTown': 'Old Town',
        'SWISU': 'South & West of Iowa State University',
        'Sawyer': 'Sawyer',
        'SawyerW': 'Sawyer West',
        'Somerst': 'Somerset',
        'StoneBr': 'Stone Brook',
        'Timber': 'Timberland',
        'Veenker': 'Veenker'
    }
    return neighborhood_dict.get(value, value)

# Condition1 translation dictionary
def translate_condition1(value):
    condition_dict = {
        'Artery': 'Adjacent to arterial street',
        'Feedr': 'Adjacent to feeder street',
        'Norm': 'Normal',
        'RRNn': 'Within 200\' of North-South Railroad',
        'RRAn': 'Adjacent to North-South Railroad',
        'PosN': 'Near positive off-site feature--park, greenbelt, etc.',
        'PosA': 'Adjacent to positive off-site feature',
        'RRNe': 'Within 200\' of East-West Railroad',
        'RRAe': 'Adjacent to East-West Railroad'
    }
    return condition_dict.get(value, value)

# Condition2 translation dictionary
def translate_condition2(value):
    condition_dict = {
        'Artery': 'Adjacent to arterial street',
        'Feedr': 'Adjacent to feeder street',
        'Norm': 'Normal',
        'RRNn': 'Within 200\' of North-South Railroad',
        'RRAn': 'Adjacent to North-South Railroad',
        'PosN': 'Near positive off-site feature--park, greenbelt, etc.',
        'PosA': 'Adjacent to positive off-site feature',
        'RRNe': 'Within 200\' of East-West Railroad',
        'RRAe': 'Adjacent to East-West Railroad'
    }
    return condition_dict.get(value, value)

# BldgType translation dictionary
def translate_bldg_type(value):
    bldg_type_dict = {
        '1Fam': 'Single-family Detached',
        '2FmCon': 'Two-family Conversion; originally built as one-family dwelling',
        'Duplx': 'Duplex',
        'TwnhsE': 'Townhouse End Unit',
        'TwnhsI': 'Townhouse Inside Unit'
    }
    return bldg_type_dict.get(value, value)

# HouseStyle translation dictionary
def translate_house_style(value):
    house_style_dict = {
        '1Story': 'One story',
        '1.5Fin': 'One and one-half story: 2nd level finished',
        '1.5Unf': 'One and one-half story: 2nd level unfinished',
        '2Story': 'Two story',
        '2.5Fin': 'Two and one-half story: 2nd level finished',
        '2.5Unf': 'Two and one-half story: 2nd level unfinished',
        'SFoyer': 'Split Foyer',
        'SLvl': 'Split Level'
    }
    return house_style_dict.get(value, value)

# RoofStyle translation dictionary
def translate_roof_style(value):
    roof_style_dict = {
        'Flat': 'Flat',
        'Gable': 'Gable',
        'Gambrel': 'Gabrel (Barn)',
        'Hip': 'Hip',
        'Mansard': 'Mansard',
        'Shed': 'Shed'
    }
    return roof_style_dict.get(value, value)

# RoofMatl translation dictionary
def translate_roof_matl(value):
    roof_matl_dict = {
        'ClyTile': 'Clay or Tile',
        'CompShg': 'Standard (Composite) Shingle',
        'Membran': 'Membrane',
        'Metal': 'Metal',
        'Roll': 'Roll',
        'Tar&Grv': 'Gravel & Tar',
        'WdShake': 'Wood Shakes',
        'WdShngl': 'Wood Shingles'
    }
    return roof_matl_dict.get(value, value)

# Exterior1st and Exterior2nd translation dictionaries
def translate_exterior(value):
    exterior_dict = {
        'AsbShng': 'Asbestos Shingles',
        'AsphShn': 'Asphalt Shingles',
        'BrkComm': 'Brick Common',
        'BrkFace': 'Brick Face',
        'CBlock': 'Cinder Block',
        'CemntBd': 'Cement Board',
        'HdBoard': 'Hard Board',
        'ImStucc': 'Imitation Stucco',
        'MetalSd': 'Metal Siding',
        'Other': 'Other',
        'Plywood': 'Plywood',
        'PreCast': 'PreCast',
        'Stone': 'Stone',
        'Stucco': 'Stucco',
        'VinylSd': 'Vinyl Siding',
        'Wd Sdng': 'Wood Siding',
        'WdShing': 'Wood Shingles'
    }
    return exterior_dict.get(value, value)

# MasVnrType translation dictionary
def translate_mas_vnr_type(value):
    mas_vnr_type_dict = {
        'BrkCmn': 'Brick Common',
        'BrkFace': 'Brick Face',
        'CBlock': 'Cinder Block',
        'None': 'None',
        'Stone': 'Stone'
    }
    return mas_vnr_type_dict.get(value, value)

# ExterQual and ExterCond translation dictionaries
def translate_exter_qual(value):
    exter_qual_dict = {
        'Ex': 'Excellent',
        'Gd': 'Good',
        'TA': 'Average/Typical',
        'Fa': 'Fair',
        'Po': 'Poor'
    }
    return exter_qual_dict.get(value, value)

def translate_exter_cond(value):
    exter_cond_dict = {
        'Ex': 'Excellent',
        'Gd': 'Good',
        'TA': 'Average/Typical',
        'Fa': 'Fair',
        'Po': 'Poor'
    }
    return exter_cond_dict.get(value, value)

# Foundation translation dictionary
def translate_foundation(value):
    foundation_dict = {
        'BrkTil': 'Brick & Tile',
        'CBlock': 'Cinder Block',
        'PConc': 'Poured Concrete',
        'Slab': 'Slab',
        'Stone': 'Stone',
        'Wood': 'Wood'
    }
    return foundation_dict.get(value, value)

# BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, and BsmtFinType2 translation dictionaries
def translate_bsmt_qual(value):
    bsmt_qual_dict = {
        'Ex': 'Excellent (100+ inches)',
        'Gd': 'Good (90-99 inches)',
        'TA': 'Typical (80-89 inches)',
        'Fa': 'Fair (70-79 inches)',
        'Po': 'Poor (<70 inches',
        'NA': 'No Basement'
    }
    return bsmt_qual_dict.get(value, value)

def translate_bsmt_cond(value):
    bsmt_cond_dict = {
        'Ex': 'Excellent',
        'Gd': 'Good',
        'TA': 'Typical - slight dampness allowed',
        'Fa': 'Fair - dampness or some cracking or settling',
        'Po': 'Poor - severe cracking, settling, or wetness',
        'NA': 'No Basement'
    }
    return bsmt_cond_dict.get(value, value)

def translate_bsmt_exposure(value):
    bsmt_exposure_dict = {
        'Gd': 'Good Exposure',
        'Av': 'Average Exposure (split levels or foyers typically score average or above)',
        'Mn': 'Minimum Exposure',
        'No': 'No Exposure',
        'NA': 'No Basement'
    }
    return bsmt_exposure_dict.get(value, value)

def translate_bsmt_fin_type1(value):
    bsmt_fin_type_dict = {
        'GLQ': 'Good Living Quarters',
        'ALQ': 'Average Living Quarters',
        'BLQ': 'Below Average Living Quarters',
        'Rec': 'Average Rec Room',
        'LwQ': 'Low Quality',
        'Unf': 'Unfinished',
        'NA': 'No Basement'
    }
    return bsmt_fin_type_dict.get(value, value)

def translate_bsmt_fin_type2(value):
    bsmt_fin_type_dict = {
        'GLQ': 'Good Living Quarters',
        'ALQ': 'Average Living Quarters',
        'BLQ': 'Below Average Living Quarters',
        'Rec': 'Average Rec Room',
        'LwQ': 'Low Quality',
        'Unf': 'Unfinished',
        'NA': 'No Basement'
    }
    return bsmt_fin_type_dict.get(value, value)

# Heating translation dictionary
def translate_heating(value):
    heating_dict = {
        'Floor': 'Floor Furnace',
        'GasA': 'Gas forced warm air furnace',
        'GasW': 'Gas hot water or steam heat',
        'Grav': 'Gravity furnace',
        'OthW': 'Hot water or steam heat other than gas',
        'Wall': 'Wall furnace'
    }
    return heating_dict.get(value, value)

# HeatingQC translation dictionary
def translate_heating_qc(value):
    heating_qc_dict = {
        'Ex': 'Excellent',
        'Gd': 'Good',
        'TA': 'Average/Typical',
        'Fa': 'Fair',
        'Po': 'Poor'
    }
    return heating_qc_dict.get(value, value)

# CentralAir translation dictionary
def translate_central_air(value):
    central_air_dict = {
        'N': 'No',
        'Y': 'Yes'
    }
    return central_air_dict.get(value, value)

# Electrical translation dictionary
def translate_electrical(value):
    electrical_dict = {
        'SBrkr': 'Standard Circuit Breakers & Romex',
        'FuseA': 'Fuse Box over 60 AMP and all Romex wiring (Average)',
        'FuseF': '60 AMP Fuse Box and mostly Romex wiring (Fair)',
        'FuseP': '60 AMP Fuse Box and mostly knob & tube wiring (poor)',
        'Mix': 'Mixed'
    }
    return electrical_dict.get(value, value)

# GarageType translation dictionary
def translate_garage_type(value):
    garage_type_dict = {
        '2Types': 'More than one type of garage',
        'Attchd': 'Attached to home',
        'Basment': 'Basement Garage',
        'BuiltIn': 'Built-In (Garage part of house - typically has room above garage)',
        'CarPort': 'Car Port',
        'Detchd': 'Detached from home',
        'NA': 'No Garage'
    }
    return garage_type_dict.get(value, value)

# GarageFinish translation dictionary
def translate_garage_finish(value):
    garage_finish_dict = {
        'Fin': 'Finished',
        'RFn': 'Rough Finished',
        'Unf': 'Unfinished',
        'NA': 'No Garage'
    }
    return garage_finish_dict.get(value, value)

# GarageQual and GarageCond translation dictionaries
def translate_garage_qual(value):
    garage_qual_dict = {
        'Ex': 'Excellent',
        'Gd': 'Good',
        'TA': 'Typical/Average',
        'Fa': 'Fair',
        'Po': 'Poor',
        'NA': 'No Garage'
    }
    return garage_qual_dict.get(value, value)

def translate_garage_cond(value):
    garage_cond_dict = {
        'Ex': 'Excellent',
        'Gd': 'Good',
        'TA': 'Typical/Average',
        'Fa': 'Fair',
        'Po': 'Poor',
        'NA': 'No Garage'
    }
    return garage_cond_dict.get(value, value)

# PavedDrive translation dictionary
def translate_paved_drive(value):
    paved_drive_dict = {
        'Y': 'Paved',
        'P': 'Partial Pavement',
        'N': 'Dirt/Gravel'
    }
    return paved_drive_dict.get(value, value)

# Fence translation dictionary
def translate_fence(value):
    fence_dict = {
        'GdPrv': 'Good Privacy',
        'MnPrv': 'Minimum Privacy',
        'GdWo': 'Good Wood',
        'MnWw': 'Minimum Wood/Wire',
        'NA': 'No Fence'
    }
    return fence_dict.get(value, value)

# MiscFeature translation dictionary
def translate_misc_feature(value):
    misc_feature_dict = {
        'Elev': 'Elevator',
        'Gar2': '2nd Garage (if not described in garage section)',
        'Othr': 'Other',
        'Shed': 'Shed (over 100 SF)',
        'TenC': 'Tennis Court',
        'NA': 'None'
    }
    return misc_feature_dict.get(value, value)

# SaleType translation dictionary
def translate_sale_type(value):
    sale_type_dict = {
        'WD': 'Warranty Deed - Conventional',
        'CWD': 'Warranty Deed - Cash',
        'VWD': 'Warranty Deed - VA Loan',
        'New': 'Home just constructed and sold',
        'COD': 'Court Officer Deed/Estate',
        'Con': 'Contract 15% Down payment regular terms',
        'ConLw': 'Contract Low Down payment and low interest',
        'ConLI': 'Contract Low Interest',
        'ConLD': 'Contract Low Down',
        'Oth': 'Other'
    }
    return sale_type_dict.get(value, value)

# SaleCondition translation dictionary
def translate_sale_condition(value):
    sale_condition_dict = {
        'Normal': 'Normal Sale',
        'Abnorml': 'Abnormal Sale -  trade, foreclosure, short sale',
        'AdjLand': 'Adjoining Land Purchase',
        'Alloca': 'Allocation - two linked properties with separate deeds, typically condo with a garage unit',
        'Family': 'Sale between family members',
        'Partial': 'Home was not completed when last assessed (associated with New Homes)'
    }
    return sale_condition_dict.get(value, value)
