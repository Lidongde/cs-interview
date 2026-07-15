import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// 容器内构建时 API 由 nginx 反代，开发时用 /api 代理到本地 8080
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
})
