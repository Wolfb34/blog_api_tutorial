*Deploy Instructions*

Ensure that storage, registry, metallb and ingress are enabled in microk8s.

Add the three images to the repository:

```
sudo docker build -t localhost:32000/blog-ui:v1 blog-ui/ && sudo docker push localhost:32000/blog-ui:v1
sudo docker build -t localhost:32000/flask-api:v1 flask-api/ && sudo docker push localhost:32000/flask-api:v1
sudo docker build -t localhost:32000/init-database:v1 -f DockerfileDataBase flask-api/ && sudo docker push localhost:32000/init-database:v1
```

Run `microk8s helm3 install blog-ui-chart blog-ui-chart` and the website should eventually be available at my-blog.com.

*Scaling Instructions*
The application can be scaled horizontally by executing `kubectl scale --replicas=<n> deployment <deployment>` where `n` is the desired number and `deployment` is one of `blog-api-chart` and `blog-ui-chart`.

*Uninstall Instructions*
The application can be uninstalled by executing `microk8s helm3 delete blog-ui-chart`.

*Upgrade Instructions*
Execute a canary deployment by upgrading the version in the topmost Chart.yaml file and then executing `microk8s helm3 install blog-ui-chart-canary blog-ui-chart`. (Not final instructions)

Execute a deployment rollout by upgrading the image or updating the template, updating the AppVersion and Version in the topmost Chart.yaml file and then executing `microk8s helm3 upgrade blog-ui-chart blog-ui-chart`.
