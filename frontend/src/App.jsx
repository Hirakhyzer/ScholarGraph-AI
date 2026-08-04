import { BookOpen, Brain, GitBranch, GraduationCap, Layers, Search, Sparkles } from 'lucide-react';

const metrics = [
  { label: 'Papers analyzed', value: '128', detail: 'sample workspace' },
  { label: 'Topic clusters', value: '14', detail: 'methods + themes' },
  { label: 'Gap signals', value: '37', detail: 'limitations detected' },
  { label: 'Thesis readiness', value: '82%', detail: 'prototype score' },
];

const matrixRows = [
  {
    paper: 'Explainable AI for Literature Review',
    method: 'Knowledge graph + NLP',
    limitation: 'Human validation is limited',
    gap: 'Supervisor-centered evaluation',
  },
  {
    paper: 'Graph Mining for Research Discovery',
    method: 'Network clustering',
    limitation: 'Citation bias',
    gap: 'Content-level evidence fusion',
  },
  {
    paper: 'AI Tools in Doctoral Research',
    method: 'Mixed-method study',
    limitation: 'Small participant pool',
    gap: 'Cross-institutional validation',
  },
];

function MetricCard({ label, value, detail }) {
  return (
    <article className="metric-card">
      <span>{label}</span>
      <strong>{value}</strong>
      <small>{detail}</small>
    </article>
  );
}

function App() {
  return (
    <main className="app-shell">
      <aside className="sidebar">
        <div className="brand-mark">
          <GraduationCap size={30} />
          <div>
            <h1>ScholarGraph</h1>
            <p>AI Research Lab</p>
          </div>
        </div>

        <nav>
          <a className="active"><Layers size={18} /> Dashboard</a>
          <a><BookOpen size={18} /> Papers</a>
          <a><GitBranch size={18} /> Knowledge Graph</a>
          <a><Search size={18} /> Gap Detector</a>
          <a><Brain size={18} /> Thesis Planner</a>
        </nav>
      </aside>

      <section className="content">
        <header className="hero-card">
          <div>
            <p className="eyebrow"><Sparkles size={16} /> PhD-level research intelligence</p>
            <h2>Turn scattered papers into a defensible research roadmap.</h2>
            <p>
              ScholarGraph AI organizes literature into themes, methods, datasets, limitations,
              research gaps, and thesis-ready questions.
            </p>
          </div>
          <button>Analyze Paper</button>
        </header>

        <section className="metrics-grid">
          {metrics.map((metric) => (
            <MetricCard key={metric.label} {...metric} />
          ))}
        </section>

        <section className="dashboard-grid">
          <article className="graph-card">
            <div className="section-heading">
              <h3>Knowledge Graph Preview</h3>
              <p>Relationships between papers, methods, datasets, limitations, and gaps.</p>
            </div>
            <div className="graph-canvas">
              <span className="node paper">Paper</span>
              <span className="node method">Method</span>
              <span className="node dataset">Dataset</span>
              <span className="node gap">Gap</span>
              <span className="edge edge-one" />
              <span className="edge edge-two" />
              <span className="edge edge-three" />
            </div>
          </article>

          <article className="gap-card">
            <div className="section-heading">
              <h3>Top Gap Signals</h3>
              <p>Transparent candidates requiring human scholarly verification.</p>
            </div>
            <ul>
              <li>Limited multilingual evaluation</li>
              <li>Weak external validity</li>
              <li>Missing reproducibility protocol</li>
              <li>Dataset bias not fully explored</li>
            </ul>
          </article>
        </section>

        <section className="matrix-card">
          <div className="section-heading">
            <h3>Literature Review Matrix</h3>
            <p>A structured view for dissertation chapter planning.</p>
          </div>
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Paper</th>
                  <th>Method</th>
                  <th>Limitation</th>
                  <th>Possible Gap</th>
                </tr>
              </thead>
              <tbody>
                {matrixRows.map((row) => (
                  <tr key={row.paper}>
                    <td>{row.paper}</td>
                    <td>{row.method}</td>
                    <td>{row.limitation}</td>
                    <td>{row.gap}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </section>
    </main>
  );
}

export default App;
