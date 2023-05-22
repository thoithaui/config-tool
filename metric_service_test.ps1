# Prompt for administrative privileges
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    $arguments = "& '" + $MyInvocation.MyCommand.Definition + "'"
    Start-Process powershell.exe -Verb RunAs -ArgumentList $arguments
    Exit
}

# Your script code here
Write-Host "Running the script as an administrator..."

# Delete and stop the service if it already exists.
if (Get-Service metric_test -ErrorAction SilentlyContinue) {
  Stop-Service metric_test
  (Get-Service metric_test).WaitForStatus('Stopped')
  Start-Sleep -s 1
  sc.exe delete metric_test
}

$workdir = Split-Path $MyInvocation.MyCommand.Path

# Create the new service.
New-Service -name metric_test `
  -displayName metric_test `
  -binaryPathName "`"$workdir\metricbeat.exe`" --environment=windows_service -c `"$workdir\metricbeat.yml`" --path.home `"$workdir`" --path.data `"$workdir\data`" --path.logs `"$workdir\data\logs`" -E logging.files.redirect_stderr=true"`
  


# Attempt to set the service to delayed start using sc config.
Try {
  Start-Process -FilePath sc.exe -ArgumentList 'config metric_test start= delayed-auto'
}
Catch { Write-Host -f red "An error occured setting the service to delayed start." }

Pause