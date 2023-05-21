f = open("C:/filebeat/filebeat_run_test.bat", "w+")
f.truncate(0)  # need '0' when using r+
f.write("@echo off\n")
f.write('start rmdir /s /q "C:/filebeat/data/registry/filebeat"\n')
f.write('cd "C:/filebeat"\n')
f.write("start .\\filebeat.exe -c filebeat.yml -e\n")
f.close
