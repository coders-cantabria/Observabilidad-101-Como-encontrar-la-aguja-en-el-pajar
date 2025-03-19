#!/bin/zsh
docker run \
  --name lgtm \
  -p 8100:3000 \
  -p 4317:4317 \
  -p 4318:4318 \
  --rm \
  -ti \
  -v $PWD/.lgtm/grafana:/data/grafana \
  -v $PWD/.lgtm/prometheus:/data/prometheus \
  -v $PWD/.lgtm/loki:/loki \
  -e GF_PATHS_DATA=/data/grafana \
  docker.io/grafana/otel-lgtm:latest