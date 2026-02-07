# Script para configurar o ambiente de conversão de documentos
# Adiciona Pandoc e MiKTeX ao PATH do usuário

Write-Host "🔧 Configurando ambiente de conversão de documentos..." -ForegroundColor Cyan
Write-Host ""

# Verificar se está rodando como administrador (não necessário, mas útil)
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if ($isAdmin) {
    Write-Host "✅ Rodando como Administrador" -ForegroundColor Green
}
else {
    Write-Host "⚠️  Rodando como usuário normal (OK para PATH do usuário)" -ForegroundColor Yellow
}

Write-Host ""

# Caminhos a adicionar (inclui fallback para Pandoc em Program Files)
$pathsToAdd = @(
    "$env:LOCALAPPDATA\Pandoc",
    "C:\Program Files\Pandoc",
    "C:\Program Files\MiKTeX\miktex\bin\x64"
)

# Comandos de instalação correspondentes
$installCommands = @{
    "$env:LOCALAPPDATA\Pandoc"               = "winget install --id JohnMacFarlane.Pandoc"
    "C:\Program Files\Pandoc"                = "winget install --id JohnMacFarlane.Pandoc"
    "C:\Program Files\MiKTeX\miktex\bin\x64" = "winget install MiKTeX.MiKTeX"
}

# 1. Pegar PATH atual do usuário de forma limpa
$userPathRaw = [Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)
$userPathList = $userPathRaw -split ';' | Where-Object { $_ -ne "" }
$changed = $false

foreach ($path in $pathsToAdd) {
    if (Test-Path $path) {
        if ($userPathList -notcontains $path) {
            Write-Host "➕ Adicionando $path ao PATH..." -ForegroundColor Yellow
            $userPathList += $path
            $changed = $true
        }
        else {
            Write-Host "✅ $path já está no PATH" -ForegroundColor Green
        }
    }
    else {
        Write-Host "❌ Caminho não encontrado: $path" -ForegroundColor Red
        Write-Host "   Instale com: $($installCommands[$path])" -ForegroundColor Yellow
    }
}

Write-Host ""
# 2. Salvar apenas se houver mudança
if ($changed) {
    $newPathValue = $userPathList -join ';'
    [Environment]::SetEnvironmentVariable("Path", $newPathValue, [System.EnvironmentVariableTarget]::User)

    # 3. Atualizar a sessão atual com segurança
    # Em vez de sobrescrever, apenas adicionamos ao que já existe na memória
    foreach ($path in $pathsToAdd) {
        if ($env:PATH -notlike "*$path*") {
            $env:PATH += ";$path"
        }
    }

    Write-Host "🚀 PATH atualizado para esta sessão e para o sistema!" -ForegroundColor Green
}
else {
    Write-Host "✅ Nenhuma alteração necessária no PATH." -ForegroundColor Green
}

Write-Host ""
Write-Host "🧪 Testando instalações..." -ForegroundColor Cyan
Write-Host ""

# Testar Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Python não encontrado" -ForegroundColor Red
}

# Testar Pandoc
try {
    $pandocVersion = pandoc --version 2>&1 | Select-Object -First 1
    Write-Host "✅ Pandoc: $pandocVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Pandoc não encontrado" -ForegroundColor Red
}

# Testar MiKTeX
try {
    $xelatexVersion = xelatex --version 2>&1 | Select-Object -First 1
    Write-Host "✅ MiKTeX: $xelatexVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ MiKTeX não encontrado" -ForegroundColor Red
}

Write-Host ""
Write-Host "✅ Configuração concluída!" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANTE: Feche e reabra o terminal para que as mudanças tenham efeito completo." -ForegroundColor Yellow
Write-Host ""
Write-Host "📝 Para testar as conversões:" -ForegroundColor Cyan
Write-Host "   python ferramentas/conversao-word-e-pdf/md_para_word.py README.md" -ForegroundColor White
Write-Host "   python ferramentas/conversao-word-e-pdf/md_para_pdf.py README.md" -ForegroundColor White
