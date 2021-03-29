# Async etcd3 client

[![Build Status](https://cloud.drone.io/api/badges/SergeyTsaplin/aioetcd/status.svg)](https://cloud.drone.io/SergeyTsaplin/aioetcd)

`aioetcd` is a fully typed asynchronous client for Etcd3.

Currently supports the following RPC's:

* KV
* Auth
* Lease

## How to contibute

### How to [re]generate grpc and protobuf stubs

* Install generation dependencies:

  ```bash
  pip install -r gen_requirements.txt
  ```

* [Re]generate the stubs:

  ```bash
  python3 -m grpc.tools.protoc \
    -Iproto \
    --python_out=aioetcd/_rpc \
    --grpc_python_out=aioetcd/_rpc \
    --mypy_out=aioetcd/_rpc2 \
    proto/*.proto
  ```
