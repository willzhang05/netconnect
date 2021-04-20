from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.models import *
from users.matching import matching


def login(request):
    return render(request, 'login.html')


@login_required
def matches(request):
    matches = request.user.profile.matches.all()
    match_pcts = {match: matching(request.user.profile, match)
                  for match in matches}
    return render(request, 'matches.html', {'matches': match_pcts})


@login_required
def map(request):
    return render(request, 'map.html')
