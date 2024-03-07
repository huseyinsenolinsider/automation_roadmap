from WebPush import WebPush

class PriceAlertPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, price_info, discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

        if not isinstance(price_info, int):
            raise ValueError("price_info sadece integer değer alabilir")
        if not isinstance(discount_rate, float):
            raise ValueError("discount_rate sadece float değer alabilir")


    def discountPrice(self):
        return self.price_info - (self.price_info * (self.discount_rate/100))