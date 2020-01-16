Prerequisites: python3.7+, pip3, virtualenv, aws-cli
    
    virtualenv venv -p python3

    . venv/bin/activate

    pip3 install -r requirements.txt

    zappa init

    zappa deploy dev

    zappa status dev

    deactivate



    . venv/bin/activate

    zappa update dev

    zappa rollback dev # -n 1

    deactivate


    . venv/bin/activate

    zappa undeploy dev

    deactivate