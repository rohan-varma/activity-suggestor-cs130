#!/bin/bash
git log --pretty=format:"%C(auto) %h  %cd %<(16,trunc)%ae %d %s" --graph --date=short --all