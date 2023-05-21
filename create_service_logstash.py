from string import Template

metric_resource = "D:\Program Files\logstash-8.7.1"
file_run = "bin\logstash.bat"
file_config = "metricbeat.yml"
depends_on = '-DependsOn "elasticsearch-service-x64"'

f = open(metric_resource + "/metric_service_test.ps1", "w+")
f.truncate(0)  # need '0' when using r+
f.close
service_name = "metric_test"
# open both files
with open("install_template.txt", "r") as firstfile, open(
    metric_resource + "/metric_service_test.ps1", "a"
) as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)
# d = {
#     'service_name': 'This is the title',
#     'subtitle': 'And this is the subtitle',
#     'list': '\n'.join(['first', 'second', 'third'])
# }
# Read in the file
with open(metric_resource + "/metric_service_test.ps1", "r") as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace("$service_name", service_name)
filedata = filedata.replace("$file_run", file_run)
filedata = filedata.replace("$file_config", file_config)
filedata = filedata.replace("$depends_on", depends_on)

# Write the file out again
with open(metric_resource + "/metric_service_test.ps1", "w") as file:
    file.write(filedata)
