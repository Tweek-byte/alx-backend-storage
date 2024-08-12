#!/usr/bin/env python3
'''Module 10.
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of the doc of a collection
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
