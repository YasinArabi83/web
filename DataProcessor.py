class DataProcessor:
    def __init__(self, pages: list):
        self.pages = pages

    def data_processor(self):
        car_ads = []
        try_pars = lambda is_number: int(is_number) if is_number.isdecimal() else 0
        format_modifier = lambda mileage: mileage.replace(',', '').replace(' km', '')
        for page in self.pages:
            for ad in page:
                if ad["type"] == "ad":
                    car_ad = {
                        "title": ad["detail"]["title"],
                        "year": int(ad["detail"]["year"]),
                        "mileage": try_pars(format_modifier(ad["detail"]["mileage"])),
                        "location": ad["detail"]["location"],
                        "body_color": ad["detail"]["body_color"],
                        "price": try_pars(format_modifier(ad["price"]["price"])),
                    }
                    car_ads.append(car_ad)

        return car_ads
