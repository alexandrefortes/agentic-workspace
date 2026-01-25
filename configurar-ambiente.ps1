# Script para configurar o ambiente de conversão de documentos
# Adiciona Pandoc e MiKTeX ao PATH do usuário

Write-Host "🔧 Configurando ambiente de conversão de documentos..." -ForegroundColor Cyan
Write-Host ""

# Verificar se está rodando como administrador (não necessário, mas útil)
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if ($isAdmin) {
    Write-Host "✅ Rodando como Administrador" -ForegroundColor Green
} else {
    Write-Host "⚠️  Rodando como usuário normal (OK para PATH do usuário)" -ForegroundColor Yellow
}

Write-Host ""

# Caminhos a adicionar
$pandocPath = "$env:LOCALAPPDATA\Pandoc"
$miktexPath = "C:\Program Files\MiKTeX\miktex\bin\x64"

# Obter PATH atual do usuário
$currentPath = [Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)

# Verificar e adicionar Pandoc
if (Test-Path $pandocPath) {
    if ($currentPath -notlike "*$pandocPath*") {
        Write-Host "➕ Adicionando Pandoc ao PATH..." -ForegroundColor Yellow
        $newPath = $currentPath + ";$pandocPath"
        [Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::User)
        Write-Host "✅ Pandoc adicionado ao PATH" -ForegroundColor Green
    } else {
        Write-Host "✅ Pandoc já está no PATH" -ForegroundColor Green
    }
} else {
    Write-Host "❌ Pandoc não encontrado em: $pandocPath" -ForegroundColor Red
    Write-Host "   Instale com: winget install --id JohnMacFarlane.Pandoc" -ForegroundColor Yellow
}

Write-Host ""

# Verificar e adicionar MiKTeX
if (Test-Path $miktexPath) {
    if ($currentPath -notlike "*$miktexPath*") {
        Write-Host "➕ Adicionando MiKTeX ao PATH..." -ForegroundColor Yellow
        $currentPath = [Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)
        $newPath = $currentPath + ";$miktexPath"
        [Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::User)
        Write-Host "✅ MiKTeX adicionado ao PATH" -ForegroundColor Green
    } else {
        Write-Host "✅ MiKTeX já está no PATH" -ForegroundColor Green
    }
} else {
    Write-Host "❌ MiKTeX não encontrado em: $miktexPath" -ForegroundColor Red
    Write-Host "   Instale com: winget install MiKTeX.MiKTeX" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🔄 Atualizando PATH da sessão atual..." -ForegroundColor Cyan
$env:PATH = [Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)

Write-Host ""
Write-Host "🧪 Testando instalações..." -ForegroundColor Cyan
Write-Host ""

# Testar Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python não encontrado" -ForegroundColor Red
}

# Testar Pandoc
try {
    $pandocVersion = pandoc --version 2>&1 | Select-Object -First 1
    Write-Host "✅ Pandoc: $pandocVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Pandoc não encontrado" -ForegroundColor Red
}

# Testar MiKTeX
try {
    $xelatexVersion = xelatex --version 2>&1 | Select-Object -First 1
    Write-Host "✅ MiKTeX: $xelatexVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ MiKTeX não encontrado" -ForegroundColor Red
}

Write-Host ""
Write-Host "✅ Configuração concluída!" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANTE: Feche e reabra o terminal para que as mudanças tenham efeito completo." -ForegroundColor Yellow
Write-Host ""
Write-Host "📝 Para testar as conversões:" -ForegroundColor Cyan
Write-Host "   python ferramentas/md_para_word.py README.md" -ForegroundColor White
Write-Host "   python ferramentas/md_para_pdf.py README.md" -ForegroundColor White
