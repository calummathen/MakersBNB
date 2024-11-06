from flask import session, redirect, url_for

def protect_route():
    if not session.get('id'):
        return redirect(url_for('get_root'))
    return None