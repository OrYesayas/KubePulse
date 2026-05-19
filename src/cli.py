import click
import json
from collector import ClusterCollector
from analyzer import ClusterAnalyzer
from reporter import ClusterReporter

@click.group()
def cli():
    """KubePulse: A lightweight CLI tool for Kubernetes cluster health scanning."""
    pass

@cli.command()
@click.option('--namespace', default=None, help='Specific namespace to scan (default: all namespaces)')
@click.option('--offline-file', default=None, type=click.Path(exists=True), help='Path to a local JSON cluster dump for disconnected/offline scan')
@click.option('--format', default='terminal', type=click.Choice(['terminal', 'json']), help='Output format')
def scan(namespace, offline_file, format):
    """Scan cluster health and generate a diagnostic report."""
    reporter = ClusterReporter()
    
    if offline_file:
        click.echo(f"⚠️ Running in OFFLINE/DISCONNECTED mode using: {offline_file}")
        with open(offline_file, 'r') as f:
            raw_data = json.load(f)
    else:
        click.echo("🔌 Connecting to live Kubernetes cluster...")
        try:
            collector = ClusterCollector()
            raw_data = collector.collect_all_data(namespace=namespace)
        except Exception as e:
            click.echo(f"❌ Error connecting to cluster: {e}", err=True)
            return

    click.echo("🔍 Analyzing cluster state against configuration rules...")
    analyzer = ClusterAnalyzer(raw_data)
    issues = analyzer.run_checks()
    
    if format == 'terminal':
        reporter.print_to_terminal(issues)
    elif format == 'json':
        reporter.export_to_json(issues)

if __name__ == '__main__':
    cli()