from police_api import PoliceAPI
from collections import OrderedDict
from utils.postcode import get_lat_long_of_postcode


def is_ongoing(crime):
    incomplete_statuses = ['<Crime.Outcome> Under investigation',
                           '<Crime.Outcome> Awaiting court outcome',
                           '<Crime.Outcome> Action to be taken by another organisation',
                           None]
    return str(crime.outcome_status) in incomplete_statuses


def get_ordered_dict_sorted_by_number_of_definitions(unsorted_dict):
    return OrderedDict(sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=True))


def list_recent_crime_categories_and_resolutions_in_order(postcode):
    api = PoliceAPI()
    hood = api.locate_neighbourhood(*get_lat_long_of_postcode(postcode))

    recent_crimes = api.get_crimes_area(hood.boundary)

    all_outcomes_of_recent_crimes = []
    for crime in recent_crimes:
        if str(crime.outcome_status) not in all_outcomes_of_recent_crimes:
            all_outcomes_of_recent_crimes.append(str(crime.outcome_status))

    recent_crimes_by_category = {}

    # TODO: it could be richer to have non exclusive categories (tagging vs one category)

    # Build up categories
    for crime in recent_crimes:
        recent_crimes_by_category[crime.category.name] = []

    for crime in recent_crimes:
        if is_ongoing(crime) is False:
            recent_crimes_by_category[crime.category.name].append(crime)

    def get_outcome_breakdown(crime_category_string):
        crime_category = recent_crimes_by_category[crime_category_string]

        crime_outcomes = {}  # Build category specific crime outcomes
        for crime in crime_category:
            status = str(crime.outcome_status)
            crime_outcomes[status] = []
        for crime in crime_category:
            status = str(crime.outcome_status)
            crime_outcomes[status].append(crime)

        counted_crime_outcomes = {}
        for category in crime_outcomes:
            counted_crime_outcomes[category] = len(crime_outcomes[category])

        counted_crime_outcomes_ordered = get_ordered_dict_sorted_by_number_of_definitions(counted_crime_outcomes)
        return counted_crime_outcomes_ordered

    for category in recent_crimes_by_category.keys():
        print(category)
        print(get_outcome_breakdown(category))
        print()


train_station_postcode = 'LE2 0QB'
list_recent_crime_categories_and_resolutions_in_order(train_station_postcode)
