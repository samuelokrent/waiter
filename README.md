Waiter up-for-grabs food negotiation

# Installation

### Setup virtualvenv

##### Install

```bash
pip install virtualenv
virtualenv venv
```

##### Activate

```bash
source venv/bin/activate
# Verify it works by running 'python --version'
```

##### Deactivate

```bash
source deactivate
# Verify it works by running 'python --version'
```

### Dependencies

```bash
brew install mysql
# Make sure you are in the Python 3 virtual environment (see above)
pip install django mysqlclient
```

# Running the server

See the `run.sh` script

# Deployment (for public access)

First install localtunnel using `npm install -g localtunnel` (if you don't have Node.JS installed then do `brew install node`.

To run it, do `lt --subdomain claimed --port 8000` and visit [http://claimed.localtunnel.me](http://claimed.localtunnel.me)
