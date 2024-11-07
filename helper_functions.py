from flask import session, redirect, url_for

def protect_route():
    if not session.get('id'):
        return redirect(url_for('get_root'))
    return None

def calculate_total_price(price_per_night, check_in, check_out):
    delta = check_out - check_in
    days_between = delta.days
    return price_per_night * days_between