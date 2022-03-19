################################
### Instruction for MacOS 11 ###
################################

# Install hyperkit
brew install hyperkit

# Kubernetes
brew install kubectl

# Minikube
brew install minikube
minikube start -p aged --kubernetes-version=v1.16.1 --driver=hyperkit

# Kubeless
export RELEASE=$(curl -s https://api.github.com/repos/vmware-archive/kubeless/releases/latest | grep tag_name | cut -d '"' -f 4)
kubectl create ns kubeless
kubectl create -f https://github.com/kubeless/kubeless/releases/download/$RELEASE/kubeless-$RELEASE.yaml
kubectl get pods -n kubeless
kubectl get deployment -n kubeless
kubectl get customresourcedefinition
export OS=$(uname -s| tr '[:upper:]' '[:lower:]')
curl -OL https://github.com/vmware-archive/kubeless/releases/download/$RELEASE/kubeless_$OS-amd64.zip && \
  unzip kubeless_$OS-amd64.zip && \
  sudo mv bundles/kubeless_$OS-amd64/kubeless /usr/local/bin/
