#!/usr/bin/env bash

gunicorn --bind :8000 -w 4 -k uvicorn.workers.UvicornWorker src.app:app