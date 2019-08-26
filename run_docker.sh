#!/usr/bin/env bash
sudo docker build -t singularitynet/edge-detection-service .
sudo docker run -d -v /home/zelalem/pytorch-hed/etcd:/pytorch-hed/etcd -v /home/israel/net/ssl:/ssl -v /etc/letsencrypt:/etc/letsencrypt -it -p 8012:8012 -p 8002:8002 -p 8001:8001 --name edge-detection-service singularitynet/edge-detection-service