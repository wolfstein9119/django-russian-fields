from .base import BaseMeta


class INNMeta(BaseMeta):
    PERSON_MODE = 'person'
    LEGAL_MODE = 'legal'
    GENERAL_MODE = 'general'

    PERSON_INN_LENGTH = 12
    LEGAL_INN_LENGTH = 10

    available_length = (PERSON_INN_LENGTH, LEGAL_INN_LENGTH)
    available_mode = (PERSON_MODE, LEGAL_MODE, GENERAL_MODE)

    settings = {
        PERSON_MODE: {
            'max_length': PERSON_INN_LENGTH,
            'min_length': PERSON_INN_LENGTH,
            'record_number_range': {
                'start_index': 4,
                'end_index': 10
            },
            'control_number_range': {
                'start_index': 10,
                'end_index': 12
            }
        },
        LEGAL_MODE: {
            'max_length': LEGAL_INN_LENGTH,
            'min_length': LEGAL_INN_LENGTH,
            'record_number_range': {
                'start_index': 4,
                'end_index': 9
            },
            'control_number_range': {
                'start_index': 9,
                'end_index': 10
            }
        },
        GENERAL_MODE: {
            'max_length': PERSON_INN_LENGTH,
            'min_length': LEGAL_INN_LENGTH,
        }
    }
