# Simple-cv-app

**This repo is under development an is subject to change.**

*General Idea:* I decided to start developing my own simple computer vision app which (I hope in the future) will implement all necessary features and technologies needed to be considered as enterprise level. Note that such repo is aimed only for educational purposes.

The latest version is accessible at: http://vladargunov-test-app.win

## First part: Core

In the first part I made a minimally working example of 2 microservices, one of which implements a CV model and another one takes care of the frontend. The CV part was written in the FastAPI framework, and the frontend part was written in the Pyramid Web Framework. The orchestration is performed via Kubernetes.

For the local development, the CV part can be started (inside a virtual environment with requirements_local.txt installed) via the command `uvicorn app.main:app --host 0.0.0.0 --port 80` while being in the [model-ml](model-ml) directory. It spins up a FastAPI server which can be tested via [localhost:80/docs](localhost:80/docs) link. At the time of the writing it has only one endpoint which classifies a submitted image using [MobileNet_V2](https://pytorch.org/vision/stable/models/mobilenetv2.html) model.

The local development of the frontend part (which I am very bad at) can be done via the command `python app.py`, which is performed while you are in the [frontend/app](frontend/app) directory. Here it will show a simple HTML page, equivalent to the one hosted publicly, where you can submit yuor images for classification. If you test it locally, change the URL_MODEL variable inside the [app.py](frontend/app.app.py) file to *localhost:80* while also running the ML server.

When deploying the app to a Kubernetes, connect to a remote machine via *kubectl*, navigate to directory [model-ml/k8s](model-ml/k8s) and use the command `kubectl apply -f deployment.yaml`. Execute the same command inside the [frontend/k8s](frontend/k8s) directory and also perform a command `kubectl apply -f ingress.yaml` in order to set up an ingress for a public IP endpoint. Then using a DNS service link the public IP endpoint associated with the Ingress to a public name.

Please note, that I used a Kubernetes cluster with already preinstalled nginx controller from the [VK Cloud](https://mcs.mail.ru) platform. And the DNS services were provided by [Cloudflare](https://www.cloudflare.com/en-gb/). 

*Things to do in the next step:*

- Set up a CI/CD pipeline using [github actions](https://github.com/features/actions).

- Introduce infrastructure management via [Terraform](https://www.terraform.io) tool

- Make nice frontend using [Vue.js](https://vuejs.org) framework

- Set up testing

- Introduce data validation and refactor the previous code for greater robustness.


