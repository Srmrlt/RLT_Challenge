#!/bin/bash
set -e
echo "Running init-mongo.sh script..." > /docker-entrypoint-initdb.d/debug.log
mongorestore \
  --username root \
  --password example12345 \
  --authenticationDatabase admin \
  --db sampleDB \
  --collection sample_collection \
  /docker-entrypoint-initdb.d/sample_collection.bson \
  >> /docker-entrypoint-initdb.d/debug.log 2>&1
echo "Finished running init-mongo.sh script." >> /docker-entrypoint-initdb.d/debug.log
