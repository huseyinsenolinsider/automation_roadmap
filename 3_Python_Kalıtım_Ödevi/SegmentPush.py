from WebPush import WebPush

class SegmentPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

        if not isinstance(segment_name, str):
            raise ValueError("segment_name sadece string değer alabilir")