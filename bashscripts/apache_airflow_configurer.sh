function install_supporting_packages(){
	sudo apt-get install python-setuptools
	sudo apt-get install python-pip
	sudo pip install --upgrade pip
}

function install_postgres(){
	sudo apt-get install postgresql postgresql-contrib
	sudo -u postgres psql

	# yet to add connector here,
	CREATE ROLE postgres;
	CREATE DATABASE airflow;
	GRANT ALL PRIVILEGES on database airflow to postgres;
	ALTER ROLE ubuntu SUPERUSER;
	ALTER ROLE ubuntu CREATEDB;
	GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to postgres;
}

function install_airflow(){
	# exporting path for airflow
	export AIRFLOW_HOME=~/airflow
	# installing dependencies
	(sudo apt-get install libmysqlclient-dev && sudo apt-get install libssl-dev && sudo apt-get install libkrb5-dev && sudo apt-get install libsasl2-dev)
	# installing airflow
	sudo pip install apache-airflow
}	
