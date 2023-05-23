import os

script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path).replace("\\", "/")


def metric_create_ps1(resource, service_name, logstash):
    file_run = "metricbeat.exe"
    file_config = "metricbeat.yml"
    depends_on = ""
    if logstash.strip() != "":
        depends_on = '-dependsOn "' + logstash + '"'

    f = open(resource + "/metric_service.ps1", "w+")
    f.truncate(0)  # need '0' when using r+
    f.close
    # open both files
    with open(folder_path + "/metricbeat_ps1.ps1", "r") as firstfile, open(
        resource + "/metric_service.ps1", "a"
    ) as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    # Read in the file
    with open(resource + "/metric_service.ps1", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$service_name", service_name)
    filedata = filedata.replace("$file_run", file_run)
    filedata = filedata.replace("$file_config", file_config)
    filedata = filedata.replace("$depends_on", depends_on)

    # Write the file out again
    with open(resource + "/metric_service.ps1", "w") as file:
        file.write(filedata)
