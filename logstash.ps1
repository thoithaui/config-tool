$serviceName = "Logstash"
$servicePath = "C:\logstash-8.7.1\bin\logstash.bat"  # Đường dẫn đến tệp .bat của Logstash
$AppDirectory = "C:\logstash-8.7.1\bin"

# Kiểm tra xem dịch vụ đã tồn tại hay chưa
$serviceExists = Get-Service | Where-Object { $_.Name -eq $serviceName }

if ($serviceExists) {
    Stop-Service -Name $serviceName
    Start-Sleep -Seconds 5  # Chờ dịch vụ dừng hoàn toàn

    # Xóa dịch vụ
    & ./nssm.exe remove $serviceName confirm

}

# Cài đặt Logstash như một dịch vụ mới
Write-Host "Installing service $serviceName..."
& ./nssm.exe install $serviceName $servicePath
& ./nssm.exe set $serviceName AppDirectory $AppDirectory
& ./nssm.exe set $serviceName AppDirectory $serviceName
& ./nssm.exe set $serviceName Start SERVICE_AUTO_START
& ./nssm.exe set $serviceName DependOnService "elasticsearch-service-x64 --config.reload.automatic"
