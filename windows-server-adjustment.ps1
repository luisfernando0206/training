# AJUSTES DE HORÁRIO. UTILIZANDO BAHIA PARA EVITAR PROBLEMAS COM HORÁRIO DE VERÃO
Set-TimeZone "Bahia Standard Time"

# AJUSTES REGIONAIS PARA LOCALIZAÇÃO NO BRASIL (INSTANCIAS EM US-EAST-1)
Set-WinSystemLocale -SystemLocale pt-BR
Set-Culture -CultureInfo pt-BR

# AJUSTES DE PERFORMANCE
$powerConstants = @{}
PowerCfg.exe -ALIASES | Where-Object { $_ -match 'SCHEME_' } | ForEach-Object {
    $guid,$alias = ($_ -split '\s+', 2).Trim()
    $powerConstants[$guid] = $alias
}

# LISTAGEM DOS ESQUEMAS DE ENERGIA
$powerSchemes = PowerCfg.exe -LIST | Where-Object { $_ -match '^Power Scheme' } | ForEach-Object {
    $guid = $_ -replace '.*GUID:\s*([-a-f0-9]+).*', '$1'
    [PsCustomObject]@{
        Name     = $_.Trim("* ") -replace '.*\(([^)]+)\)$', '$1'          # LOCALIZED !
        Alias    = $powerConstants[$guid]
        Guid     = $guid
        IsActive = $_ -match '\*$'
    }
}

# DEFINIÇÃO DO ESQUEMA DE ENERGIA EM UMA VARIÁVEL (ALTA PERFORMANCE)
$desiredScheme = $powerSchemes | Where-Object { $_.Alias -eq 'SCHEME_MIN' }

# CONFIGURAÇÃO DO ESQUEMA DE ENERGIA
Powercfg.exe -SETACTIVE $desiredScheme.Alias

# AJUSTE DO TAMANHO DO ARQUIVO PAGEFILE.SYS
$computersys = Get-WmiObject Win32_ComputerSystem -EnableAllPrivileges;
$computersys.AutomaticManagedPagefile = $False;
$computersys.Put();
$pagefile = Get-WmiObject -Query "Select * From Win32_PageFileSetting Where Name like '%pagefile.sys'";
$pagefile.InitialSize = 5120; #5GB
$pagefile.MaximumSize = 5120; #5GB
$pagefile.Put();

# AJUSTE DE MEMÓRIA HEAP
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\SubSystems\' -Name 'Windows' -Value '%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,20480 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16'

# INSTALAR TELNET
Install-WindowsFeature Telnet-Client

# BAIXAR TREESIZE PORTABLE
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$url = "https://downloads.jam-software.de/treesize_free/TreeSizeFree-Portable.zip"
$output = "C:\TreeSizeFree-Portable.zip"
(New-Object System.Net.WebClient).DownloadFile($url, $output)

# DESATIVANDO WINDOWS UPDATE - REALIZAÇÃO DO UPDATE PELO PATCH MANAGER DO SSM
$WUSettings = (New-Object -com "Microsoft.Update.AutoUpdate").Settings
$WUSettings.NotificationLevel=1
$WUSettings.save()
