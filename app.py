from flask import Flask, request, redirect, render_template, flash
from forex_calc import convert_forex
from forex_python.converter import RatesNotAvailableError, CurrencyCodes, CurrencyRates


app = Flask(__name__)
app.config['SECRET_KEY'] = '123abc'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

c = CurrencyCodes()


@app.route('/')
def show_form():
    """Render the form with currency converter and amount fields"""
    return render_template('forex-form.html')


@app.route('/show-conv')
def show_conv_amount():
    """
    Capture values from the form and throw flash error messages 
    for invalid form values
    
    """

    errors = False
    conv_from = request.args.get('conv-from').upper()
    conv_to = request.args.get('conv-to').upper()
    
    conv_from_symbol = c.get_symbol(conv_from)
    conv_to_symbol = c.get_symbol(conv_to)

    if conv_from == conv_to:
        flash("The currency abbreviations must be different from one another", 'error_same')
        errors = True
        
    try:
        amount = float(request.args.get('amt'))
    except ValueError:
        flash('Amount should be a number', 'error_amt')
        errors = True
    else:
        if amount <= 0:
            flash("Amount should be greater than 0", 'error_amt')
            errors = True
    
    if conv_from_symbol == None:
        flash("Invalid currency alphabetic code to convert from", 'error_conv_from')
        errors = True
    elif conv_to_symbol == None:
        flash("Invalid currency alphabetic code to convert to", 'error_conv_to')
        errors = True
    else:
        converted_amt = convert_forex(conv_from, conv_to, amount)
        
    if errors:
        return redirect('/')
    else:
        return render_template('conv-page.html', conv_from_symbol=conv_from_symbol, conv_to_symbol=conv_to_symbol, amount=amount, converted_amt=round(converted_amt, 2))
    








