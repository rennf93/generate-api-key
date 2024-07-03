#!/bin/sh -l

# Extract inputs from 'with' GitHub context using the INPUT_ prefix
export KEY_LENGTH="${INPUT_KEY_LENGTH:-32}"

# Generate the API key
key=$(python /usr/src/app/run.py)

# Mask the key in the logs
echo "::add-mask::$key"

# Set the key as an output
echo "key=$key" >> $GITHUB_ENV