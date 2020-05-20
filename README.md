Prerequisites: python3.7, pip3, aws-cli
    
    python3 -m venv venv

    . venv/bin/activate

    pip3 install -r requirements.txt

    zappa init

    zappa deploy dev

    zappa status dev

    zappa tail dev

    zappa invoke dev 'main.time'

    zappa invoke dev "print(1 + 2 + 3); print(4 + 5 + 6)" --raw

    deactivate



    . venv/bin/activate

    zappa update dev

    zappa rollback dev # -n 1

    deactivate


    . venv/bin/activate

    zappa undeploy dev

    deactivate