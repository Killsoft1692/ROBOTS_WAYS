#!/usr/bin/env python
import sys
import asyncio
from pymongo import MongoClient

from uploader import Uploader
from models.map import Map
from models.robot import Robot
from settings import MONGO_URI

mongo = MongoClient(MONGO_URI)
db = mongo.ways_db
mapper = Map()

up = Uploader(db, mapper)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    filename = input("type here name of file with map:  ")
    try:
        up.upload(filename)
    except FileNotFoundError:
        print('Wrong filename')
        sys.exit()
    tasks = [loop.create_task(Robot().walking(route.get('map', {}).get('data'))) for route in db.ways.find({})]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except ValueError:
        print('No routs found')
    finally:
        loop.close()
