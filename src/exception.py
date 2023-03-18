## Here we will write our own exception
import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() ## Execution info - gives 3 imp info(has info wrt line number on which exception occurred)
    file_name = exc_tb.tb_frame.f_code.co_filename ## Thus we get the file name(Custom Exc handling doc)
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

## Whenever we get an exception, we need to call above function

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys) -> None:
        super().__init__(error_message) ## Inheriting init function, then inherit exception class
        self.error_message = error_message_detail(error_message, error_detail=error_detail) ## error_detail is tracked by sys

    def __str__(self):
        return self().error_message     
