class ClusterAnalyzer:
    def __init__(self, raw_data):
        self.data = raw_data

    def run_checks(self):
        
        issues = []
        
        
        for pod in self.data.get("pods", []):
            if pod["status"] != "Running":
                issues.append({
                    "severity": "CRITICAL",
                    "resource": f"Pod/{pod['name']}",
                    "namespace": pod["namespace"],
                    "message": f"Pod is in '{pod['status']}' state."
                })
                
            
            for c_status in pod.get("container_statuses", []):
                if c_status["restart_count"] > 5:
                    issues.append({
                        "severity": "WARNING",
                        "resource": f"Pod/{pod['name']} (Container: {c_status['name']})",
                        "namespace": pod["namespace"],
                        "message": f"High restart count detected: {c_status['restart_count']} restarts."
                    })
                if c_status["waiting_reason"] in ["CrashLoopBackOff", "ErrImagePull", "ImagePullBackOff"]:
                    issues.append({
                        "severity": "CRITICAL",
                        "resource": f"Pod/{pod['name']}",
                        "namespace": pod["namespace"],
                        "message": f"Container waiting due to: {c_status['waiting_reason']}."
                    })

           
            for res in pod.get("resources", []):
                if not res["limits"] or "memory" not in res["limits"]:
                    issues.append({
                        "severity": "WARNING",
                        "resource": f"Pod/{pod['name']}",
                        "namespace": pod["namespace"],
                        "message": f"Container '{res['name']}' has no Memory Limits configured."
                    })

       
        for node in self.data.get("nodes", []):
            if node["status"] != "True": 
                issues.append({
                    "severity": "CRITICAL",
                    "resource": f"Node/{node['name']}",
                    "namespace": "Cluster-Level",
                    "message": f"Node status condition 'Ready' is: {node['status']}."
                })
                
        return issues