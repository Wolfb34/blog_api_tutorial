*Deploy Instructions*

Ensure that storage, registry, metallb and istio are enabled in microk8s.

Create the TLS secret:
`kubectl create -n istio-system secret tls istio-ingressgateway-certs --key tls/tls.key --cert tls/tls.crt`

Copy the certification to the right folders:
```
sudo mkdir -p /etc/istio/ingressgateway-certs
sudo cp tls/tls.key /etc/istio/ingressgateway-certs
sudo cp tls/tls.crt /etc/istio/ingressgateway-certs
```

Add the three images to the repository:

```
sudo docker build -t localhost:32000/blog-ui:v1 blog-ui/ && sudo docker push localhost:32000/blog-ui:v1
sudo docker build -t localhost:32000/flask-api:v1 flask-api/ && sudo docker push localhost:32000/flask-api:v1
sudo docker build -t localhost:32000/init-database:v1 -f DockerfileDataBase flask-api/ && sudo docker push localhost:32000/init-database:v1
```

Run `microk8s helm3 install blog-ui-chart blog-ui-chart`.

Run `kubectl get svc istio-ingressgateway -n istio-system`. The external IP shown here is used to access the website.

Get to the website with `http://<ip>:443`.

*Scaling Instructions*
The application can be scaled horizontally by executing `kubectl scale --replicas=<n> deployment <deployment>` where `n` is the desired number and `deployment` is one of `blog-api-chart` and `blog-ui-chart`.

*Uninstall Instructions*
The application can be uninstalled by executing `microk8s helm3 delete blog-ui-chart`.

*Upgrade Instructions*
Execute a canary deployment by adding a canary development to the chart and then executing `microk8s helm3 upgrade blog-ui-chart blog-ui-chart`. This can include adding a canaryVersion to Chart.yaml and updating the Version of the chart.

Execute a deployment rollout by upgrading the image or updating the template, updating the AppVersion and Version in the topmost Chart.yaml file and then executing `microk8s helm3 upgrade blog-ui-chart blog-ui-chart`.
