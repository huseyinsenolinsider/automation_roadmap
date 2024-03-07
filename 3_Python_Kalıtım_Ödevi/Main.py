from WebPush import WebPush
from TriggerPush import TriggerPush
from BulkPush import BulkPush
from SegmentPush import SegmentPush
from PriceAlertPush import PriceAlertPush
from InStockPush import InStockPush

web = WebPush("web", True, 123, 123, 123, "tr", "web")
trigger = TriggerPush("web", True, 123, 123, 123, "tr", "trigger", "cart")
bulk = BulkPush("web", True, 123, 123, 123, "tr", "bulk", 123123)
segment = SegmentPush("web", False, 123, 123, 123, "tr", "bulk", "segmentt")
price_alert = PriceAlertPush("web", True, 123, 123, 123, "tr", "price_alert", 50, 10.0)
in_stock = InStockPush("web", True, 123, 123, 123, "tr", "in_stock", False)

trigger.send_push()
bulk.send_push()

print(price_alert.price_info, price_alert.discount_rate, price_alert.discountPrice())


print(in_stock.stock_info)
in_stock.stockUpdate()
print(in_stock.stock_info)
in_stock.stockUpdate()
print(in_stock.stock_info)
