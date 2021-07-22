APPNAME=flaskapp
VENVDIR=.venv

# SYSPYTHON=python3
SYSPYTHON=python
# VENVDIR_BIN=${VENVDIR}/bin
VENVDIR_BIN=${VENVDIR}/Scripts

PYTHON=${VENVDIR_BIN}/python
FLASK=${VENVDIR_BIN}/flask
PIP=${VENVDIR_BIN}/pip

SYSTEMD_DIR=/etc/systemd/system/${APPNAME}.service
NGINX_SITES_ENABLED=/etc/nginx/sites-enabled

.PHONY: list-ports
list-ports:
	sudo lsof -i -P -n | grep LISTEN

.PHONY: daemon-status
daemon-status:
	sudo systemctl status ${APPNAME}

.PHONY: daemon-start
daemon-start:
	sudo systemctl start ${APPNAME}

.PHONY: daemon-stop
daemon-stop:
	sudo systemctl stop ${APPNAME}

.PHONY: daemon-restart
daemon-restart:
	sudo systemctl restart ${APPNAME}
	sudo systemctl status ${APPNAME}

.PHONY: nginx-restart
nginx-restart:
	sudo systemctl stop nginx 
	sudo systemctl start nginx

.PHONY: run-dev
run-dev:
	export FLASK_ENV=development && ${FLASK} run

.PHONY: venv
venv: venv-clear
	${SYSPYTHON} -m venv ${VENVDIR}
	${PIP} install -r requirements.txt

.PHONY: venv-clear
venv-clear:
	rm -rf ${VENVDIR}
