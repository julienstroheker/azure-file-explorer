# AZURE-FILE-EXPLORER

Simple service returning a list a folder from a Azure storage file container

## Build

```bash
docker build -t azure-file-explorer .
```

## Run

You have to set 3 variables to target which storage account and container you want to query :
- STORAGE_ACCOUNT_NAME
- STORAGE_ACCOUNT_KEY
- SHARE_NAME

```bash
docker run -it --rm -p 5000:5000 \
    -e STORAGE_ACCOUNT_NAME=teststorageaccount \
    -e STORAGE_ACCOUNT_KEY=dskjdakj43kjdakj3/dkjawdkj3kd3(ndakjwda+M3DR/dsdsds/grgrsve3f== \
    -e SHARE_NAME=test1 \
    azure-file-explorer
```

## Example - Results

```javascript
{
    "0": "test1",
    "1": "test2"
}
```

## Deploy into Kubernetes

```bash
kubectl create -f https://....
```