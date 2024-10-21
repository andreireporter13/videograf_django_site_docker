# # Exemplu de price_data:
# price_data = {
#     "now": {
#         "amount": 2.99,
#         "__typename": "Money"
#     },
#     "was": None,  # sau poate conține date
#     "unitInfo": {
#         "price": {
#             "amount": 2.99,
#             "__typename": "Money"
#         },
#         "description": "KG",
#         "__typename": "ProductUnitInfo"
#     },
#     "discount": {
#         "segmentId": 676268,
#         "description": "stapelen tot 40%",
#         "promotionType": "NATIONAL",
#         "segmentType": "AH",
#         "subtitle": None,
#         "theme": "TIERED_OFFER",
#         "tieredOffer": [
#             "1 stuk 25% korting",
#             "2 stuks 40% korting"
#         ],
#         "wasPriceVisible": True,
#         "smartLabel": None,
#         "__typename": "ProductPriceDiscountV2"
#     },
#     "__typename": "ProductPriceV2"
# }

# # Inițializare listă pentru a stoca dicționarele de prețuri
# price_info_list = []

# # Extragem prețul curent (now)
# try:
#     price_now = price_data.get('now', {}).get('amount', None)
# except AttributeError as e:
#     print(f"Error extracting price_now: {e}")

# # Adăugăm primul dicționar pentru price_now
# price_info_list.append({
#     "price_now": price_now,
#     "price_was": None,  # În acest pas, nu folosim price_was
#     "price_type": "standard"
# })

# # Verificăm dacă există discount și tieredOffer
# try:
#     discount_data = price_data.get('discount', {})
#     discount_description = discount_data.get('description', None)
#     tiered_offer = discount_data.get('tieredOffer', [])
# except AttributeError as e:
#     print(f"Error extracting discount data: {e}")

# # Dacă există discount și tieredOffer, adăugăm aceste informații
# if discount_description and tiered_offer:
#     for offer in tiered_offer:
#         # Creăm un nou dicționar pentru fiecare nivel de ofertă din tieredOffer
#         discount_info = {
#             "price_now": price_now,  # Prețul curent rămâne același
#             "price_was": None,  # Dacă e nevoie să incluzi price_was, poți adăuga în logica ta
#             "price_type": offer  # Adăugăm fiecare ofertă (din tieredOffer) ca un nou price_type
#         }
#         price_info_list.append(discount_info)

# # Afișăm lista de dicționare pentru testare
# for price_info in price_info_list:
#     print(price_info)

import request

accountId = ''
locationId = ''

response = f'https://mybusiness.googleapis.com/v4/accounts/{accountId}/locations/{locationId}'