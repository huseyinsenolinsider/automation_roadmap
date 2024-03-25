class WebPush:
    optin = False

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

        if not isinstance(optin, bool):
            raise ValueError("optin sadece boolean değer alabilir")

    def sendPush(self):
        print(self.push_type, "Push Gönderildi!")
