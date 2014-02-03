#! /bin/bash

function check_install {
    if [ -z "`which "$1" 2>/dev/null`" ]
    then
        executable=$1
        shift
        while [ -n "$1" ]
        do
            DEBIAN_FRONTEND=noninteractive apt-get -q -y install "$1"
            print_info "$1 installed for $executable"
            shift
        done
    else
        print_warn "$2 already installed"
    fi
}

function check_remove {
    if [ -n "`which "$1" 2>/dev/null`" ]
    then
        DEBIAN_FRONTEND=noninteractive apt-get -q -y remove --purge "$2"
        print_info "$2 removed"
    else
        print_warn "$2 is not installed"
    fi
}

function check_sanity {
    # Do some sanity checking.
    if [ $(/usr/bin/id -u) != "0" ]
    then
        die 'Must be run by root user'
    fi

    if [ ! -f /etc/debian_version ]
    then
        die "Distribution is not supported"
    fi
}

function install_docker {
    check_install docker docker
}

function update {
    apt-get update
    apt-get dist-upgrade
}

function docker_postgres {
    docker run -i -t ubuntu /bin/bash
    update
    apt-get install python-software-properties
    apt-get install software-properties-common
    add-apt-repository ppa:pitti/postgresql
    apt-get update
    apt-get -y install postgresql-9.2 postgresql-client-9.2 postgresql-contrib-9.2
}

function setup_docker {
    sudo -u postgres createuser -P -d -r -s docker
    sudo -u postgres createdb -O docker docker
}

update
install_docker
docker_postgres
setup_docker
check_sanity
