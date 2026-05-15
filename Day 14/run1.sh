#!/bin/bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
gunicorn --bind 127.0.0.1:8000 server1:app


# gunicorn server1:app --bind 127.0.0.1:8000
# gunicorn --bind 127.0.0.1:8000 server1:app