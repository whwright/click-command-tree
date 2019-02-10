#!/usr/bin/env bash

set -o errexit

finish() {
    rm -rf testvenv*
}
trap finish EXIT

pythons=("python3.4" "python3.5" "python3.6")
versions=("5.0" "5.1" "6.0" "6.1" "6.2" "6.3" "6.4" "6.5" "6.6" "6.7" "7.0")

for python in ${pythons[@]}; do
    for version in ${versions[@]}; do
        version=$(echo ${version} | remove-quotes)
        echo "trying ${python} ${version}"

        venv="testvenv-${python}-${version}"
        virtualenv -p $(which ${python}) "${venv}" > /dev/null
        "${venv}/bin/pip" install "click==${version}" > /dev/null
        "${venv}/bin/python" -m unittest discover -v
    done
done

finish
