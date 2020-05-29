from forex_python.converter import CurrencyRates

c = CurrencyRates()

def convert_forex(conv_from, conv_to, amt):
    """Uses the inputs from the form as parameters, converts from/to desired currencies"""
    
    converted_amount = c.convert(conv_from, conv_to, amt)
    return converted_amount
    
    
        