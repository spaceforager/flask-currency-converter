from flask import Flask, request, redirect, render_template, flash
from forex_calc import convert_forex
from forex_python.converter import RatesNotAvailableError



app = Flask(__name__)
app.config['SECRET_KEY'] = '123abc'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def show_form():
    """Show the form and accepts form entries"""
    return render_template('forex-form.html')


@app.route('/show-conv')
def show_conv_amount():
    """Show the converted amount"""
    conv_from = request.args.get('conv-from')
    conv_to = request.args.get('conv-to')
    amount = float(request.args.get('amt'))

    try:
        converted_amt = convert_forex(conv_from, conv_to, amount)
    except ValueError:
        flash("Invalid amount")
        
    except RatesNotAvailableError:
        flash("The currency alphabetic code is invalid")
    
    
    
    return render_template('conv-page.html', conv_from=conv_from, conv_to=conv_to, amount=amount, converted_amt=converted_amt)


