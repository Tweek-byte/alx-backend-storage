#!/usr/bin/env python3
'''Module 8
'''


def list_all(mongo_collection):
    '''Lists all documents of a collection.
    '''
    return [doc for doc in mongo_collection.find()]
