
import json, html
data = json.load(open('semgrep.json'))
rows = []
for r in data.get('results', []):
    rows.append(f'<tr><td>{html.escape(r.get("path", ""))}</td><td>{r.get("start", {}).get("line", "")}</td><td>{html.escape(r.get("check_id", ""))}</td><td>{html.escape(r.get("extra", {}).get("severity", ""))}</td><td>{html.escape(r.get("extra", {}).get("message", ""))}</td></tr>')
html_out = '<html><head><title>Semgrep Report</title></head><body><h1>Semgrep Report</h1><table border=1><tr><th>Archivo</th><th>Línea</th><th>Regla</th><th>Severidad</th><th>Mensaje</th></tr>' + ''.join(rows) + '</table></body></html>'
open('semgrep-report.html', 'w').write(html_out)

