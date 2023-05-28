import os
import shutil

script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path).replace("\\", "/")


def metricbeat_yml(source, logstash_host):
    source = source + "/metricbeat.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    # Read in the file
    with open(folder_path + "/metricbeat_template.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$logstash-host", logstash_host)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_config_mysql(source):
    mysql_process_path = source+"/module/mysql/process"
    mysql_module_path = source+"/module/mysql"
    if not os.path.exists(mysql_process_path):
        shutil.rmtree(mysql_module_path)
        shutil.copytree(folder_path+"/mysql", mysql_module_path)


def metricbeat_module_mysql(source, mysql_host):
    source = source + "/modules.d/mysql.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    error_paths = ''
    for i in mysql_host:
        if error_paths == '':
            error_paths+='"'+i.strip()+'/"'
        else: 
            error_paths+=',"'+i.strip()+'/"'

    # Read in the file
    with open(folder_path + "/metricbeat_module_mysql.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$mysql-host", error_paths)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_module_mongodb(source, mongodb_host):
    source = source + "/modules.d/mongodb.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    error_paths = ''
    for i in mongodb_host:
        if error_paths == '':
            error_paths+='"'+i.strip()+'"'
        else: 
            error_paths+=',"'+i.strip()+'"'
    
    # Read in the file
    with open(folder_path + "/metricbeat_module_mongodb.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$mongodb-host", error_paths)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_module_system(source):
    source = source + "/modules.d/system.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    # Read in the file
    with open(folder_path + "/metricbeat_module_system.yml", "r") as file:
        filedata = file.read()

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)


def metricbeat_module_tomcat(source, tomcat_host):
    source = source + "/modules.d/tomcat.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    error_paths = ''
    for i in tomcat_host:
        if error_paths == '':
            error_paths+="'"+i.strip()+"'"
        else:
            error_paths+=",'"+i.strip()+"'"
    
    # Read in the file
    with open(folder_path + "/metricbeat_module_tomcat.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$tomcat-hosts", error_paths)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)
        
def filebeat_config_yml(source, tomcat_path, logstash_host):
    source = source + "/filebeat.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()
    
    tomcat_config = ""
    for i in tomcat_path:
        if i!="":
            with open(folder_path + "/filebeat_template_tomcat.yml", "r") as file:
                conf = file.read()
            conf = conf.replace("$logs-path", i.strip())
            tomcat_config+=conf
    
    # Read in the file
    with open(folder_path + "/filebeat_template.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$logstash-host", logstash_host)
    filedata = filedata.replace("$tomcat-config", tomcat_config)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)
        
def filebeat_module_mysql(source, mysql_paths):
    source = source + "/modules.d/mysql.yml"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    error_paths = ''
    slow_paths = ''
    for i in mysql_paths:
        if i!="":
            if error_paths == '':
                error_paths+='"'+i.strip()+'/*error.log*"'
                slow_paths+='"'+i.strip()+'/*slow.log*"'
            else:
                error_paths+=',"'+i.strip()+'/*error.log*"'
                slow_paths+=',"'+i.strip()+'/*slow.log*"'
    
    
    # Read in the file
    with open(folder_path + "/filebeat_module_mysql.yml", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$error-paths", error_paths)
    filedata = filedata.replace("$slow-paths", slow_paths)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)
    
def logstash_conf(source, beat_port, elastic, e_user, e_pass):
    source = source + "/config/logstash.conf"
    f = open(source, "w+")
    f.truncate(0)  # need '0' when using r+
    f.close()

    # Read in the file
    with open(folder_path + "/logstash_template.conf", "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("$port", beat_port)
    filedata = filedata.replace("$elastic", elastic)
    filedata = filedata.replace("$user", e_user)
    filedata = filedata.replace("$pass", e_pass)

    # Write the file out again
    with open(source, "w") as file:
        file.write(filedata)