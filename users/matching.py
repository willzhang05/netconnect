def matching(a, b):  # should take two profile objects, will return percentage match between two users

    total_points = 0
    max_points = 1338

    # gender
    total_points += (400 if a.gender == b.gender else 0)
    # class rank
    total_points += (40 if a.class_rank == b.class_rank else 0)
    # politics
    total_points += (70 if a.politics == b.politics else 0)
    # major
    total_points += (20 if a.major == b.major else 0)
    # roommates
    total_points += (400 if a.roommates == b.roommates else 0)
    # semesters
    total_points += (300 if a.semesters == b.semesters else 0)

    aTime = a.bedtime
    bTime = b.bedtime
    aSeconds = (aTime.hour * 60 + aTime.minute) * 60 + aTime.second
    bSeconds = (bTime.hour * 60 + bTime.minute) * 60 + bTime.second
    # bedtime - note, this isn't very robust but essentially calculates hour difference in bedtimes to an extent that we need
    total_points += 20 - abs((aSeconds - bSeconds)) / 60 / 60
    # tidiness
    total_points += 5 * (4 - abs(a.tidiness_factor -
                                 b.tidiness_factor))
    # party
    total_points += 10 * (4 - abs(a.party_factor - b.party_factor))

    # guest
    total_points += 7 * (4 - abs(a.guest_factor - b.guest_factor))

    return (total_points / max_points) * 100
