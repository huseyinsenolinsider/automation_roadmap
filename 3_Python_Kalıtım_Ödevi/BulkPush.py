from WebPush import WebPush


class BulkPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date

        if not isinstance(send_date, int):
            raise ValueError("send_date sadece integer değer alabilir")
