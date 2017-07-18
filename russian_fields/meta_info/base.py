class BaseMeta(object):
    settings = {}

    @classmethod
    def get_range(cls, mode, range_name):
        assert mode in cls.settings
        mode_settings = cls.settings[mode]

        assert range_name in mode_settings
        range_info = mode_settings[range_name]
        return range_info['start_index'], range_info['end_index']

    @classmethod
    def get_length(cls, mode):
        assert mode in cls.settings
        mode_settings = cls.settings[mode]
        return mode_settings['min_length'], mode_settings['max_length']