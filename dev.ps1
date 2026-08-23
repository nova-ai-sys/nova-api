# NOVA API - Development server launcher (Windows)
# Usage: .\dev.ps1
#
# The web UI lives in the nova-frontend repository and is started there.

Write-Host "`n  NOVA API Server" -ForegroundColor Cyan
Write-Host "  ===============" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot
uv run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000 --reload-exclude .venv
