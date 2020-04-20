# web_app/models.py
from web_app import db 

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Tweet = db.Column(db.String(288))
    author_id = db.Column(db.String(128))

# helper function to transform to json 
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "Ethereum": "ETH is money"},
            {"id": 2, "Bitcoin": "Bitcoin fixes this"},
            {"id": 3, "Zcash": "Privacy matters"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records