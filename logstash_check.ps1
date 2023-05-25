# Đường dẫn đến thư mục Logstash
$logstashPath = "C:\path\to\logstash"

# Tên dịch vụ Logstash
$serviceName = "Logstash"

# Câu lệnh để chạy Logstash
$command = "$logstashPath\bin\logstash.bat -f $logstashPath\config\logstash.conf"

# Tạo dịch vụ Logstash
New-Service -Name $serviceName -BinaryPathName "cmd.exe /c $command" -Description "Logstash Service"

# Cấu hình dịch vụ Logstash
Set-Service -Name $serviceName -StartupType Automatic
