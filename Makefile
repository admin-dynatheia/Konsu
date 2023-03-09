# This is a makefile

SUDO = sudo apt-get
PIP = sudo pip
INSTALL = ${SUDO} install
INSTALL2 = ${PIP} install



all:
	python3 ./src/main.py
install:
	${INSTALL} git
	${INSTALL} python3-pip
	${INSTALL2} pynmea2
	${INSTALL2} serial
	${INSTALL2} pandas
	${INSTALL2} geopandas
update:
	${SUDO} update
	${SUDO} upgrade

