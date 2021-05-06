import json

from django.http import JsonResponse
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
    matches = sorted(match_pcts.items(),
                     key=lambda x: match_pcts[x[0]], reverse=True)
    return render(request, 'matches.html', {'matches': matches})


@login_required
def marker(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'lat' in data and 'lng' in data and 'radius' in data:
            profile = Profile.objects.get(user=request.user)
            if data['lat'] and data['lng']:
                profile.search_lat = float(data['lat'])
                profile.search_lng = float(data['lng'])
            if data['radius']:
                profile.search_radius = float(data['radius'])
            profile.save()
            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'errors': ['Missing one or more required fields']})
    else:
        data = {}
        data['lat'] = request.user.profile.search_lat
        data['lng'] = request.user.profile.search_lng
        data['radius'] = request.user.profile.search_radius

        return JsonResponse(data)


@login_required
def map(request):
    location_set = bool(request.user.profile.search_lat) and bool(request.user.profile.search_lng)
    return render(request, 'map.html', {'location_set': location_set})
