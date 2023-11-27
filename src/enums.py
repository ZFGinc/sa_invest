import enum

class role_code_type(enum.Enum):
  ADMIN = 0
  PROJECT_EDITOR = 1
  PROJECT_VIEWER = 2
  REPORT_EXPORTER_ALL = 2 
    
class project_state_type(enum.Enum):
  APPLICANTION_SHORT = 0
  APPLICANTION_FULL = 1
  DELETED = 2
  ENDED = 3
  FREEZE = 4
  ARCHIVE = 5
  PROJECT_IN_COMISSION = 6
  PROJECT_ON_SUPPORT = 7

class support_type (enum.Enum):
  FINANCE = 0
  CREDIT = 1
  EARTH = 2
  EQUIP = 3
  TECH = 4

class unit_type (enum.Enum):
  RUB = 0
  PIECES = 1
  METERS = 2
  METERS_CUBIC = 3
  METERS_SQUARE = 4
  HECTARES = 5

class programm_level_type (enum.Enum):
  FEDERAL = 0
  REGION = 1
  MUNICIPAL = 2

class decision_type (enum.Enum):
  EG = 0
  MVK = 1