#### Python/Flask Setup


1. Install [MiniConda (python 3.6) for whichever computer you want. It's more than you need, but it simplifies a few steps.
](https://conda.io/miniconda.html)

1.  In your shell (either bash or windows prompt), type: 
    ```
    conda create -n fake_bus python=3.6
    ```
    where *fake_bus* is the name of the virtual environment. Check that anaconda is now in your $PATH
1. To activate the environment on bash, use the command:
    ``` 
    source activate fake_bus
    ```
    and to deactivate it, use 
    ``` 
    source deactivate
    ```
    On my Windows install, CMD shows the name of the activated environment in the prompt automatically, Powershell doesn't. For CMD or Powershell, it's almost the same, just remove the ```source```.  
1. Grab this repository:
https://github.com/hanhanhan/fake_bus_api.git
1. Inside the root of the *fake_bus* directory, with the *fake_bus*  environment activated, use the command: 
    ```
    pip install -r requirements.txt 
    ```
1. At your command line, type *python -V* (uppercase *V*!). Confirm that python that the version that starts is **3.6**, not some earlier system version.

1. To start the server, use:
    ```
    python main.py
    ```
    That should get it running on port 5000!

#### Thing that could not work:
* python is sometimes aliased to an earlier system version, not 3.6. If so, just use 
    ```
    python3.6 main.py
    ``` 
to run the server

#### More Usage:
1. To run tests, use: 
    ```
    python -m unittest discover tests
    ```
    from inside the fake_bus directory, or just `python testname.py` to run an individual test.

2. Step through debugger - insert 
    ```
    import ipdb; pdb.set_trace()
    ```
    anywhere you'd like to start stepping through the program. `pp locals()` will pretty print all the local variables, to see other commands use `h`.


