import paramiko
import os
import argparse 

def parse_args():
    parser = argparse.ArgumentParser(description='update 42,43,44,62 service,the same as lcoal /home/ppz/ai_new')
    parser.add_argument('commit', type=str)
    args = parser.parse_args()
    return args

def update_git():
    pull_service('43.247.184.42')
    pull_service('43.247.184.43')
    pull_service('43.247.184.44')
    pull_service('43.247.184.62')
def pull_service(service_ip):
    print('**************************{} pull start **********************'.format(service_ip))
    pkey = '/home/ppz/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(pkey)
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(service_ip, username='root', pkey=key)
    stdin, stdout, stderr = ssh.exec_command('pwd')
    print stdout.read()
    stdin, stdout, stderr = ssh.exec_command(
        'cd /home/ppz/test_git/ai_new;git pull git@43.247.184.45:/AI/git_rep/ai_new.git')
    print stdout.read()
    print('**************************{} pull done **********************'.format(service_ip))
if __name__ == "__main__":
    args = parse_args()
    print("*******************git add************************")
    os.system('cd /home/ppz/ai_new;'
              'git add ./app ./lib ./py-faster-rcnn ./tests')
    print("******************git status after add******************")
    os.system('cd /home/ppz/ai_new;git status')
    os.system('cd /home/ppz/ai_new;git commit -m {}'.format(args.commit))
    print("*****************git status after commit*************")
    os.system('cd /home/ppz/ai_new;git status')
    print('****************git push**************************')
    os.system('cd /home/ppz/ai_new;git push git@43.247.184.45:/AI/git_rep/ai_new.git')
    update_git()
    print('All done')
