

def get_card_details():
    """ user enters name, card_no, expiration date & cvc_no"""
    print('Please Enter your credit card details:')
    name = 'JOE BRIGGS'
    card_no = '2555288811112222'
    expiration = '08/27'
    cvc = '488'
    return dict(name=name, card_no=card_no, expiration=expiration, cvc=cvc)

