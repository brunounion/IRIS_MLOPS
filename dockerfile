# IRIS_MLOPS_DOCKERFILE
FROM python:3.8-slim-buster 
# image code https://github.com/docker-library/python/blob/ced32ddcaaa100447201a3b611e3556433db983d/3.8/buster/slim/Dockerfile



RUN REPO="https://github.com/brunounion/IRIS_MLOPS.git" \
    && apt-get update \
    && apt-get install git -y \ 
    && git clone "https://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:x-oauth-basic@github.com/brunounion/IRIS_MLOPS.git"

RUN cd IRIS_MLOPS \
    && pip install -r requirements.txt

CMD cd IRIS_MLOPS && gunicorn iris_api_gunicorn:app --bind 0.0.0.0:5000 --workers 4
# apt-get already updated by the base image
# installing git


