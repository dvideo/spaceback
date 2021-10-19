# Development Environment 

There are a few different ways to set up your environment:

1. Using Docker Compose via command line
2. Running apps directly via command line

Notes if using Docker (option 1): 

- You will need to have Docker already installed on your local machine. If you don't already have it installed, please use option 2 - it isn't necessary to learn a new tool (although it's very handy) for this exercise.

### 1. Using Docker Compose via command line

To run the main application container (`app`) in the background use:

    docker-compose up -d 

Then, to start a bash session inside the running app container run:

    docker-compose exec app /bin/bash

Here you should have access to `python`, `pip`, `pipenv`, `node` and `npm`.

You can start multiple session inside the container using the same `docker-compose exec app /bin/bash` command in multiple terminals. This may make it easier to run both the backend Flask app and frontend React devleopment server.

### 2. Running Flask and React Development Server CLI directly via command line

Ensure you have Python 3.9 installed. (Other versions may work, however this has only been tested on 3.9.4), [pipenv](https://pipenv.pypa.io/en/latest/install/), [Node.js](https://nodejs.dev/learn/how-to-install-nodejs) and [React scripts](https://www.npmjs.com/package/react-scripts).

## Finishing Up

#### Flask Backend

Initialize a virtual Python 3 environment via `pipenv`:

    cd backend
    pipenv --three
    pipenv install

Then run `bootstrap.sh`:

    ./bootstrap.sh

You should now be able to access the Flask API at `http://localhost:5000/vehicles`.

#### React Frontend

Use `npm` to start the React development server directory:

    npm start

You should now be able to access the React App at `http://localhost:3000`.

## Notes

- If you have any issues at all, especially with getting your development environment working, please reach out to us ASAP. Our intention isn't to make you troubleshoot an existing project's configuration. (You wouldn't spend the majority of your work day doing that in real life). We are more than happy to do that for you!
- Make your first priority getting everything to work! Save the bonus points for after you get things working all the way through.
- Do not worry about server-side rendering of any JavaScript React components
- Add any additional npm modules, python packages or other tools you'd like
- This project was boostrapped using [Create React App](https://create-react-app.dev/). See [CREATE_REACT_APP_README.md](CREATE_REACT_APP_README.md) for more info on some of the scaffolding.
