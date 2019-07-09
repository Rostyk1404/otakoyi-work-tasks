"""Contains configuration variables for MongoResponseBuilder."""

from pymongo import MongoClient

mongoDB_client = MongoClient("mongodb://localhost:27017/")
