# Delete and stop the service if it already exists.
if (Get-Service $service_name -ErrorAction SilentlyContinue) {
  Stop-Service $service_name
  (Get-Service $service_name).WaitForStatus('Stopped')
  Start-Sleep -s 3
  sc.exe delete $service_name
}

$workdir = Split-Path $MyInvocation.MyCommand.Path

# Create the new service.
New-Service -name $service_name `
  -displayName $service_name `
  -binaryPathName "`"$workdir\$file_run`" --environment=windows_service -c `"$workdir\$file_config`" --path.home `"$workdir`" --path.data `"$workdir\data`" --path.logs `"$workdir\data\logs`" -E logging.files.redirect_stderr=true"`
  $depends_on


# Attempt to set the service to delayed start using sc config.
Try {
  Start-Process -FilePath sc.exe -ArgumentList 'config $service_name start= delayed-auto'
}
Catch { Write-Host -f red "An error occured setting the service to delayed start." }