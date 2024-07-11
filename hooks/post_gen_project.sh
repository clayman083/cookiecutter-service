#! /bin/sh

set -ex

pdm lock --with lint --with debug --with test
pdm install

git init
git add -A
git commit -m "Initial project structure"
