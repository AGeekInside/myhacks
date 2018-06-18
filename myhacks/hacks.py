import os
import pstats
import socket
import subprocess


def get_hostname_ip():
    '''Returns the hostname and ip of the current machine'''

    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name, host_ip
    except:
        print('Unable to retrieve hostname and ip.')

    return None

def isTrue(test):
    '''Returns True, if the test string is in the accepted 'true' list.'''
    trues_list = ['true', '1', 'yes']
    return test.lower() in trues_list

def output_lines(num_lines=50):
    '''Outputs the top lines.'''

    p = pstats.Stats('profile')
    p.strip_dirs()
    p.sort_stats('tottime')
    p.print_stats(num_lines)


def run(s, output_cmd=True, stdout=False):
    '''Runs a subprocess.'''

    if output_cmd:
        print(f'Running: {s}')

    p_out = subprocess.run(s,
                           stdout=subprocess.PIPE,
                           shell=True,
                           check=True)

    if stdout:
        return p_out.stdout.decode('utf-8').strip()
    else:
        return p_out

def restart_docker():
    '''Reloads systemd config and restarts docker daemon.'''

    cmds = [ "sudo systemctl daemon-reload",
             "sudo systemctl restart docker" ]

    for cmd in cmds:
        run(cmd)


def term_run(s):
    '''Runs a command in a new terminal.'''

    cmd = f'gnome-terminal -e "{s}"'
    run(cmd, output_cmd=False)


def get_branch_cnt(repo_dir, remote=False):
    '''Returns the number of branches in a git repo.'''

    if remote:
        branch_cmd = 'git branch -r'
    else:
        branch_cmd = 'git branch'

    cmd = f'cd {repo_dir} ; {branch_cmd} | wc -l'
    p = run(cmd, output_cmd=False)
    out = p.stdout.decode('utf-8').strip()
    return out


def make_executable(path):
    '''Makes the given file executable.'''
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)


def get_git_status(repo_dir):
    '''Returns the git status.'''

    cmd = f'cd {repo_dir} ; git status'
    git_status = run(cmd, output_cmd=False).stdout.decode('utf-8').strip()
    return git_status


def search_status(term, status):
    '''Searches status for term and returns that line.'''

    lines = status.split('\n')
    for line in lines:
        if term in line:
            return line
    return None


def get_branch_name(status):
    '''Returns the name of the current branch.'''

    branch_line = search_status('On branch', status)
    current_branch = branch_line.split(' ')[-1]
    return current_branch


def has_changes(status):
    '''Returns if the git repo has changes to be commited.'''

    if search_status('nothing to commit', status):
        return False
    else:
        return True


def get_remote_branches():
    '''Returns a list of remote branch names.'''

    cmd = 'git branch -r'





def get_git_info(repo_dir):
    '''Returns info a git repo.'''

    name = repo_dir.split('/')[-1]
    num_branches = get_branch_cnt(repo_dir)

    status = get_git_status(repo_dir)
    current_branch = get_branch_name(status)
    changes = has_changes(status)
    git_info = {
        'name': name,
        'num_branches': num_branches,
        'branch': current_branch,
        'changes?': changes,
    }

    return git_info


def compile_repo_info(repos,
                      all=False):
    '''Creates info for tabulate output.'''

    git_info = {
        'name': [],
        'num_branches': [],
        'branch': [],
        'changes?': [],
    }

    change_only = not all
    for repo in repos:
        repo_info = get_git_info(repo)
        if change_only:
            if repo_info['changes?']:
                for key in repo_info:
                    git_info[key].append(repo_info[key])
        else:
            for key in repo_info:
                git_info[key].append(repo_info[key])

    return git_info


def find_repos(root):
    '''Searches the directory and sub-directories for git repos.'''

    git_metadata = '.git'

    repos = []
    for root, dirs, files in os.walk(root):
        if git_metadata in dirs:
            repos.append(root)

    return repos
