output "k8s_deployment_metadata" {
    value = kubernetes_deployment.k8s_deployment.metadata
    description = "extra information about the kubernetes deployment"
  
}

output "k8s_service_metadata" {
    value = kubernetes_service.k8s_service.metadata
    description = "extra information about the kubernetes service"
  
}