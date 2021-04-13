from models import Profile
from .models import Profile
import operator

def matching(a, b): # should take two profile objects, will return percentage match between two users
    
    total_points = 0
    max_points = 1338
    
    total_points = total_points + (400 if a.gender == b.gender else 0)                  # gender
    total_points = total_points + (40 if a.class_rank == b.class_rank else 0)           # class rank
    total_points = total_points + (70 if a.politics == b.politics else 0)               # politics
    total_points = total_points + (20 if a.major == b.major else 0)                     # major
    total_points = total_points + (400 if a.roommates == b.roommates else 0)            # roommates
    total_points = total_points + (300 if a.semesters == b.semesters else 0)            # semesters
    total_points = total_points + 20 - abs(a.bedtime - b.bedtime)/60/60                 # bedtime - note, this isn't very robust but essentially calculates hour difference in bedtimes to an extent that we need
    total_points = total_points + 5*(4 - abs(a.tidiness_factor - b.tidiness_factor))    # tidiness
    total_points = total_points + 10*(4 - abs(a.party_factor - b.party_factor))         # party
    total_points = total_points + 7*(4 - abs(a.guest_factor - b.guest_factor))          # guest

    return (total_points/max_points)*100

def matchingsearch(a): # takes one profile and checks it with every other profile in the database, creates a dictionary listing for that profile and returns it
    all_profiles = Profile.objects.all()
    dict = {}
    for x in all_profiles:
        dict[x] = matching(a, x)
    
    # sort dict in descending order
    sorted_dict = dict(sorted(dict.items(), key=operator.itemgetter(1), reverse=True))
    
    return sorted_dict