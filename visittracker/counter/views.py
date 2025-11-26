from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta

def visit_counter(request):

    # ---------------- COOKIE COUNTER ----------------
    visit_count_cookie = request.COOKIES.get("visit_count_cookie")
    if visit_count_cookie:
        visit_count_cookie = int(visit_count_cookie) + 1
    else:
        visit_count_cookie = 1

    # ---------------- LAST VISIT COOKIE ----------------
    last_visit_cookie = request.COOKIES.get("last_visit_cookie")
    if not last_visit_cookie:
        last_visit_cookie = "First Visit"
    else:
        last_visit_cookie = last_visit_cookie

    # ---------------- SESSION COUNTER ----------------
    visit_count_session = request.session.get("visit_count_session", 0)
    visit_count_session += 1
    request.session["visit_count_session"] = visit_count_session

    # ---------------- LAST VISIT SESSION ----------------
    last_visit_sess = request.session.get("last_visit_session", "First Visit")
    request.session["last_visit_session"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = render(request, "counter.html", {
        "cookie_count": visit_count_cookie,
        "session_count": visit_count_session,
        "cookie_last": last_visit_cookie,
        "session_last": last_visit_sess
    })

    # Set cookie expiry to 2 minutes
    expiry_time = datetime.now() + timedelta(minutes=2)

    response.set_cookie("visit_count_cookie", str(visit_count_cookie), expires=expiry_time)
    response.set_cookie("last_visit_cookie", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), expires=expiry_time)

    return response


def reset_counter(request):
    response = redirect("visit_counter")

    # Delete cookies
    response.delete_cookie("visit_count_cookie")
    response.delete_cookie("last_visit_cookie")

    # Clear session values
    request.session.flush()

    return response
