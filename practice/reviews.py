import json
from collections import namedtuple


def get_data(filename):
    """Takes a file name and returns the raw string data."""
    with open(filename, 'r') as file:
        raw_data = file.read()
        return raw_data


def scrubber(raw_data):
    data = raw_data.split('\n')
    good_data = [d for d in data if d != '']
    return good_data


def load_reviews_data():
        """"""
        raw_data = get_data('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/reviews/reviews-reviews.txt')
        reviews_data = scrubber(raw_data)

        reviews = list()
        Reviews = namedtuple('Reviews', ['user_name', 'business_name', 'rating', 'text'])

        for line in reviews_data:
            ds = json.loads(line)
            rev = Reviews(user_name=ds['user_name'], business_name=ds['business_name'], rating=ds['rating'], text=ds["text"])
            reviews.append(rev)

        return reviews

def load_users():
    """"""
    raw_data = get_data('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/reviews/reviews-users.txt')
    users_data = scrubber(raw_data)

    users = list()
    Users = namedtuple('Users', ['user_name', 'hometown'])

    for line in users_data:
        ds = json.loads(line)
        #import pdb; pdb.set_trace()
        rvr = Users(user_name=ds['user_name'], hometown=ds['hometown'])
        users.append(rvr)

    return users

def load_business_data():
    """"""
    raw_data = get_data('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/reviews/reviews-businesses.txt')
    business_data = scrubber(raw_data)

    businesses = list()
    Business = namedtuple('Business', ['business_name', 'location'])

    for line in business_data:
        ds = json.loads(line)
        bus = Business(business_name=ds['business_name'], location=ds['city'])
        businesses.append(bus)

    print(businesses)
    return businesses


"""
User = namedtuple('User', ['user_name', 'hometown'])
Business = namedtuple('Business', ['business_name', 'location'])
Review = namedtuple('Review', ['user_name', 'business_name', 'rating', 'comment'])

Helen = User(user_name='Helen', hometown='Portland')
Bobby = User(user_name='Bobby', hometown='Chicago')
Carmen = User(user_name='Carmen', hometown='Portland')

Dicks_Burgers = Business(business_name='Dicks Burgers', location='Seattle')
Voodoo_Donuts = Business(business_name='Voodoo Donuts', location='Portland')

Review_1 = Review(user_name='Abby', business_name='Dicks Burgers', rating=5, comment='Oen late night!')
Review_2 = Review(user_name='Bobby', business_name='Dicks Burgers', rating=4, comment='Super tasty, but such'
                                                                                      'a long line!')
Review_3 = Review(user_name='Carmen', business_name='Dicks Burgers', rating=2, comment='Gross meat.')
Review_4 = Review(user_name='Helen', business_name='Voodoo Donuts', rating=1, comment='I do not like bubblegum'
                                                                                      'on my donuts.')
Review_5 = Review(user_name='Bobby', business_name='Voodoo Donuts', rating=5, comment='Pink building is so cute!')
Review_6 = Review(user_name='Abby', business_name='Voodoo Donuts', rating=2, comment='Diabetes inducing.')

review_list = [Review_1, Review_2, Review_3, Review_4, Review_5, Review_6]
"""

def filter_reviews_rating(rating):
    """Given a list of named tuples of businesses return those above n rating."""
    above = [review for review in review_list if review.rating > 3]
    return above


def return_reviews(reviews, business):
    """Give all the reviews for business"""
    all_revs = [review for review in reviews if review.business_name == business]
    print(all_revs)

def mean_rating(business):
    """Return the mean average of ratings for business"""
    ratings_of = [rat.business_name for rat in reviews if rat.business_name == business]
    ratings = load_reviews_data()
    filtered = [r for r in reviews if r.business_name in ratings_of]

    #averages_by_busi = [r.rating/3 for r in filtered]
    averages_by_busi = [r.rating/3 for r in filtered]
    print(averages_by_busi)

def user_reviews(user):
    user_revs = [review for review in reviews if review.user_name == user]
    print(user_revs)
    """Return all the reviews from user"""

def mean_city(users, city):
    """Return the mean average of ratings from users with city as hometown"""
    users_from = [user.user_name for user in users if user.hometown == city]
    reviews = load_reviews_data()
    filtered = [r for r in reviews if r.user_name in users_from]

    averages_by_city = [r.rating/2 for r in filtered]
    print(averages_by_city)
    """"""
    pass

# x = (3 + 9)
#reviews = load_reviews_data()
#return_reviews(reviews, 'Dicks Burgers')
reviews = load_reviews_data()
#user_reviews('Abby')
#
users = load_users()
#mean_city(users, "Portland")
#print(above3)
mean_rating('Voodoo Donuts')





