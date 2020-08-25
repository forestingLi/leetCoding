import paramiko
import threading

_SSH_HOST = '10.228.84.216'
# threading.local()这个方法的特点用来保存一个全局变量，
# 但是这个全局变量只有在当前线程才能访问
_local = threading.local()

def creat_ssh_client(ip):
    if (not ip):
        print("IP is null !")
        return
    ssh = paramiko.SSHClient()
    # 自动添加主机名及主机密钥到本地HostKeys对象，
    # 不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip,username='c4dev',password="c4dev!")
    return ssh


def run_ssh_command(ssh,cmd):
    _,stdout,stderr = ssh.exec_command(cmd)
    error = stderr.read().decode("utf-8")
    output = stdout.read().decode("utf-8")

    if error:
        raise RuntimeError(error)
    else:
        return output

def fast_run(cmd):
    ssh =getattr(_local,'ssh',None)
    if(not ssh):
        ssh = creat_ssh_client(_SSH_HOST)
        _local.ssh = ssh
    return ssh.exec_command(cmd)



