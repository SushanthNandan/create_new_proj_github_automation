#!/bin/bash

function create() {
    source .env
    python create.py "$1"
    cd $HOME"/MyProjects/"$1
    git init
    git remote add origin git@github.com:$USERNAME/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
}


proj_name=$1
echo "Creating a new Project: $proj_name"
create "$proj_name"