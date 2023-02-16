import os  # noqa
import warnings  # noqa
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time  # noqa

from Output import generate_answer


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################


def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    # Use the model to generate answers to new science-related questions
    output = []
    for text in request.text:
        # Example question: what is an atomic scale?
        # Second Example: what is an asteroid?
        # Third Example: what is electricity?
        response = generate_answer(text)
        output.append(response)
        print('''If the answer seems to be off - maybe consider asking the question differently.''')  # noqa
    return SimpleText(dict(text=output))
