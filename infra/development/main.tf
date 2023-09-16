terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~>2.23.0"
    }
  }
  required_version = "~>1.5.5"
}

provider "kubernetes" {
  config_path = var.kube_config
}

resource "kubernetes_deployment" "k8s_deployment" {
  metadata {
    name = var.deployment_name
    labels = {
      app = var.app_name
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = var.app_name
      }
    }
    template {
      metadata {
        labels = {
          app = var.app_name
        }
      }
      spec {
        container {
          name  = var.container_name
          image = var.image_name
          resources {
            requests = {
              "memory" = "64Mi"
              "cpu"    = "250m"
            }
            limits = {
              "memory" = "128Mi"
              "cpu"    = "500m"
            }
          }
          port {
            container_port = 8000

          }
        }
      }
    }
  }

}

resource "kubernetes_service" "k8s_service" {
  metadata {
    name = var.service_name
  }
  spec {
    selector = {
      app = var.app_name
    }
    port {
      protocol    = "TCP"
      port        = 9600
      target_port = 8000
    }
    type = "LoadBalancer"
  }
}