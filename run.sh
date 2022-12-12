#!/bin/bash

set -e

ACTION=$1
shift
PARAMS=$*

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

if [ -f /.dockerenv ]; then
    echo "Cannot run $0 inside a docker container"
    exit 2
fi

usage() {
  PROG=`basename $0`
  echo "$PROG [<options>]"
  echo "    console - Build and connect to python"
  echo "    run - Build and run the measurements"
}

COMPOSE="docker-compose -f docker-compose.yml $COMPOSE_ARGS"

docker_build() {
  local service=$1
  if [[ -v CI ]]
  then
    BUILD_ARG="--build-arg BUILDKIT_INLINE_CACHE=1"
  fi
  BUILD="$COMPOSE build $BUILD_ARG $service"
  $BUILD
}

docker_run() {
  local service=$1
  shift
  local cmd=$@

  docker_build $service
  RUN_SERVICE="$COMPOSE run $service ${cmd[@]}"
  $RUN_SERVICE
}

docker_compose_up() {
  local service=$1
  shift
  local cmd=$@

  docker_build $service
  COMPOSE_UP="$COMPOSE up -d $service ${cmd[@]}"
  COMPOSE_HTTP_TIMEOUT=200 $COMPOSE_UP
}


_docker_console() {
  local service=$1
  shift
  #sends arguments if any or send /bin/bash for default
  cmd=${@:-/bin/bash}

  echo $cmd

  if [[ -v CI ]];then
    touch $SCRIPT_DIR/$service/scripts/bash_history
  fi
  docker_run $service ${cmd[@]}
}

docker_python_console() {
  cd docker
  _docker_console python
}

docker_python_stop()
{
  $COMPOSE stop
}


docker_python_run() {
    cd docker
    _docker_console python bash /work/runner.sh
    docker-compose down
}

case "x$ACTION" in
    xconsole|xstop|xrun)
        docker_python_${ACTION} ${PARAMS[@]}
        ;;
    *) usage
        exit 1
    ;;
esac
