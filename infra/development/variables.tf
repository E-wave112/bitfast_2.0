variable "kube_config" {
  default     = "~/.kube/config"
  type        = string
  description = "path to a k8s config"

}

variable "app_name" {
  default     = "bitfast"
  type        = string
  description = "name of the app to select from the deployment"

}

variable "app_name_green" {
  default     = "bitfast_green"
  type        = string
  description = "name of the app to select from the deployment (used for green deployment)"

}

variable "deployment_name" {
  default     = "bitfast"
  type        = string
  description = "name of the kuberenetes deployment"

}

variable "deployment_name_green" {
  default     = "bitfast-green"
  type        = string
  description = "name of the kuberenetes deployment"

}

variable "service_name" {
  default     = "bitfast-service"
  type        = string
  description = "name of the k8s service discovery config"

}

variable "container_name" {
  default     = "bitfast"
  type        = string
  description = "name of the docker container"

}

variable "image_name" {
  default     = "ewave112/bitfast-image:dev"
  type        = string
  description = "name of remote docker image"

}

variable "image_name_green" {
  default     = "ewave112/bitfast-image:dev-v2"
  type        = string
  description = "name of remote docker image (to be used for green deployment)"

}