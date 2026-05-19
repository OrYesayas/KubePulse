import json
from rich.console import Console
from rich.table import Table

class ClusterReporter:
    def __init__(self):
        self.console = Console()

    def print_to_terminal(self, issues):
        
        if not issues:
            self.console.print("\n✨ [bold green]No issues detected! Your cluster is healthy.[/bold green]\n")
            return
            
        table = Table(title="KubePulse Security & Health Diagnostic Report")
        table.add_column("Severity", justify="center")
        table.add_column("Namespace", justify="left")
        table.add_column("Resource", justify="left")
        table.add_column("Message", justify="left")
        
        for issue in issues:
            sev = issue["severity"]
            color = "red" if sev == "CRITICAL" else "yellow"
            
            table.add_row(
                f"[bold {color}]{sev}[/bold {color}]",
                issue["namespace"],
                issue["resource"],
                issue["message"]
            )
            
        self.console.print("\n")
        self.console.print(table)
        self.console.print(f"\n📢 [bold json]Total incidents found: {len(issues)}[/bold json]\n")

    def export_to_json(self, issues, filename="kubepulse_report.json"):
       
        with open(filename, 'w') as f:
            json.dump(issues, f, indent=4)
        self.console.print(f"💾 Report successfully exported to [bold cyan]{filename}[/bold cyan]")