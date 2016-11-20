from .base import BaseMeta


class OGRNMeta(BaseMeta):
    LEGAL_MODE = 'legal'
    BUSINESS_MODE = 'business'
    GENERAL_MODE = 'general'

    LEGAL_OGRN_LENGTH = 13
    BUSINESS_ORGN_LENGTH = 15

    available_length = (LEGAL_OGRN_LENGTH, BUSINESS_ORGN_LENGTH)
    available_mode = (LEGAL_MODE, BUSINESS_MODE, GENERAL_MODE)

    settings = {
        LEGAL_MODE: {
            'max_length': LEGAL_OGRN_LENGTH,
            'min_length': LEGAL_OGRN_LENGTH,
            'record_number_range': {
                'start_index': 7,
                'end_index': 12
            },
            'control_number_range': {
                'start_index': 12,
                'end_index': 13
            },
            'without_control_range': {
                'start_index': 0,
                'end_index': 12
            }
        },
        BUSINESS_MODE: {
            'max_length': BUSINESS_ORGN_LENGTH,
            'min_length': BUSINESS_ORGN_LENGTH,
            'record_number_range': {
                'start_index': 7,
                'end_index': 14
            },
            'control_number_range': {
                'start_index': 14,
                'end_index': 15
            },
            'without_control_range': {
                'start_index': 0,
                'end_index': 14
            }
        },
        GENERAL_MODE: {
            'max_length': BUSINESS_ORGN_LENGTH,
            'min_length': LEGAL_OGRN_LENGTH,
        }
    }
