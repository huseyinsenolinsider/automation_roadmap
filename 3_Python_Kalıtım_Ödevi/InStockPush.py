from WebPush import WebPush


class InStockPush(WebPush):

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

        if not isinstance(stock_info, bool):
            raise ValueError("stock_info sadece boolean değer alabilir")

    def stockUpdate(self):
        if self.stock_info:
            self.stock_info = False
            return self.stock_info
        else:
            self.stock_info = True
            return self.stock_info
