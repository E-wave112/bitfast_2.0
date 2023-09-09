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
    name = "bitfast"
    labels = {
      app = "bitfast"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "bitfast"
      }
    }
    template {
      metadata {
        labels = {
          app = "bitfast"
        }
      }
      spec {
        container {
          name  = "bitfast"
          image = "ewave112/bitfast-image:dev"
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
    name = "bitfast-service"
  }
  spec {
    selector = {
      app = "bitfast"
    }
    port {
      protocol    = "TCP"
      port        = 9600
      target_port = 8000
    }
    type = "LoadBalancer"
  }
}