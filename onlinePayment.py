from flask import Flask, redirect, request

import stripe
#dev api gotta learn to change it
stripe.api_key = 'sk_test_51PuVHZJPpXkyeWaBITMqQtb6z84fOaZvSQE50AEivL23rfCuXa2HBet2i2f6zK4mv4yKIKfimG0MFR5YF3J2JlrA00AJ3n1yPp'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

#change to a payment url when the front end is started
YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # gotta intergrate the the database when its made
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)