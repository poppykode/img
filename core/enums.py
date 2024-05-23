from enum import Enum

class RoleEnum(Enum):
    CANDIDATE = 'Candidate'
    COACH = 'Coach'
    ADMIN = 'Admin'

class CandidateInquiryEnum(Enum):
    WHERE_ARE_YOU = "Where are you"
    WHO_THE_PATIENT_IS = "Who the patient is"
    OTHER_INFORMATION_ABOUT_THE_PATIENT = "Other information about the patient"
    WHAT_YOU_MUST_DO = "What you must do"

class PatientDisclosureEnum(Enum):
    FREELY_DIVULGED_TO_DOCTOR = "Freely divulged to doctor"
    DIVULGED_TO_DOCTOR_IF_ASKED = "Divulged to doctor if asked"
    IDEAS_CONCERNS_AND_EXPECTATIONS = "Ideas concerns and expectations"

class ExaminerMarkSheetEnum(Enum):
    DATA_GATHERING = "Data Gathering"
    MANAGEMENT = "Management"
    INTERPERSONAL_SKILLS = "Interpersonal skills"

class CurrencyEnum(Enum):
    USD = 'usd'
    GBP = 'gbp'