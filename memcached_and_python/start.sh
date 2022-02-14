#!/bin/bash -eu
docker run --detach --publish 11211:11211 --name my-memcached memcached
