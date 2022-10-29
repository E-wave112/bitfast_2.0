#!/bin/bash

set -eu

# run a python script
uvicorn application:app --reload