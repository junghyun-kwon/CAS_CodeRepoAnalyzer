#!/usr/bin/env bash

docker build -t cas_code_repo_analyser .
docker run -it --rm --name cas_code_repo_analyser-app cas_code_repo_analyser