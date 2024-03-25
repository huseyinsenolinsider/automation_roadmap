from WebPush import WebPush


class TriggerPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page

        if not isinstance(trigger_page, str):
            raise ValueError("trigger_page sadece string değer alabilir")
