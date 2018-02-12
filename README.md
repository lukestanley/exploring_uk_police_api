# exploring_uk_police_api
Just playing around with the police API, finding most common recent outcomes in a given area


You can try it like this:

    git clone https://github.com/lukestanley/exploring_uk_police_api.git

    cd exploring_uk_police_api

    pip install pipenv

    pipenv install

    pipenv shell

    python main.py

You might want to enter your UK postcode, edit the bottom of main.py

Example output:

    Drugs
    OrderedDict([('<Crime.Outcome> Local resolution', 1)])

    Shoplifting
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 10), ('<Crime.Outcome> Unable to prosecute suspect', 5), ('<Crime.Outcome> Local resolution', 1)])

    Violence and sexual offences
    OrderedDict([('<Crime.Outcome> Unable to prosecute suspect', 18), ('<Crime.Outcome> Investigation complete; no suspect identified', 5), ('<Crime.Outcome> Formal action is not in the public interest', 2), ('<Crime.Outcome> Offender given a caution', 1), ('<Crime.Outcome> Further investigation is not in the public interest', 1), ('<Crime.Outcome> Offender sent to prison', 1)])

    Robbery
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 1), ('<Crime.Outcome> Unable to prosecute suspect', 1)])

    Other theft
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 18), ('<Crime.Outcome> Unable to prosecute suspect', 2), ('<Crime.Outcome> Formal action is not in the public interest', 1)])

    Possession of weapons
    OrderedDict([('<Crime.Outcome> Offender given community sentence', 1), ('<Crime.Outcome> Investigation complete; no suspect identified', 1), ('<Crime.Outcome> Unable to prosecute suspect', 1)])

    Burglary
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 5), ('<Crime.Outcome> Unable to prosecute suspect', 1)])

    Bicycle theft
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 8)])

    Other crime
    OrderedDict([('<Crime.Outcome> Formal action is not in the public interest', 1)])

    Public order
    OrderedDict([('<Crime.Outcome> Unable to prosecute suspect', 3), ('<Crime.Outcome> Offender given a caution', 2), ('<Crime.Outcome> Investigation complete; no suspect identified', 2), ('<Crime.Outcome> Formal action is not in the public interest', 1), ('<Crime.Outcome> Local resolution', 1)])

    Criminal damage and arson
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 4), ('<Crime.Outcome> Unable to prosecute suspect', 1)])

    Vehicle crime
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 7), ('<Crime.Outcome> Unable to prosecute suspect', 1)])

    Anti-social behaviour
    OrderedDict([('None', 51)])

    Theft from the person
    OrderedDict([('<Crime.Outcome> Investigation complete; no suspect identified', 2)])


