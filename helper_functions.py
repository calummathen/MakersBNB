from flask import session, redirect, url_for

def protect_route():
    if not session.get('id'):
        return redirect(url_for('get_login_page'))
    return None

def calculate_total_price(price_per_night, check_in, check_out):
    delta = check_out - check_in
    days_between = delta.days
    return price_per_night * days_between


def location_filter(spaces, location):
    filtered_spaces = []
    location = location.lower()
    print(location)

    for space in spaces:
        print(space.address)
        address = space.address
        address_lines = address.split()
        for line in address_lines:
            if location in line.lower():
                filtered_spaces.append(space)
    return filtered_spaces