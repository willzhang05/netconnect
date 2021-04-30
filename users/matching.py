import geopy.distance

FACTOR_WEIGHTS = {
    'class_rank': 10,
    'major': 5,
    'roommates': 10,
    'semesters': 10,
    'politics': 5,
    'social_factor': 20,
    'tidiness_factor': 15,
    'party_factor': 10,
    'guest_factor': 5,
    'location': 10,
}

def search_location_overlap(a, b):
    if a.search_lat == b.search_lat and a.search_lng == b.search_lng:
        return True
    
    distance = geopy.distance.distance((a.search_lat, a.search_lng), (b.search_lat, b.search_lng)).miles
    result_diff = (a.search_radius - b.search_radius)**2 
    result_sum = (a.search_radius + b.search_radius)**2
    return result_diff < distance < result_sum


def matching(a, b):  # should take two profile objects, will return percentage match between two users

    total_points = 0
    max_points = sum(FACTOR_WEIGHTS.values())

    # class rank
    if a.class_rank == b.class_rank:
        total_points += FACTOR_WEIGHTS['class_rank']

    # politics
    if a.politics == b.politics:
        total_points += FACTOR_WEIGHTS['politics']

    # major
    if a.major.upper() == b.major.upper():
        total_points += FACTOR_WEIGHTS['major']

    # roommates
    if a.roommates == b.roommates:
        roommate_factor = 1.0
    elif abs(a.roommates - b.roommates) <= 2:
        roommate_factor = 0.5
    else:
        roommate_factor = 0.0
    total_points += FACTOR_WEIGHTS['roommates'] * roommate_factor

    # semesters
    if a.semesters == b.semesters:
        semesters_factor = 1.0
    elif abs(a.semesters - b.semesters) <= 2:
        semesters_factor = 0.5
    else:
        semesters_factor = 0.0
    total_points += FACTOR_WEIGHTS['semesters'] * semesters_factor

    # social
    total_points += FACTOR_WEIGHTS['social_factor'] * \
        ((4.0 - abs(a.social_factor - b.social_factor)) / 4.0)
    # tidiness
    total_points += FACTOR_WEIGHTS['tidiness_factor'] * \
        ((4.0 - abs(a.tidiness_factor - b.tidiness_factor)) / 4.0)
    # party
    total_points += FACTOR_WEIGHTS['party_factor'] * \
        ((4.0 - abs(a.party_factor - b.party_factor)) / 4.0)
    # guest
    total_points += FACTOR_WEIGHTS['guest_factor'] * \
        ((4.0 - abs(a.guest_factor - b.guest_factor)) / 4.0)

    # location
    if a.search_lat and a.search_lng and a.search_radius and b.search_lat and b.search_lng and b.search_radius:
        total_points += FACTOR_WEIGHTS['location'] * search_location_overlap(a, b)
    

    return (total_points / max_points) * 100
