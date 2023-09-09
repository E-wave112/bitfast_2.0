variable "kube_config" {
  default     = "~/.kube/config"
  description = "path to a k8s config"

}

variable "app_name" {
  default = "bitfast"
  description = "name of the app to select from the deployment"
  
}

variable "deployment_name" {
  default = "bitfast"
  description = "name of the kuberenetes deployment"
  
}

variable "service_name" {
  default = "bitfast-service"
  description = "name of the k8s service discovery config"
  
}

variable "container_name" {
  default = "bitfast"
  description = "name of the docker container"
  
}

variable "image_name" {
  default = "ewave112/bitfast-image:dev"
  description = "name of remote docker image"
  
}