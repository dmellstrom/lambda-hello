Prerequisites: python3.7+, pip3, virtualenv, aws-cli
    
    virtualenv venv

    . venv/bin/activate

    pip3 install -r requirements.txt

    zappa init

    zappa deploy dev

    deactivate



    . venv/bin/activate

    zappa update dev

    deactivate