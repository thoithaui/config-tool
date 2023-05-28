import os

script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path).replace("\\", "/")


def metric_create_ps1(source, service_name, logstash):
    file_run = "metricbeat.exe"
    file_config = "metricbeat.yml"
    depends_on = ""
    if logstash.strip() != "":
        depends_on = '-dependsOn "' + logstash + '"'

    f = open(source + "/metric_service.ps1", "w+")
    f.truncate(0)  # need '0' when using r+
    f.close
    # open both files
    with open(folder_path + "/metricbeat_ps1.ps1", "r") as firstfile, open(
        source + "/metric_service.ps1", "a"
    ) as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    # Read in the file
    with open(source + "/metric_service.ps1", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$service_name", service_name)
    filedata = filedata.replace("$file_run", file_run)
    filedata = filedata.replace("$file_config", file_config)
    filedata = filedata.replace("$depends_on", depends_on)

    # Write the file out again
    with open(source + "/metric_service.ps1", "w") as file:
        file.write(filedata)
        
        
def filebeat_create_ps1(source, service_name, logstash):
    file_run = "filebeat.exe"
    file_config = "filebeat.yml"
    depends_on = ""
    if logstash.strip() != "":
        depends_on = '-dependsOn "' + logstash + '"'

    f = open(source + "/filebeat_service.ps1", "w+")
    f.truncate(0)  # need '0' when using r+
    f.close
    # open both files
    with open(folder_path + "/filebeat_ps1.ps1", "r") as firstfile, open(
        source + "/filebeat_service.ps1", "a"
    ) as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    # Read in the file
    with open(source + "/filebeat_service.ps1", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$service_name", service_name)
    filedata = filedata.replace("$file_run", file_run)
    filedata = filedata.replace("$file_config", file_config)
    filedata = filedata.replace("$depends_on", depends_on)

    # Write the file out again
    with open(source + "/filebeat_service.ps1", "w") as file:
        file.write(filedata)

def logstash_create_ps1(source, service_name):
    service_path = source+"/bin"
    app_directory = source+"/bin/logstash.bat"
    
    f = open(source + "/logstash_service.ps1", "w+")
    f.truncate(0)  # need '0' when using r+
    f.close
    # open both files
    with open(folder_path + "/logstash_ps1.ps1", "r") as firstfile, open(
        source + "/logstash_service.ps1", "a"
    ) as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    # Read in the file
    with open(source + "/logstash_service.ps1", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$serviceName", service_name)
    filedata = filedata.replace("$servicePath", service_path)
    filedata = filedata.replace("$AppDirectory", app_directory)

    # Write the file out again
    with open(source + "/logstash_service.ps1", "w") as file:
        file.write(filedata)