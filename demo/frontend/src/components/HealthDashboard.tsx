import { useEffect, useState } from 'react'
import axios from 'axios'
import '../App.css'

interface HealthResponse {
  status: string
  timestamp: string
  components: {
    postgres: string
    redis: string
    kafka: string
  }
}

type LoadingState = 'loading' | 'success' | 'error'

function HealthDashboard() {
  const [health, setHealth] = useState<HealthResponse | null>(null)
  const [state, setState] = useState<LoadingState>('loading')
  const [errorMsg, setErrorMsg] = useState('')

  const fetchHealth = async () => {
    setState('loading')
    setErrorMsg('')
    try {
      const resp = await axios.get<HealthResponse>('/api/health', { timeout: 10000 })
      setHealth(resp.data)
      setState('success')
    } catch (err) {
      setErrorMsg(err instanceof Error ? err.message : String(err))
      setState('error')
    }
  }

  useEffect(() => {
    fetchHealth()
  }, [])

  const components = health?.components ?? { postgres: 'UNKNOWN', redis: 'UNKNOWN', kafka: 'UNKNOWN' }

  return (
    <div className="container">
      <h1>Demo 健康检查</h1>
      <p>全栈脚手架连通性验证</p>

      <div className="cards">
        {(['postgres', 'redis', 'kafka'] as const).map((name) => {
          const status = components[name] ?? 'UNKNOWN'
          const isUp = status === 'UP'
          return (
            <div key={name} className={`card ${isUp ? 'up' : 'down'}`}>
              <div className="name">{name}</div>
              <div className={`status ${isUp ? 'up' : 'down'}`}>{status}</div>
            </div>
          )
        })}
      </div>

      {state === 'loading' && <p>检查中...</p>}
      {state === 'error' && <p style={{ color: '#f87171' }}>请求失败: {errorMsg}</p>}
      {state === 'success' && health && (
        <p className="timestamp">总状态: {health.status} | 时间: {health.timestamp}</p>
      )}

      <button onClick={fetchHealth} disabled={state === 'loading'}>
        刷新
      </button>
    </div>
  )
}

export default HealthDashboard
