import os
import shutil

script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path).replace("\\", "/")


def metricbeat_yml(resource, logstash_host):
    print(logstash_host)
    source = resource + "/metricbeat.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close

    # Read in the file
    with open(folder_path + "/metricbeat_template.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$logstash-host", logstash_host)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_config_mysql(resource):
    dirpath = resource + "/module/mysql/process"
    path = resource + "/module/mysql"
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        shutil.rmtree(path)
    else:
        shutil.copytree("./mysql", path)


def metricbeat_module_mysql(resource, mysql_host):
    source = resource + "/modules.d/mysql.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close

    # Read in the file
    with open(folder_path + "/metricbeat_module_mysql.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$mysql-host", mysql_host)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_module_mongodb(resource, mongodb_host):
    source = resource + "/modules.d/mongodb.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close

    # Read in the file
    with open(folder_path + "/metricbeat_module_mongodb.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$mongodb-host", mongodb_host)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_module_system(resource):
    source = resource + "/modules.d/system.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close

    # Read in the file
    with open(folder_path + "/metricbeat_module_system.yml", "r") as file:
        filedata = file.read()

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_module_tomcat(resource, tomcat_host):
    source = resource + "/modules.d/tomcat.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close

    # Read in the file
    with open(folder_path + "/metricbeat_module_tomcat.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$tomcat-host", tomcat_host)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)
