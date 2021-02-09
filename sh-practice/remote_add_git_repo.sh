#!/bin/bash

repo=$1
user=$2

curl -u "$user" https://api.github.com/user/repos -d '{"name":"'$repo'"}'
git remote add origin "https://github.com/$user/$repo"
