from models import Profile

def matching(a, b): # should take two profile objects, will return percentage match between two users
    total_points = 0
    max_points = 70
    
    total_points = total_points + (10 if a.politics == b.politics else 0)           # politics
    total_points = total_points + (10 if a.gender == b.gender else 0)               # gender
    total_points = total_points + 10 - abs(a.class_rank - b.class_rank)             # class rank
    total_points = total_points + (10 if a.major == b.major else 0)                 # major
    total_points = total_points + 10 - abs(a.tidiness_factor - b.tidiness_factor)   # tidiness
    total_points = total_points + 10 - abs(a.party_factor - b.party_factor)         # party
    total_points = total_points + 10 - abs(a.guest_factor - b.guest_factor)         # guest

    return total_points


user1 = Profile()
user2 = Profile()

matching(user1, user2)