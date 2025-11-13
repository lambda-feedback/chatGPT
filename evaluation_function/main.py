
from lf_toolkit import create_server, run

from .evaluation import evaluation_function
from .preview import preview_function

def main():
    """Run the IPC server with the evaluation and preview functions.
    """

    print("Creating Server")
    server = create_server()

    print("Setting Eval")
    server.eval(evaluation_function)
    print("seeting Preview")
    server.preview(preview_function)

    print("Running server")
    run(server)

if __name__ == "__main__":
    main()