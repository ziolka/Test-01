DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    
    if customer.get("discount") is not None:
        discount = customer.get("discount")
        return price * (1 - discount)
    else:
        return price * (1 - DEFAULT_DISCOUNT)
    
    
        
    
        
    