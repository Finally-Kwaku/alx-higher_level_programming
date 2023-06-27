#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sX "$1" DELETE
