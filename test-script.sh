#!/bin/bash
if [ -d SFIA2 ]; then
    cd SFIA2 && git pull origin develop
else
    git clone --single-branch --branch develop https://github.com/ahsansabir30/SFIA2.git SFIA2
    cd SFIA2
fi

cd project

cd s1
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html
deactivate
cd ..

cd s2
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html
deactivate
cd ..

cd s3
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html
deactivate
cd ..

cd s4
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html
deactivate
cd ..