import json
from collections import namedtuple

#

#
# with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/reviews/reviews-users.txt', 'r') as reviewers:
#     reviewer_data = reviewers.read()
#     #print(reviewer_data)
#
# with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/reviews/reviews-reviews.txt', 'r') as reviews_data:
#     reviews = reviews_data.read()
#     #print(reviews)

def load_review_data():
    """"""
    with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/reviews/reviews-businesses.txt', 'r') as business:
        business_data = business.read().split('\n')
        data = [d for d in business_data if d != '']

        businesses = list()
        Business = namedtuple('Business', ['business_name', 'location'])

        for raw in data:
            ds = json.loads(raw)
            bus = Business(business_name=ds['business_name'], location=ds['city'])
            businesses.append(bus)


        print(businesses)
        return businesses

        # business_data = json.loads(business_data)
        # print(business_data)

load_review_data()

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
""""""

def filter_reviews_rating(rating):
    """Given a list of named tuples of businesses return those above n rating."""
    above = [review for review in review_list if review.rating > 3]
    return above


def someotherfunc():
    """"""
    pass


#l = list()
#vd_results = [taco for taco in Review_list if 'Voodoo Donuts' == taco.business_name]
#user_results_Abby = [taco for taco in Review_list if 'Abby' == taco.user_name]

#mean_rating_vd = [sum(rating)/len(vd_results) for taco in Review_list if 'Voodoo Donuts' == taco.business_name]
#dick_ratings = [rating for rating in Dicks_Burgers if ]
#print(vd_results)
#print(user_results_Abby)
#print(dick_ratings)
#print(mean_rating_v

print(above3)






