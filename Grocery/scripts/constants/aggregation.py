class DatabaseConstants:
    database_name = "interns_b2_23"
    collection_name = "kajal_grocery_item_collection"
    uri = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
    aggregate = [
        {
            '$addFields': {
                'total_amount': {
                    '$multiply': [
                        '$quantity', '$amount'
                    ]
                }
            }
        }, {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$total_amount'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]


