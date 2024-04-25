from enum import Enum

class RoleEnum(Enum):
    CANDIDATE = 'Candidate'
    COACH = 'Coach'
    ADMIN = 'Admin'

class CandidateInquiryEnum(Enum):
    LOCATION = "Where are you"
    PATIENT_INFO = "Who the patient is"
    OTHER_PATIENT_INFO = "Other information about the patient"
    ACTION_REQUIRED = "What you must do"

class PatientDisclosureEnum(Enum):
    FREELY_DIVULGED = "Freely divulged to doctor"
    DIVULGED_IF_ASKED = "Divulged to doctor if asked"
    IDEAS_CONCERNS_EXPECTATIONS = "Ideas concerns and expectations"