from kubernetes import client, config

class ClusterCollector:
    def __init__(self):
       
        config.load_kube_config()
        self.v1 = client.CoreV1Module()
        self.apps_v1 = client.AppsV1Api()

    def collect_all_data(self, namespace=None):
        
        data = {
            "pods": [],
            "nodes": [],
            "events": []
        }
        
        # איסוף פודים
        if namespace:
            pods_list = self.v1.list_namespaced_pod(namespace=namespace)
        else:
            pods_list = self.v1.list_pod_for_all_namespaces()
            
        for pod in pods_list.items:
            data["pods"].append({
                "name": pod.metadata.name,
                "namespace": pod.metadata.namespace,
                "status": pod.status.phase,
                "container_statuses": [
                    {
                        "name": c.name,
                        "ready": c.ready,
                        "restart_count": c.restart_count,
                        "waiting_reason": c.state.waiting.reason if c.state.waiting else None
                    } for c in (pod.status.container_statuses or [])
                ],
                "resources": [
                    {
                        "name": c.name,
                        "limits": c.resources.limits,
                        "requests": c.resources.requests
                    } for c in pod.spec.containers
                ]
            })
            
       
        nodes_list = self.v1.list_node()
        for node in nodes_list.items:
           
            ready_status = next((c.status for c in node.status.conditions if c.type == "Ready"), "Unknown")
            data["nodes"].append({
                "name": node.metadata.name,
                "status": ready_status,
                "cpu_capacity": node.status.capacity.get("cpu"),
                "memory_capacity": node.status.capacity.get("memory")
            })
            
        return data