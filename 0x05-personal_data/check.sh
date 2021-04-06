#!/usr/bin/env bash
pep8 "filtered_logger.py" 
pep8 "encrypt_password.py"
autopep8 --in-place --aggressive --aggressive "filtered_logger.py"
autopep8 --in-place --aggressive --aggressive "encrypt_password.py"
pep8 "filtered_logger.py" 
pep8 "encrypt_password.py"