from fabric.api import env, run, cd, settings


env.hosts = ['dev@138.197.69.255']
env.warn_only = True

PROJECT_DIR = '/home/dev/devdb/'
BACKEND_DIR = '{}project/backend/'.format(PROJECT_DIR)
FRONTEND_DIR = '{}project/frontend/'.format(PROJECT_DIR)
VENV_DIR = '{}env/bin/'.format(PROJECT_DIR)
MANAGE_PY = '{}python {}manage.py '.format(VENV_DIR, BACKEND_DIR)


def deploy_backend():
    PROMPTS = {
        "Type 'yes' to continue, or 'no' to cancel: ": 'yes',
    }

    with cd(BACKEND_DIR):
        run('git pull')
        run('{}pip install -r requirements.txt'.format(VENV_DIR))
        run('{}migrate'.format(MANAGE_PY))

        with settings(prompts=PROMPTS):
            run('{}collectstatic'.format(MANAGE_PY))

        run('sudo supervisorctl pid devdb | xargs kill -HUP')
        run('sudo supervisorctl status devdb')
        run('sudo supervisorctl restart devdb-celery')

        run('{}check'.format(MANAGE_PY))


def deploy_frontend(do_git=True):
    with cd(FRONTEND_DIR):
        if do_git:
            run('git pull')

        run('npm install')
        run('npm run build')


def deploy_all():
    deploy_backend()
    deploy_frontend(False)
